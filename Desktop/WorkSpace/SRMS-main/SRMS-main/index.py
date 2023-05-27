from tkinter import*
from PIL import Image, ImageTk
from result_stu import ReportStuClass
from login import LoginClass
import os


class SRMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1390x700+0+0")
        self.root.config(bg="white")

    # ....title........
        title = Label(self.root, text=" Welcome TO Student Result Management System", padx=10, compound=LEFT, font=(
            "goudy old sytle", 40, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=120)

        # ...Content Window..........
        self.bg_img = Image.open("images/admin.png")

        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_img = Label(self.root, image=self.bg_img).place(
            x=80, y=180, width=350, height=350)

        # ...Content Window..........
        self.stu_img = Image.open("images/student.png")

        self.stu_img = ImageTk.PhotoImage(self.stu_img)

        self.lb2_img = Label(self.root, image=self.stu_img).place(
            x=800, y=180, width=350, height=350)

        btn_admin = Button(self.root, text="Admin", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.login).place(x=150, y=550, width=200, height=40)
        btn_student = Button(self.root, text="Student", font=(
            "goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=900, y=550, width=200, height=40)

    def add_report(self):
        self.root.destroy()
        os.system("python result_stu.py")

    def login(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = SRMS(root)
    root.mainloop()
