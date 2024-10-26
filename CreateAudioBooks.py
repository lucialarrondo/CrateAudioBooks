#Modules.
import pyttsx3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES
from pygame import mixer

#We create the translator object that will be used later in the code.
translator = Translator()

#We create the main window.
mw=Tk()
mw.geometry('700x500')
mw.title('Create your own audiobook')
mw.config(bg='darkgray')

#Heading of the window.
headingFrame=Frame(mw,bg='darkgray',bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel=Label(headingFrame,text='Create your own audiobook',bg='white',font=('Times',20,'bold'))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

#Taking the text from the user.
Frame1=Frame(mw,bg='darkgray')
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)
label1=Label(Frame1,text='Enter the text you want to convert to audio: ',bg='darkgray',fg='black',font=('Times',14))
label1.place(relx=0.05,rely=0.2,relheight=0.2)
ctext=StringVar()
text=Entry(Frame1,font=('Times 12'),textvariable=ctext)
text.place(relx=0.05,rely=0.4,relwidth=1,relheight=0.2)

#The user needs to pick the language that will have their audio.
Frame2=Frame(mw,bg='darkgray')
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)
label2=Label(Frame2,text='Enter the language you want your audio: ',bg='darkgray',fg='black',font=('Times',14))
label2.place(relx=0.05,rely=0.35,relheight=0.2)
menu = ttk.Combobox(state="readonly",values=list(LANGUAGES.values()))
menu.place(relx=0.6,rely=0.46,relheight=0.05,relwidth=0.2)

#The user needs to pick the accent that will have their audio.
Frame3=Frame(mw,bg='darkgray')
Frame3.place(relx=0.1,rely=0.52,relwidth=0.7,relheight=0.3)
label3=Label(Frame3,text='Enter the accent you want your audio: ',bg='darkgray',fg='black',font=('Times',14))
label3.place(relx=0.05,rely=0.52,relheight=0.2)

#The next function download and play the audiobook.
def downloadandplay():
    try:
        text_entered=text.get()
        #We use the translator object to translate the text to the language that the user want their audio.
        text2=translator.translate(text_entered,dest=menu.get())
        #We create the p object to use the pyttsx3 module and with that create the audio.
        p = pyttsx3.init()
        rate = p.getProperty('rate')
        #We change the rate of the audio, because the default one is to fast.
        p.setProperty('rate', rate - 50)
        #We call the checkbutton function.
        checkbutton(text2)
    #We use the except to make sure that the user introduce their input.
    except:
        messagebox.showinfo('Create your own audiobook', 'Wrong input, try again!')

#The next function creates two checkbuttons, so the user can pick the accent that they want their audiobooks.
def checkbutton(text2):
    p = pyttsx3.init()
    #If the users picks the english accent, the audio will play and downloaded in that accent.
    if checkbutton1.get() == 1 and checkbutton2.get() == 0:
        voices = p.getProperty('voices')
        p.setProperty('voice', voices[1].id)
        p.save_to_file(text2.text, 'audiobook.wav')
        p.runAndWait()
        mixer.init()
        sound = mixer.Sound("audiobook.wav")
        sound.play()
    # If the users picks the spanish accent, the audio will play and downloaded in that accent.
    elif checkbutton2.get() == 1 and checkbutton1.get()==0:
        voices = p.getProperty('voices')
        p.setProperty('voice', voices[0].id)
        p.save_to_file(text2.text, 'audiobook.wav')
        p.runAndWait()
        mixer.init()
        sound = mixer.Sound("audiobook.wav")
        sound.play()
    #If the user does not check any possibility, a messagebox will appear informing that they must pick one.
    elif checkbutton2.get() == 0 and checkbutton1.get() == 0:
        messagebox.showinfo('Create your own audiobook', 'You must pick a choice!')
    #If the user does check boths possibilities, a messagebox will appear informing that they must just pick one.
    else:
        messagebox.showinfo('Create your own audiobook', 'You must pick just one choice!')

#We create the button that calls the downloadandplay function.
button1=Button(mw,text='Download and play your audio',font='Times 12 bold',bg='darkred',fg='white',padx=2,command=downloadandplay)
button1.place(relx=0.32,rely=0.8,relwidth=0.35,relheight=0.05)

#We create two int variables that will be use for the checkbutton function.
checkbutton1 = IntVar()
checkbutton2 = IntVar()

#We create two checkbuttons that will be use for the checkbutton function.
button2 = Checkbutton(mw, text = 'English',variable = checkbutton1, onvalue = 1, offvalue = 0, bg='darkgray',height = 2,width = 10)
button3 = Checkbutton(mw, text = 'Spanish',variable = checkbutton2, onvalue = 1, offvalue = 0, bg='darkgray',height = 2,width = 10)
button2.place(relx=0.55,rely=0.67)
button3.place(relx=0.68,rely=0.67)

mw.mainloop()


