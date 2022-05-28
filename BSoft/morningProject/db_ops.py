import MySQLdb

empId = int(input("Enter employee id"))
desig = input("Enter new designation")
dbcon = MySQLdb.connect("localhost","root","","sample_db")
dbcursor = dbcon.cursor()
query = """update employee set designation='%s' where emp_id='%d'""" % (desig,empId)
try:
    dbcursor.execute(query)
    dbcon.commit()
except:
    dbcon.rollback()
    print("Update operation aborted.")
dbcon.close()