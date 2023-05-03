from tkinter import *
import re
root = Tk()

#Login Widgets
def myLogin():
    root.title("LOGIN")

    #SPACES
    myEmptyLabel = Label(root, text="", pady=30)
    myEmptyLabel.grid(row=0, column=0)

    #LOGIN
    myLogin_ = Label(root, text="Login", font=("Arial", 20, "bold"), pady=10)
    myLogin_.grid(row=1, column=0, columnspan=4)
 

    myEmptyLabel2 = Label(root, text="")
    myEmptyLabel2.grid(row=2, column=0, padx=15)

    #USERNAME
    myUsername = Label(root, text="Username", font=("Arial", 12))
    myUsername.grid(row=2, column=1, sticky=W)


    #ENTER USERNAME
    login_username=Entry(root, width=40)
    login_username.grid(row=3, column=1,  columnspan=2, sticky=E)
    myEmptyLabel3 = Label(root, text="")
    myEmptyLabel3.grid(row=3, column=3, padx=15)

    #PASSWORD
    myPassword = Label(root, text="Password", font=("Arial", 12))
    myPassword.grid(row=4, column=1, sticky=W)

    #ENTER PASSWORD
    login_pass=Entry(root, width=40, show="*")
    login_pass.grid(row=5, column=1,  columnspan=2, sticky=E)
    myEmptyLabel4 = Label(root, text="", padx=15)
    myEmptyLabel4.grid(row=6, column=0, columnspan=3)

    #LOGIN BUTTON
    login_button=Button(root, text="Login", padx=10, bg="#00FFFF", command=lambda: showSuccesfull_Login(widgets))
    login_button.grid(row=7, column=1, columnspan=2, sticky=W+E)
    myEmptyLabel5 = Label(root, text="")
    myEmptyLabel5.grid(row=8, column=0, padx=10, pady=30)
    myEmptyLabel6 = Label(root, text="", pady=15)
    myEmptyLabel6.grid(row=9, column=0, columnspan=3)


   # create the "Register Now" button and pass the list of widgets to myRegister
    regNow = Button(root, text="Register Now", font=("Arial", 10), fg="#00AEA5", borderwidth=0, highlightthickness=0, command=lambda: myRegister(widgets))
    regNow.grid(row=9, column=1, columnspan=2)

    # store the widgets created in this function in a list
    widgets = [ myEmptyLabel, myLogin_, myEmptyLabel2, myUsername, login_username, myEmptyLabel3, myPassword, login_pass, myEmptyLabel4, login_button, myEmptyLabel5, myEmptyLabel6, regNow]

    # return the list of widgets for later use
    return widgets

def myRegister(widgets):
    root.title("REGISTRATION")
    global e_username, e_pass, e_con_pass, e_email
    # destroy each widget in the list
    for widget in widgets:
        widget.destroy()
     
     
       #SPACES
    myEmptyLabel = Label(root, text="", pady=5)
    myEmptyLabel.grid(row=0, column=0)

    # #LOGIN
    myLogin = Label(root, text="Registration", font=("Arial", 20, "bold"), pady=10)
    myLogin.grid(row=1, column=0, columnspan=4, sticky="W"+"E")
 

    myEmptyLabel2 = Label(root, text="")
    myEmptyLabel2.grid(row=2, column=0, padx=15)

    #USERNAME
    myUsername = Label(root, text="Username", font=("Arial", 12))
    myUsername.grid(row=2, column=1, sticky=W)
    myEmptyLabel3 = Label(root, text="")
    myEmptyLabel3.grid(row=3, column=3, padx=15)

    # ENTER USERNAME
    e_username=Entry(root, width=40)
    e_username.grid(row=3, column=1,  columnspan=2, sticky=E)

    #PASSWORD
    myPassword = Label(root, text="Password", font=("Arial", 12))
    myPassword.grid(row=4, column=1, sticky=W)

    #ENTER PASSWORD
    e_pass=Entry(root, width=40, show="*")
    e_pass.grid(row=5, column=1,  columnspan=2, sticky=E)

    #CONFIRM PASSWORD
    myConfirmPassword = Label(root, text="Confirm Password", font=("Arial", 12))
    myConfirmPassword.grid(row=6, column=1, sticky=W)

    #ENTER CONFIRM PASSWORD
    e_con_pass=Entry(root, width=40, show="*")
    e_con_pass.grid(row=7, column=1,  columnspan=2, sticky=E)
    
    
    #EMAIL
    myEmail = Label(root, text="Email", font=("Arial", 12))
    myEmail.grid(row=8, column=1, sticky=W)

    #ENTER EMAIL
    e_email=Entry(root, width=40)
    e_email.grid(row=9, column=1,  columnspan=2, sticky=E)
    myEmptyLabel4 = Label(root, text="", pady=15)
    myEmptyLabel4.grid(row=10, column=0, columnspan=3)


     #LOGIN BUTTON
    login_button=Button(root, text="Login", padx=10, bg="#00FFFF", command= lambda: validating_Login_Reg(e_username.get(), e_pass.get(), e_con_pass.get(), e_email.get(), widgets))
    login_button.grid(row=11, column=1, columnspan=2, sticky=W+E)
    myEmptyLabel5 = Label(root, text="")
    myEmptyLabel5.grid(row=12, column=0, padx=10, pady=30)

    backLogin = Button(root, text="Back to Login", font=("Arial", 10), fg="#00AEA5", borderwidth=0, highlightthickness=0, command=lambda: return_login_page(widgets))
    backLogin.grid(row=13, column=1, columnspan=2)
    myEmptyLabel6 = Label(root, text="", pady=15)
    myEmptyLabel6.grid(row=14, column=0, columnspan=3)
    # store the widgets created in this function in a list
    widgets = [myEmptyLabel,myConfirmPassword,e_con_pass, myEmail, myLogin, e_email, myEmptyLabel2, myUsername, myEmptyLabel3, e_username, myEmptyLabel3, myPassword, myEmptyLabel3, e_pass, myEmptyLabel5, myEmptyLabel4, login_button, myEmptyLabel5, backLogin]

    # return the list of widgets for later use
    return widgets


