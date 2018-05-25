import tkinter as tk
import tkinter.messagebox as tm
from tkinter import ttk


LARGE_FONT = ("Verdana", 12)
logged_in = False

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self,default="logo_icon.ico")
        tk.Tk.wm_title(self,"Restaurant Management System")

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,LoginPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        if logged_in:
            self.show_frame(StartPage)
        else:
            self.show_frame(LoginPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Start Page",font=LARGE_FONT)
        label.pack(pady = 10,padx = 10)


        button1 = ttk.Button(self,text="Visit Page 1",
                            command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page one", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two",
                           command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page One",
                           command=lambda: controller.show_frame(PageOne))
        button2.pack()

class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.label_username = tk.Label(self,text="Username")
        self.label_password = tk.Label(self,text = "Password")
        self.label_username.grid(row=0, sticky="E")
        self.label_password.grid(row=1, sticky="E")


        self.entry_username = tk.Entry(self)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)


        self.checkbox = tk.Checkbutton(self,text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = tk.Button(self,text="Login",
                           command=lambda:self._login_btn_clicked(controller))
        self.logbtn.grid(columnspan=2)

    def _login_btn_clicked(self,controller):
        global logged_in
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "john" and password == "password":
            tm.showinfo("Login info", "Welcome John")
            logged_in = True
            controller.show_frame(StartPage)
        else:
            tm.showerror("Login error", "Incorrect username")
            logged_in = False



app = SeaofBTCapp()
app.mainloop()