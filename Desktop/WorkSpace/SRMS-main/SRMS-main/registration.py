
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Regsitration Window")
        self.root.geometry("1350x700+0+0")

        left_lbl = Label(self.root, bg="#08A3D2").place(
            x=0, y=0, width=600, relheight=1)

        right_lbl = Label(self.root, bg="#031F3C").place(
            x=600, y=0, relwidth=1, relheight=1)
        self.bg = ImageTk.PhotoImage(file="images/side.png")
        bg = Label(self.root, image=self.bg, bg="#08A3D2").place(
            x=80, y=100, width=400, height=500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="Register Here", font=(
            "times new roman", 25, "bold"), bg="white", fg="green").place(x=50, y=30)

# --------------------------------Row1-------------------------------------------------------------------

        f_name = Label(frame1, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)

        self.text_fname = Entry(frame1, text="First Name",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_fname.place(x=50, y=130, width=250)
        l_name = Label(frame1, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=100)

        self.text_lname = Entry(frame1, text="Last Name",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_lname.place(x=370, y=130, width=250)
# --------------------------------Row 2-------------------------------------------------------------------
        contact = Label(frame1, text="Contact NO.", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=170)

        self.text_contact = Entry(frame1, text="Contact No.",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_contact.place(x=50, y=200, width=250)

        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)

        self.text_email = Entry(frame1, text="Email",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_email.place(x=370, y=200, width=250)
# --------------------------------Row 3-------------------------------------------------------------------
        question = Label(frame1, text="Security Question.", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=240)

        self.cmb_ques = ttk.Combobox(frame1, text="Security Question",  font=(
            "goudy old sytle", 13), state='readonly', justify=CENTER)
        self.cmb_ques['values'] = ("Select", "Your pet name",
                                   "your birth place", "your fav.food")
        self.cmb_ques.place(x=50, y=270, width=250)
        self.cmb_ques.current(0)
        answer = Label(frame1, text="Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=240)

        self.text_ans = Entry(frame1, text="Answer",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_ans.place(x=370, y=270, width=250)

# --------------------------------Row 3-------------------------------------------------------------------
        password = Label(frame1, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=310)

        self.text_password = Entry(frame1, text="Password",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_password.place(x=50, y=340, width=250)

        c_pass = Label(frame1, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=310)

        self.text_c_pass = Entry(frame1, text="Confirm Password",  font=(
            "goudy old sytle", 15), bg="lightgray")
        self.text_c_pass.place(x=370, y=340, width=250)

        self.btn_img = ImageTk.PhotoImage(file="images/register.png")
        btn_register = Button(frame1, image=self.btn_img, bd=0,
                              cursor="hand2", command=self.register_data).place(x=50, y=420)

        btn_login = Button(self.root, text="Sign In", font=("times new roman", 20), bd=0,
                           cursor="hand2", command=self.login_window).place(x=200, y=460, width=180)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")

    def clear(self):
        self.text_fname.delete(0, END),
        self.text_lname.delete(0, END),
        self.text_contact.delete(0, END),
        self.text_email.delete(0, END),

        self.text_ans.delete(0, END),
        self.text_password.delete(0, END),
        self.text_c_pass.delete(0, END),
        self.cmb_ques.current(0)

    def register_data(self):
        if self.text_fname.get() == "" or self.text_email.get() == "" or self.text_contact.get() == "" or self.cmb_ques.get() == "Select" or self.text_ans.get() == "" or self.text_password.get() == "" or self.text_c_pass.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        elif self.text_password.get() != self.text_c_pass.get():
            messagebox.showerror(
                "Error", "Password or Confirm password should be same", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?", (
                            self.text_email.get(),))
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror(
                        "Error", "User Already exist, Please try again another email", parent=self.root)
                else:

                    cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)", (
                        self.text_fname.get(),
                        self.text_lname.get(),
                        self.text_contact.get(),
                        self.text_email.get(),
                        self.cmb_ques.get(),
                        self.text_ans.get(),
                        self.text_password.get()


                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Register Successfull", parent=self.root)
                    self.clear()
                    self.login_window()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

           # - self.text_lname.get(),
            # self.text_contact.get(),
           # self.text_email.get(),
            # self.cmb_ques.get(),
            # self.text_ans.get(),
            # self.text_password.get(),
            # self.text_c_pass.get()


root = Tk()
obj = Register(root)
root.mainloop()
