from tkinter import *
from random import *
from time import *

class Conveyor(Frame):
    def __init__(self, master, picture, width):
        super(Conveyor, self).__init__()
        self.image_number_list = [] # 셔플된 이미지의 번호를 저장하기 위한 리스트. 13개
        self.labels = [] # 컨베이어 frame에 추가되는 이미지 label 위젯의 리스트
        self.master = master # 컨베이어 frame의 parent 설정
        self.width = width # 메인 테이블의 가로 길이. = 4
        self.n = width*(width-1)+1 # 컨베이어에 넣을 이미지의 수. = 13
        self.picture = picture # app에서 생성한 이미지 받아와서 저장
        self.image_flags = list(False for i in range(self.width*self.width)) # 이미지가 컨베이어에 올라갔는지 아닌지 체크하기 위한 리스트. 초기 세팅은 모두 FALSE.
        
        self.conveyor_canvas = Canvas(self, width=55*self.n-16, height=30) # 현재 위치 표시를 위한 캔버스 위젯 생성
        # self.picture_canvas = Canvas(self, width=55*self.n, height=60, bg= 'black')

        # 컨베이어에 올릴 이미지 셔플링
        self.random_shuffle()

        for i in range(0, self.n):
            # TODO
            # 셔플 결과대로 이미지 label 생성하여 리스트에 저장
            # self.labels.append(self.picture[self.image_number_list[i]])
            self.labels.append(Label(self, image=self.picture[self.image_number_list[i]], background='black'))


        # 현재 index 설정 = 시작 위치 설정 (10번째)
        self.cur_idx = 9

        # 현재 이미지 설정 = 시작 이미지 설정
        # 선택한 이미지와 비교 목적으로 저장
        self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
        print(self.cur_image)

        # TODO
        # 캔버스 세팅
        self.conveyor_canvas.pack()
        # self.picture_canvas.pack()
        # 노란색 삼각형 생성
        self.tri_yel = self.conveyor_canvas.create_polygon((7+55*self.cur_idx, 15, 17+55*self.cur_idx, 30, 27+55*self.cur_idx, 15), fill= 'yellow', outline= 'black')
        # 빨간색 FINAL 문자열 생성
        self.fin_red = self.conveyor_canvas.create_text(14+55*(self.n-1),25, text= 'FINAL', fill= 'red', font=('bold', 9))
        # 컨베이어에 카드들 표시
        # for conv in range(self.n):
        #     self.picture_canvas.create_image(29+55*conv,32, image= self.labels[conv])
        for i in range(0, self.n):
            self.labels[i].pack(side= LEFT)





    # 이미지 셔플 함수
    def random_shuffle(self):
        # TODO
        # 0~15 숫자 중 임의로 중복되지 않는 13개의 숫자 선택
        self.image_number_list = sample(range(self.width*self.width), self.n)
        
    #event function
    def matching(self):
        if self.master.table.selected_image == self.cur_image:
            print('correct')
            self.correct_match()
        else:
            print('wrong')
            self.wrong_match()

    # 선택한 그림이 현재 위치의 그림과 일치하는 경우의 처리 함수
    def correct_match(self):
        # 마지막 이미지를 찾은 경우
        if self.cur_idx == self.n - 1:
            # TODO
            # 게임 종료
            win = True
            self.master.quit_game(win= win)


        # 캔버스 위젯
        # 현재 위치 표시 도형 우측 이동
        # 현재 이미지 및 현재 위치 재설정
        # canvas.itemconfig(도형의객체, outline='white', fill='white', + 추가적인 parameter 세팅) 기존에 생성된 도형 객체의 변경 가능
        else:
            # 현재 위치가 컨베이어의 가장 우측 도형을 지목할 때
            if self.cur_idx == self.n-2:
                # TODO
                self.conveyor_canvas.move(self.tri_yel, 55,0)
                # self.conveyor_canvas.create_text(self.fin_red)
                pass
            # 그 외 도형 이동
            else:
                # TODO
                # 노란 삼각형을 오른쪽으로 한 칸 이동
                self.conveyor_canvas.move(self.tri_yel, 55, 0)
            # TODO
            # 현재 찾을 이미지와 해당 이미지의 위치 갱신
            self.cur_idx += 1
            self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])


    # 선택한 그림이 현재 위치의 그림과 일치하지 않는 경우의 처리 함수
    def wrong_match(self):
        # 마지막 기회에서 틀린 경우
        if(self.cur_idx == 0):
            # TODO
            # 게임 종료
            win = False
            self.master.quit_game(win=win)

        # 캔버스 위젯
        # 가장 왼쪽의 이미지를 제거
        # 기존 이미지들 좌측으로 한 칸씩 이동
        # 컨베이어에 추가되지 않은 이미지 중 하나 선택하여 가장 우측에 추가
        # 현재 위치 재설정
        # canvas.itemconfig(도형의객체, outline='white', fill='white', + 추가적인 parameter 세팅) 기존에 생성된 도형 객체의 변경 가능
        else:
            # FINAL에서 오답 선택했을 때
            if self.cur_idx == self.n-1:
                # TODO
                # 노란 삼각형 복구
                self.conveyor_canvas.move(self.tri_yel, -55, 0)
            # 그 외 도형 이동
            else:
                # TODO
                # 노란 삼각형을 왼쪽으로 한 칸 이동
                self.conveyor_canvas.move(self.tri_yel, -55, 0)
            # 새 이미지 추가
            while True:
                new_image = randint(0, self.width*self.width-1)
                if new_image not in self.image_number_list :
                    break

            # 기존 이미지 좌측으로 한 칸씩 이동
            # label.config(parameter = configuration) 기존의 label 위젯 변경 가능 TODO
            for i in range(0,self.n-1):
                self.labels[i].config(image=self.picture[self.image_number_list [i+1]])
                self.image_number_list [i] = self.image_number_list [i+1]

            # # 새 이미지 추가
            self.image_number_list[self.n-1] = new_image
            self.labels[self.n-1].config(image=self.picture[self.image_number_list [self.n-1]])
        self.cur_idx -= 1
        self.cur_image = self.picture.index(self.picture[self.image_number_list[self.cur_idx]])
