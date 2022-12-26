from tkinter import *
import winsound
import pygame
from tkVideoPlayer import TkinterVideo

pygame.mixer.init()

def openNew():
    new =Toplevel()
    new.title("毁灭画面")
    new.geometry("1000x1000")
    label2 = Label(new , text = "毁灭")
    label2.pack()
    videoplayer = TkinterVideo(master=new, scaled=True)
    videoplayer.load(r"destory.mp4")
    videoplayer.pack(expand=True, fill="both")

    videoplayer.play()

def countdown(x):
    times['text'] = x
    times.pack(padx = 5, pady= 20)
    if x > 0:
        root.after(1000, countdown, x - 1)
    if x == 0:
        times['text'] = "世界已经毁灭了!!!!!"
        openNew()

def play():
    countdown(5)
    pygame.mixer.music.load("countdown.wav")
    pygame.mixer.music.play()

root = Tk()
root.title("世界毁灭程序")
root.geometry("400x500")


label = Label(root)
label['text'] = "毁灭世界"
label.pack(padx = 0 , pady = 20)

times = Label(root , font = 50)

button = Button(text="确定", font = 50  , command = play)
button.pack()

root.mainloop()
