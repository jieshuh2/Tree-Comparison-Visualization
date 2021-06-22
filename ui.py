from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from node import *
from tkinter import Grid
import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.use("TkAgg")
LargeFont = ("Verdana", 12)

SmallFont = ("Verdana", 8)
MiddleFont = ("Verdana", 10)
class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "")
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.root1 = Node(0,"default",0,"default")
        self.root2 = Node(0,"default",0,"default")
        self.f1 = 0
        self.f2 = 0
        self.titles = {}
        self.maxheight = -1
        
        self.frames = {}
        for f in (StartPage,PageOne):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Grid.rowconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        Grid.rowconfigure(self, index = 1, weight = 1)
        Grid.columnconfigure(self, index = 1, weight = 1)
        Grid.rowconfigure(self, index = 3, weight = 1)
        Grid.columnconfigure(self, index = 3, weight = 1)
        Grid.rowconfigure(self, index = 5, weight = 1)
        Grid.columnconfigure(self, index = 5, weight = 1)
        label = tk.Label(self, text = "请输入表格\n 然后点击开始", font = LargeFont)
        label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")
        button1 = ttk.Button(self, text="表一", command = lambda:self.insertform1(controller))
        button1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nsew")
        self.label1 =  tk.Label(self, text = "", font = SmallFont)
        self.label1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")
        button2 = ttk.Button(self, text="表二", command = lambda:self.insertform2(controller))
        button2.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nsew")
        self.label2 =  tk.Label(self, text = "", font = SmallFont)
        self.label2.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "nsew")
        button3 = ttk.Button(self, text="开始", command = lambda:self.start(controller))
        button3.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "nsew")
    #gurante that form1 and two are placed
    def start(self, cont):
        if (cont.f1 == 1 and cont.f2 == 1):
            # wb3 = Workbook()
            # ws3 = wb3.active
            # compare(cont.root1, cont.root2, ws3, -1)
            # wb3.save("output/form3.xlsx")
            cont.show_frame(PageOne)
        elif (cont.f1 == 0):
            messagebox.showinfo(message = "请输入表一")
        elif (cont.f2 == 0):
            messagebox.showinfo(message ="请输入表二")
        else:
            messagebox.showinfo(message ="请输入表格")
    def insertform1(self, cont):
        filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
        self.label1.configure(text = filename)
        cont.root1 = form1(filename)
        cont.f1 = 1
    def insertform2(self, cont):
        filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
        self.label2.configure(text = filename)
        cont.root2 = form2(filename)
        cont.f2 = 1
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Grid.rowconfigure(self, index = 0, weight = 1)
        # Grid.columnconfigure(self, index = 0, weight = 1)
        # Grid.rowconfigure(self, index = 1, weight = 1)
        # Grid.columnconfigure(self, index = 1, weight = 1)
        # Grid.rowconfigure(self, index = 2, weight = 1)
        # Grid.columnconfigure(self, index = 2, weight = 1)
        # Grid.rowconfigure(self, index = 3, weight = 1)
        # Grid.columnconfigure(self, index = 3, weight = 1)
        input1 = tk.Entry(self)
        input1.insert(0,"待展开层级数")
        input1.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
        self.controller = controller
        self.num = 0
        self.dele = 0
        
        input2 = tk.Entry(self)
        input2.insert(0,"待合成前缀")
        input2.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
        button = ttk.Button(self, text="添加", command = lambda:self.addtitle(input2))
        button.grid(row = 1, column = 3, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
    
        button1 = ttk.Button(self, text="返回", command = lambda:controller.show_frame(StartPage))
        button1.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nsew")
        button3 = ttk.Button(self, text="展开", command = lambda:self.nextpage(input1, parent))
        button3.grid(row = 3, column = 3, padx = 10, pady = 10, sticky = "nsew")

    def addtitle(self, input2):
        title1 = input2.get()
        self.controller.titles[title1] = 1
        button = ttk.Button(self, text = title1, command = lambda:self.delete(button, title1))
        button.grid(row = 2, column = self.num, padx = 10, pady = 10, sticky = "nsew")
        self.num += 1;
        
        input2.delete(0, "end")

    def delete(self, button, title1):
        self.controller.titles[title1] = 0
        button.grid_forget()
        self.dele += 1;
        if self.dele == self.num:
            self.num = 0
            self.dele = 0
    def nextpage(self, input1, parent):
        height = input1.get()
        try: 
            int(height)
            self.controller.maxheight = int(height)
        except:
            pass
        frame = PageTwo(parent, self.controller)
        frame.grid(row = 0, column = 0, sticky = "nsew")
        frame.tkraise()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.id1 = 0
        self.dic1 = {}
        self.dic2 = {}
        self.dic3 = {}
        self.empty = Node(-1, "", -1, "")
        # canvas = tk.Canvas(self)
        # canvas.pack(side = "left", fill = "both", expand = 1)
        Grid.rowconfigure(self, index = 1, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        Grid.rowconfigure(self, index = 3, weight = 3)
        Grid.columnconfigure(self, index = 5, weight = 1)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white")
        style.map('Treeview', background = [('selected', 'blue')], foreground= [('selected', 'white')])

        # scroll1 = ttk.Scrollbar(self, orient = "vertical", command = canvas.yview)
        # scroll1.pack(side = "right", fill = "y")
        # canvas.configure(yscrollcommand = scroll1.set)
        # canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

        # frame2 = tk.Frame(canvas)
        # canvas.create_window((0,0), window = frame2, anchor = "nw")

        text1 = tk.Label(self, text = "表一", font = MiddleFont)
        text1.grid(row = 0, column = 0, padx = 10, sticky = "nsew")
        button5 = ttk.Button(self, text="查找", command = lambda:self.locateform(tree3, tree1, self.dic3))
        button5.grid(row = 0, column = 4, padx = 10)
        tree1 = ttk.Treeview(self)
        tree1['columns'] = ["name", "number", "info"]
        tree1.column("#0", width = 120)
        tree1.column("name", anchor = "w", width = 80, minwidth = 60)
        tree1.column("number", anchor = "center", width = 40)
        tree1.column("info", anchor = "w", width = 120)
        tree1.heading("#0", text = "层级数", anchor = "w")
        tree1.heading("name", text = "子女号", anchor = "w")
        tree1.heading("number", text = "数量", anchor = "center")
        tree1.heading("info", text = "信息", anchor = "w")
        self.bbf(tree1, -1, controller.root1, 1)
        tree1.grid(row = 1, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "nsew")

        text2 = tk.Label(self, text = "表二", font = MiddleFont)
        text2.grid(row = 0, column = 5, padx = 10, sticky = "nsew")
        button6 = ttk.Button(self, text="查找", command = lambda:self.locateform(tree3, tree2, self.dic3))
        button6.grid(row = 0, column = 9, padx = 10)

        tree2 = ttk.Treeview(self)
        tree2['columns'] = ["name", "number", "info"]
        tree2.column("#0", width = 120)
        tree2.column("name", anchor = "w", width = 80, minwidth = 60)
        tree2.column("number", anchor = "center", width = 40)
        tree2.column("info", anchor = "w", width = 120)
        tree2.heading("#0", text = "层级数", anchor = "w")
        tree2.heading("name", text = "子女号", anchor = "w")
        tree2.heading("number", text = "数量", anchor = "center")
        tree2.heading("info", text = "信息", anchor = "w")
        self.bbf(tree2, -1, controller.root2, 2)
        tree2.grid(row = 1, column = 5, columnspan = 5, pady = 10, padx = 10, sticky = "nsew")

        text3 = tk.Label(self, text = "对比表：黑色:相同，蓝色：表一，红色：表二", font = MiddleFont)
        text3.grid(row = 2, column = 0, padx = 10, sticky = "nsew")
        tree3 = ttk.Treeview(self)

        tree3['columns'] = ["name", "number", "info"]
        tree3.column("#0", width = 120)
        tree3.column("name", anchor = "w", width = 80, minwidth = 60)
        tree3.column("number", anchor = "center", width = 40)
        tree3.column("info", anchor = "w", width = 120)
        tree3.heading("#0", text = "层级数", anchor = "w")
        tree3.heading("name", text = "子女号", anchor = "w")
        tree3.heading("number", text = "数量(表一|表二)", anchor = "center")
        tree3.heading("info", text = "信息", anchor = "w")
        # self.bbf(tree3, -1, controller.root2)

        tree3.tag_configure('form1', foreground = "blue")
        tree3.tag_configure('form2', foreground = "red")
        tree3.tag_configure('same', foreground = "black")

        self.compare(controller.root1, controller.root2, tree3, controller.titles)
        tree3.grid(row = 3, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "nsew")

        buttons = tk.Frame(self)
        buttons.grid(row = 3, column = 5, columnspan = 5, pady = 10, padx = 10, sticky = "nsew")
        Grid.rowconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        Grid.rowconfigure(self, index = 1, weight = 1)
        button3 = ttk.Button(buttons, text="从表一查找所选", command = lambda: self.locateform(tree1, tree3, self.dic1))
        button3.grid(row = 0, column = 5, pady = 10, sticky = "nsew")

        button4 = ttk.Button(buttons, text="从表二查找所选", command = lambda: self.locateform(tree2, tree3, self.dic2))
        button4.grid(row = 1, column = 5, pady = 10, sticky = "nsew")

        button1 = ttk.Button(buttons, text="返回", command = lambda:controller.show_frame(PageOne))
        button1.grid(row = 2, column = 5, pady = 10, sticky = "nsew")
        button2 = ttk.Button(buttons, text="返回主页", command = lambda:controller.show_frame(StartPage))
        button2.grid(row = 3, column = 5, pady = 10, sticky = "nsew")

        
    def bbf(self, tree, pid, node, tn):
        if pid == -1:
            pid = ""
        else:
            pid = str(pid)
        iid = tree.insert(parent = pid, index = 'end', text = str(node.height),
            values = (node.name, node.number, node.info))
        if tn == 1:
            self.dic1[str(node.height).strip() + "-" + str(node.name).strip()] = iid
        else:
            self.dic2[str(node.height).strip() + "-" + str(node.name).strip()] = iid
        for i in node.children:
            self.bbf(tree, iid, i, tn)
    
    def compare(self, node1, node2, tree, titles):
        if node1.children == [] and node2.children == []:
            return
        elif node1.children == []:
            for i in node2.children:
                if i.name[-1] == "*":
                    i.name = i.name[:-1]
                # writenode2(i, True, ws)
                if node2.iid == -1:
                    pid = ""
                else:
                    pid = str(node2.iid)
                i.iid = tree.insert(parent = pid, index = 'end', text = str(i.height),
                    values = (i.name, i.number, i.info), tags = ('form2',))
                self.dic3[str(i.height).strip() + "-" + str(i.name).strip()] = i.iid
                self.compare(empty, i, tree, titles)
            return
        elif node2.children == []:
            for i in node1.children:
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                i.iid = tree.insert(parent = pid, index = 'end', text = str(i.height),
                    values = (i.name, i.number, i.info), tags = ('form1',))
                self.dic3[str(i.height).strip() + "-" + str(i.name).strip()] = i.iid
                self.compare(i, empty, tree, titles)  
            return
        dic = {}
        for n1 in node1.children:
            dic[n1.name] = n1
        for n2 in node2.children:
            if n2.name[-1] == "*":
                n2.name = n2.name[:-1]
            if dic.get(n2.name) != None:
                n1 = dic.get(n2.name)
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),
                    values = (n1.name, str(n1.number) + " | " + str(n2.number), n1.info), tags = ('same',))
                n2.iid = n1.iid
                n1.find = 1
                n2.find = 1
                self.dic3[str(n1.height).strip() + "-" + str(n1.name).strip()] = n1.iid
                self.compare(n1, n2, tree, titles)
                # compare(n1, n2, ws)
        for n1 in node1.children:
            if n1.find == 0:
                # writenode1(n1, True, ws)
                # compare(n1, empty, ws)
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),
                    values = (n1.name, n1.number, n1.info), tags = ('form1',))
                self.dic3[str(n1.height).strip() + "-" + str(n1.name).strip()] = n1.iid
                self.compare(n1, empty, tree, titles) 
        for n2 in node2.children:
            if n2.find == 0:
                # writenode2(n2, True, ws)
                # compare(empty, n2, ws)
                if node2.iid == -1:
                    pid = ""
                else:
                    pid = str(node2.iid)
                n2.iid = tree.insert(parent = pid, index = 'end', text = str(n2.height),
                    values = (n2.name, n2.number, n2.info), tags = ('form2',))
                self.dic3[str(n2.height).strip() + "-" + str(n2.name).strip()] = n2.iid
                self.compare(empty, n2, tree, titles) 
    def locateform(self, treesearch, treeselect, dic):
        itm = treeselect.selection()[0]
        height = treeselect.item(itm)["text"].strip()
        name = treeselect.item(itm)["values"][0]
        name = name.strip();
        key = height + "-" + name
        iid = dic.get(key)
        if (iid == None):
            key = height + "-" + name + "*"
            iid = dic.get(key)
        if (iid == None and name[-1] == "*"):
            key = height + "-" + name[:-1]
            iid = dic.get(key)
        if (iid != None):
            treesearch.see(iid)
            treesearch.focus([iid])
            treesearch.selection_set(iid)
            # treesearch.item(iid[, option[, **kw]])