from tkinter import *
from tkinter import messagebox
import re

#Login Widgets
def myLogin():
    global login_window
    login_window=Tk()
    login_window.title("LOGIN")

    #SPACES
    myEmptyLabel = Label(login_window, text="", pady=30)
    myEmptyLabel.grid(row=0, column=0)

    #LOGIN
    myLogin_ = Label(login_window, text="Login", font=("Arial", 20, "bold"), pady=10)
    myLogin_.grid(row=1, column=0, columnspan=4)
 

    myEmptyLabel2 = Label(login_window, text="")
    myEmptyLabel2.grid(row=2, column=0, padx=15)

    #USERNAME
    myUsername = Label(login_window, text="Username", font=("Arial", 12))
    myUsername.grid(row=2, column=1, sticky=W)


    #ENTER USERNAME
    login_username=Entry(login_window, width=40)
    login_username.grid(row=3, column=1,  columnspan=2, sticky=E)
    myEmptyLabel3 = Label(login_window, text="")
    myEmptyLabel3.grid(row=3, column=3, padx=15)

    #PASSWORD
    myPassword = Label(login_window, text="Password", font=("Arial", 12))
    myPassword.grid(row=4, column=1, sticky=W)

    #ENTER PASSWORD
    login_pass=Entry(login_window, width=40, show="*")
    login_pass.grid(row=5, column=1,  columnspan=2, sticky=E)
    myEmptyLabel4 = Label(login_window, text="", padx=15)
    myEmptyLabel4.grid(row=6, column=0, columnspan=3)

    #LOGIN BUTTON
    login_button=Button(login_window, text="Login", padx=10, bg="#00FFFF", command=showSuccesfull_Login)
    login_button.grid(row=7, column=1, columnspan=2, sticky=W+E)
    myEmptyLabel5 = Label(login_window, text="")
    myEmptyLabel5.grid(row=8, column=0, padx=10, pady=30)
    myEmptyLabel6 = Label(login_window, text="", pady=15)
    myEmptyLabel6.grid(row=9, column=0, columnspan=3)


   # create the "Register Now" button and pass the list of widgets to myRegister
    regNow = Button(login_window, text="Register Now", font=("Arial", 10), fg="#00AEA5", borderwidth=0, highlightthickness=0, command=myRegister)
    regNow.grid(row=9, column=1, columnspan=2)

    
def myRegister():
    global e_username, e_pass, e_con_pass, e_email, reg_window, login_window
    login_window.destroy()
    reg_window = Tk()
    reg_window.title("REGISTRATION")
       #SPACES
    myEmptyLabel = Label(reg_window, text="", pady=5)
    myEmptyLabel.grid(row=0, column=0)

    # #LOGIN
    myLogin = Label(reg_window, text="Registration", font=("Arial", 20, "bold"), pady=10)
    myLogin.grid(row=1, column=0, columnspan=4, sticky="W"+"E")
 

    myEmptyLabel2 = Label(reg_window, text="")
    myEmptyLabel2.grid(row=2, column=0, padx=15)

    #USERNAME
    myUsername = Label(reg_window, text="Username", font=("Arial", 12))
    myUsername.grid(row=2, column=1, sticky=W)
    myEmptyLabel3 = Label(reg_window, text="")
    myEmptyLabel3.grid(row=3, column=3, padx=15)

    # ENTER USERNAME
    e_username=Entry(reg_window, width=40)
    e_username.grid(row=3, column=1,  columnspan=2, sticky=E)

    #PASSWORD
    myPassword = Label(reg_window, text="Password", font=("Arial", 12))
    myPassword.grid(row=4, column=1, sticky=W)

    #ENTER PASSWORD
    e_pass=Entry(reg_window, width=40, show="*")
    e_pass.grid(row=5, column=1,  columnspan=2, sticky=E)

    #CONFIRM PASSWORD
    myConfirmPassword = Label(reg_window, text="Confirm Password", font=("Arial", 12))
    myConfirmPassword.grid(row=6, column=1, sticky=W)

    #ENTER CONFIRM PASSWORD
    e_con_pass=Entry(reg_window, width=40, show="*")
    e_con_pass.grid(row=7, column=1,  columnspan=2, sticky=E)
    
    
    #EMAIL
    myEmail = Label(reg_window, text="Email", font=("Arial", 12))
    myEmail.grid(row=8, column=1, sticky=W)

    #ENTER EMAIL
    e_email=Entry(reg_window, width=40)
    e_email.grid(row=9, column=1,  columnspan=2, sticky=E)
    myEmptyLabel4 = Label(reg_window, text="", pady=15)
    myEmptyLabel4.grid(row=10, column=0, columnspan=3)


     #LOGIN BUTTON
    login_button=Button(reg_window, text="Login", padx=10, bg="#00FFFF", command= lambda: validating_Login_Reg(e_username.get(), e_pass.get(), e_con_pass.get(), e_email.get()))
    login_button.grid(row=11, column=1, columnspan=2, sticky=W+E)
    myEmptyLabel5 = Label(reg_window, text="")
    myEmptyLabel5.grid(row=12, column=0, padx=10, pady=30)

    backLogin = Button(reg_window, text="Back to Login", font=("Arial", 10), fg="#00AEA5", borderwidth=0, highlightthickness=0, command=return_login_page)
    backLogin.grid(row=13, column=1, columnspan=2)
    myEmptyLabel6 = Label(reg_window, text="", pady=15)
    myEmptyLabel6.grid(row=14, column=0, columnspan=3)
  


