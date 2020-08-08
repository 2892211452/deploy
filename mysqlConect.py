
import pymysql
from path import *
from dataTest import *



# 打开数据库连接
db = pymysql.connect("localhost","root","156354","dm" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句

def insert(title, url, img, src):
    sql = """insert  into dm (title ,url , img ,src )
                        value('titleValue', 'urlValue','imgValue',"srcValue");"""
    sql = sql.replace('titleValue', title)
    sql = sql.replace('urlValue', url)
    sql = sql.replace('imgValue', img)
    sql = sql.replace('srcValue', src)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
        
        # 关闭数据库连接
        # db.close()


def select(name):
    sql = """
select * from dm where title  like '%name%';
"""
    sql = sql.replace('name', name)

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        results = cursor.fetchall()
        res =[]
        for row in results:
            title = row[0]
            url = row[1]
            image = row[2]
            src = row[3]

            # 对src 进行数组化处理
            src = list(src)
            length = len(src)
            src = src[1:(length-1)]
            src = ''.join(src)

            import re
            r=re.compile('\[.*?\]')
            content=r.findall(src)
            ans =[]
            for i in content:
                print(i)
                i = i.replace('[','')
                i = i.replace("'",'')

                i = i.replace(']','')

                i = i.replace(' ','') # 删除空格 调了半天bug

                r = i.split(',')
                
                # # 加入解析的接口
                # r[1]="https://saas.jialingmm.net/code.php?type=flv&amp;vid="+r[1]+"&amp;userlink=http%3A%2F%2Fwww.imomoe.in%2Fplayer%2F7845-0-0.html&amp;adress=HuNan_ChangSha"
                ans.append({
                    '集数': r[0],
                    'url':r[1]
                })
            src = ans




            res.append({
                'title':title,
                'url':url,
                'image':image,
                'src':src,
            })
        return res
       # 打印结果
            # print(row)
    except:
        # 如果发生错误则回滚
        db.rollback()
        
        # 关闭数据库连接
        # db.close()



if __name__ =="__main__":
    for i in range(1, 7266):
        try:
            output = open(FileDir+'/dm/data'+str(i) +'.pkl', 'rb')


            data=pickle.load(output)
            src = str(data['video'])
            title = data['name']
            url = data['url']
            img = data['imgUrl']
            insert(title, url, img, src)
            if i % 10 ==0:
                print(i)
        except:
            print('error')


