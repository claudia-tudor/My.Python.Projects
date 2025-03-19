import tkinter  
import random  

random_no_tci = None  
guess_made_tci = None  

FormGuess_tci = tkinter.Tk()  
FormGuess_tci.title("Guess the Number")  
FormGuess_tci.geometry("400x200")  

def Randomize_tci():  
    global random_no_tci  
    random_no_tci = random.randint(100, 500)  
    Label_initials_Message_tci.config(text="No guess yet", fg="black", bg="white")  

def Check_tci():  
    global guess_made_tci  
    guess_made_tci = int(Text_Number_tci.get())  

    if guess_made_tci < random_no_tci:  
        Label_initials_Message_tci.config(text="Up Up Up", fg="black", bg="white")  
    elif guess_made_tci > random_no_tci:  
        Label_initials_Message_tci.config(text="Down Down Down", fg="black", bg="white")  
    else:  
        Label_initials_Message_tci.config(text="Yes Yes Yes", fg="blue", bg="yellow")  

Button_Initials_Randomize_tci = tkinter.Button(text="Generate", fg="darkgrey", bg="grey", command=Randomize_tci)  
Label_initials_Text_tci = tkinter.Label(text="Write a number", fg="blue", bg="yellow")  
Text_Number_tci = tkinter.Entry(FormGuess_tci)  
Button_Initials_Check_tci = tkinter.Button(text="Compare", fg="darkgrey", bg="grey", command=Check_tci)  
Label_initials_Message_tci = tkinter.Label(text="No guess yet", fg="green", bg="pink")  

Button_Initials_Randomize_tci.grid(row=0, column=0)  
Label_initials_Text_tci.grid(row=1, column=1)  
Button_Initials_Check_tci.grid(row=2, column=0)  
Text_Number_tci.grid(row=2, column=1)  
Label_initials_Message_tci.grid(row=3, column=1)  

FormGuess_tci.mainloop()