#Return to Login Page
def return_login_page(widgets):
    for widget in widgets:
        widget.destroy()
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
def validating_Login_Reg(username, password, con_pass, email, widgets):
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
        showSuccesfull_Registation(widgets)

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
def showSuccesfull_Login(widgets):
    root.title("Successfully Login")
    for widget in widgets:
        widget.destroy()
    myInfo_emoji = Label(root, text="\u24D8\ufe0f ", font=("Arial", 20, "bold"),pady=10)
    myInfo_emoji.grid(row=0, column=0)
    Success_Login_Text=Label(root, text="Successfully Login'", font=("Arial", 16, "bold"))
    Success_Login_Text.grid(row=1, column=1)
    myEmptyLabel = Label(root, text="        ", font=("Arial", 20, "bold"),pady=10)
    myEmptyLabel.grid(row=0, column=2)
    myEmptyLabel1=Label(root, text="", padx=20)
    myEmptyLabel1.grid(row=1, column=2)
    ok_button=Button(root, text="OK", padx=10, command=root.quit)
    ok_button.grid(row=3, column=1)
    myEmptyLabel2 = Label(root, text="")
    myEmptyLabel2.grid(row=4, column=0, padx=10, pady=5)

 #Successful Registration Page 
def showSuccesfull_Registation(widgets):
    root.title("Registered")
    for widget in widgets:
        widget.destroy()
    myInfo_emoji = Label(root, text="\u24D8\ufe0f ", font=("Arial", 20, "bold"),pady=10)
    myInfo_emoji.grid(row=0, column=0)
    Success_Login_Text=Label(root, text="Registered Successfully'", font=("Arial", 16, "bold"))
    Success_Login_Text.grid(row=1, column=1)
    myEmptyLabel = Label(root, text="        ", font=("Arial", 20, "bold"),pady=10)
    myEmptyLabel.grid(row=0, column=2)
    myEmptyLabel1=Label(root, text="", padx=20)
    myEmptyLabel1.grid(row=1, column=2)
    ok_button=Button(root, text="OK", padx=10, command=lambda: button_Reg_to_Login(widgets))
    ok_button.grid(row=3, column=1)
    myEmptyLabel2 = Label(root, text="")
    myEmptyLabel2.grid(row=4, column=0, padx=10, pady=10)
    widgets=[myInfo_emoji, Success_Login_Text, myEmptyLabel, myEmptyLabel1, ok_button, myEmptyLabel2]
    return widgets

#After Registered Move Back to Login Page
def button_Reg_to_Login(widgets):
    root.title("Return to Login")
    for widget in widgets:
        widget.destroy()
    myInfo_emoji = Label(root, text="\u24D8\ufe0f", font=("Arial", 20, "bold"), pady=10)
    myInfo_emoji.grid(row=0, column=0)
    Success_Login_Text = Label(root, text="Return To Login", font=("Arial", 16, "bold"))
    Success_Login_Text.grid(row=1, column=1)
    myEmptyLabel = Label(root, text="        ", font=("Arial", 20, "bold"), pady=10)
    myEmptyLabel.grid(row=0, column=2)
    myEmptyLabel1 = Label(root, text="", padx=20)
    myEmptyLabel1.grid(row=1, column=2)
    ok_button = Button(root, text="OK", padx=10, command=lambda: return_login_page(widgets))
    ok_button.grid(row=3, column=1)
    myEmptyLabel2 = Label(root, text="")
    myEmptyLabel2.grid(row=4, column=0)

    widgets = [myInfo_emoji, Success_Login_Text, myEmptyLabel, myEmptyLabel1, ok_button, myEmptyLabel2]
    return widgets

    

myLogin()
root.mainloop()