import sys
import time
from collections import OrderedDict
from Settings.DBSettings import DATABASES
from MysqlClass import Mysql
import requests

sys.setdefaultencoding('utf-8')


"""
    在简书中搜索相关文章
"""

ct = 1


def get_pages(mysql, base_url, domain_name, article_table, search_name):

    """
        获取文章详细信息
        将文章id，url，user，user_url，title，image，body，time，views，comments，likes，tip 存入 article中
    """

    html = requests.get(base_url).content

    result = eval(html)

    endpages = result['total_pages'] + 1

    print("endpages:%s" % endpages)
    for page in range(1, endpages):
        base_url = 'http://www.jianshu.com/search/do?q=' + search_name + '&page=%s&type=type' % page
        print(base_url)
        time.sleep(10)
        get_details(mysql, base_url, domain_name, article_table)


def get_details(mysql, base_url, domain_name, article_table ):
    """
    """

    global ct
    article = OrderedDict()
    # cmd = 'curl -s --connect-timeout 10 %s' % base_url
    # p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # res = p.stdout.readlines()
    html = requests.get(base_url).content
    result = eval(html)
    # result = eval(res[0])
    print(result)
    for tag in result['entries']:
        article['article_id'] = str(tag['id'])
        article['article_title'] = tag['title']
        article['article_url'] = domain_name + '/p/' + tag['slug']
        article['article_user'] = tag['user']['nickname']
        article['article_user_url'] = domain_name + '/users/' + tag['user']['slug']
        article['article_time'] = tag['first_shared_at']
        article['article_views_count'] = str(tag['views_count'])
        article['public_comments_count'] = str(tag['public_comments_count'])
        article['article_likes_count'] = str(tag['likes_count'])
        article['total_rewards_count'] = str(tag['total_rewards_count'])

        created_time = mysql.get_current_time()
        article['created'] = created_time

        print("----开始插入第 %s 条数据----" % ct)

        for key, values in article.items():
            print(key+':'+values)
        result = mysql.insert_data(article_table, article)
        if result:
            print("article_table：数据保存成功！")
        else:
            print("article_table：数据保存失败！")

        ct += 1


if __name__ == '__main__':

    host = DATABASES['default']['HOST']
    user = DATABASES['default']['USER']
    passwd = DATABASES['default']['PASSWORD']
    db = DATABASES['default']['NAME']
    port = DATABASES['default']['PORT']
    article_table = 'jianshu_searcharticle'
    search_name = ''
    domain_name = 'http://www.jianshu.com'
    base_url = 'http://www.jianshu.com/search/do?q=' + search_name
    mysql = Mysql(host, user, passwd, db, port)
    get_pages(mysql, base_url, domain_name, article_table, search_name)
