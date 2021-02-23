import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbx
from tkinter.simpledialog import askinteger
import pyinputplus as iinput
import sys


def Turn(btn):
    global plays
    button = buttons[btn]
    button["state"] = "disabled"
    button["text"] = plays
    Check(btn)
    Player()
    display["text"] = plays

def Check(btn):
    RowCheck(btn)
    ColumnCheck(btn)
    Crosscheck(btn)
    Crosscheck2(btn)
    TieCheck()


def RowCheck(btn):
    global buttons, win, n

    helper = ""
    for y in range(n):
        for x in range(n):
            helper += buttons[y*n + x]["text"]
            if wino in helper:
                End("O")
            elif winx in helper:
                End("X")
        helper = ""

def ColumnCheck(btn):
    global buttons, win, n
    helper = ""
    for y in range(n):
        for x in range(n):
            helper += buttons[x*n + y]["text"]
            if wino in helper:
                End("O")
            elif winx in helper:
                End("X")
        helper = ""

def Crosscheck(btn):
    global buttons, win, n
    i = -1
    z = 0
    helper = ""
    for x in range(n+1, 0, -1):
        for y in range(0, i):
            vypocet = x + y*n
            if y > 0:
                vypocet += z

            helper += buttons[vypocet]["text"]       
            if wino in helper:
                End("O")
            elif winx in helper:
                End("X")
            z+=1
        z = 0
        i+=1
        helper = ""
    helper = ""

    for x in range(0, n):        
        helper += buttons[x + x*n]["text"]
        if wino in helper:
            End("O")
        elif winx in helper:
            End("X")

    i = -1
    z = 0
    helper = ""
    for y in range(n+1, 0, -1):
        for x in range(0, i):
            vypocet = y*n + x
            if x > 0:
                vypocet += z*n       
            helper += buttons[vypocet]["text"]       
            if wino in helper:
                End("O")
            elif winx in helper:
                End("X")
            z+=1
        z = 0
        i+=1
        helper = ""
    helper = ""

def Crosscheck2(btn):
    global buttons, win, n
    
    helper = ""
    for x in range(n):
        for y in range(n):
            vypocet = x + y*(n-1)
            helper += buttons[vypocet]["text"]
            if wino in helper:
                End("O")
            elif winx in helper:
                End("X")
            if vypocet%n == 0:
                break
        helper = ""


    helper = ""
    for x in range(n):
        for y in range(n):
            vypocet = (n*n - n) + x - y*(n-1)
            helper += buttons[vypocet]["text"]
            if wino in helper:
                End("O")
            elif winx in helper:
                End("X")
            if vypocet%n == n-1:
                break
        helper = ""
    
def TieCheck():
    x = 0
    for item in buttons:
        if item["state"] == "normal":
            break
        elif item["state"] == "disabled":
            x+= 1
         
    if x == len(buttons):
        Tie()


def Tie():
    if msgbx.askquestion(title="TIE!", message="Do you want to play antother game?") == "yes":
        window.destroy()
        main()
    else:
        exit()

def End(winner):
    if msgbx.askquestion(title=winner + " WON!", message="Do you want to play antother game?") == "yes":     
        window.destroy()   
        main()
    else:
        window.destroy()
        sys.exit()

def Player():
    global plays
    if plays == "O":
        plays = "X"
    else:
        plays = "O"

wino = ""
winx = ""



plays = "O"
buttons = []
n = 3
win = 3
window = ""
display = ""
def main():
    #background stuff
    global window, display, n, win, wino, winx
    global n, win

    #vytvoreni okna
    window = tk.Tk()
    window.title("TicTacToe")

    #userinput
    n = askinteger("Rows", "How many rows do you want?\n(min 3, max 50 due to performance issues)", minvalue=3, parent=window, maxvalue=50)    
    if n == None:
        sys.exit()
    win = askinteger("Win", "How many columns in row has to be a win?\n", minvalue=3, maxvalue=n, parent=window)
    if win == None:
        sys.exit()

    #vytvoreni dat pro kontrolu vyhry
    global wino, winx
    wino = ""
    winx = ""
    for x in range(win):
        wino += "O"
        winx += "X"
    i = 0

    #vytvoreni tlacitek
    buttons.clear()
    for x in range(n):
        for y in range(n):        
            button = tk.Button(window, width=2, command=lambda i=i:Turn(i))
            button.grid(column=(i%n), row=int(i/n))
            buttons.append(button)
            i += 1
    
    #vytvoreni displaye pro zobrazeni kdo hraje
    display = tk.Label(text=plays)
    display.grid(row=n+1)

    
    #spusteni okna
    window.mainloop()



if __name__ == "__main__":
    main()
