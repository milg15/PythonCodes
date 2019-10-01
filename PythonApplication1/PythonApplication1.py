
from tkinter import *
from tkinter import ttk
import math

root = Tk()
li = []
lo = []
flg = True



def popupf():
    popup = Tk()
    popup.resizable(width=False, height=False)
    w2 = Canvas(popup, width=250, height=20)
    w2.pack()
    e = Entry(popup)
    e.pack()
    e.focus_set()
    popup.wm_title("Valor de K")
    label = ttk.Label(popup, text="Ingrese el Valor de k o alpha", font="Arial")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Homotecia", command = lambda:[homotecia(float(e.get())), popup.destroy()])
    B1.pack()
    B2 = ttk.Button(popup, text="Semejanza", command = lambda:[semejanza(float(e.get())), popup.destroy()])
    B2.pack()
    popup.mainloop()

def semejanza(k):
    global li
    for p in li[1:]:
        transformacion2(p, k)
    w.create_oval(lo[0][0]*10+497, (lo[0][1]*10-297)*-1, lo[0][0]*10+503, (lo[0][1]*10-303)*-1,
            fill="#00f")
    w.create_text(lo[0][0]*10+507, (lo[0][1]*10-307)*-1, anchor='nw', font="Arial",
         text="(" + str(round(lo[0][0],2)) + ", " + str(round(lo[0][1],2)) + ")")
    w.create_line(lo[0][0]*10+500, (lo[0][1]*10-300)*-1, lo[-1][0]*10+500, (lo[-1][1]*10-300)*-1)
    for i in range (1,len(lo)):
        w.create_oval(lo[i][0]*10+497, (lo[i][1]*10-297)*-1, lo[i][0]*10+503, (lo[i][1]*10-303)*-1,
            fill="#00f")
        w.create_text(lo[i][0]*10+507, (lo[i][1]*10-307)*-1, anchor='nw', font="Arial",
            text="(" + str(round(lo[i][0],2)) + ", " + str(round(lo[i][1],2)) + ")")
        w.create_line(lo[i-1][0]*10+500, (lo[i-1][1]*10-300)*-1, lo[i][0]*10+500, (lo[i][1]*10-300)*-1)
    print(lo)

def homotecia(k):
    global li
    for p in li[1:]:
        transformacion1(li[0], p, k)
    w.create_oval(lo[0][0]*10+497, (lo[0][1]*10-297)*-1, lo[0][0]*10+503, (lo[0][1]*10-303)*-1,
            fill="#00f")
    w.create_text(lo[0][0]*10+507, (lo[0][1]*10-307)*-1, anchor='nw', font="Arial",
         text="(" + str(round(lo[0][0],2)) + ", " + str(round(lo[0][1],2)) + ")")
    w.create_line(lo[0][0]*10+500, (lo[0][1]*10-300)*-1, lo[-1][0]*10+500, (lo[-1][1]*10-300)*-1)
    for i in range (1,len(lo)):
        w.create_oval(lo[i][0]*10+497, (lo[i][1]*10-297)*-1, lo[i][0]*10+503, (lo[i][1]*10-303)*-1,
            fill="#00f")
        w.create_text(lo[i][0]*10+507, (lo[i][1]*10-307)*-1, anchor='nw', font="Arial",
            text="(" + str(round(lo[i][0],2)) + ", " + str(round(lo[i][1],2)) + ")")
        w.create_line(lo[i-1][0]*10+500, (lo[i-1][1]*10-300)*-1, lo[i][0]*10+500, (lo[i][1]*10-300)*-1)

def transformacion1(c, p, k):
    global lo
    x = p[0]
    y = p[1]
    x = x*k - k*c[0] + c[0]
    y = y*k - k*c[1] + c[1]
    lo.append([x,y])


def transformacion2(p, k):
    global lo
    x = p[0]
    y = p[1]
    x = p[0]*math.cos(k) - p[1]*math.sin(k)
    y = p[0]*math.sin(k) + p[1]*math.cos(k)
    lo.append([x,y])    

def mb1c(event):
    if flg:
        if event.x >= 200 and not len(li):
         li.append([(event.x-500)/10,(300-event.y)/10])
         w.create_text(event.x+7, event.y+7, anchor='nw', font="Arial",
         text="[" + str((event.x-500)/10) + ", " + str((300-event.y)/10) + "]")
         w.create_text(20, 80, ancho='nw', font="Arial", text= "Centro: (" + str((event.x-500)/10) + ", " + str((300-event.y)/10) + ")" )
         w.create_oval(event.x-3, event.y-3, event.x+3, event.y+3,
            fill="#f00")
        elif event.x >= 200:
         li.append([(event.x-500)/10,(300-event.y)/10])
         w.create_text(event.x+7, event.y+7, anchor='nw', font="Arial",
         text="(" + str((event.x-500)/10) + ", " + str((300-event.y)/10) + ")")
         w.create_text(20, 80+40*len(li), ancho='nw', font="Arial",
                 text= "Punto " + str(len(li)) + ": (" + str((event.x-500)/10) + ", " + str((300-event.y)/10) + ")" )
         w.create_oval(event.x-3, event.y-3, event.x+3, event.y+3,
            fill="#000")
        if len(li) > 2:
            w.create_line(li[-2][0]*10+500,(li[-2][1]*10-300)*-1, li[-1][0]*10+500,(li[-1][1]*10-300)*-1)


def updater(event):
    if event.x >= 200 and flg:
     w.delete("upp")
     w.create_text(20, 20, anchor='nw', font="Arial",
     text="Current Pos (" + str((event.x-500)/10) + ", " + str((300-event.y)/10) + ")", tag="upp")




def mb2c(event):
    global flg
    if flg and len(li) > 3:
        flg = False
        w.delete("upp")
        w.create_line(li[-1][0]*10+500,(li[-1][1]*10-300)*-1, li[1][0]*10+500,(li[1][1]*10-300)*-1)
        popupf()
        semejanza(45)


w = Canvas(root, width=800, height=600) 

w.pack() 



root.resizable(width=False, height=False)
w.create_line(200, 0, 200, 600 ) 
w.bind("<Button-1>", mb1c)
w.bind("<Button-2>", mb2c)
w.bind("<Motion>", updater)

w.create_line(203, 300, 800, 300, dash=(7,3))  # x-axis
w.create_line(500, 3, 500, 600, dash=(7,3))    # y-axis


root.mainloop()


