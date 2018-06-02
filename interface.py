import tkinter as tk
import tkinter.messagebox as tm
from tkinter import ttk


LARGE_FONT = ("Verdana", 12)
logged_in = False

class Root(tk.Tk):

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
            self.show_frame(StartPage)

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
                            command=lambda: controller.show_frame(PageTwo))
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
        self.grid()

        for r in range(6):
            self.master.rowconfigure(r, weight=1)

        Frame1 = tk.Frame(self, bg="red")
        Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")
        Frame2 = tk.Frame(self)
        Frame2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky="WENS")
        Frame3 = tk.Frame(self, bg="green")
        Frame3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky="WENS")

        notebook = ttk.Notebook(Frame1)
        f1 = ttk.Frame(notebook)
        f2 = ttk.Frame(notebook)
        f3 = ttk.Frame(notebook)
        f4 = ttk.Frame(notebook)
        f5 = ttk.Frame(notebook)
        f6 = ttk.Frame(notebook)
        notebook.add(f1,text = 'Starter')
        notebook.add(f2,text = 'Main Menu')
        notebook.add(f3, text='Salad')
        notebook.add(f4, text='Pizza')
        notebook.add(f5, text='Desert')
        notebook.add(f6, text='Drink')
        notebook.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")

        treeview = ttk.Treeview(f1)

        treeview.pack()
        treeview.config(columns = ('name','price'))
        treeview.heading('#0',text = '#')
        treeview.heading('name',text = 'Name')
        treeview.heading('price', text='Price')

        treeview.insert('', 'end', text="1", values=("French Fries","$3"))



        # set frame resize priorities
        f1.rowconfigure(0, weight=1)
        f1.columnconfigure(0, weight=1)

        listbox = tk.Listbox(Frame2)
        listbox.insert(1, "Python")
        listbox.insert(2, "Perl")
        listbox.insert(3, "C")
        listbox.insert(4, "PHP")
        listbox.insert(5, "JSP")
        listbox.insert(6, "Ruby")
        listbox.grid(row=1, column=0, rowspan=4, columnspan=2, sticky="WENS")

        dummy_buttons = []
        for i in range(4):
            button = ttk.Button(Frame2, text="Button",
                                command = lambda: self._addToMenu(Frame2))
            button.grid(row=i+1, column=2, sticky="WENS")
            dummy_buttons.append(ttk.Button)



        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))

        button2 = ttk.Button(self, text="Page One",
                           command=lambda: controller.show_frame(PageOne))
        button1.grid(row=6, column=0, rowspan=1, columnspan=1, sticky="WENS")
"""
        def _addToMenu(frame):
            label_username = tk.Label(self, text="Username")
            label_password = tk.Label(self, text="Password")
            label_username.grid(row=0, sticky="E")
            self.label_password.grid(row=1, sticky="E")

            entry_table = tk.Entry(self)
            entry_food = tk.Entry(self)
            entry_amount = tk.Entry(self)
            entry_username.grid(row=0, column=1)
            entry_password.grid(row=1, column=1)
            """

"""
        def _removeFromMenu():

        def _makeOrder():

        def _clear():
"""

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



app = Root()
app.mainloop()