def return_login_page():
    reg_window.destroy()
    myLogin()

def success_login():
    global button_to_login
    button_to_login.destroy()
    myLogin()


#Auto Remove Invalid if User Type
def reset_color(event):
        if e_username.get() == "\u26A0\ufe0f Invalid UserName":
            e_username.delete(0, END)
            e_username.config(fg="black")
        if e_pass.get()== "\u26A0\ufe0f Should contain at least 6 characters":     
            e_pass.config(fg="black")
            e_pass.delete(0, END)

#For Validation of Account
def validating_Login_Reg(username, password, con_pass, email):
     global warning_Emoji 
     valid_username=True
     valid_pass=True
     valid_confirm_pass=True
     valid_email=True
     pattern = r'^[a-zA-Z0-9_]{6,20}$'
     if not re.search(pattern, username):
         e_username.delete(0, END)
         e_username.insert(0, "\u26A0\ufe0f Invalid UserName")
         e_username.config(fg="red", borderwidth=0, highlightthickness=0)
         valid_username=False
     else:
       valid_username=True
     pattern = r'^[a-zA-Z0-9_]{6,20}$'
     if not re.search(pattern, password):
         e_pass.delete(0, END)
         e_pass.config(show="")
         e_pass.insert(0, "\u26A0\ufe0f Should contain at least 6 characters")
         e_pass.config(fg="red", borderwidth=0, highlightthickness=0)

         valid_pass=False
     else:
       valid_pass=True
    
     if password != con_pass:
         e_con_pass.delete(0, END)
         e_con_pass.config(show="")
         e_con_pass.insert(0, "\u26A0\ufe0f Password Not Match")
         e_con_pass.config(fg="red", borderwidth=0, highlightthickness=0)
         valid_confirm_pass= False
     email_pattern=r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
     if not re.search(email_pattern, email):
         e_email.delete(0, END)
         e_email.config(show="")
         e_email.insert(0, "\u26A0\ufe0f Invalid Email Address")
         e_email.config(fg="red", borderwidth=0, highlightthickness=0)
         valid_email= False
    
    
     e_username.bind("<Key>", reset_username)
     e_pass.bind("<Key>", reset_pass)
     e_con_pass.bind("<Key>", reset_con_pass)
     e_email.bind("<Key>", reset_email)

     if valid_username and valid_pass and valid_confirm_pass and valid_email:
        showSuccesfull_Registation()

#Auto Remove Invalid if User Type
def reset_username(event):
        if e_username.get() == "\u26A0\ufe0f Invalid UserName":
            e_username.delete(0, END)
            e_username.config(fg="black")

