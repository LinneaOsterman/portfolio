from tkinter import *
from pygame import mixer
from random import randint, choice

# create the main window
top = Tk()
top.title("Math Game")
top.geometry("600x400")

# set column and row configurations for layout
top.columnconfigure([0,1,2,3,4], minsize=120, weight=1)
top.rowconfigure([0,1,2,3,4], minsize=100, weight=1)

# load and display the background image (generated with AI)
bg = PhotoImage(file = "background_mathgame.png")
bgLabel = Label(top, image = bg)
bgLabel.place(x = 0, y = 0)

# initialize mixer for sound effects
mixer.init()

# load joy sounds and a fail sound (sounds from pixabay.com by Shut_Up_Ghost, UNIVERSFIELD and Pixabay)
yaySounds = [mixer.Sound("windoot.wav"), mixer.Sound("game-bonus.wav"), mixer.Sound("cha-ching.wav"), mixer.Sound("cartoon-yay.wav"), mixer.Sound("funny-yay.wav"), mixer.Sound("yay2.wav"), mixer.Sound("yay.wav")]
failSound = mixer.Sound("wahwah.wav")

# check the answer and update counters
def checkAnswer(event):
    if int(answer.get()) == int(number1.cget("text")) + int(number2.cget("text")):
        # play a random joy sound for correct answer
        choice(yaySounds).play()
        answer.delete(0,"end")
        global rights
        rights += 1
        rightsLabel.config(text=f"Right answers: {rights}")
        newNumbers()
    else:
        # play a failure sound for incorrect answer
        failSound.play()
        answer.delete(0,"end")
        global wrongs
        wrongs += 1
        wrongsLabel.config(text=f"Wrong answers: {wrongs}")

# generates new summables, performed after every correct answer
def newNumbers():
    number1.config(text=randint(0,11))
    number2.config(text=randint(0,11))

# guide text for the user
guideText = Label(top, text="Count and enter the sum in the box",fg="white",bg="black", font=("Century Gothic", 15))
guideText.grid(row=0, column=0, columnspan=5, sticky=S)

# labels for summables and the addition sign
number1 = Label(top, text=f"{randint(0,11)}",fg="white",bg="black", font=("Century Gothic", 35))
number1.grid(row=1, column=1)
number2 = Label(top, text=f"{randint(0,11)}",fg="white",bg="black", font=("Century Gothic", 35))
number2.grid(row=1, column=3)
plus = Label(top, text="+", fg="white", bg="black", font=("Century Gothic", 30))
plus.grid(row=1, column=2)

# counters for right and wrong answers
rights = 0
rightsLabel = Label(top, text=f"Right answers: {rights}", fg="white", bg="black", font=("Century Gothic", 10))
rightsLabel.grid(row=2, column=3, columnspan=2)
wrongs = 0
wrongsLabel = Label(top, text=f"Wrong answers: {wrongs}", fg="white", bg="black", font=("Century Gothic", 10))
wrongsLabel.grid(row=3, column=3, columnspan=2, sticky=N)

# entry box for answers / user input
answer = Entry(fg="black",bg="pink", font=("Century Gothic", 20))
answer.grid(row=2, column=2)

# button for checking the answers
checkButton = Button(text="Check answer",bg="white",fg="black")
checkButton.bind("<Button-1>", checkAnswer)
checkButton.grid(row=3, column=2, sticky=N)

# bind enter key to check the answer
top.bind('<Return>', checkAnswer)

# start the main event loop
top.mainloop()
