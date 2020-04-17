from datetime import date
from tkinter import *
import time

x=0
o=0
score=[[5,5,5],[5,5,5],[5,5,5]]
click=0
def int():
    global score
    global click
    #time.sleep(1)
    score=[[5,5,5],[5,5,5],[5,5,5]]
    click=0
    dis=''
    d1.config(text=dis)
    d2.config(text=dis)
    d3.config(text=dis)
    d4.config(text=dis)
    d5.config(text=dis)
    d6.config(text=dis)
    d7.config(text=dis)
    d8.config(text=dis)
    d9.config(text=dis)
   
def end():
    root=Tk()
    global x
    global o
    root.title("Zero Cross")
    root.geometry('400x400')

    if x>o:
        string="X WIN"
    elif x==o:
        string="DRAW"
    else:
        string="O WIN"
    lbl = Label(root, text=string,font=("Arial Bold", 35), fg=colfg)
    lbl.place(x=150,y=150)
    

    windows.destroy()
    root.mainloop()
def do1():

    global score
    global click
    
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'
   
    score[0][0]=dis
    d1.config(text=dis)
    check()
    if click==9:
        time.sleep(1)
        int()
    
def do2():
    
    global score
    global click
    
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'
    score[0][1]=dis
    d2.config(text=dis)
    check()
    if click==9:
        time.sleep(1)
        int()


        
def do3():
    
    global score
    global click

    
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'
    score[0][2]=dis
    d3.config(text=dis)
    check()
    if click==9:


        time.sleep(1)
        int()


        
def do4():
    
    global score
    global click
    
    click+=1

    if click%2==0:
        dis='X'
    else:
        dis='O'

    score[1][0]=dis
    d4.config(text=dis)
    check()
    if click==9:
        time.sleep(1)
        int()

def do5():

    global score
    global click
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'
    score[1][1]=dis
    d5.config(text=dis)

    check()
    if click==9:
        time.sleep(1)
        int()
 
def do6():
    
    global score
    global click
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'

   # dis='X'if click%2==0 else 'O'
    score[1][2]=dis
    d6.config(text=dis)
    check()
    if click==9:
        time.sleep(1)
        int()
    
def do7():
    
    global score
    global click
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'
    dis='X'if click%2==0 else 'O'
    score[2][0]=dis
    d7.config(text=dis)
    check()
    if click==9:
        int()
    
  

        
def do8():
    
    global score
    global click
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'

    score[2][1]=dis
    d8.config(text=dis)
    
    check()
    if click==9:
        time.sleep(1)
        int()


        
def do9():
    global score
    global click
    click+=1
    if click%2==0:
        dis='X'
    else:
        dis='O'
    score[2][2]=dis
    d9.config(text=dis)

    
    if click==9:
        time.sleep(1)
        int()
def update():
    sx.config(text=str(x))
    so.config(text=str(o))
    int()
def check():
    global score
    global o
    global x
    if score[0][0]==score[0][1] and score[0][0]==score[0][2]: #1
        if score[0][0]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[0][0]=='O':

            o+=1
            time.sleep(1)
            update()
    elif score[1][0]==score[1][1] and score[1][0]==score[1][2]: #2
        if score[1][0]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[1][0]=='O':
            o+=1
            
            time.sleep(1)
            update()
    elif score[2][0]==score[2][1] and score[2][1]==score[2][2]: #3
        if score[2][0]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[2][0]=='O':
            o+=1
            time.sleep(1)
            update()
    elif score[2][0]==score[1][0] and score[1][0]==score[0][0]:#4
        if score[2][0]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[2][0]=='O':
            o+=1
            time.sleep(1)
            update()
    elif score[2][1]==score[1][1] and score[1][1]==score[0][1]:#5
        if score[2][1]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[2][1]=='O':
            o+=1
            time.sleep(1)
            update()

    elif score[2][2]==score[1][2] and score[1][2]==score[0][2]:#6
        if score[2][2]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[2][2]=='O':
            o+=1
            time.sleep(1)
            update()
    elif score[0][2]==score[1][1] and score[1][1]==score[2][0]:#7
        if score[1][1]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[1][1]=='O':
            o+=1
            time.sleep(1)
            update()
    elif score[0][0]==score[1][1] and score[2][2]==score[1][1]:#8
        if score[0][0]=='X':
            x+=1
            time.sleep(1)
            update()
        if score[0][0]=='O':
            o+=1
            time.sleep(1)
            update()
    

windows = Tk()
score=[[5,5,5],[5,5,5],[5,5,5]]
click=0
windows.title("Zero Cross")
windows.geometry('800x800')
colfg='#1abc9c'
lbl = Label(windows, text="Zero Cross",font=("Arial Bold", 35), fg=colfg)
lbl.place(x=300,y=50)
a=100
b=300

e1 = Button(windows,font=("Arial Bold",35) ,bg='#1abc9c', fg='#ecf0f1',width=3,command=do1)
e1.place(x=a,y=b)
d1 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d1.place(x=a,y=b)

e2 = Button(windows,font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3,command=do2)
e2.place(x=a+100,y=b)
d2 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d2.place(x=a+100,y=b)
e3 = Button(windows,font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3,command=do3)
e3.place(x=a+200,y=b)
d3 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d3.place(x=a+200,y=b)
e4 = Button(windows,font=("Arial Bold",35) ,bg='#1abc9c', fg='#ecf0f1',width=3,command=do4)
e4.place(x=a,y=b+100)
d4 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d4.place(x=a,y=b+100)
e5 = Button(windows,font=("Arial Bold",35),bg='#1abc9c', fg='#ecf0f1',width=3,command=do5)
e5.place(x=a+100,y=b+100)
d5 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d5.place(x=a+100,y=b+100)
e6 = Button(windows,font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3,command=do6)
e6.place(x=a+200,y=b+100)
d6 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d6.place(x=a+200,y=b+100)
e7 = Button(windows,font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3,command=do7)
e7.place(x=a,y=b+200)
d7 = Label(windows,font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1')
d7.place(x=a,y=b+200)
e8 = Button(windows,font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3,command=do8)
e8.place(x=a+100,y=b+200)
d8 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3)
d8.place(x=a+100,y=b+200)
e9 = Button(windows,font=("Arial Bold",35) ,bg='#1abc9c', fg='#ecf0f1',width=3,command=do9)
e9.place(x=a+200,y=b+200)
d9 = Label(windows, font=("Arial Bold",35), bg='#1abc9c', fg='#ecf0f1',width=3)
d9.place(x=a+200,y=b+200)
b2=Button(windows,text='Exit',font=("Arial Bold", 10), bg=colfg, fg='#ecf0f1',command=end)
b2.place(x=550,y=600)

sx = Label(windows, text=str(x),font=("Arial Bold", 35), fg=colfg)
sx.place(x=500,y=250)
so = Label(windows, text=str(o),font=("Arial Bold", 35), fg=colfg)
so.place(x=600,y=250)
lbl = Label(windows, text='X',font=("Arial Bold", 35), fg=colfg)
lbl.place(x=500,y=200)
lb2 = Label(windows, text='O',font=("Arial Bold", 35), fg=colfg)
lb2.place(x=600,y=200)

windows.mainloop()


