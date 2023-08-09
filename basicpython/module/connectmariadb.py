import pymysql

#Connect to the database
def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

#print(connectdb())