from imagebtn import *
from tkinter import *
from random import *
import time
import pandas as pd

class Maintable(Frame):
    n = 0
    selected_image = 0
    
    def __init__(self, master, picture, alphabet, width):
        super(Maintable, self).__init__()
        self.image_number_list = []  # 셔플된 이미지의 번호를 저장하기 위한 리스트. 16개
        self.master = master # maintable frame의 parent 설정
        self.width = width # maintable의 넓이. = 4
        self.n = width * width # maintable에 추가될 이미지 수. = 16
        self.picture = picture # app에서 생성한 이미지 받아와서 저장
        self.alphabet = alphabet

        self.button_canvas = Canvas(self, width=105*self.width, height= 105*self.width)
        self.button_canvas.pack()

        # 숨겨진 이미지 셔플링
        self.random_shuffle()

        self.Buttons = pd.DataFrame(index= range(width), columns= range(width))
        for i in range(0,self.width):
            for j in range(0,self.width):
                # TODO
                # ImageButton widget 생성하고 각 widget에 숨겨진 이미지 추가
                self.Buttons[j][i] = ImageButton(parent= self) #create a button
                self.Buttons[j][i].add_hidden(self.alphabet[self.image_number_list[4*i+j]], self.picture[self.image_number_list[4*i+j]]) #attach a letter and a picture
                self.Buttons[j][i].config(image= self.Buttons[j][i].alphabet)
                self.Buttons[j][i].place(x=10+100*i, y=10+100*j)
                # 이미지 클릭시 이벤트 bind
                self.Buttons[j][i].bind('<ButtonPress-1>', self.show_hidden)
                self.Buttons[j][i].bind('<ButtonRelease-1>', self.hide_picture)


    def random_shuffle(self):
        # TODO
        # hidden 이미지 셔플링
        self.image_number_list = list(range(self.n))
        shuffle(self.image_number_list)


    # 선택된 알파벳 ImageButton의 숨겨진 이미지 출력
    def show_hidden(self, event):
        event.widget.config(image=event.widget.get_hidden())
        Maintable.selected_image = self.picture.index(event.widget.hidden)
        # Bind the mouse click event to the triangle


    def hide_picture(self, event):
        time.sleep(0.5)
        # TODO
        # 카드를 알파벳이 보이게 되돌려 놓음
        # # 뒤집은 카드가 찾는 카드일 경우 또는 그렇지 않을 경우의 처리
        if Maintable.selected_image == self.master.conveyor.cur_image:
            pass
        else:
            event.widget.config(image= event.widget.alphabet)

        self.master.conveyor.matching()




