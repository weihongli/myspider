import pymysql
from Settings.DBSettings import DATABASES


class Mysql(object):

    def __init__(self):
        try:
            self.db = pymysql.connect(
                host=DATABASES['default']['HOST'],
                user=DATABASES['default']['USER'],
                passwd=DATABASES['default']['PASSWORD'],
                db=DATABASES['default']['NAME'],
                port=DATABASES['default']['PORT'],
                charset='utf8')
            self.cur = self.db.cursor()
        except pymysql.Error as e:
            print('连接数据库失败', e.args[0], e.args[1])

    def insert_data_to_pages(self, my_dict):
        sql = "insert into pages(scatalogid,title,href,content,fullcontent) " \
              "values(%(scatalogid)s,%(title)s,%(href)s,%(content)s,%(fullcontent)s)"
        try:
            result = self.cur.execute(sql, my_dict)
            self.db.commit()
            if result:
                return 1
            else:
                return 0
        except pymysql.Error as e:
            self.db.rollback()
            if "key 'PRIMARY'" in e.args[1]:
                print("数据已存在，未插入数据")
            else:
                print("插入数据失败，原因 %d: %s" % (e.args[0], e.args[1]))

    def find_data(self, table):
        try:
            sql = "select * from {0}".format(table)
            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result
        except pymysql.Error as e:
            print("查询数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
