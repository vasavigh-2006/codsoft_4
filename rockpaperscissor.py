import tkinter as tk
import random
from tkinter import messagebox

root=tk.Tk()
root.geometry("360x360")
root.title("Rock paper Scissors")


label=tk.Label(root,text="WELCOME TO ROCK PAPER SCISSORS!!",font=("Verdana",12))
label.pack()
label=tk.Label(root,text=" ",font=("Verdana",10))
label.pack(padx=10)


choices=["Rock","Paper","Scissor"]
playerscore=0
compscore=0
total=10

label=tk.Label(root,text="Choose among rock paper and scissors",font=("Verdana",10))
label.pack(padx=10)
label=tk.Label(root,text=" ",font=("Verdana",10))
label.pack(padx=10)

playerlabel = tk.Label(root, text="Your Score: 0", font=("Verdana", 10))
playerlabel.pack(padx=10)
complabel = tk.Label(root, text="Computer score: 0", font=("Verdana", 10))
complabel.pack(padx=10)
resultlabel = tk.Label(root, text="", font=("Verdana", 10))
resultlabel.pack(pady=10)
def restart():
    global playerscore,compscore
    playerscore=0
    compscore=0
    resultlabel.config(text="Resetting game")
    complabel.config(text=f"Computer Score :{compscore}")
    playerlabel.config(text=f"Your Score :{playerscore}")

def announcewinner():
    global playerscore,compscore
    if playerscore>=total:
        messagebox.showinfo(title= "Game Over",message=f"\n Game over Your points is {playerscore},\n You win the round")
        restart()
    elif compscore>=total:
        messagebox.showinfo(title=" Game Over",message=f"\n Game over Computer points is {compscore},\n Computer wins the round")
        restart()
       

   
def play(playerchoice):
    global playerscore,compscore
    compchoice=random.choice(choices)
    display=f"\n Your chose {playerchoice} and the computer chose {compchoice}."
    
    
    if playerchoice==compchoice:
        display+="\n Its a draw !!"
    elif(playerchoice=="Rock" and compchoice=="Scissor")or(playerchoice=="Paper" and compchoice=="Rock")or(playerchoice=="Scissor" and compchoice=="Paper"):
        display+="\n Congratulations You win!!"
        playerscore+=1
    else:
        display+="\n Computer wins!!"
        compscore+=1
    resultlabel.config(text=display)
    complabel.config(text=f"Computer Score :{compscore}")
    playerlabel.config(text=f"Your Score :{playerscore}")

    announcewinner()

def closing():
    m=messagebox.askyesnocancel("Exit", "Do you want to exit from the game?")
    if m is True:
        root.destroy()  
  

for choice in choices:
    button=tk.Button(root,text=choice,font=("Arial",10),width="10",bg="yellow",command= lambda c= choice:play(c))
    button.pack(pady=5)


root.protocol("WM_DELETE_WINDOW", closing)
root.mainloop()
