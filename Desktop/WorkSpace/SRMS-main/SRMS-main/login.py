from distutils import command
from tkinter import*
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox
import os


class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        left_lbl = Label(self.root, bg="#08A3D2").place(
            x=0, y=0, width=600, relheight=1)

        right_lbl = Label(self.root, bg="#031F3C").place(
            x=600, y=0, relwidth=1, relheight=1)

# ===============frames===============

        login_frame = Frame(self.root, bg="white").place(
            x=250, y=100, width=800, height=500)

        # ....title........
        title = Label(login_frame, text="Login Here",  font=(
            "goudy old sytle", 30, "bold"), bg="white", fg="#08A3D2").place(x=500, y=150)

        email = Label(login_frame, text="Email Address",  font=(
            "goudy old sytle", 20), bg="white", fg="gray").place(x=480, y=250)
        self.txt_email = Entry(login_frame, text="Email Address",  font=(
            "goudy old sytle", 20), bg="lightgray")
        self.txt_email.place(x=480, y=300, width=350, height=35)

        pasword = Label(login_frame, text="Password",  font=(
            "goudy old sytle", 20), bg="white", fg="gray").place(x=480, y=350)
        self.txt_password = Entry(login_frame, text="Password",  font=(
            "goudy old sytle", 20), bg="lightgray")
        self.txt_password.place(x=480, y=400, width=350, height=35)

        # =========Button==================
        self.btn_reg = Button(self.root, text='Register New Account', font=("goudy old style", 15, "bold"),
                              bg="white", bd=0, fg="#B00857", cursor="hand2", command=self.register_window).place(
            x=460, y=450, width=250, height=20)
        self.btn_login = Button(self.root, text='Login', font=("goudy old style", 20, "bold"),
                                bg="#B00857", bd=1, fg="white", cursor="hand2", command=self.login).place(
            x=480, y=500, width=120, height=60)

        # ==============images====================================

        self.bg_img = Image.open("images/login2.jpg")
        self.bg_img = self.bg_img.resize((500, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_img = Label(self.root, image=self.bg_img, bg="#F5CBA7").place(
            x=90, y=120, width=350, height=450)

    def register_window(self):
        self.root.destroy()
        os.system("python registration.py")

    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()

                cur.execute("select * from employee where email=? and password=?",
                            (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid user name and pasword", parent=self.root)

                else:
                    messagebox.showinfo(
                        "Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__ == "__main__":
    root = Tk()
    obj = LoginClass(root)
    root.mainloop()
