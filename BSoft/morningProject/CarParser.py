import xml.sax

class CarParser(xml.sax.ContentHandler):
    def __init__(self):
        self.MyData = ""
        self.make = ""
        self.model = ""
        self.type=""
        self.bhp=""
        self.exshowroom=""

    def startElement(self, tag, attributes):
        self.MyData = tag
        if tag == "car":
            print ("---- Cars ----")
            name = attributes['name']
            name = attributes['name']
            print ("Name : ", name)

    def endElement(self, tag):
        if self.MyData == "make":
            print ("Make : ", self.make)
        elif self.MyData == "model":
            print ("Model : ", self.model)
        elif self.MyData == "type":
            print ("Type : ", self.type)
        elif self.MyData == "bhp":
            print ("Power (bhp) : ", self.bhp)
        elif self.MyData == "exshowroom":
            print ("Ex-Showroom Price : ", self.exshowroom)
        self.MyData = ""

    def characters(self, content):
        if self.MyData == "make":
            self.make = content
        elif self.MyData == "model":
            self.model = content
        elif self.MyData == "bhp":
            self.bhp = content
        elif self.MyData == "type":
            self.type = content
        elif self.MyData == "exshowroom":
            self.exshowroom = content


if (__name__ == "__main__"):
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    handle = CarParser()
    parser.setContentHandler(handle)
    parser.parse("cars.xml")
