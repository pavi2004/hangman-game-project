import os
from tkinter.filedialog import askdirectory

import pygame
from mutagen.id3 import ID3
from tkinter import *
from PIL import Image,ImageTk
root = Tk()
#root.minsize(300,300)

root.geometry('230x250')
root.config(bg="#101357")

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=15,fg="white",bg="#101357")

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname


def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname


label = Label(root,text='Music Player',bg="#101357",fg="white")
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()




previousbutton = Button(root,text = 'Previous Song',bg="#101357",fg="white")
previousbutton.pack(side=LEFT)

stopbutton = Button(root,text='Stop Music',bg="#101357",fg="white")
stopbutton.pack(side=LEFT, padx = 3)

nextbutton = Button(root,text = 'Next Song',bg="#101357",fg="white")
nextbutton.pack(side=LEFT,padx = 3)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
nextbutton.bind("<Button-1>",nextsong)

songlabel.pack()

root.mainloop()
