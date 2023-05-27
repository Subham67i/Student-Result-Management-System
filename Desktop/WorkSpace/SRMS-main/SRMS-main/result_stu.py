from tkinter import*
from PIL import Image, ImageTk
import sqlite3
from tkinter import ttk, messagebox
import os


class ReportStuClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1390x700+0+00")
        self.root.config(bg="white")
        self.root.focus_force()

        # ....title........
        title = Label(self.root, text="View Student Result",  font=(
            "goudy old sytle", 20, "bold"), bg="orange", fg="#262626").place(x=10, y=15, width=1180, height=50)

        # ========Variable==========
        self.var_serach = StringVar()
        self.var_id = ""

# ============Search===========
        lbl_search = Label(self.root, text="Search By Roll No.", font=(
            "goudy old style", 15, "bold"), bg="white").place(x=350, y=100)
        txt_serach = Entry(self.root, textvariable=self.var_serach, font=(
            "goudy old style", 20, "bold"), bg="lightyellow").place(x=520, y=100, width=150)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, "bold"),
                            bg="#03a9f4", fg="white", cursor="hand2", command=self.search).place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, "bold"),
                           bg="gray", fg="white", cursor="hand2", command=self.clear).place(x=800, y=100, width=100, height=35)

        lbl_roll = Label(self.root, text="Roll No.", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=150, y=230, width=150, height=50)
        lbl_name = Label(self.root, text="Name", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=300, y=230, width=150, height=50)
        lbl_course = Label(self.root, text="Course", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=450, y=230, width=150, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=600, y=230, width=150, height=50)
        lbl_full_marks = Label(self.root, text="Full Marks", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=750, y=230, width=150, height=50)
        lbl_per = Label(self.root, text="Percentage", font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE).place(x=900, y=230, width=150, height=50)

        self.roll = Label(self.root,  font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.roll.place(x=150, y=280, width=150, height=50)
        self.name = Label(self.root,  font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.name.place(x=300, y=280, width=150, height=50)
        self.course = Label(self.root, font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.course.place(x=450, y=280, width=150, height=50)
        self.marks = Label(self.root,  font=(
            "goudy old style", 15, "bold"),  bd=2, relief=GROOVE)
        self.marks.place(x=600, y=280, width=150, height=50)
        self.full_marks = Label(self.root,  font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.full_marks.place(x=750, y=280, width=150, height=50)
        self.per = Label(self.root,  font=(
            "goudy old style", 15, "bold"), bg="white", bd=2, relief=GROOVE)
        self.per.place(x=900, y=280, width=150, height=50)


# =================================
        btn_delete = Button(self.root, text='Back', font=("goudy old style", 15, "bold"),
                            bg="red", fg="white", cursor="hand2", command=self.back).place(x=500, y=350, width=150, height=35)

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_serach.get() == "":
                messagebox.showerror(
                    "Error", "RollNO. should be required", parent=self.root)
            else:
                cur.execute(
                    "select * from result where roll=?", (self.var_serach.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id = row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.marks.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.per.config(text=row[6])

                else:
                    messagebox.showerror(
                        "Error", "No record found", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id = ""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_serach.set("")

    def back(self):
        self.root.destroy()
        os.system("python index.py")


if __name__ == "__main__":
    root = Tk()
    obj = ReportStuClass(root)
    root.mainloop()
