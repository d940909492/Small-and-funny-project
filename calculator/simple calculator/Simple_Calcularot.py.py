from tkinter import *

def button_input(input_):
    global Cal_input
    global Cal_output
    Cal_input += str(input_)
    Cal_output.set(Cal_input)

def output_Result():
    global Cal_input
    global Cal_output
    try:
        Result = str(eval(Cal_input))
        Cal_output.set(Result)
        Cal_input = Result

    except:
        Cal_output = "傻逼，正常的用,行吗?"
        Cal_input = ""


def clear():
    global Cal_input
    Cal_output.set("")
    Cal_input = ""



start = Tk()
start.title("Calculator tool")
Cal_input = ""
Cal_output = StringVar()

font_size = 80

start.geometry("400x600")
label = Label(start, text= "Simple Calculator", font = ('Arial' , 15))
label.pack()
showResult = Label(start, textvariable = Cal_output, bg = "white", width = 30, height = 2)
showResult.pack(padx = 10, pady = 10)

buttonframe = Frame(start)
buttonframe.pack()

buttonframe.columnconfigure(0,weight = 1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2, weight=1)


button1 = Button(buttonframe, text = "1", height=3, width=8, font=font_size, command = lambda : button_input(1))
button1.grid(row = 0,column = 0, sticky = NSEW)

button2 = Button(buttonframe, text = "2", height=3, width=8, font=font_size, command = lambda : button_input(2))
button2.grid(row = 0,column = 1, sticky = NSEW)

button3 = Button(buttonframe, text = "3", height=3, width=8, font=font_size, command = lambda : button_input(3))
button3.grid(row = 0,column = 2, sticky = NSEW)

button4 = Button(buttonframe, text = "4", height=3, width=8, font=font_size, command = lambda : button_input(4))
button4.grid(row = 1,column = 0, sticky = NSEW)

button5 = Button(buttonframe, text = "5", height=3, width=8, font=font_size, command = lambda : button_input(5))
button5.grid(row = 1,column = 1, sticky = NSEW)

button6 = Button(buttonframe, text = "6", height=3, width=8, font=font_size, command = lambda : button_input(6))
button6.grid(row = 1,column = 2, sticky = NSEW)

button7 = Button(buttonframe, text = "7", height=3, width=8, font=font_size, command = lambda : button_input(7))
button7.grid(row = 2,column = 0, sticky = NSEW)

button8 = Button(buttonframe, text = "8", height=3, width=8, font=font_size, command = lambda : button_input(8))
button8.grid(row = 2,column = 1, sticky = NSEW)

button9 = Button(buttonframe, text = "9", height=3, width=8, font=font_size, command = lambda : button_input(9))
button9.grid(row = 2,column = 2, sticky = NSEW)

button0 = Button(buttonframe, text = "0", height=3, width=8, font=font_size, command = lambda : button_input(0))
button0.grid(row = 3,column = 0, sticky = NSEW)

buttonadd = Button(buttonframe, text = "+", height=3, width=8, font=font_size, command = lambda : button_input('+'))
buttonadd.grid(row = 3,column = 1, sticky = NSEW)

buttonminus = Button(buttonframe, text = "-", height=3, width=8, font=font_size, command = lambda : button_input('-'))
buttonminus.grid(row = 3,column = 2, sticky = NSEW)

buttonmul = Button(buttonframe, text = "*", height=3, width=8, font=font_size, command = lambda : button_input('*'))
buttonmul.grid(row = 4,column = 0, sticky = NSEW)

buttondev = Button(buttonframe, text = "/", height=3, width=8, font=font_size, command = lambda : button_input('/'))
buttondev.grid(row = 4,column = 1, sticky = NSEW)

buttonequal = Button(buttonframe, text = "=", height=3, width=8, font=font_size, command = output_Result)
buttonequal.grid(row = 4,column = 2, sticky = NSEW)

buttondec = Button(buttonframe, text='.', height=4, width=15, font=font_size, command = lambda : button_input('.'))
buttondec.grid(row = 5,column = 0, sticky = NSEW)

buttonsquare = Button(buttonframe, text='square', height=4, width=15, font=font_size, command = lambda : button_input('**'))
buttonsquare.grid(row = 5,column = 1, sticky = NSEW)

buttonsqrt = Button(buttonframe, text='sqrt', height=4, width=15, font=font_size, command = lambda : button_input('**0.5 '))
buttonsqrt.grid(row = 5,column = 2, sticky = NSEW)

buttonframe.pack(fill = 'x')

buttonClear =  Button(start, text='clear', height=4, width=15, font=font_size, command = clear)
buttonClear.pack(padx = 5 , pady = 5)

start.mainloop()