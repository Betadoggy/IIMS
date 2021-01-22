# Individual Inventory Management System(IIMS)
# 개인 재고관리 체계

import krfmt as k
import colors
from pyfiglet import Figlet # ASCII 텍스트 아트 모듈

strFormat = "%s" * 5 + "\n"

invenlist = [] 
statelist = ["Active", "Loaned", "Loss", "Damaged"]
taglist = []

# Figlet 객체
f = Figlet(font='slant')

class Cli():
    def print_line(self):
        print("="*10)

    def print_subjectRow(self): # 행 제목 출력
        strOut = strFormat % (k.fmt("ID", 10, 'l'), k.fmt("Name", 10, 'l'), k.fmt("Position", 10, 'l'), k.fmt("State", 10, 'l'), k.fmt("Tags", 10, 'l'))
        print(strOut, end='')
    
    def print_all(self):    # 모든 재고 출력
        Cli().print_line()
        Cli().print_subjectRow()
        for i in invenlist:
            i.print_info()
        Cli().print_line()

    def print_Title(self):  # 제목 출력
        print(f.renderText("IIMS"), end='')
        print("Individual Inventory Management System v0.0.1")
        print("Copyright (C) 2021 Gyuseong Moon")


class Inventory():
    def __init__(self, id, name, pos, state, tag):
        self.id = id        # 코드 "LL0000"(6자리)
        self.name = name    # 이름
        self.pos = pos      # 좌표 "000"(3계단: (x, y, z))
        self.state = state  # 현황
        self.tag = tag      # 태그

    def print_info(self):
        print(strFormat % (k.fmt(self.id, 10, 'l'), k.fmt(self.name, 10, 'l'), k.fmt(self.pos, 10, 'l'), k.fmt(self.state, 10, 'l'), k.fmt(self.tag, 10, 'l')), end='')


def main():
    i1 = Inventory("AA0001", "테스트1", 184, 0, "전자기기")
    invenlist.append(i1)

    i2 = Inventory("FD7161", "테스트2", 975, 3, "몰라")
    invenlist.append(i2)

    Cli().print_Title()
    Cli().print_all()

if __name__ == "__main__":
    main()