#Auto Remove Invalid if User Type
def reset_pass(event):
            if e_pass.get()== "\u26A0\ufe0f Should contain at least 6 characters":     
                e_pass.config(fg="black", show="*")
                e_pass.delete(0, END)

 #Auto Remove Invalid if User Type   
def reset_con_pass(event):
     if e_con_pass.get()== "\u26A0\ufe0f Password Not Match":
            e_con_pass.delete(0, END)
            e_con_pass.config(fg="black", show="*")

#Auto Remove Invalid if User Type
def reset_email(event):
        if e_email.get() == "\u26A0\ufe0f Invalid Email Address":
            e_email.delete(0, END)
            e_email.config(fg="black")

 #Successful Login Page   
def showSuccesfull_Login():
    global login_window, success_login_window
    login_window.destroy()
    success_login_window=Tk()
    success_login_window.title("Successfully Login")
    myInfo_emoji = Label(success_login_window, text="\u24D8\ufe0f ", font=("Arial", 20, "bold"),pady=10)
    myInfo_emoji.grid(row=0, column=0)
    Success_Login_Text=Label(success_login_window, text="Successfully Login'", font=("Arial", 16, "bold"))
    Success_Login_Text.grid(row=1, column=1)
    myEmptyLabel = Label(success_login_window, text="        ", font=("Arial", 20, "bold"),pady=10)
    myEmptyLabel.grid(row=0, column=2)
    myEmptyLabel1=Label(success_login_window, text="", padx=20)
    myEmptyLabel1.grid(row=1, column=2)
    ok_button=Button(success_login_window, text="OK", padx=10, command=success_login_window.quit)
    ok_button.grid(row=3, column=1)
    myEmptyLabel2 = Label(success_login_window, text="")
    myEmptyLabel2.grid(row=4, column=0, padx=10, pady=5)

 #Successful Registration Page 
def showSuccesfull_Registation():
    global reg_window,success_reg_window
    reg_window.destroy()
    success_reg_window=Tk()
    success_reg_window.title("Registered Successfully")
    myInfo_emoji = Label(success_reg_window, text="\u24D8\ufe0f ", font=("Arial", 20, "bold"),pady=10)
    myInfo_emoji.grid(row=0, column=0)
    Success_Login_Text=Label(success_reg_window, text="Registered Successfully'", font=("Arial", 16, "bold"))
    Success_Login_Text.grid(row=1, column=1)
    myEmptyLabel = Label(success_reg_window, text="        ", font=("Arial", 20, "bold"),pady=10)
    myEmptyLabel.grid(row=0, column=2)
    myEmptyLabel1=Label(success_reg_window, text="", padx=20)
    myEmptyLabel1.grid(row=1, column=2)
    ok_button=Button(success_reg_window, text="OK", padx=10, command=button_Reg_to_Login)
    ok_button.grid(row=3, column=1)
    myEmptyLabel2 = Label(success_reg_window, text="")
    myEmptyLabel2.grid(row=4, column=0, padx=10, pady=10)

#After Registered Move Back to Login Page
def button_Reg_to_Login():
    global success_reg_window, button_to_login
    success_reg_window.destroy()
    button_to_login=Tk()
    button_to_login.title("Return To Login")
    myInfo_emoji = Label(button_to_login, text="\u24D8\ufe0f", font=("Arial", 20, "bold"))
    myInfo_emoji.grid(row=0, column=0)
    Success_Login_Text = Label(button_to_login, text="Return To Login", font=("Arial", 16, "bold"))
    Success_Login_Text.grid(row=1, column=1)
    myEmptyLabel = Label(button_to_login, text="        ", font=("Arial", 20, "bold"))
    myEmptyLabel.grid(row=0, column=2)
    myEmptyLabel1 = Label(button_to_login, text="", padx=20)
    myEmptyLabel1.grid(row=1, column=2)
    ok_button = Button(button_to_login, text="OK", padx=10, command=success_login)
    ok_button.grid(row=3, column=1)
    myEmptyLabel2 = Label(button_to_login, text="")
    myEmptyLabel2.grid(row=4, column=0)

    

myLogin()
login_window.mainloop()