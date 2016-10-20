import sqlite3

db = sqlite3.connect("discobandit.db")
c = db.cursor()
c2 = db.cursor()

def helper(g):
    x = c2.execute("SELECT mark FROM courses WHERE courses.id = " +str(g) + ";")
    #prin(x)
    a = 0.0
    b = 0.0
    for j in x:
        #print j
        a += j[0]
        b += 1.0
    if b == 0:
        return -1
    return a/b

l = c.execute("SELECT name, id FROM students;")

print "Note: -1 indicates no grades were found"

for m in l:
    #print m[1]
    print "Name: %s ID: %d Average: %f"%(m[0], m[1], helper(m[1]))

db.commit()
db.close() 
