import Connect
from tkinter import *
from tkinter.ttk import *
import xml.etree.ElementTree as ET
import folium
import googlemaps

class Interface:
    line_list = []
    #country_list = []
    def sendmail(self):
        pass

    def __init__(self):
        #======= 구글 지도 api key ========
        self.__key = "AIzaSyDyJvpUNI8aZh0pPu-SRG-HBdDbxwyg4Tw"
        #==================================

        self.tem=  Connect.CarrerNetPassing()
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.title("너의 편입은? Fly")

        self.bgimage = PhotoImage(file='resource\\bg.png') #<- 이미지를 마음에 드는걸로 바꾸면됨 :)
        self.canvas = Canvas(self.window, width=1280, height=720)
        self.canvas.create_image(0,0,anchor=NW, image=self.bgimage)
        self.canvas.pack()


        self.canvas.create_line(300, 0, 300, 730)
        self.canvas.create_line(0, 250, 300, 250)
        #self.canvas.create_line(0, 350, 300, 350)

        self.canvas.create_line(500, 0, 500, 730)
        self.canvas.create_line(300, 150, 500, 150)

        self.canvas.create_line(300, 400, 500, 400)

# ----------------------------------- 여긴 계열 선택 ----------------------------------------------\
        self.brand = ["전체", "인문계열", "사회계열", "교육계열", "공학계열", "자연계열", "의약계열", "예체능계열"]
        self.str1 = StringVar()
        self.str1.trace('w', self.changeDepartment)
        self.canvas.create_text(40, 40, text="계열")
        self.line_select = Combobox(self.window, state='readonly', textvariable=self.str1, values=self.brand)
        self.line_select.place(x=100, y=30)

# ----------------------------------- 여긴 학과 선택 ----------------------------------------------
        self.canvas.create_text(40, 80, text="학과")
        self.department_select = Combobox(self.window)
        self.department_select['value'] = self.line_list  # 학과를 xml로 로드해서 가져와야함 (리스트로 받는다)
        self.department_select.place(x=100, y=70)

#----------------------------------- 여긴 OO도 선택지역 ----------------------------------------------
        self.canvas.create_text(40, 120, text="지역-도")
        self.region_select = Combobox(self.window)
        self.region_select['value'] = ("서울특별시", "인천광역시", "부산광역시", "대전광역시", "대구광역시", "광주광역시", "울산광역시", "경기도",
                                       "충청북도", "충청남도", "경상북도", "경상남도", "강원도", "전라북도", "전라남도", "제주도")
        self.region_select.place(x=100, y=110)

#----------------------------------- 여긴 OO시 선택지역 ---------------------------------------------
        self.canvas.create_text(40, 160, text="지역-시")
        self.country_select = Combobox(self.window)
        self.country_select['value'] = None
        self.country_select.place(x=100, y=150)



#----------------------------------- 여긴 지도임 -------------------------------------------------

        self.temp_find = u'한국산업기술대학교'
        self.gmaps = googlemaps.Client(key=self.__key)
        self.geo = self.gmaps.geocode(self.temp_find, language='ko')
        print(self.geo)


        self.gmail_image = PhotoImage(file='resource\\gmail.png')
        self.gmailButton = Button(self.window, image=self.gmail_image, width=10,command=self.sendmail)
        self.gmailButton.place(x=1225, y=0)

# ----------------------------------- 여긴 지도임 -------------------------------------------------

        self.show_resultButton=Button(self.window,text='검색', width=10, command=self.showResult)
        self.show_resultButton.place(x=180, y=200)

        self.window.mainloop()



    def changeDepartment(self, index, value, op):
        self.temp = self.tem.getUniversiryInfo_line(self.line_select.current())
        tree = ET.ElementTree(ET.fromstring(self.temp))
        note = tree.iter('facilName')
        self.line_list.clear()
        for elt in tree.iter('facilName'):
            temp = [x for x in elt.text.split(',')]
            for i in temp:
                self.line_list.append(i)

        self.department_select['value'] = self.line_list

    def showResult(self):
        pass


Interface()
