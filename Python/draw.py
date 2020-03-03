import tkinter
import math

HEIGHT = 800
WIDTH = 800
MENUZONEHEIGHT = 100
MENUHEIGHT = 35
MENUWIDTH = 400
a=1
b=0
c=0
s=2   #   степень, в которую возводистя x
Index=1
root = tkinter.Tk()


# Задаем зону рисования ---------------------------
canvas = tkinter.Canvas (root, height = HEIGHT, width = WIDTH, bg = 'white')
canvas.pack()
# Координатные оси ---------------------------
canvas.create_line(WIDTH/2,HEIGHT,WIDTH/2,0,width=1)
canvas.create_line(0,HEIGHT/2,WIDTH,HEIGHT/2,width=1)

# Задаем формулу рисования графика ---------------------------

def  Draw ():
    for i in range (0, WIDTH*Index):
        x = i / Index
        k=(x-WIDTH/2)
        y = HEIGHT/2 - (a*(k**s)+b*k+c)/Index  #   умножение на Index тут происходит, чтобы увеличить масштаб
        canvas.create_line(i, HEIGHT/2 - k, i+1, HEIGHT/2 - k, width=1, fill='black')  # - простая линия y = x для тестирования коэффициентов
        canvas.create_oval(x, y, x+1, y+1, width = 1, fill = 'black')



#   canvas.create_oval(x, y, x, y, width = 0, fill = 'white')  - рисование точки через овал
 #            canvas.create_line(x, y, x+1, y, fill="#ff0000")  - рисование точки через линию
 #   canvas.create_line(10, 10, 590, 590, fill="#ff0000")   #  просто рисуем линию




# Выделяем зону под кнопки и место ввода ---------------------------
#frame1 = tkinter.Frame(root, bg = '#b3d9ff')
#frame1.pack (side='top', fill = 'both')
frame2 = tkinter.Frame(root, bg = 'gray', height=MENUZONEHEIGHT)
frame2.pack(side='bottom', fill = 'x')
#frame2_1 = tkinter.Frame(frame2, bg = 'gray')
#frame2_1.pack(side='left', fill = 'both')
frameF = tkinter.Frame(frame2, bg = '#e6e6e6', width = MENUWIDTH, height = MENUHEIGHT)
frameF.place(y=MENUZONEHEIGHT/2.5, relx=0.5)
#frame2_2 = tkinter.Frame(frame2, bg = 'gray')
#frame2_2.pack(side='left', fill = 'both')s
text1 = tkinter.Label (frameF, bg = '#e6e6e6', text="   Push a button to draw a graphic ")
text1.pack(side='left')
#formula_a = tkinter.Entry (frameF)
#formula_a.pack(side='left')    #  - тут должно было быть место для ввода формулы или отдельных коэффициентов, но Питон отказался переводить string во float
button = tkinter.Button (frameF, text="Draw", command = Draw)
button.pack(side='right')
#, command=Draw





if tkinter._default_root:
    tkinter._default_root.update()
root.mainloop()
