import pymysql
def connect():
    db = pymysql.connect(host='localhost', user='root', password='Yz200409012041Ab', database='userdate1', charset='utf8')
    return db