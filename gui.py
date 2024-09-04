from tkinter import *
from tkinter import messagebox, simpledialog

window = Tk()
window.title('Log In')
window.geometry('925x500+300+200')
window.configure(bg="pink")
window.resizable(False,False)

b = 150

def inc(b):
    b += 20
    return b

def signin():
    username=user.get()
    userpassword=code.get()
    
    if username =='admin' and userpassword=='1234': 
        screen = Toplevel(window)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="beige")
        b = 150
        def add_post():
            global b 
            b = inc(b)
            txt = simpledialog.askstring("Post", "Enter your post")
            Label(screen,bg='pink',font=('Times New Roman',12,'bold'),text=txt).place(x=600, y=b)
        mybutton = Button(screen,image=img)
        mybutton.place(x=70,y=80)
        Label(screen,text='Hello, Welcome To Vilter! Post your memories and keep track of your thoughts.',bg='beige',fg='#db97f0', font=('Calibri(Body)',18,'bold')).place(x=80,y=30)
        post = Button(screen,text='Post',fg='purple',bg='pink', font=('Times New Roman',18,'bold'),command=add_post)
        post.place(x=600,y=90)
        screen.mainloop()

    elif username != 'admin' and userpassword != '1234': 
        messagebox.showerror("Invalid","Invalid username and password")

    elif userpassword != "1234":
        messagebox.showerror("Invalid","Invalid password")

    elif username != "admin":
        messagebox.showerror("Invalid","Invalid username")

img2 = PhotoImage(file='camera.widgetlogo2.png')
label1 = Label(window,image=img2,bg=('white')).place(x=60,y=60)

frame = Frame(window,width=350,height=350,bg="pink")
frame.place(x=480,y=70)

heading = Label(frame,text='Log in',fg='#57a1f8',bg='pink',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
################-------------------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name=user.get()
    if name == '':
        user.insert(0, 'Username')
        
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#################--------------------------------------------

def on_enter(e):
    code.delete(0, 'end')
 
def on_leave(e):
    name=code.get()
    if code == '':
        code.insert(0, 'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
############################----------------------------------

img= PhotoImage(file='login2.png')

Button(frame,width=39,pady=7,text='Log in',bg='#57a1f8',fg='white',border=0, command=signin).place(x=35,y=204)

def CreateAcc():
    messagebox.showinfo("Account Created", "Details sucessfully captured. Your account will be created in the next 24 hours.")

def sign_up():
    screen1 = Toplevel(window)
    screen1.title("Sign Up")
    screen1.geometry('925x500+300+200')
    screen1.config(bg="pink")
    Label(screen1,text='Sign up to Vilter and create your account.',bg='pink',font=('Calibri(Body)',20,'bold')).place(x=0,y=0)
    Label(screen1,text='Create your username: ').place(x=50,y=50)   
    create_user = Entry(screen1,width=39, border=0)
    create_user.place(x=250,y=50)

    Label(screen1, text='Create your password: ').place(x=50,y=100) 
    create_psw = Entry(screen1,width=39,border=0)
    create_psw.place(x=190,y=100)

    def check_fields():
        if create_user.get() == '' or create_psw.get() == '':
            messagebox.showerror("Error", "Both fields must be filled")
        else:
            CreateAcc()

    acc = Button(screen1,width=39, text='Create Account',border=0,command=check_fields)
    acc.place(x=140,y=150)

    screen1.mainloop()

signup = Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command= sign_up)
signup.place(x=215,y=270) 
label = Label(frame, text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)
 
window.mainloop()