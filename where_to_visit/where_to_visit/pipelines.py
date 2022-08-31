# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class WhereToVisitPipeline:

    def __init__(self):
        self.con = sqlite3.connect("../sample.db")
        self.cur = self.con.cursor()
        self.create_table()
    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
        city_name TEXT,
        attraction_name TEXT,
        rating TEXT,
        image_url TEXT,
        reviews TEXT,
        about TEXT
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES(?,?,?,?,?,?)""",
                         (item["city_name"], item["attraction_name"], item["rating"], item["image_url"], item["reviews"], item["about"]))
        self.con.commit()
        return item
