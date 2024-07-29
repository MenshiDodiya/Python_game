from tkinter import *

root = Tk()
turn = 1
def show(digit):
    global turn
    if turn == 1:
        if digit == 1:
            s1.set('X')
            b1.config(state=DISABLED)
        elif digit == 2:
            s2.set('X')
            b2.config(state=DISABLED)
        elif digit == 3:
            s3.set('X')
            b3.config(state=DISABLED)
        elif digit == 4:
            s4.set('X')
            b4.config(state=DISABLED)
        elif digit == 5:
            s5.set('X')
            b5.config(state=DISABLED)
        elif digit == 6:
            s6.set('X')
            b6.config(state=DISABLED)
        elif digit == 7:
            s7.set('X')
            b7.config(state=DISABLED)
        elif digit == 8:
            s8.set('X')
            b8.config(state=DISABLED)
        elif digit == 9:
            s9.set('X')
            b9.config(state=DISABLED)

        turn = 2
    elif turn == 2:
        if digit == 1:
            s1.set('0')
            b1.config(state=DISABLED)
        elif digit == 2:
            s2.set('0')
            b2.config(state=DISABLED)
        elif digit == 3:
            s3.set('0')
            b3.config(state=DISABLED)
        elif digit == 4:
            s4.set('0')
            b4.config(state=DISABLED)
        elif digit == 5:
            s5.set('0')
            b5.config(state=DISABLED)
        elif digit == 6:
            s6.set('0')
            b6.config(state=DISABLED)
        elif digit == 7:
            s7.set('0')
            b7.config(state=DISABLED)
        elif digit == 8:
            s8.set('0')
            b8.config(state=DISABLED)
        elif digit == 9:
            s9.set('0')
            b9.config(state=DISABLED)
        turn = 1

    if s1.get() == 'X' and s2.get() == 'X' and s3.get() == 'X' or\
            s4.get() == 'X' and s5.get() == 'X' and s6.get() == 'X' or \
            s7.get() == 'X' and s8.get() == 'X' and s9.get() == 'X'  or \
            s1.get() == 'X' and s4.get() == 'X' and s7.get() == 'X' or \
            s2.get() == 'X' and s5.get() == 'X' and s8.get() == 'X' or \
            s3.get() == 'X' and s6.get() == 'X' and s9.get() == 'X' or \
            s1.get() == 'X' and s5.get() == 'X' and s9.get() == 'X' or \
            s3.get() == 'X' and s5.get() == 'X' and s7.get() == 'X' :
           #print("player1 is winner")
           #root.quit()
        l1 = Label(text="Player",font=('arial',22))
        l1.grid(row=3,column=1)
        l2 = Label(text=" 1 is ", font=('arial', 22))
        l2.grid(row=3, column=2)
        l3 = Label(text="Winner ", font=('arial', 22))
        l3.grid(row=3, column=3)


    elif s1.get() == '0' and s2.get() == '0' and s3.get() == '0' or\
            s4.get() == '0' and s5.get() == '0' and s6.get() == '0' or \
            s7.get() == '0' and s8.get() == '0' and s9.get() == '0' or\
            s1.get() == '0' and s4.get() == '0' and s7.get() == '0' or \
            s2.get() == '0' and s5.get() == '0' and s8.get() == '0' or\
            s3.get() == '0' and s6.get() == '0' and s9.get() == '0' or\
            s1.get() == '0' and s5.get() == '0' and s9.get() == '0' or\
            s3.get() == '0' and s5.get() == '0' and s7.get() == '0':
            # print("player2 is winner")
            # root.quit()
        l1 = Label(text="Player", font=('arial', 22))
        l1.grid(row=3, column=1)
        l2 = Label(text=" 2 is ", font=('arial', 22))
        l2.grid(row=3, column=2)
        l3 = Label(text="Winner ", font=('arial', 22))
        l3.grid(row=3, column=3)

    elif s1.get() != '' and s2.get() != '' and s3.get() != ''  and s4.get() != '' and s5.get() != ''\
            and s6.get() != '' and s7.get() != '' and s8.get() != '' and s9.get() != '' :
        # print("The Game is Tie")
        # root.quit()
        l1 = Label(text="The Game", font=('arial', 20))
        l1.grid(row=3, column=1)
        l2 = Label(text=" is Tie ", font=('arial', 20))
        l2.grid(row=3, column=2)


s1 = StringVar()
b1 = Button(height=3,width=10,textvariable=s1,command=lambda :show(1))
b1.grid(row=0,column=1,padx=10, pady=10)
s2 = StringVar()
b2 = Button(height=3,width=10,textvariable=s2,command=lambda :show(2))
b2.grid(row=0,column=2,padx=10, pady=10)
s3 = StringVar()
b3 = Button(height=3,width=10,textvariable=s3,command=lambda :show(3))
b3.grid(row=0,column=3,padx=10, pady=10)

s4 = StringVar()
b4 = Button(height=3,width=10,textvariable=s4,command=lambda :show(4))
b4.grid(row=1,column=1,padx=10, pady=10)
s5 = StringVar()
b5 = Button(height=3,width=10,textvariable=s5,command=lambda :show(5))
b5.grid(row=1,column=2,padx=10, pady=10)
s6 = StringVar()
b6 = Button(height=3,width=10,textvariable=s6,command=lambda :show(6))
b6.grid(row=1,column=3,padx=10, pady=10)

s7 = StringVar()
b7 = Button(height=3,width=10,textvariable=s7,command=lambda :show(7))
b7.grid(row=2,column=1,padx=10, pady=10)
s8 = StringVar()
b8 = Button(height=3,width=10,textvariable=s8,command=lambda :show(8))
b8.grid(row=2,column=2,padx=10, pady=10)
s9 = StringVar()
b9 = Button(height=3,width=10,textvariable=s9,command=lambda :show(9))
b9.grid(row=2,column=3,padx=10, pady=10)

mainloop()