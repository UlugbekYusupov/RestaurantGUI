"""
File: interface.py
Authors:
        Name                        Student ID        Major                                     Role
        Kilichbek Haydarov          16012676        Computer Science & Engineering              Project Manager
        Ulugbek Yusupov             Unknown         Computer Science & Engineering              Senior Developer

Description: A program to help restaurant employees to manage and keep
            track of tables and orders from that tables, and calculate total
            prices. This program also provides the bar chart of daily income
            in a particular week

Version: 1.0.0

"""


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
    """
    Class to create the main frame for holding
    all secondary frames

    """
    def __init__(self, *args, **kwargs):
        """
        Construct main frame by extending parent class tk.Tk

        :param args: a non-keyworded, variable-length argument list
        :param kwargs: a keyworded, variable-length argument list
        """
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default="logo_icon.ico")
        tk.Tk.wm_title(self,"Restaurant Management System")

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight=1)

        # Create page objects
        self.frames = {}
        for F in (StartPage, Week, PageTwo,LoginPage,Today,):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # If a user successully logged in, Start Page is displayed, otherwise again Login Page
        if logged_in:
            self.show_frame(StartPage)
        else:
            self.show_frame(LoginPage)

    def show_frame(self,cont):
        """
        Display the frame based on the passed argument

        :param cont: container for page frame to be displayed
        :return: None
        """
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    """
    Class for Initial Page which contains
    few buttons to navigate between other pages

    """
    def __init__(self,parent,controller):
        """
        Construct a page by extending built-in class tk.Frame

        :param parent: a container which can be obtained from Root Class
        :param controller: the main frame
        """

        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text="Start Page",font=LARGE_FONT)
        label.pack(pady = 10,padx = 10)


        button1 = ttk.Button(self,text="Order",
                            command=lambda:controller.show_frame(PageTwo))
        button2 = ttk.Button(self, text="Daily Income",
                            command=lambda: controller.show_frame(Today))
        button3 = ttk.Button(self, text="Weekly Income",
                             command=lambda: controller.show_frame(Week))

        button1.pack()
        button2.pack()
        button3.pack()


        #TODO Fix the bug with displaying Matplotlib graph on main page

        
class Today(tk.Frame):
    """
    Class for Today Page which displays today's income in a graph
    using matplotlib

    """
    def __init__(self, parent, controller):
        """
        Construct a page by extending built-in class tk.Frame

        :param parent: a container which can be obtained from Root Class
        :param controller: the main frame
        """

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Today Graph", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
       
        button1.pack()

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

