import pymysql as mysql
def ConnectionPool():
    db=mysql.connect(host='localhost',port=3306,user="root",password="8770837068",db="attendanceandleave")
    cmd=db.cursor(mysql.cursors.DictCursor)
    return (db,cmd)