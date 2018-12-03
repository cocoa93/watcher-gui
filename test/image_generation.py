# -*- coding: UTF-8 -*-
################################
################################
# 모듈명    : image_generation.py
# 작성자    : 서혜리
# 설명      : 5초마다 랜덤으로 포스이미지를 생성하여 출력하는 테스팅용 gui 프로그램. input.txt파일을 같은 디렉토리 안에 넣어야 작동함
################################
################################


import tkinter as tk
from random import *
from PIL import Image, ImageDraw

root = tk.Tk()
root.title('이미지 보기')
root.geometry('800x350')

def imageGen():
    f = open('input.txt', 'r')
    #fw = open('output.txt', 'w')
    winy, winx = map(int, f.readline().split())
    seat_w, seat_h = map(int, f.readline().split())

    #fw.write("%d %d\n" % (winy, winx))
    #fw.write("%d %d\n" % (seat_w, seat_h))

    image = Image.new("RGB", (winx, winy), (0, 0, 0))
    draw = ImageDraw.Draw(image)

    for i in range(42):
        x, y = map(int, f.readline().split())
        # fw.write("%d %d\n" % (x, y))
        num = f.readline().split()

        for j in num:
            col = randint(1, 2)

            if j == '0':
                colrgb = (0, 0, 0)
                col = 0
            elif col == 1:
                colrgb = (67, 65, 66)
            else:
                colrgb = (64, 132, 34)
            #fw.write("%d " % col)

            draw.rectangle([(x, y), (x + seat_w, y + seat_h)], fill=colrgb)

            x = x + 3 + seat_w

        #fw.write("\n")
    f.close()
    #fw.close()
    filename = "random_generated.png"
    image.save(filename)

def image_update():
    imageGen()
    img.config(file="random_generated.png")
    lbl.config()
    root.after(5000,image_update)


img = tk.PhotoImage()
lbl = tk.Label(image=img)
lbl.image = img  # 레퍼런스 추가
lbl.place(x=0, y=0)
root.after(1000, image_update)
root.mainloop()
