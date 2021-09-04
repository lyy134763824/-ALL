import pymysql

db = pymysql.connect(
            '127.0.0.1',
            'lyy',
            '123',
            'maoyan_db',
            charset='utf8',
        )
cursor = db.cursor()
ins = 'insert into filmtab values(%s,%s,%s)'
cursor.executemany(ins,[('a','b','c'),('d','e','f')])

db.commit()
db.close()
cursor.close()




