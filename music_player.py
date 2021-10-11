from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pygame
import keyboard
import sys
w = Tk()
#w.geometry("290x200")
w.title("Music player")
w.configure(bg="#222222")
#w.resizable(False)

pygame.init()
pygame.mixer.init()

def open_file():
    global file_open
    file_open = filedialog.askopenfilename()
    
    playing = Label(w, text="Currently Playing: "+ file_open, font="None 12 bold", bg="#222222", fg="white")
    playing.grid(row=0, column=0)

    pygame.mixer.music.load(file_open)
    
def play_button():
    pygame.mixer.music.play()

def pause():
    #if keyboard.is_pressed("space"):
    pygame.mixer.music.pause()
    
def resume():
    #if keyboard.is_pressed("Enter")
    pygame.mixer.music.unpause()
def exit():
    sys.exit()

a1 = Button(w, text="Open file", command=open_file, width=10, height=2, font="None 12 bold") 
a1.grid(row=1, column=0, padx=100)
a2 =Button(w, text="Play", command=play_button, width=10, height=2, font="None 12 bold") 
a2.grid(row=2, column=0, padx=100)
a3 =Button(w, text="Pause", command=pause, width=10, height=2, font="None 12 bold") 
a3.grid(row=3, column=0, padx=100)
a4 =Button(w, text="Resume", command=resume, width=10, height=2, font="None 12 bold") 
a4.grid(row=4, column=0, padx=100)



w.mainloop()