class Week(tk.Frame):
    """
        Class to create a dummy page which can be used
        for some purpose later

    """
    def __init__(self,parent,controller):
        """
            Construct a page by extending built-in class tk.Frame

            :param parent: a container which can be obtained from Root Class
            :param controller: the main frame
        """
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Income", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self,text="Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()
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
        
        
class PageTwo(tk.Frame):
    """
        Class to create a second page for keeping track of tabels
        in the restaurant and menu options

    """
    def __init__(self,parent,controller):
        """
            Construct a page by extending built-in class tk.Frame

            :param parent: a container which can be obtained from Root Class
            :param controller: the main frame
        """
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tabels", font=LARGE_FONT)
        self.grid()

        for r in range(6):
            self.master.rowconfigure(r, weight=1)

        Frame1 = tk.Frame(self)
        Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")
        Frame2 = tk.Frame(self)
        Frame2.grid(row=0, column=2, rowspan=6, columnspan=3, sticky="WENS")

        self.listbox = tk.Listbox(Frame1)
        for i in range(10):
            self.listbox.insert(i+1, "Table {:d}".format(i+1))
        self.listbox.grid(row=1, column=0, rowspan=4, columnspan=3, sticky="WENS")
        self.listbox.focus()
        self.listbox.bind('<Double-1>', lambda event: self.menuPopUpWindow(event))
        self.listbox.bind('<<ListboxSelect>>', lambda event,frame=Frame2:self.onselect(event,frame))

        menu_button = ttk.Button(Frame1,text="Close Table",command = lambda: self.closeTable())
        menu_button.grid(row=5,column = 0,columnspan = 3,sticky="WENS")

        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button2 = ttk.Button(self, text="Today",
                             command=lambda: controller.show_frame(Today))
       
        button1.grid(row=6,column=0,sticky="WENS")
        button2.grid(row=6,column=1,sticky="WENS")
      

    def closeTable(self):
        """
        Calculates total price of the selected tabel and sends to the database
        and the cleans the content of the file associated with that table for
        later purpose

        :return: None
        """
        table = self.selection_get() #TODO Adding total price and date to database
        file = open("Files/"+table+".txt","r")
        total_price = 0.0
        for line in file:
            food,price,amount,total = line.split("\t")
            total_price += float(total[1:])
        file.close()
        open("Files/"+table+".txt", 'w').close()
        self.treeview.delete(*self.treeview.get_children())

    def onselect(self,event,frame):
        """
        Prints the all ordered meals for the selected tabel and total price as well

        :param event: SELECT event passed by the .bind(<event>,<callback function> method)
        :param frame: on this frame the list of ordered meals is displayed
        :return: None
        """
        self.treeview = ttk.Treeview(frame)
        self.treeview.grid(row=0, column=2, rowspan=6, columnspan=3, sticky="WENS")
        self.treeview.config(columns=('name', 'price','amount','total'))
        self.treeview.column("#0",width=0)
        self.treeview.heading('name', text='Name')
        self.treeview.heading('price', text='Price')
        self.treeview.heading('amount', text='Amount')
        self.treeview.heading('total', text='Total')
        self.treeview.delete(*self.treeview.get_children())
        table = self.listbox.selection_get()
        total_price = 0.0
        file = open("Files/" + table + ".txt", "r")
        for line in file:
            food,price,amount,total = line.split("\t")
            self.treeview.insert('','end',text="1",values=(food,price,amount,total))
            total_price += float(total[1:])
        self.treeview.insert('','end',text="------",values=("-------","------",
                                                            "------","${:0.2f}".format(total_price)))

        file.close()

    def menuPopUpWindow(self,event):
        """
        Pop-up window which contains the list of meals and drinks
         is displayed when a user double-clicks on any tabel
         All meals are retrieved from the menu.txt file

        :param event: DOUBLE_CLICK event passed by the .bind(<event>,<callback function> method)
        :return: None
        """
        win = tk.Toplevel()
        win.wm_title("Menu")
        win.geometry("500x500+30+30")
        tabel_no = str(self.listbox.selection_get())
        l = tk.Label(win,text=tabel_no)
        l.grid(row=4,column=0)

        notebook = ttk.Notebook(win)
        notebook_frames = []
        food_category_list = ['Starter', 'Main Course', 'Salad', 'Pizza', 'Dessert', 'Drink']
        self.treeviews = []

        for i in range(6):
            notebook_frames.append(ttk.Frame(notebook))
            notebook.add(notebook_frames[-1],text=food_category_list[i])
            self.treeviews.append(ttk.Treeview(notebook_frames[-1]))
            self.treeviews[-1].column("#0",width=0)
            self.treeviews[-1].pack()
            self.treeviews[-1].pack()
            self.treeviews[-1].config(columns=('name', 'price'))
            self.treeviews[-1].heading('#0', text='#')
            self.treeviews[-1].heading('name', text='Name')
            self.treeviews[-1].heading('price', text='Price')
            self.treeviews[-1].bind('<Double-1>', lambda x,num = i: self.amountPopUpWindow(event, table=tabel_no,
                                                                                              index=num))
            notebook_frames[-1].rowconfigure(0, weight=1)
            notebook_frames[-1].columnconfigure(0, weight=1)

        menu = open("menu.txt","r")
        for line in menu:
            name,price,category = line.split(",")
            category = category[:-1]
            if(category=="Starter"):
                self.treeviews[0].insert('', 'end', text=i, values=(name, price))
            elif(category=="Main Course"):
                self.treeviews[1].insert('', 'end', text=i, values=(name, price))
            elif(category=="Salad"):
                self.treeviews[2].insert('', 'end', text=i, values=(name, price))
            elif (category == "Pizza"):
                self.treeviews[3].insert('', 'end', text=i, values=(name, price))
            elif (category == "Dessert"):
                self.treeviews[4].insert('', 'end', text=i, values=(name, price))
            else:
                self.treeviews[5].insert('', 'end', text="1", values=(name, price))
        menu.close()

        notebook.grid(row=0, column=0, rowspan=3, columnspan=2, sticky="WENS")
        b = ttk.Button(win, text="Okay", command=win.destroy)
        b.grid(row=5, column=0)

    def amountPopUpWindow(self,event,table,index):
        """
        Pop-up window is displayed when a user double-clicks on a meal from the list and
        requires the user to enter the amount of food or drink to be ordered

        :param event: DOUBLE_CLICK event passed by the .bind(<event>,<callback function> method)
        :param table: The number of tabel which has ordered food
        :param index: The number of frame which indicates the category of food
        :return: None

        """
        win = tk.Toplevel()
        win.wm_title(str(index)+"Amount")
        win.geometry("320x200+30+30")
        item = self.treeviews[index].focus()
        values = self.treeviews[index].item(item)['values']
        food,price = values[0],float(values[-1][1:])
        l = tk.Label(win, text=food)
        l.grid(row=0, column=0)

        l1 = tk.Label(win, text="Enter amount (${:.2f} per portion):".format(price))
        l1.grid(row=1, column=0)

        self.entry_amount = tk.Entry(win)
        self.entry_amount.grid(row=1, column=1)

        b = ttk.Button(win, text="Order", command=lambda: self._calculate(win,table,food,price))
        b.grid(row=2, column=0)

    def _calculate(self,popup_window,tab,food,price):
        """
        Calculates total price for ordered meal based on its own price

        :param popup_window: pop-up window which will be destroyed after the calucation is done
        :param tab: the tabel number which is used to create a unique file associated with it
        :param food: the name of food to be ordered
        :param price: the price of food to be ordered
        :return: None
        """

        amount = int(self.entry_amount.get())
        file = open("Files/" + tab + ".txt", "a")
        file.write(food + "\t$" + str(price) + "\t" + str(amount) + "\t$" + str(price * amount) + "\n")
        file.close()
        popup_window.destroy()


class LoginPage(tk.Frame):
    """
    Class for Login Page which is used for authentication
    """
    def __init__(self,parent,controller):
        """
            Construct a page by extending built-in class tk.Frame

            :param parent: a container which can be obtained from Root Class
            :param controller: the main frame
        """
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
        """
        Validates entered usearname and password with True values
        if the process is successful, it grants access to Start Page,
        otherwise Login Error is showed

        :param controller: the main frame
        :return: None
        """
        global logged_in
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "ulugbek" and password == "1996":
            tm.showinfo("Login info", "Welcome Ulugbek")
            logged_in = True
            controller.show_frame(StartPage)
        else:
            tm.showerror("Login error", "Incorrect username")
            logged_in = False



app = Root()
app.geometry("{0}x{1}+0+0".format(app.winfo_screenwidth(),
                                  app.winfo_screenheight()))
app.mainloop()
