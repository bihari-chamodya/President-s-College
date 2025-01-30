from customtkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3
import bcrypt
import webbrowser

# Database Connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    username TEXT NOT NULL,
    password TEXT NOT NULL
)''')
conn.commit()

# Global Variable for Frame Movement
x = 50

def login_user():
    username = userNameEntry.get().strip()
    password = passwordEntry.get().strip()
    
    if not username or not password:
        messagebox.showerror('Error', 'All fields are required')
        return
    
    cursor.execute('SELECT password FROM user WHERE username=?', (username,))
    result = cursor.fetchone()
    
    if result:
        stored_password = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            messagebox.showinfo('Success', 'Successfully Logged In')
            webbrowser.open('index.html')
        else:
            messagebox.showerror('Error', 'Invalid Password')
            passwordEntry.delete(0, END)
    else:
        messagebox.showerror('Error', 'Invalid Username')
        userNameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        window.focus()

def register_user():
    username = userNameEntry.get().strip()
    password = passwordEntry.get().strip()
    
    if not username or not password:
        messagebox.showerror('Error', 'All fields are required')
        return
    
    cursor.execute('SELECT username FROM user WHERE username=?', (username,))
    if cursor.fetchone() is not None:
        messagebox.showerror('Error', 'Username already exists')
    else:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        cursor.execute('INSERT INTO user VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        messagebox.showinfo('Success', 'Registration Successful')
        move_right()
        userNameEntry.delete(0, END)
        passwordEntry.delete(0, END)
        window.focus()

def move_right():
    global x
    if x < 380:
        x += 1
        topFrame.place(x=x, y=12)
        window.after(1, move_right)
    else:
        SignupLabel.configure(text='Login')
        innerButton.configure(text='Login', command=login_user)

def move_left():
    global x
    if x > 50:
        x -= 1
        topFrame.place(x=x, y=12)
        window.after(1, move_left)
    else:
        SignupLabel.configure(text='Sign Up')
        innerButton.configure(text='Sign Up', command=register_user)

# GUI Setup
window = CTk()
window.title('Login & Signup Form')
window.wm_geometry('+300+100')
window.resizable(False, False)
window.config(bg='white')

mainFrame = CTkFrame(window, fg_color='blue4', width=600, height=400)
mainFrame.grid(row=0, column=0, pady=30, padx=30)

LoginButton = CTkButton(mainFrame, text='Login', fg_color='blue4', font=('Arial', 15, 'bold'),
                        hover_color='blue2', border_color='blue2', border_width=1, cursor='hand2', command=move_right)
LoginButton.place(x=380, y=300)

SignUpButton = CTkButton(mainFrame, text='Sign Up', fg_color='blue4', font=('Arial', 15, 'bold'),
                         hover_color='blue2', border_color='blue2', border_width=1, cursor='hand2', command=move_left)
SignUpButton.place(x=75, y=300)

topFrame = CTkFrame(window, fg_color='white', width=250, height=400)
topFrame.place(x=50, y=12)

try:
    LoginImage = CTkImage(light_image=Image.open('image/login.png'), size=(128, 128))
    LoginImageLabel = CTkLabel(topFrame, image=LoginImage, text='')
    LoginImageLabel.grid(row=0, column=0, pady=(20, 0))
except Exception as e:
    print("Error loading image:", e)

SignupLabel = CTkLabel(topFrame, text='Sign Up', text_color='blue4', font=('Arial', 30, 'bold'))
SignupLabel.grid(row=1, column=0, pady=(15, 0))

userNameEntry = CTkEntry(topFrame, font=('Arial', 20, 'bold'), placeholder_text='User Name',
                         fg_color='white', text_color='black', width=200, height=30)
userNameEntry.grid(row=2, column=0, padx=20, pady=(20, 10))

passwordEntry = CTkEntry(topFrame, font=('Arial', 20, 'bold'), placeholder_text='Password',
                         fg_color='white', text_color='black', width=200, height=30, show='*')
passwordEntry.grid(row=3, column=0, padx=20, pady=(20, 10))

innerButton = CTkButton(topFrame, text='Sign Up', fg_color='blue2', hover_color='blue4', cursor='hand2',
                        font=('Arial', 20, 'bold'), command=register_user)
innerButton.grid(row=4, column=0, pady=20)

window.mainloop()


conn.close()
