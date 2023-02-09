from tkinter import *
import fnmatch,os,pygame
from pygame import mixer
from tkinter import filedialog,ttk
from PIL import ImageTk

r1=Tk()
r1.title('Music Player')
r1.geometry('400x300+325+100')
r1.config(bg='#90EE90')
r1.resizable(False,False)
mixer.init()
rootpath=filedialog.askdirectory()

lbox=Listbox(r1,fg='black',bg='#90EE90',width=40,height=9,font=('times new roman',14))
lbox.pack(padx=20,pady=20)
lbox.place(x=10,y=10)

lbl=Label(r1,text='',bg='#90EE90',fg='Black',font=('times new roman',14))
lbl.place(x=450,y=250)

top=Frame(r1,bg='#90EE90').pack(padx=10,pady=5,anchor='center')

previmg=PhotoImage(file='previous.png')
nextimg=PhotoImage(file='next.png')
pauseimg=PhotoImage(file='pause.png')
playimg=PhotoImage(file='play.png')
stopimg=ImageTk.PhotoImage(file='stop.jpg')
muteimg=PhotoImage(file='mute.png')

def play():
    lbl.config(text=lbox.get('active'))
    mixer.music.load(rootpath + "\\" + lbox.get('active'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    lbox.select_clear('active')

def pause():
    if pausebtn["text"]=="Pause":
        mixer.music.pause()
        pausebtn["text"]="Play"
    else:
        mixer.music.unpause()
        pausebtn["text"]="Pause"

def next():
    global next_song_name
    next_song=lbox.curselection()
    next_song=next_song[0]+1
    next_song_name=lbox.get(next_song)
    lbl.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    lbox.select_clear(0,'end')
    lbox.activate(next_song)
    lbox.select_set(next_song)

def prev():
    next_song=lbox.curselection()
    next_song=next_song[0]-1
    next_song_name=lbox.get(next_song)
    lbl.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    lbox.select_clear(0,'end')
    lbox.activate(next_song)
    lbox.select_set(next_song)

def mute():
    if  pygame.mixer.music.get_volume()==0:
        pygame.mixer.music.set_volume(1)
    else:
        pygame.mixer.music.set_volume(0)

prevbtn=Button(r1,text='Prev',image=previmg,bd=0,command=prev)
prevbtn.place(x=80,y=225)
playbtn=Button(r1,text='play',image=playimg,bd=0,command=play)
playbtn.place(x=140,y=225)
pausebtn=Button(r1,text='Stop',image=pauseimg,bd=0,command=pause)
pausebtn.place(x=200,y=225)
Nextbtn=Button(r1,text='Next',image=nextimg,bd=0,command=next)
Nextbtn.place(x=260,y=225)
stopbtn=Button(r1,text='Stop',image=stopimg,bd=0,command=stop)
stopbtn.place(x=320,y=225)
mutebtn=Button(r1,text='Mute',image=muteimg,bd=0,command=mute)
mutebtn.place(x=20,y=225)

for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,'*.mp3'):
        lbox.insert('end',filename)

r1.mainloop()