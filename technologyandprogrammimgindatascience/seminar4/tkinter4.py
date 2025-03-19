import tkinter  
import random  

random_number_tci = None  
guess_made_tci = None  

MainForm_tci = tkinter.Tk()  
MainForm_tci.title("Guess the Number")  
MainForm_tci.geometry("400x200")  

def Randomize_tci():  
    global random_number_tci  
    random_number_tci = random.randint(700, 1000)  
    Label_initials_Message_tci.config(text="No number yet", fg="black", bg="white")  

# Function to check the entered number  
def Check_tci():  
    global guess_made_tci  
    guess_made_tci = int(Text_Number_tci.get())  

    if guess_made_tci < random_number_tci:  
        Label_initials_Message_tci.config(text="Upper", fg="black", bg="white")  
    elif guess_made_tci > random_number_tci:  
        Label_initials_Message_tci.config(text="Lower", fg="black", bg="white")  
    else:  
        Label_initials_Message_tci.config(text="You are right", fg="white", bg="red")  

Button_Initials_Randomize_tci = tkinter.Button(text="Set", fg="darkgrey", bg="grey", command=Randomize_tci)  
Label_initials_Text_tci = tkinter.Label(text="Take a guess", fg="blue", bg="yellow")  
Text_Number_tci = tkinter.Entry(MainForm_tci)  
Button_Initials_Check_tci = tkinter.Button(text="Verify", fg="darkgrey", bg="grey", command=Check_tci)  
Label_initials_Message_tci = tkinter.Label(text="No number yet", fg="green", bg="pink")  

Button_Initials_Randomize_tci.grid(row=0, column=0)  
Label_initials_Text_tci.grid(row=1, column=1)  
Button_Initials_Check_tci.grid(row=2, column=0)  
Text_Number_tci.grid(row=2, column=1)  
Label_initials_Message_tci.grid(row=3, column=1)  

MainForm_tci.mainloop()