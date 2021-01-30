# Individual Inventory Management System(IIMS)
# 개인 재고관리 체계

import pymysql
import pandas as pd
import krfmt as k
import colors
import os
from pyfiglet import Figlet # ASCII 텍스트 아트 모듈

strFormat = "%s" * 5 + "\n"

invenlist = [] 
taglist = []

iims_db = pymysql.connect(
    user='root',
    passwd='Mgs_56565656',
    host='127.0.0.1',
    db='iims',
    charset='utf8'
)

cursor = iims_db.cursor(pymysql.cursors.DictCursor)

# Figlet 객체
f = Figlet(font='slant')

class Cli():
    def print_line(self):
        print("="*10)
    
    def print_title(self):  # 제목 출력
        print(f.renderText("IIMS"), end='')
        print("Individual Inventory Management System v0.0.1")
        print("Copyright (C) 2021 Gyuseong Moon")

def select_all():
    sql = "SELECT * FROM items;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)
    print(result)

def sql_excute(sql):
    cursor.excute(sql)
    cursor.commit()

def main():
    Cli().print_title()
    Cli().print_line()

    select_all()

    while True:
        userinput = input()
        if userinput == "exit":
            break

if __name__ == "__main__":
    main()