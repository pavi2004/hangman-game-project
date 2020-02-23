from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random
from PIL import Image,ImageTk


def start():
    global root 
    root = Tk()

    load11=Image.open('start.png')

    photos=ImageTk.PhotoImage(load11)
    button = Button(root, image=photos,command = game) 
    button.grid(column = 0 , row = 2)

    root.mainloop()

def game():
    root.destroy()
    global window
    window=Tk()
    window.title("Hangman")
    window.config(bg="white")


    wordlist=["ANT","APPLE","PYTHON","HAPPY","WELCOME","CODEIT","CAT","ABOUT", "ABOVE","ACROSS", "ACT", "ACTOR", "ACTIVE", "ACTIVITY", "ADD", "AFRAID", "AFTER", "AGAIN", "AGE","AGREE", "AIR", "ALONE", "ALONG", "ALREADY", "ALWAYS","AMOUNT", "ANGRY", "ANOTHER", "ANSWER", "ANY", "APPEAR", "APPLE", "AREA", "ARM", "ARMY","ART","ASK", "ATTACK", "BABY",  "BACK", "BAD", "BAG", "BALL", "BANK", "BASKET", "BATH", "BEAR", "BEAUTIFUL","BED", "BEDROOM", "BEGIN","BELL", "BEST", "BIG", "BIRD", "BIRTH", "BIRTHDAY", "BITE", "BLACK", "BLOCK", "BLOOD", "BLUE", "BOARD", "BOAT", "BODY", "BOIL", "BONE", "BOOK", "BORDER", "BORN", "BORROW", "BOTTLE", "BOTTOM", "BOWL", "BOX", "BOY","BROTHER","CAKE", "CALL", "CAN", "CANDLE", "CAP", "CAR", "CARD", "CARE","CARRY", "CASE","CATCH", "CENTURY", "CHAIR", "CHANCE", "CHANGE", "CHASE", "CHEAP", "CHEESE", "CHICKEN", "CHILD", "CHOCOLATE","DANCE", "DANGER", "DARK", "DAUGHTER", "DAY", "DEAD","DECIDE", "DEER", "DESK", "DESTROY", "DEVELOP", "DIE","DINNER", "DIRECTION", "DIRTY", "DISCOVER", "DISH","DOG", "DOOR","DRAW", "DREAM", "EAR", "EARLY", "EARN", "EARTH", "EAST", "EASY", "EAT", "EGG", "EIGHT","FACE", "FACT", "FAIL", "FALL", "FALSE", "FAMILY", "FAMOUS", "FAR", "FARM", "FATHER", "FEAR","GAME", "GARDEN", "GATE", "GENERAL","GET", "GIFT", "GIVE", "HALF", "HALL", "HAMMER", "HAND", "HAT", "ICE", "IDEA", "IMPORTANT","JELLY", "JOB", "JOIN", "JUICE", "JUMP","KEEP", "KEY", "KID", "KILL","LADDER", "LADY", "LAMP", "LAND", "LARGE","LAUGH","MACHINE", "MAIN", "MAKE", "MALE", "MAN", "MANY","MAP","MOTHER","NAME", "NARROW", "NATION", "NATURE", "NEAR", "NECK", "NEED","OBEY", "OBJECT", "PAGE", "PAIN", "PAINT","QUEEN", "QUESTION", "QUICK", "QUIET", "RADIO", "RAIN", "READ","SAD", "SAFE", "SAIL", "SALT","SISTER", "TEA", "TEACH", "TEAM", "TEAR", "TELEPHONE","UNDER","UNIT", "USEFUL", "USUAL","VEGETABLE", "VERY", "VILLAGE", "VOICE", "VISIT","WAIT", "WAKE", "WALK", "WANT", "WARM", "WASH", "WASTE", "WATCH", "WATER","YEAR", "YELLOW", "YES", "YESTERDAY", "YET", "ZERO", "ZOO", "ZOOM"]

    load1=Image.open('0.jpg')
    load2=Image.open('1.jpg')
    load3=Image.open('2.jpg')
    load4=Image.open('3.jpg')
    load5=Image.open('4.jpg')
    load6=Image.open('5.jpg')
    load7=Image.open('6.jpg')
    load8=Image.open('7.jpg')
    load9=Image.open('8.jpg')
    load10=Image.open('9.jpg')
    load11=Image.open('10.jpg')

    photos=[ImageTk.PhotoImage(load1),ImageTk.PhotoImage(load2),ImageTk.PhotoImage(load3),ImageTk.PhotoImage(load4),ImageTk.PhotoImage(load5),ImageTk.PhotoImage(load6),ImageTk.PhotoImage(load7),ImageTk.PhotoImage(load8),ImageTk.PhotoImage(load9),ImageTk.PhotoImage(load10),ImageTk.PhotoImage(load11)]
    imageLabel=Label(window,image=photos[0])
    imageLabel.grid(row=1,column=0,columnspan=5)
    Label(window,text="Find the word!!",font=("Arial Bold", 30),bg="white",fg="grey").grid(row=0,column=0,columnspan=9)
    def newGame():
        global theWordWithSpace
        global numberOfGuesses
        numberOfGuesses=0
        imageLabel.config(image=photos[0])
        theword=random.choice(wordlist)
        theWordWithSpace=" ".join(theword)
        lblword.set(" ".join("_"*len(theword)))
    
    def guess(letter):
        global numberOfGuesses
        if numberOfGuesses<=10:
            txt=list(theWordWithSpace)
            print(txt)
            guessed=list(lblword.get())
            if theWordWithSpace.count(letter)>0:
                for i in range(len(txt)):
                    if txt[i]==letter:
                        guessed[i]=letter
                        lblword.set("".join(guessed))
                        if lblword.get()==theWordWithSpace:
                            messagebox.showinfo("Hangman","you guessed it")
                            newGame()
                            
            else:
                numberOfGuesses+=1
                imageLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==10:
                    messagebox.showinfo("Hangman","game over")

    n=0
    for c in ascii_uppercase:
        Button(window,text=c,command=lambda c=c:guess(c),width=4,bg="white").grid(row=2+n//9,column=n%9)
        n+=1     
        
        Button(window,text="new",command=lambda :newGame(),width=4,bg="white").grid(row=4,column=8)
        lblword=StringVar()
        Label(window,textvariable=lblword,bg="white").grid(row=1,column=4,columnspan=5,padx=10,pady=20)
    Button(window,text="Exit",command=end,width=50,bg="white").grid(row=5,column=0,columnspan=9)   
    newGame()
    window.mainloop() 

def end():
    window.destroy()
start()
