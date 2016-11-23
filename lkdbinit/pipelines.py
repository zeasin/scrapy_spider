# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456@qwe',
        db='longkang',
        charset='utf8',
        use_unicode=False
    )
    return conn

class LkdbinitPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()

        hospital_id = 16 #医院id
        hospital_city = '350200'
        hospital_name = '厦门大学附属中山医院厦禾健康体检中心'
        package_id = 0 #套餐id

        try:
            # 插入套餐信息
            tc_sql = "INSERT INTO lk_t_check_package(package_title,package_image,package_characteristic,hospital_id,hospital_name,hospital_city,package_price) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(tc_sql, (item['title'], item['image'], item['feature'], hospital_id,hospital_name,hospital_city,item['price']))
            package_id = dbObject.insert_id()

            for it in item['items']:
                hospital_check_item_id = 0  # 医院检查项目id
                hospital_check_item_name = ''
                hospital_check_item_remark = ''

                # 插入医院检查项目表
                select_check_item_sql = "select * from lk_h_hospital_item where title = %s and h_id=%s"
                cursor.execute(select_check_item_sql,(it['title'],hospital_id))

                if cursor.rowcount == 0:
                    insert_check_item_sql = 'insert into lk_h_hospital_item(title,remark,h_id) values (%s,%s,%s)'
                    cursor.execute(insert_check_item_sql,(it['title'],it['remark'],hospital_id))
                    hospital_check_item_id = dbObject.insert_id()
                    hospital_check_item_name = it['title']
                    hospital_check_item_remark = it['remark']
                else:
                    result = cursor.fetchone()
                    hospital_check_item_id = result[0]
                    hospital_check_item_name = result[2]
                    hospital_check_item_remark = result[3]

                # 插入套餐检查项目表
                tc_item_sql = "insert into lk_t_check_package_items(package_id,check_item_id,check_item_name,remark) values (%s,%s,%s,%s)"
                cursor.execute(tc_item_sql, (package_id,hospital_check_item_id, hospital_check_item_name, hospital_check_item_remark))

            dbObject.commit()


        except Exception as ex:
            print(ex)
            dbObject.rollback()

        return item