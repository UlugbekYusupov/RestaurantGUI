import tkinter as tk
import tkinter.messagebox as tm
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import sqlite3 as lite
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        for F in (StartPage, PageOne, PageTwo,LoginPage,Today):
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
        
        button3 = ttk.Button(self, text="Today",
                             command=lambda: controller.show_frame(Today))
        button3.pack()

        # Connection to Database and querying data from connected db
        con = lite.connect('incomes.db')
        cursor = con.execute("SELECT days,income from db_table")

        # Splitting each column
        a = cursor.fetchall()
        b = dict(a)
        plt.show()
        days = tuple(b.keys())
        y_pos = np.arange(len(days))
        incomes = list(b.values())

        # Attaching Data to window by using bar charts
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        width = .5
        k = b.bar(days, incomes, width, align='center', alpha=1)
        plt.ylabel('INCOME')
        plt.title('WEEKLY INCOME')

        # Setting color of each bar column
        k[0].set_color('r')
        k[1].set_color('b')
        k[2].set_color('g')
        k[3].set_color('m')
        k[4].set_color('c')
        k[5].set_color('k')
        k[6].set_color('y')

        # Initializing canvas for our bar chart
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Today(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Today Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Income Graph",
                             command=lambda: controller.show_frame(PageOne))
        button2.pack()
        # Connection to Database and querying data from connected db
        con = lite.connect('incomes.db')
        cursor = con.execute("SELECT hours,hourly_income from today")

        # Splitting each column
        t = cursor.fetchall()
        b = dict(t)
        plt.show()
        hours = tuple(b.keys())
        y_pos = np.arange(len(hours))
        hourly_incomes = list(b.values())

        # Attaching Data to window by using line
        f = Figure(figsize=(5, 5), dpi=100)
        b = f.add_subplot(111)
        width = .5
        k = b.plot(hours, hourly_incomes)
        plt.ylabel('HOURS')
        plt.title('TODAY')

        # Initializing canvas for our bar chart
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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
