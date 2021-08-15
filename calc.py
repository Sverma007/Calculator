from tkinter import * 

window = Tk()
window.geometry("375x6000")
window.minsize(375,600)
window.maxsize(375,600)
window.config(bg="gray")
window.title("Calculator")
icon = PhotoImage(file= 'icon.png')
window.iconphoto(False,icon)


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == 'C':
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get() + text )
        screen.update()

scvalue = StringVar()
scvalue.set("")
f= Frame(window,padx=20,pady=20)
screen = Entry(f,textvar= scvalue,font= "lucida 50 bold",bg = 'light blue')
screen.pack(fill= X, padx=20,pady= 15)
f.pack()

options1 = ["7", "8", "9","C"]
options2 = ["4", "5", "6","*"]
options3 = ["1", "2", "3","-"]
options4 = ["0", "/", "+","="]

f= Frame(window, bg = "gray",padx=20,pady=10)
for i in options1:
    b=Button(f,text=i,padx=10,pady=10,font ="lucide 20 bold")
    b.pack(side=LEFT, padx= 10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

f= Frame(window, bg = "gray",padx=20,pady=10)
for i in options2:
    b=Button(f,text=i,padx=10,pady=10,font = "lucide 20 bold")
    b.pack(side=LEFT, padx= 10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

f= Frame(window, bg = "gray",padx=20,pady=10)
for i in options3:
    b=Button(f,text=i,padx=10,pady=10,font ="lucide 20 bold")
    b.pack(side=LEFT, padx= 10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

f= Frame(window, bg = "gray",padx=20,pady=10)
for i in options4:
    b=Button(f,text=i,padx=10,pady=10,font ="lucide 20 bold")
    b.pack(side=LEFT, padx= 10,pady=10)
    b.bind("<Button-1>",click)
f.pack()

label1= Label(window,text="Calculator Designed By Suneet Verma",font = "roboto 8 italic",bg='gray',fg='white')
label1.place(x=85,y=580)

window.mainloop()