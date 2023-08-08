from tkinter import *
from tkinter import ttk
import re
import random
import pyglet
from tinytag import TinyTag
import os


first_way='music/'
root = Tk()
root.title("Stick Player")
root.geometry()
root.option_add("*tearOff", FALSE)
root.resizable(False, False)
a = os.listdir(first_way)
number_song=0

way=first_way+a[number_song]
tag = TinyTag.get(way)
sound = pyglet.media.load(way, streaming=False)

player = pyglet.media.Player()

STOPPED = False

data=0.6

def print_time():
    label_name['text']= player.time    
     
def play_music():
    player.play()
    get_name_song()
    get_add_song()
    #print_time()
    
def next_song():
    global number_song, way, tag, sound, player
    if enabled.get() == 1:
        number_song=random.randint(0, len(a))
    else:
        number_song-=1
    try:
        way=first_way+a[number_song]
    except:
        number_song=0
        way=first_way+a[number_song]
    tag = TinyTag.get(way)
    sound = pyglet.media.load(way, streaming=False)
    player = pyglet.media.Player()
    player.queue(sound)
    play_music()
    
def previous_song():
    global number_song, way, tag, sound, player
    if enabled.get():
        number_song=random.randint(0, len(a))
    else:
        number_song-=1
    try:
        way=first_way+a[number_song]
    except:
        number_song=0
        way=first_way+a[number_song]
    tag = TinyTag.get(way)
    sound = pyglet.media.load(way, streaming=False)
    player = pyglet.media.Player()
    player.queue(sound)
    play_music()
    
def play_pause():
    player.pause()

def volume_edit(*args):
    player.volume=round(val.get(),2)
    label_text_volume_b['text']=player.volume
    
def go_to():
    global data
    data = entry.get()
    player.seek(int(data))
    
def directory():
    global first_way
    first_way=input('Путь к папке с музыкой: ')
    
def get_name_song():
    label_name['text']=str(tag.title)+' - '+str(tag.artist)
    
def get_add_song():
    label_add['text']=str(round(tag.duration,2))+' sec | '+'Samplerate: '+str(tag.samplerate)+' | '+str(tag.bitrate)+' kBits/s | '+str(tag.channels)+' channel | '+ str(tag.year)
   
val = DoubleVar(value=0.5)
enabled=IntVar()


player.queue(sound)

btn_play=ttk.Button(text='Play', command=play_music)
btn_play.grid(row=0, column=1)

btn_next=ttk.Button(text='<- Previos', command=previous_song)
btn_next.grid(row=0, column=3)

btn_next=ttk.Button(text='Next ->', command=next_song)
btn_next.grid(row=0, column=4)

btn_pause=ttk.Button(text='Pause', command=play_pause)
btn_pause.grid(row=0, column=2)

volume = ttk.Scale(orient=HORIZONTAL, length=100, from_=0.0, to=1.0, variable=val)
volume.grid(row=0, column=6)

enabled_checkbutton = ttk.Checkbutton(text="Random", variable=enabled)
enabled_checkbutton.grid(row=0, column=10)

btn_fl=ttk.Button(text='Open...', command=directory)
btn_fl.grid(row=0, column=11)

btn_goto=ttk.Button(text='Go to', command=go_to)
btn_goto.grid(row=0, column=8)

label_name = ttk.Label(text='')
label_name.grid(row=1, column=0, columnspan=6)

label_add = ttk.Label(text='')
label_add.grid(row=1, column=6, columnspan=6)

entry=ttk.Entry(width=10)
entry.grid(row=0, column=9)

label_text_volume=ttk.Label(text='Volume: ')
label_text_volume.grid(row=0, column=5)

label_text_volume_b=ttk.Label(text='0.5')
label_text_volume_b.grid(row=0, column=7)

if player.playing: print(player.time)

val.trace_add("write", volume_edit)

root.mainloop()
pyglet.app.run()
