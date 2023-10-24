import tkinter as tk #it imports tkinter 
root = tk.Tk() #creates a new window
root.geometry("500x500") #creates the window with that specific dimensions ('X*Y')
root.title("Calculator") #enter the string as title
label = tk.Label(root,text='Calculator',font=('Arial',20))#it creates a label 
label.pack(padx=30,pady=30)#it adds the label to window with pad x means distance from top
textbox = tk.Text(root,height=3,font=('bold',15))#it creates a text box
textbox.pack(padx=20,pady=10)#it adds the textbox to windows
#button = tk.Button(root,text="Calculate!",font=('bold',15))#it creates a button
#button.pack(padx=10,pady=10)#it adds the button to window
buttonframe = tk.Frame(root)#it creates a button frame (a group of buttons places so that button can be added in future)
buttonframe.columnconfigure(0,weight=1)#it creates a space for button 1
buttonframe.columnconfigure(1,weight=1)#it creates space for button 2
buttonframe.columnconfigure(2,weight=1)#it creates space for button 3
btn1 = tk.Button(buttonframe,text="+",font=("bold",10))#it creates button 1
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)#it adds button to its place
btn2 = tk.Button(buttonframe,text="-",font=("bold",10))#it creates button 1
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)#it adds button to its place
btn3 = tk.Button(buttonframe,text="x",font=("bold",10))#it creates button 1
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)#it adds button to its place
btn4 = tk.Button(buttonframe,text="/",font=("bold",10))#it creates button 1
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)#it adds button to its place
btn5 = tk.Button(buttonframe,text="//",font=("bold",10))#it creates button 1
btn5.grid(row=2,column=0, sticky=tk.W+tk.E)#it adds button to its place
btn6 = tk.Button(buttonframe,text="%",font=("bold",10))#it creates button 1
btn6.grid(row=3,column=0, sticky=tk.W+tk.E)#it adds button to its place
buttonframe.pack()
root.mainloop()#it will launch the created window
