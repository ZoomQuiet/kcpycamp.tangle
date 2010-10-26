import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", passwd="sa", db="mycds")

rs = conn.cursor()

rs.execute("SELECT * cds")

rows = rs.fetchall()

for row in rows:
    print row

conn.close()

