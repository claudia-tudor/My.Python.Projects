import tkinter
Form_tci=tkinter.Tk()
Form_tci.title("Compare form")
Form_tci.geometry("600x250") 

def compare_number():
    if int(Text_first_tci.get())<int(Text_second_tci.get()):
        Label_result_tci.config(text="First number is smaller than the second")
    elif int(Text_first_tci.get())>int(Text_second_tci.get()):
        Label_result_tci.config(text="First number is bigger than the second")
    else:
        Label_result_tci.config(text="First number is equal to the second")
        
Label_first_tci=tkinter.Label(text="Enter first number" , fg="blue" , bg="yellow")
Label_second_tci=tkinter.Label(text="Enter second number" , fg="green" , bg="pink")
Text_first_tci=tkinter.Entry(Form_tci)
Text_second_tci=tkinter.Entry(Form_tci)
Button_compare_tci=tkinter.Button(text="Compare" , fg="darkgrey" , bg="grey" , command=compare_number)
Label_result_tci=tkinter.Label(text="Result" , fg="orange" , bg="azure")

Label_first_tci.grid(row=0, column=0)
Text_first_tci.grid(row=0, column=1)
Label_second_tci.grid(row=1, column=0)
Text_second_tci.grid(row=1, column=1)
Button_compare_tci.grid(row=2, column=0)
Label_result_tci.grid(row=2, column=1)

Form_tci.mainloop()
