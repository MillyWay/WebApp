import pymysql
def insert_data(email,pwd):
    db = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234',
                        db='b',
                        charset='utf8')
    c = db.cursor()
    setdata = (email, pwd)
    c.execute("INSERT INTO usertbl VALUES (%s, %s)", setdata) 
    db.commit()

def get_data(email,pwd):
    db = pymysql.connect(host='127.0.0.1',
                        user='root',
                        password='1234',
                        db='b',
                        charset='utf8')
    c = db.cursor()
    setdata = (email, pwd)
    c.execute("SELECT * FROM usertbl WHERE email = %s AND password = %s)", setdata) 
    ret = c.fetchone()
    print(ret)

    #get_data('wkdgustj2582@gmail.com','1234')