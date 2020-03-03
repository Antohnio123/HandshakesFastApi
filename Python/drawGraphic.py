import tkinter
import math
root = tkinter.Tk()
#   canvas.create_oval(x, y, x, y, width = 0, fill = 'white')  - рисование точки через овал
 #            canvas.create_line(x, y, x+1, y, fill="#ff0000")  - рисование точки через линию
 #   canvas.create_line(10, 10, 590, 590, fill="#ff0000")   #  просто рисуем линию
sin = math.sin(1)
HEIGHT = 600
WIDTH = 600
MENUZONEHEIGHT = 120
MENUHEIGHT = 35
MENUWIDTH = 500
IndexK:float =1                 #   коэффициент для регулирования масштаба графика
Index:float = 0.1      #   коэффициент для задания начального масштаба графика

# a*(k**s)+b*k+c - стандартная формула для графика
formula_a = "1"

# Задаем зону рисования ---------------------------
canvas = tkinter.Canvas (root, height = HEIGHT, width = WIDTH, bg = 'white')
canvas.pack()
# Координатные оси ---------------------------
def Coordinates():
    canvas.create_line(WIDTH/2,HEIGHT,WIDTH/2,0,width=1, arrow=tkinter.LAST, arrowshape="4 6 4")
    canvas.create_line(0,HEIGHT/2,WIDTH,HEIGHT/2,width=1, arrow=tkinter.LAST, arrowshape="4 6 4")
    for i in range (1, 10):   # рисуем деления на координатных прямых
        if i == 5:
            continue
        else:
            canvas.create_line(i*WIDTH/10, HEIGHT/2-3, i*WIDTH/10, HEIGHT/2+3, width=1)  # - деления на координатных осях
            canvas.create_text(i*WIDTH/10, HEIGHT/2-8, text= str(round(Index*(i*WIDTH/10-WIDTH/2),3)),font=("Verdana", "6"))  # - цифры на координатных осях
            canvas.create_line(WIDTH / 2-3, i * HEIGHT/10,  WIDTH/2+3, i * HEIGHT/10, width=1)
            canvas.create_text(WIDTH / 2 - 10,i * HEIGHT / 10, text=str(round(Index * (-i * HEIGHT / 10 + HEIGHT / 2),3)),
                               font=("Verdana", "6"))
Coordinates()
# Задаем формулу рисования графика ---------------------------

def  Draw ():
    if formula_a.get()!="":     #   исключаем ошибку, вылезающую при попытке нарисовать график при остутствии формулы
        f = formula_a.get()
        f=f.replace('x', 'n')
        for i in range (0, int(WIDTH)):
            x = i
            n=(x-WIDTH/2)*Index   #   умножение на Index тут приведёт к расширению или сужению графика по оси x
            try:    #  исключаем деление на ноль, рисовать эту точку всё равно не надо - она на оси y
                y = HEIGHT/2 - eval(f)/Index #   метод EVAL переводит string в выполняемое выражение.   Деление на Index тут происходит, чтобы изменять масштаб по y
         #   canvas.create_line(i, HEIGHT/2 - n, i+1, HEIGHT/2 - n, width=1, fill='black')  # - простая линия y = x для тестирования коэффициентов
                canvas.create_oval(x, int(y.real), x+1, int(y.real)+1, width = 1, fill = 'black')  # - сначала пришлось перевести в int float числа,  а потом методом .real ещё и отсечь комплексные
            except ArithmeticError:
                print ("Ошибка  деления на ноль при i =" + str(i))

def  Clear ():
    canvas.delete("all")  # Очищаем экран и снова рисуем координатные оси:
    Coordinates()
#------------------------------------------------------------------------------------------
def Scale():
    global Index
    Index = 0.001*scale.get()
    Clear()
    Draw()
    global textS
    textS['text'] = " Scale: now 1 pixel is " + str(Index)+ "  "


# Выделяем зону под кнопки и место ввода --------------------------------------------------------
frame2 = tkinter.Frame(root, bg = 'gray', height=MENUZONEHEIGHT) # - серое поле внизу для кнопок и переключателей
frame2.pack(side='bottom', fill = 'x')
#frame2_1 = tkinter.Frame(frame2, bg = 'gray')
#frame2_1.pack(side='left', fill = 'both')
frameF = tkinter.Frame(frame2, bg = '#e6e6e6', width = MENUWIDTH, height = MENUHEIGHT) # - первый ряд: зона ввода формулы и 2 кнопок
frameF.place(y=MENUZONEHEIGHT/7, relx=0.05)
#frame2_2 = tkinter.Frame(frame2, bg = 'gray')
#frame2_2.pack(side='left', fill = 'both')
text1 = tkinter.Label (frameF, bg = '#e6e6e6', text=" Enter a formula, use * -multyply, ** -exponent.\n math.sin(x) - sine, x**(1/2) -square root...") # - текст слева от формулы
text1.pack(side='left')
text1 = tkinter.Label (frameF, bg = '#e6e6e6', text=" y(x) = ") # - текст второй слева от формулы
text1.pack(side='left')
formula_a = tkinter.Entry (frameF)   # - поле ввода формулы
formula_a.pack(side='left')
button = tkinter.Button (frameF, text="Draw", command = Draw)
button.pack(side='left')
buttonCS = tkinter.Button (frameF, text="Clear Screen", command = Clear)
buttonCS.pack(side='right')



frameS = tkinter.Frame(frame2, bg = '#e6e6e6', width = WIDTH, height = MENUHEIGHT)     # - второй ряд: зона настройки масштаба
frameS.place(y=MENUZONEHEIGHT/2, relx=0.05)
buttonS = tkinter.Button (frameS, text="Change scale -->", command = Scale)
buttonS.pack(side='left')
scale = tkinter.Scale( frameS, orient=tkinter.HORIZONTAL, from_=1,to=301, resolution = 5)   # - вместо переменной ввёл метод, привязанный к этой переменной
scale.pack(side='left')
textS = tkinter.Label (frameS, bg = '#e6e6e6', text=" Scale: now 1 pixel is " + str(Index)+ "  ") # - указатель текущего масштаба
textS.pack(side='right')

if tkinter._default_root:
    tkinter._default_root.update()
root.mainloop()
