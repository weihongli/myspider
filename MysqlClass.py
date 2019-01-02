import pymysql


class Mysql(object):

    def __init__(self, host, user, passwd, db, port):
        try:
            self.db = pymysql.connect(
                host=host,
                user=user,
                passwd=passwd,
                db=db,
                port=port,
                charset='utf8')
            self.cur = self.db.cursor()
        except pymysql.Error as e:
            print('连接数据库失败', e.args[0], e.args[1])

    def insert_data_to_pages(self,my_dict):
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

    def insert_data(self, table, my_dict):
        try:
            cols = ','.join(my_dict.keys())
            values = '","'.join(my_dict.values())
            values = '"' + values + '"'
            try:
                sql = "insert into %s (%s) values(%s)" % (table, cols, values)
                print(sql)
                result = self.cur.execute(sql)
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
        except pymysql.Error as e:
            print("数据库错误，原因%d: %s" % (e.args[0], e.args[1]))

    def find_data(self, table):
        try:
            sql = "select * from {0}".format(table)
            self.cur.execute(sql)
            result = self.cur.fetchall()
            return result
        except pymysql.Error as e:
            print("查询数据失败，原因 %d: %s" % (e.args[0], e.args[1]))
