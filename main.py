import tkinter as tk

window = tk.Tk()
#window.title("Hello wold")
#window.geometry("300x300")

def button_click(number):
  current=textw.get()
  textw.delete(0,'end')
  textw.insert(0,current+str(number))

def button_clear():
  textw.delete(0,'end')

def button_add():
  global number1
  number1 = textw.get()
  textw.delete(0,'end')
  

def button_equal():
  number2=textw.get()
  sumnumb=int(number1) + int(number2)
  textw.delete(0,'end')
  textw.insert(0,sumnumb)

textw=tk.Entry()
textw.grid(row=0,column=0, columnspan=3)




button1 = tk.Button(text="1",padx=30,pady=10,command=lambda :button_click(1))
button2 = tk.Button(text="2",padx=30,pady=10,command=lambda :button_click(2))
button3 = tk.Button(text="3",padx=30,pady=10,command=lambda : button_click(3))

button4 = tk.Button(text="4",padx=30,pady=10,command=lambda : button_click(4))
button5 = tk.Button(text="5",padx=30,pady=10,command=lambda : button_click(5))
button6 = tk.Button(text="6",padx=30,pady=10,command=lambda : button_click(6))

button7 = tk.Button(text="7",padx=30,pady=10,command=lambda : button_click(7))
button8 = tk.Button(text="8",padx=30,pady=10,command=lambda : button_click(8))
button9 = tk.Button(text="9",padx=30,pady=10,command=lambda : button_click(9))

button0 = tk.Button(text="0",padx=30,pady=10,command=lambda : button_click(0))


button_clear=tk.Button(text="Clear",padx=60,pady=10,command=button_clear)

button_add=tk.Button(text="+",padx=30,pady=10,command=button_add)
button_equal=tk.Button(text="=",padx=70,pady=10,command=button_equal)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

'''
def button_click():
  label1=tk.Label(text=textw.get())
  label1.pack()


textw=tk.Entry()
textw.pack()
hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!",command=button_click)
button.pack()
'''


#for i in range 10:
 


tk.mainloop()