from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from node import *
from tkinter import Grid
LargeFont = ("Verdana", 12)

SmallFont = ("Verdana", 8)
MiddleFont = ("Verdana", 10)
class UI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "杨晖")
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
        self.nolist = {}
        
        self.frames = {}
        # for f in (StartPage,PageOne, PageTwo):
        #     frame = f(container, self)
        #     self.frames[f] = frame
        #     frame.grid(row = 0, column = 0, sticky = "nsew")
        frame = PageTwo(container, self)
        self.frames[PageTwo] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(PageTwo)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    #for simplicity merge start page and page one into page two. 
# class StartPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         Grid.rowconfigure(self, index = 0, weight = 1)
#         Grid.columnconfigure(self, index = 0, weight = 1)
#         Grid.rowconfigure(self, index = 1, weight = 1)
#         Grid.columnconfigure(self, index = 1, weight = 1)
#         Grid.rowconfigure(self, index = 3, weight = 1)
#         Grid.columnconfigure(self, index = 3, weight = 1)
#         Grid.rowconfigure(self, index = 5, weight = 1)
#         Grid.columnconfigure(self, index = 5, weight = 1)
#         label = tk.Label(self, text = "请输入表格\n 然后点击开始", font = LargeFont)
#         label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "nsew")
#         button1 = ttk.Button(self, text="表一", command = lambda:self.insertform1(controller))
#         button1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "nsew")
#         self.label1 =  tk.Label(self, text = "", font = SmallFont)
#         self.label1.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "nsew")
#         button2 = ttk.Button(self, text="表二", command = lambda:self.insertform2(controller))
#         button2.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nsew")
#         self.label2 =  tk.Label(self, text = "", font = SmallFont)
#         self.label2.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "nsew")
#         button3 = ttk.Button(self, text="开始", command = lambda:self.start(controller))
#         button3.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "nsew")
#     #gurante that form1 and two are placed
#     def start(self, cont):
#         if (cont.f1 == 1 and cont.f2 == 1):
#             # wb3 = Workbook()
#             # ws3 = wb3.active
#             # compare(cont.root1, cont.root2, ws3, -1)
#             # wb3.save("output/form3.xlsx")
#             cont.show_frame(PageOne)
#         elif (cont.f1 == 0):
#             messagebox.showinfo(message = "请输入表一")
#         elif (cont.f2 == 0):
#             messagebox.showinfo(message ="请输入表二")
#         else:
#             messagebox.showinfo(message ="请输入表格")
#     def insertform1(self, cont):
#         filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
#         self.label1.configure(text = filename)
#         cont.root1 = form1(filename)
#         cont.f1 = 1
#     def insertform2(self, cont):
#         filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
#         self.label2.configure(text = filename)
#         cont.root2 = form2(filename)
#         cont.f2 = 1
# class PageOne(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         input1 = tk.Entry(self)
#         input1.insert(0,"待展开层级数")
#         input1.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
#         self.controller = controller
#         self.num = 0
#         self.dele = 0
        
#         input2 = tk.Entry(self)
#         input2.insert(0,"规则名1")
#         input3 = tk.Entry(self)
#         input3.insert(0,"规则名2")
#         label = tk.Label(self, text = "=", font = SmallFont)
#         label.grid(row = 1, column = 3, columnspan = 1, pady = 10, sticky = "nsew")
#         input3.grid(row = 1, column = 4, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
#         input2.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
#         button = ttk.Button(self, text="添加", command = lambda:self.addtitle(input2, input3))
#         button.grid(row = 1, column = 7, columnspan = 1, padx = 10, pady = 10, sticky = "nsew")
    
#         button1 = ttk.Button(self, text="返回", command = lambda:controller.show_frame(StartPage))
#         button1.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "nsew")
#         button3 = ttk.Button(self, text="展开", command = lambda:self.nextpage(input1, parent))
#         button3.grid(row = 3, column = 7, padx = 10, pady = 10, sticky = "nsew")

#     def addtitle(self, input2, input3):
#         title1 = input2.get() + "=" + input3.get()
#         self.controller.titles[title1] = 1
#         button = ttk.Button(self, text = title1, command = lambda:self.delete(button, title1))
#         button.grid(row = 2, column = self.num, padx = 10, pady = 10, sticky = "nsew")
#         self.num += 1;
        
#         input2.delete(0, "end")

#     def delete(self, button, title1):
#         self.controller.titles[title1] = 0
#         button.grid_forget()
#         self.dele += 1;
#         if self.dele == self.num:
#             self.num = 0
#             self.dele = 0
#     def nextpage(self, input1, parent):
#         height = input1.get()
#         try: 
#             int(height)
#             self.controller.maxheight = int(height)
#         except:
#             pass
#         frame = PageTwo(parent, self.controller)
#         frame.grid(row = 0, column = 0, sticky = "nsew")
#         frame.tkraise()
    #pop up box to select equal-name rule
class Rule(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title('以下名称视为相同')
        # ui
        self.userinfo = {}
        for i in controller.titles:
            self.userinfo[i] = controller.titles[i].copy()

        self.controller = controller
        self.setup_UI()
        
    def setup_UI(self):
        Grid.rowconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 4, weight = 1)
        tree = ttk.Treeview(self)
        self.tree = tree
        tree['columns'] = ["name1", "name2"]
        tree.column("#0", width = 30)
        tree.column("name1", anchor = "w", width = 120)
        tree.column("name2", anchor = "w", width = 120)
        tree.heading("#0", text = "视为相同", anchor = "w")
        tree.heading("name1", text = "表一名称", anchor = "w")
        tree.heading("name2", text = "表二名称", anchor = "w")
        tree.grid(row = 0, column = 0, columnspan = 9, pady = 10, padx = 10, sticky = "nsew")
        ybar2=ttk.Scrollbar(self,orient='vertical')
        ybar2['command']=tree.yview 
        ybar2.grid(row=0,column=9,sticky='ns')
        input2 = tk.Entry(self)
        input2.insert(0,"名称一")
        input3 = tk.Entry(self)
        input3.insert(0,"名称二")
        self.input2 = input2
        self.input3 = input3
        label = tk.Label(self, text = "=", font = SmallFont)
        label.grid(row = 1, column = 3, columnspan = 1, pady = 10, sticky = "nsew")
        input3.grid(row = 1, column = 4, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
        input2.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="添加", command=self.add).grid(row = 1, column = 8, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="删除所选", command=self.delete).grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="打印", command=self.printt).grid(row = 2, column = 4, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="取消", command=self.cancel).grid(row = 3, column = 4, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="确定", command=self.ok).grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        for name in self.userinfo:
            for n1 in self.userinfo[name]:
                self.tree.insert(parent = "", index = 'end', values = (n1, name))
    def printt(self):
        f = filedialog.asksaveasfile(mode='wb', defaultextension=".xlsx")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        wb = Workbook()
        ws = wb.active
        ws.append(["以下名称视为相同："])
        ws.append(["表一名称","表二名称"])
        for name in self.userinfo:
            for n1 in self.userinfo[name]:
                ws.append([n1, name])
        wb.save(f)
   
    def add(self):
        self.tree.insert(parent = "", index = 'end',
            values = (self.input2.get(), self.input3.get()))
        title = str(self.input3.get())
        if self.userinfo.get(title) == None:
            self.userinfo[title] = [str(self.input2.get())]
        else:
            self.userinfo[title].append(str(self.input2.get()))
        
    def delete(self):
        selected_item = self.tree.selection()[0] ## get selected item
        item = self.tree.item(selected_item)
        title = str(item["values"][1])
        self.userinfo[title].remove(str(item["values"][0]))
        self.tree.delete(selected_item)
    def ok(self):
        self.controller.titles = self.userinfo.copy()
        self.destroy() 
        
    def cancel(self):
        self.userinfo = None #don't change 
        self.destroy()
    #pop up box to select not unfold name rule
class Rule2(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.title('对以下项目不展开')
        # 弹窗界面
        self.userinfo = controller.nolist.copy()
        self.setup_UI()
        self.controller = controller
        
    def setup_UI(self):
        Grid.rowconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 4, weight = 1)
        # Grid.columnconfigure(self, index = 0, weight = 1)
        # # Grid.rowconfigure(self, index = 3, weight = 3)
        # Grid.columnconfigure(self, index = 8, weight = 1)
        tree = ttk.Treeview(self)
        self.tree = tree
        tree['columns'] = ["name1"]
        tree.column("#0", width = 30)
        tree.column("name1", anchor = "w", width = 240)
        tree.heading("#0", text = "", anchor = "w")
        tree.heading("name1", text = "名称", anchor = "w")

        tree.grid(row = 0, column = 0, columnspan = 8, pady = 10, padx = 10, sticky = "nsew")
        ybar2=ttk.Scrollbar(self,orient='vertical')
        ybar2['command']=tree.yview 
        ybar2.grid(row=0,column=8,sticky='ns')
        input2 = tk.Entry(self)
        input2.insert(0,"输入名称")

        self.input2 = input2
        input2.grid(row = 1, column = 0, columnspan = 7, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="添加", command=self.add).grid(row = 1, column = 7, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="删除所选", command=self.delete).grid(row = 2, column = 0, columnspan = 4,padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="打印", command=self.printt).grid(row = 2, column = 4, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="取消", command=self.cancel).grid(row = 3, column = 4, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        tk.Button(self, text="确定", command=self.ok).grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = "nsew")
        for name in self.userinfo:
            if self.userinfo[name] > 0:
                self.tree.insert(parent = "", index = 'end', values = (name))
        
    def add(self):
        self.tree.insert(parent = "", index = 'end',
            values = (self.input2.get()))
        title = str(self.input2.get())
        if self.userinfo.get(title) == None:
            self.userinfo[title] = 1
        else:
            self.userinfo[title] += 1
    def printt(self):
        f = filedialog.asksaveasfile(mode='wb', defaultextension=".xlsx")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        wb = Workbook()
        ws = wb.active
        ws.append(["不展开名称："])
        for name in self.userinfo:
            if self.userinfo[name] > 0:
                ws.append([name])
        wb.save(f)

    def delete(self):
        selected_item = self.tree.selection()[0] ## get selected item
        item = self.tree.item(selected_item)
        title = str(item["values"][0])
        self.userinfo[title] -= 1
        # print(title)
        self.tree.delete(selected_item)

    def ok(self):
        self.controller.nolist = self.userinfo.copy()
        self.destroy() 
        
    def cancel(self):
        self.userinfo = None 
        self.destroy()
class Delet(tk.Toplevel):
    def __init__(self, parent):
        super().__init__()
        self.title('已删除层级')
        # 弹窗界面
        self.parent = parent
        self.hid1 = parent.hid1
        self.hid2 = parent.hid2
        self.d1 = {}
        self.d2 = {}
        self.setup_UI()
        
    def setup_UI(self):
        Grid.rowconfigure(self, index = 0, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        # Grid.rowconfigure(self, index = 3, weight = 3)
        Grid.columnconfigure(self, index = 8, weight = 1)
        tree = ttk.Treeview(self)
        self.tree = tree
        tree['columns'] = ["node", "parent", "children"]
        tree.column("#0", width = 30)
        tree.column("node", anchor = "w", width = 120)
        tree.column("parent", anchor = "w", width = 120)
        tree.column("children", anchor = "w", width = 240)
        tree.heading("#0", text = "", anchor = "w")
        tree.heading("node",text = "表一已撤销", anchor = "w")
        tree.heading("parent", text = "父本", anchor = "w")
        tree.heading("children", text = "子本", anchor = "w")
        tree.grid(row = 0, column = 0, columnspan = 8, pady = 10, padx = 10, sticky = "nsew")
        popup = tk.Menu(tree, tearoff=0)
        self.popup = popup
        tree.bind('<Button-3>', self.popup_menu)
        popup.add_command(command=lambda:self.recover(1),label="恢复")
        ybar1=ttk.Scrollbar(self,orient='vertical')
        ybar1['command']=tree.yview 
        ybar1.grid(row=0,column=7,sticky='ns')


        tree2 = ttk.Treeview(self)
        self.tree2 = tree2
        tree2['columns'] = ["node", "parent", "children"]
        tree2.column("#0", width = 30)
        tree2.column("node", anchor = "w", width = 120)
        tree2.column("parent", anchor = "w", width = 120)
        tree2.column("children", anchor = "w", width = 240)
        tree2.heading("#0", text = "", anchor = "w")
        tree2.heading("node", text = "表二已撤销",anchor = "w")
        tree2.heading("parent", text = "父本",anchor = "w")
        tree2.heading("children", text = "子本",anchor = "w")
        tree2.grid(row = 0, column = 8, columnspan = 8, pady = 10, padx = 10, sticky = "nsew")
        ybar2=ttk.Scrollbar(self,orient='vertical')
        ybar2['command']=tree2.yview 
        ybar2.grid(row=0,column=15,sticky='ns')

        popup1 = tk.Menu(tree2, tearoff=0)
        tree2.bind('<Button-3>', self.popup_menu1)
        self.popup1 = popup1
        popup1.add_command(command=lambda:self.recover(2),label="恢复")
        for node in self.hid1:
            children = ""
            pname = self.hid1[node].name
            for c in node.children:
                if children != "":
                    children += ", "
                children += c.name
            iid = self.tree.insert(parent = "", index = 'end', values = (node.name, pname, children))
            self.d1[iid] = node
        for node in self.hid2:
            children = ""
            pname = self.hid2[node].name
            for c in node.children:
                if children != "":
                    children += ", "
                children += c.name
            iid = self.tree2.insert(parent = "", index = 'end', values = (node.name, pname, children))
            self.d2[iid] = node
    def popup_menu(self, event):
        self.tree.identify_row(event.y)
        self.popup.post(event.x_root, event.y_root)
    def popup_menu1(self, event):
        self.tree2.identify_row(event.y)
        self.popup1.post(event.x_root, event.y_root)
    def recover(self, tc):
        if tc == 1:
            selected_item = self.tree.selection()[0] ## get selected item
            node = self.d1[selected_item]
            self.parent.restore(node,tc)
            self.tree.delete(selected_item)
            self.hid1.pop(node)
            self.d1.pop(selected_item)
        else:
            selected_item = self.tree2.selection()[0]
            node = self.d2[selected_item]
            self.parent.restore(node,tc)
            self.tree2.delete(selected_item)
            self.hid2.pop(node)
            self.d2.pop(selected_item)
        # print(title)
        


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.dic1 = {} #dic[iid1] = node1
        self.dic2 = {} #dic[iid2] = node2
        self.dic3 = {} #dic[iid3] = [node1, node2]
        self.find = [] #[iids that are find by search]
        self.fidx = 0 #idx in find that is currently shown
        self.hierichy = {}
        self.hid1 = {}
        self.hid2 = {}
        self.empty = Node(-1, "", -1, "")
        # canvas = tk.Canvas(self)
        # canvas.pack(side = "left", fill = "both", expand = 1)
        Grid.rowconfigure(self, index = 1, weight = 1)
        Grid.columnconfigure(self, index = 0, weight = 1)
        # Grid.rowconfigure(self, index = 3, weight = 3)
        Grid.columnconfigure(self, index = 5, weight = 1)
        Grid.columnconfigure(self, index = 10, weight = 1)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
            background="white",
            foreground="black",
            rowheight=25,
            fieldbackground="white")
        style.map('Treeview', background = [('selected', 'blue')], foreground= [('selected', 'white')])

        text1 = tk.Label(self, text = "表一", font = MiddleFont)
        text1.grid(row = 0, column = 0, padx = 10, sticky = "nsew")
        # button5 = ttk.Button(self, text="查找", command = lambda:self.locateform(tree3, tree1, self.dic3))
        # button5.grid(row = 0, column = 4, padx = 10)
        ybar1=ttk.Scrollbar(self,orient='vertical') 
        ybar2=ttk.Scrollbar(self,orient='vertical') 
        ybar3=ttk.Scrollbar(self,orient='vertical') 
        tree1 = ttk.Treeview(self, yscrollcommand=ybar1.set)
        tree1['columns'] = ["name", "number", "info"]
        tree1.column("#0", width = 120)
        tree1.column("name", anchor = "w", width = 80, minwidth = 60)
        tree1.column("number", anchor = "center", width = 40)
        tree1.column("info", anchor = "w", width = 120)
        tree1.heading("#0", text = "层级数", anchor = "w")
        tree1.heading("name", text = "子女号", anchor = "w")
        tree1.heading("number", text = "数量", anchor = "center")
        tree1.heading("info", text = "信息(项目名称|标识码|状态)", anchor = "w")
        # self.bbf(tree1, -1, controller.root1, 1)
        tree1.grid(row = 1, column = 0, columnspan = 5, pady = 10, padx = 10, sticky = "nsew")
        tree1.bind('<Double-Button-1>', self.treeviewClick0)
        ybar1['command']=tree1.yview 
        ybar1.grid(row=1,column=4,sticky='ns')


        text2 = tk.Label(self, text = "表二", font = MiddleFont)
        text2.grid(row = 0, column = 10, padx = 10, sticky = "nsew")
        # button6 = ttk.Button(self, text="查找", command = lambda:self.locateform(tree3, tree2, self.dic3))
        # button6.grid(row = 0, column = 9, padx = 10)
        tree2 = ttk.Treeview(self, yscrollcommand=ybar2.set)
        tree2['columns'] = ["name", "number", "info"]
        tree2.column("#0", width = 120)
        tree2.column("name", anchor = "w", width = 80, minwidth = 60)
        tree2.column("number", anchor = "center", width = 40)
        tree2.column("info", anchor = "w", width = 120)
        tree2.heading("#0", text = "层级数", anchor = "w")
        tree2.heading("name", text = "子女号", anchor = "w")
        tree2.heading("number", text = "数量", anchor = "center")
        tree2.heading("info", text = "信息", anchor = "w")
        # self.bbf(tree2, -1, controller.root2, 2)
        tree2.grid(row = 1, column = 10, columnspan = 9, pady = 10, padx = 10, sticky = "nsew")
        tree2.bind('<Double-Button-1>', self.treeviewClick1)
        ybar2['command']=tree2.yview 
        ybar2.grid(row=1,column=15,sticky='ns')

        
        tree3 = ttk.Treeview(self, yscrollcommand=ybar3.set)
        tree3['columns'] = ["name", "number", "info", "namex", "numberx", "infox"]
        tree3.column("#0", width = 120)
        tree3.column("name", anchor = "w", width = 80, minwidth = 60)
        tree3.column("number", anchor = "center", width = 40)
        tree3.column("info", anchor = "w", width = 120)
        tree3.column("namex", anchor = "w", width = 80, minwidth = 60)
        tree3.column("numberx", anchor = "center", width = 40)
        tree3.column("infox", anchor = "w", width = 120)
        tree3.heading("#0", text = "层级数", anchor = "w")
        tree3.heading("name", text = "子女号", anchor = "w")
        tree3.heading("number", text = "数量", anchor = "center")
        tree3.heading("info", text = "信息(项目名称|标识码|状态)", anchor = "w")
        tree3.heading("namex", text = "子女号", anchor = "w")
        tree3.heading("numberx", text = "数量", anchor = "center")
        tree3.heading("infox", text = "信息", anchor = "w")
        # self.bbf(tree3, -1, controller.root2)
        
        tree3.tag_configure('half', foreground = "blue")
        tree3.tag_configure('dif', foreground = "red")
        tree3.tag_configure('same', foreground = "black")
        tree3.tag_configure('rule', foreground = "green")
        tree3.bind('<Double-Button-1>', self.treeviewClick2)
        self.tree1 = tree1
        self.tree2 = tree2
        self.tree3 = tree3
        tree3.grid(row = 1, column = 5, columnspan = 5, pady = 10, padx = 10, sticky = "nsew")
        ybar3['command']=tree3.yview 
        ybar3.grid(row=1,column=9,sticky='ns')

        button6 = ttk.Button(self, text="全部比较", command = lambda:self.run(op = True, fo = True))
        button6.grid(row = 0, column = 7, pady = 10, padx = 10, sticky = "nsew")
        button8 = ttk.Button(self, text="单层比较", command = lambda:self.run(op = False, fo = False))
        button8.grid(row = 0, column = 8, pady = 10, sticky = "nsew")
        hei = tk.Frame(self)
        hei.grid(row = 0, column = 5, columnspan = 2, padx = 10, pady = 10, sticky = "nsew")
        text4 = tk.Label(hei, text = "展开到层级：", font = SmallFont)
        text4.grid(row = 0, column = 0, sticky = "nsew")
        input1 = tk.Entry(hei)
        input1.insert(0,"输入层级数")
        input1.grid(row = 0, column = 1, columnspan = 3, sticky = "nsew")
        button1 = ttk.Button(hei, text="更改", command = lambda:self.unfold(input1))
        button1.grid(row = 0, column = 4, padx = 10, sticky = "nsew")
        button2 = ttk.Button(self, text="插入等号规则", command = lambda:self.askrule())
        button2.grid(row = 2, column = 8, pady = 10, sticky = "nsew")
        button7 = ttk.Button(self, text="插入不展开名称规则", command = lambda:self.askrule2())
        button7.grid(row = 2, column = 7, pady = 10, padx = 10,sticky = "nsew")

        sea = tk.Frame(self)
        sea.grid(row = 2, column = 5, columnspan = 2, padx = 10, pady = 10, sticky = "nsew")
        text5 = tk.Label(sea, text = "在表三中查找：", font = SmallFont)
        text5.grid(row = 0, column = 0, sticky = "nsew")
        input2 = tk.Entry(sea)
        input2.insert(0,"输入名称")
        fram = tk.Frame(sea)
        fram.grid(row = 0, column = 4, columnspan = 1,sticky = "nsew")
        but1 = ttk.Button(fram, text="<", command = lambda:self.bef())
        but1.grid(row = 0, column = 0, sticky = "nsew")
        but2 = ttk.Button(fram, text=">", command = lambda:self.next())
        but2.grid(row = 0, column = 1,sticky = "nsew")
        input2.grid(row = 0, column = 1, columnspan = 3, sticky = "nsew")
        self.input2 = input2
        buttonn1 = ttk.Button(sea, text="搜索", command = lambda:self.searchf3())
        buttonn1.grid(row = 0, column = 5, padx = 10, sticky = "nsew")


        
        button3 = ttk.Button(self, text="选择层级展开表", command = lambda:self.insertform1())
        button3.grid(row = 0, column = 3, pady = 10, sticky = "nsew")
        button4 = ttk.Button(self, text="选择父子本展开表", command = lambda:self.insertform2())
        button4.grid(row = 0, column = 13, pady = 10, sticky = "nsew")
        button5 = ttk.Button(self, text="打印", command = lambda:self.printt())
        button5.grid(row = 2, column = 13, pady = 10, sticky = "nsew")

        popup1 = tk.Menu(tree3, tearoff=0)
        self.popup1 = popup1
        popup1.add_command(command=lambda:self.copy2(0),label="复制表一名称")
        popup1.add_command(command=lambda:self.copy2(3),label="复制表二名称")
        # popup1.add_command(label="Ctrl+f", command=self.cntrlf)
        # tree3.bind('<Control-f>', self.searchbox)
        popup1.add_command(label="撤销表一层级", command=self.deletehierachy1)
        popup1.add_command(label="撤销表二层级", command=self.deletehierachy2)
        popup1.add_command(label="显示已撤销层级", command=self.showdeleted)
        tree3.bind('<Button-3>', self.popup_menu)

        popup2 = tk.Menu(tree2, tearoff=0)
        self.popup2 = popup2
        popup2.add_command(command=lambda:self.your_copy(tree2),label="复制名称")
        tree2.bind('<Button-3>', self.popup_menu2)

        popup3 = tk.Menu(tree1, tearoff=0)
        self.popup3 = popup3
        popup3.add_command(command=lambda:self.your_copy(tree1),label="复制名称")
        tree1.bind('<Button-3>', self.popup_menu3)
    def next(self):
        if self.find == []:
            return
        self.fidx += 1
        if self.fidx >= len(self.find):
            self.fidx -= len(self.find)
        self.tree3.see(self.find[self.fidx])
        self.tree3.focus([self.find[self.fidx]])
        self.tree3.selection_set(self.find[self.fidx])
    def bef(self):
        if self.find == []:
            return
        self.fidx -= 1
        if self.fidx < 0:
            self.fidx += len(self.find)
        self.tree3.see(self.find[self.fidx])
        self.tree3.focus([self.find[self.fidx]])
        self.tree3.selection_set(self.find[self.fidx])
    def searchf3(self):
        self.find.clear()
        self.fidx = 0
        cache = {}
        for iid in self.dic3:
            n1, n2 = self.dic3[iid]
            t = False
            if n1 != None:
                name1 = n1.name
                cache.clear()
                t = t or self.search(0, 0, name1, (str(self.input2.get())).strip(), cache)
            if n2 != None:
                name2 = n2.name
                cache.clear()
                t = t or self.search(0, 0, name2, (str(self.input2.get())).strip(), cache)
            if t:
                self.find.append(iid)
        if self.find == []:
            return
        print(self.find)
        self.tree3.see(self.find[self.fidx])
        self.tree3.focus([self.find[self.fidx]])
        self.tree3.selection_set(self.find[self.fidx])
            
    def printt(self):
        f = filedialog.asksaveasfile(mode='wb', defaultextension=".xlsx")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        wb = Workbook()
        ws = wb.active
        ws.append(["表一层级", "表一名称", "表一数量", "表一项目名称", "表一标识码","表一状态", "表二层级", "表二名称", "表二数量", "表二信息"])
        # inffo = self.controller.root1.info.split("|")
        # ws.append([self.controller.root1.height, self.controller.root1.name, self.controller.root1.number, inffo[0],
        #     int(inffo[1]), inffo[2],self.controller.root2.height, self.controller.root2.name, self.controller.root2.number, self.controller.root2.info])
        open_opt = tk.BooleanVar()
        for iid in self.dic3:
            parent_iid = self.tree3.parent(iid)
            if parent_iid:
                open_opt.set(str(self.tree3.item(parent_iid, option='open')))
                opened = open_opt.get()
                # print(dic3[parent_iid][0].name)
                # print(opened)
                if (opened):
        # for iid in self.dic3:
                    n1, n2 = self.dic3[iid]
                    if n1 == None:
                        writenode2(n2, True, ws)
                    elif n2 == None:
                        writenode1(n1, True, ws)
                    elif n1.name != n2.name:
                        inffo = n1.info.split("|")
                        h = WriteOnlyCell(ws, value=n1.height)
                        h.font = blue
                        n = WriteOnlyCell(ws, value=n1.name)
                        n.font = blue
                        num = WriteOnlyCell(ws, value=n1.number)
                        num.font = blue
                        i = WriteOnlyCell(ws, value=inffo[0])
                        i.font = blue
                        ii = WriteOnlyCell(ws, value=int(inffo[1]))
                        ii.font = blue
                        iii = WriteOnlyCell(ws, value=inffo[2])
                        iii.font = blue
                        h2 = WriteOnlyCell(ws, value=n2.height)
                        h2.font = blue
                        n22 = WriteOnlyCell(ws, value=n2.name)
                        n22.font = blue
                        num2 = WriteOnlyCell(ws, value=n2.number)
                        num2.font = blue
                        i2 = WriteOnlyCell(ws, value=n2.info)
                        i2.font = blue
                        ws.append([h, n, num, i,ii,iii, h2, n22, num2, i2])
                    else:
                        inffo = n1.info.split("|")
                        ws.append([n1.height, n1.name, n1.number, inffo[0], int(inffo[1]),inffo[2], n2.height, n2.name, n2.number, n2.info])
            else:
                n1, n2 = self.dic3[iid]
                if n1 == None:
                    writenode2(n2, True, ws)
                elif n2 == None:
                    writenode1(n1, True, ws)
                elif n1.name != n2.name:
                    inffo = n1.info.split("|")
                    h = WriteOnlyCell(ws, value=n1.height)
                    h.font = blue
                    n = WriteOnlyCell(ws, value=n1.name)
                    n.font = blue
                    num = WriteOnlyCell(ws, value=n1.number)
                    num.font = blue
                    i = WriteOnlyCell(ws, value=inffo[0])
                    i.font = blue
                    ii = WriteOnlyCell(ws, value=int(inffo[1]))
                    ii.font = blue
                    iii = WriteOnlyCell(ws, value=inffo[2])
                    iii.font = blue
                    h2 = WriteOnlyCell(ws, value=n2.height)
                    h2.font = blue
                    n22 = WriteOnlyCell(ws, value=n2.name)
                    n22.font = blue
                    num2 = WriteOnlyCell(ws, value=n2.number)
                    num2.font = blue
                    i2 = WriteOnlyCell(ws, value=n2.info)
                    i2.font = blue
                    ws.append([h, n, num, i,ii,iii, h2, n22, num2, i2])
                else:
                    inffo = n1.info.split("|")
                    ws.append([n1.height, n1.name, n1.number, inffo[0], int(inffo[1]),inffo[2], n2.height, n2.name, n2.number, n2.info])
        wb.save(f)
    def copy2(self, index):
        item = self.tree3.selection()[0]
        self.clipboard_clear()
        self.clipboard_append(self.tree3.item(item)["values"][index])
    def your_copy(self, tree):
        item = tree.selection()[0]
        self.clipboard_clear()
        self.clipboard_append(tree.item(item)["values"][0])
    def increaseheight(self,node):
        node.height -= 1
        for i in node.children:
            self.increaseheight(i)
    def decreaseheight(self,node):
        node.height += 1
        for i in node.children:
            self.decreaseheight(i)

    def showdeleted(self):
        diag = Delet(self)
        self.wait_window(diag) # 这一句很重要！！！
    def restore(self, node, tc):
        if tc == 1:
            pnode = self.hid1[node]
        else:
            pnode = self.hid2[node]
        for c in node.children:
            pnode.children.remove(c)
        pnode.children.append(node)
        sorted(pnode.children, key=lambda child: child.name)
        self.decreaseheight(node)
        self.run(op = True, fo = False)
        iid = node.id3
        self.tree3.see(iid)
        self.tree3.focus([iid])
        self.tree3.selection_set(iid)

    def deletehierachy1(self):
        fiid = self.tree3.selection()[0]
        nodes = self.dic3.get(fiid)
        node1 = nodes[0]
        if node1 != None:
            print(node1.name)
            parent_iid = self.tree1.parent(node1.id1)
            pnode = self.dic1[parent_iid]
            print(pnode.name)
            print("X")
            self.increaseheight(node1)
            for c in node1.children:
                pnode.children.append(c)
                print(c.name)
            print("X")
            for c in pnode.children:
                print(c.name)
            pnode.children.remove(node1)
            sorted(pnode.children, key=lambda child: child.name) 
            print("X")
            for c in pnode.children:
                print(c.name)
            self.hid1[node1] = pnode
            print("root2")
            self.run(op = True, fo = False)
            iid = node1.children[0].id3
            print(node1.children[0].name)
            self.tree3.see(iid)
            self.tree3.focus([iid])
            self.tree3.selection_set(iid)
    def deletehierachy2(self):
        fiid = self.tree3.selection()[0]
        nodes = self.dic3.get(fiid)
        node2 = nodes[1]
        if node2 != None:
            print(node2.name)
            parent_iid = self.tree2.parent(node2.id1)
            pnode = self.dic2[parent_iid]
            print(pnode.name)
            self.increaseheight(node2)
            for c in node2.children:
                pnode.children.append(c)
            pnode.children.remove(node2)
            sorted(pnode.children, key=lambda child: child.name) 
            self.hid2[node2] = pnode
            self.run(op = True, fo = False)
            iid = node2.children[0].id3
            self.tree3.see(iid)
            self.tree3.focus([iid])
            self.tree3.selection_set(iid)
    def popup_menu(self, event):
        self.tree3.identify_row(event.y)
        self.popup1.post(event.x_root, event.y_root)
    def popup_menu2(self, event):
        self.tree2.identify_row(event.y)
        self.popup2.post(event.x_root, event.y_root)
    def popup_menu3(self, event):
        self.tree1.identify_row(event.y)
        self.popup3.post(event.x_root, event.y_root)
            
        
    def treeviewClick0(self, event):
        self.locateform(self.tree3, self.tree1, self.dic1)
    def treeviewClick1(self, event):
        self.locateform(self.tree3, self.tree2, self.dic2)
    def treeviewClick2(self, event):
        self.locateformb()
    def bbf(self, tree, pid, node, tn):
        if pid == -1:
            pid = ""
        else:
            pid = str(pid)
        iid = tree.insert(parent = pid, index = 'end', text = str(node.height),
            values = (node.name, node.number, node.info),  open = True)
        node.id1 = iid
        if tn == 1:
            self.dic1[iid] = node
        else:
            self.dic2[iid] = node
        for i in node.children:
            self.bbf(tree, iid, i, tn)
    #make form 3
    def compare(self, node1, node2, tree, titles, op):
        opp = op
        if self.controller.maxheight > 0 and (node1.height >= self.controller.maxheight - 1 or node2.height >= self.controller.maxheight - 1):
            opp = False
        elist = {}
        for i in titles:
            elist[i] = titles[i].copy()
        if node1.children == [] and node2.children == []:
            return
        elif node1.children == []:
            for i in node2.children:
                # if i.find == 1:
                #     continue
                # if i.hid == 1:
                #     i.iid = node2.iid
                #     i.find = 1
                #     self.compare(node1, i, tree, elist, op)
                #     continue
                if i.name[-1] == "*":
                    i.name = i.name[:-1]
                # writenode2(i, True, ws)
                if node2.iid == -1:
                    pid = ""
                else:
                    pid = str(node2.iid)
                oppp = opp
                if self.controller.nolist.get(i.name) != None and  self.controller.nolist.get(i.name)> 0:
                    oppp = False
                i.iid = tree.insert(parent = pid, index = 'end', text = str(i.height), open = oppp,
                    values = ("", "", "",i.name, i.number, i.info), tags = ('dif',))
                # i.find = 1
                self.dic3[i.iid] = [None, i]
                i.id3 = i.iid
                self.compare(empty, i, tree, self.controller.titles, oppp)
            return
        elif node2.children == []:
            for i in node1.children:
                if i.number == 0:
                    continue
                # if i.hid == 1:
                #     i.iid = node1.iid
                #     i.find = 1
                #     self.compare(i, node2, tree, elist, op)
                #     continue
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                oppp = opp
                if self.controller.nolist.get(i.name) != None and self.controller.nolist.get(i.name) > 0:
                    oppp = False
                i.iid = tree.insert(parent = pid, index = 'end', text = str(i.height),open = oppp,
                    values = (i.name, i.number, i.info, "", "", ""), tags = ('dif',))
                # i.find = 1
                self.dic3[i.iid] = [i, None]
                i.id3 = i.iid
                self.compare(i, empty, tree, self.controller.titles, oppp)  
            return
        dic = {}
        predic = {}
        sdic = {}
        for n1 in node1.children:
            dic[n1.name.strip()] = n1
            pre = n1.name.split("-")[0]
            if predic.get(pre) == None:
                predic[pre] = [n1]
            else:
                predic[pre].append(n1)
            
            sfx = n1.name.split("_")[0]
            if sdic.get(sfx) == None:
                sdic[sfx] = [n1]
            else:
                sdic[sfx].append(n1)
        #combine nodes of the same name
        for n2 in node2.children:
            if n2.find == 1:
                continue
            # if n2.hid == 1:
            #     n2.iid = node2.iid
            #     n2.find = 1
            #     self.compare(node1, n2, tree, elist, op)
            #     continue
            if n2.name[-1] == "*":
                n2.name = n2.name[:-1]
            if dic.get(n2.name.strip()) != None:
                n1 = dic.get(n2.name.strip())
                if n1.find == 1:
                    continue
                if n1.number == 0:
                    n1.find = 1
                    continue
                # if n1.hid == 1:
                #     n1.find = 1
                #     n1.iid = node1.iid
                #     self.compare(n1, node2, tree, elist, op)
                #     continue
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                oppp = False
                if self.controller.nolist.get(n1.name) != None and self.controller.nolist.get(n1.name) > 0:
                    oppp = False
                if self.controller.nolist.get(n2.name) != None and self.controller.nolist.get(n2.name)> 0:
                    oppp = False
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),open = oppp,
                    values = (n1.name, n1.number, n1.info, n2.name, n2.number, n2.info), tags = ('same',))
                n2.iid = n1.iid
                n1.find = 1
                n2.find = 1
                self.dic3[n1.iid] = [n1, n2]
                n1.id3 = n1.iid
                n2.id3 = n2.iid
                self.compare(n1, n2, tree, self.controller.titles, oppp)

        #combine nodes with the same sfix of name
        for n2 in node2.children:
            if n2.find == 1:
                continue
            # if n2.hid == 1:
            #     n2.iid = node2.iid
            #     n2.find = 1
            #     self.compare(node1, n2, tree, elist, op)
            #     continue
            sfx = n2.name.split("_")[0]
            if sdic.get(sfx) != None and sdic.get(sfx) != []:
                for n1 in sdic.get(sfx):
                    if n1.find == 1:
                        continue
                    if n1.number == 0:
                        n1.find = 1
                        continue
                    break
                if n1.find == 1:
                    continue
                sdic[sfx].remove(n1)
                # if n1.hid == 1:
                #     n1.iid = node1.iid
                #     n1.find = 1
                #     self.compare(n1, node2, tree, elist, op)
                #     continue
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                oppp = False
                if self.controller.nolist.get(n1.name) != None and self.controller.nolist.get(n1.name) > 0:
                    oppp = False
                if self.controller.nolist.get(n2.name) != None and self.controller.nolist.get(n2.name)> 0:
                    oppp = False
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),open = oppp,
                    values = (n1.name, n1.number, n1.info, n2.name, n2.number, n2.info), tags = ('same',))
                n2.iid = n1.iid
                n1.find = 1
                n2.find = 1
                self.dic3[n1.iid] = [n1, n2]
                n1.id3 = n1.iid
                n2.id3 = n2.iid
                self.compare(n1, n2, tree, self.controller.titles, oppp)




        #combine nodes that are required to be the same
        for n2 in node2.children:
            if n2.find == 1:
                continue
            # if n2.hid == 1:
            #     n2.find = 1
            #     n2.iid = node2.iid
            #     self.compare(node1, n2, tree, elist, op)
            #     continue
            if elist.get(n2.name) != None and elist.get(n2.name) != []:
                for n1name in elist.get(n2.name):
                    n1 = dic[n1name.strip()]
                    if n1.find == 1:
                        continue
                    if n1.number == 0:
                        n1.find = 1
                        continue
                    break
                if n1.find == 1:
                    continue
                elist[n2.name].remove(n1name)
                
                # if n1.hid == 1:
                #     n1.find = 1
                #     n1.iid = node1.iid
                #     self.compare(n1, node2, tree, elist, op)
                #     continue
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                oppp = False
                if self.controller.nolist.get(n1.name) != None and self.controller.nolist.get(n1.name) > 0:
                    oppp = False
                if self.controller.nolist.get(n2.name) != None and self.controller.nolist.get(n2.name)> 0:
                    oppp = False
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),open = oppp,
                    values = (n1.name, n1.number, n1.info, n2.name, n2.number, n2.info), tags = ('rule',))
                n2.iid = n1.iid
                n1.find = 1
                n2.find = 1
                self.dic3[n1.iid] = [n1, n2]
                n1.id3 = n1.iid
                n2.id3 = n2.iid
                self.compare(n1, n2, tree, self.controller.titles, oppp)
        #combine nodes with the same prefix of name
        for n2 in node2.children:
            if n2.find == 1:
                continue
            # if n2.hid == 1:
            #     n2.iid = node2.iid
            #     n2.find = 1
            #     self.compare(node1, n2, tree, elist, op)
            #     continue
            pre = n2.name.split("-")[0]
            if predic.get(pre) != None and predic.get(pre) != []:
                for n1 in predic.get(pre):
                    if n1.find == 1:
                        continue
                    if n1.number == 0:
                        n1.find = 1
                        continue
                    break
                if n1.find == 1:
                    continue
                predic[pre].remove(n1)
                # if n1.hid == 1:
                #     n1.iid = node1.iid
                #     n1.find = 1
                #     self.compare(n1, node2, tree, elist, op)
                #     continue
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                oppp = opp
                if self.controller.nolist.get(n1.name) != None and self.controller.nolist.get(n1.name) > 0:
                    oppp = False
                if self.controller.nolist.get(n2.name) != None and self.controller.nolist.get(n2.name)> 0:
                    oppp = False
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),open = oppp,
                    values = (n1.name, n1.number, n1.info, n2.name, n2.number, n2.info), tags = ('half',))
                n2.iid = n1.iid
                n1.find = 1
                n2.find = 1
                self.dic3[n1.iid] = [n1, n2]
                n1.id3 = n1.iid
                n2.id3 = n2.iid
                self.compare(n1, n2, tree, self.controller.titles, oppp)
        for n1 in node1.children:
            if n1.find == 0:
                if n1.number == 0:
                    n1.find = 1
                    continue
                # writenode1(n1, True, ws)
                # compare(n1, empty, ws)
                # if n1.hid == 1:
                #     print("h")
                #     n1.find = 1
                #     n1.iid = node1.iid
                #     self.compare(n1, node2, tree, elist, op)
                #     continue
                if node1.iid == -1:
                    pid = ""
                else:
                    pid = str(node1.iid)
                oppp = opp
                if self.controller.nolist.get(n1.name) != None and self.controller.nolist.get(n1.name) > 0:
                    oppp = False
                n1.iid = tree.insert(parent = pid, index = 'end', text = str(n1.height),open = oppp,
                    values = (n1.name, n1.number, n1.info, "", "", ""), tags = ('dif',))
                n1.find = 1
                self.dic3[n1.iid] = [n1, None]
                n1.id3 = n1.iid
                self.compare(n1, empty, tree, self.controller.titles, oppp) 
        for n2 in node2.children:
            if n2.find == 0:
                # writenode2(n2, True, ws)
                # compare(empty, n2, ws)
                # if n2.hid == 1:
                #     print("hb")
                #     n2.find = 1
                #     n2.iid = node2.iid
                #     self.compare(node1, n2, tree, elist, op)
                #     continue
                if node2.iid == -1:
                    pid = ""
                else:
                    pid = str(node2.iid)
                oppp = opp
                if self.controller.nolist.get(n2.name) != None and self.controller.nolist.get(n2.name)> 0:
                    oppp = False
                n2.iid = tree.insert(parent = pid, index = 'end', text = str(n2.height),open = oppp,
                    values = ("", "", "",n2.name, n2.number, n2.info), tags = ('dif',))
                self.dic3[n2.iid] = [None, n2]
                n2.find = 1
                n2.id3 = n2.iid
                self.compare(empty, n2, tree, self.controller.titles, oppp) 
    # search for form 1/2's node on form3
    def locateform(self, treesearch, treeselect, dic):
        fiid = treeselect.selection()[0]
        # print(fiid)
        node = dic.get(fiid)
        iid = node.id3
        if iid != -1:
            treesearch.see(iid)
            treesearch.focus([iid])
            treesearch.selection_set(iid)
    # search for form 3's node on form1/2
    def locateformb(self):
        fiid = self.tree3.selection()[0]
        nodes = self.dic3.get(fiid)
        node1 = nodes[0]
        node2 = nodes[1]
        if node1 != None:
            iid1 = node1.id1
            self.tree1.see(iid1)
            self.tree1.focus([iid1])
            self.tree1.selection_set(iid1)
        if node2 != None:
            iid2 = node2.id1
            self.tree2.see(iid2)
            self.tree2.focus([iid2])
            self.tree2.selection_set(iid2)
    def insertform1(self):
        filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
        if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        for i in self.tree1.get_children():
            self.tree1.delete(i)
        self.dic1.clear()
        self.hid1.clear()
        self.controller.root1 = form1(filename)
        self.controller.f1 = 1
        self.bbf(self.tree1, -1, self.controller.root1, 1)
    def insertform2(self):
        filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
        if filename is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        for i in self.tree2.get_children():
            self.tree2.delete(i)
        self.dic2.clear()
        self.hid2.clear()
        self.controller.root2 = form2(filename)
        self.controller.f2 = 1
        self.bbf(self.tree2, -1, self.controller.root2, 2)
    #run (default open, clean max height)
    def run(self, op, fo):
        #erase the find value of each node
        clean(self.controller.root1)
        clean(self.controller.root2)
        self.dic3.clear()
        if fo:
            self.controller.maxheight = -1
        items = self.tree3.get_children()
        [self.tree3.delete(item) for item in items]
        iid = self.tree3.insert(parent = "", index = 'end', text = str(0),open = True,
                    values = (self.controller.root1.name,self.controller.root1.number, self.controller.root1.info, self.controller.root2.name, 
                        self.controller.root2.number, self.controller.root2.info))
        self.dic3[iid] = [self.controller.root1, self.controller.root2]
        self.compare(self.controller.root1, self.controller.root2, self.tree3, self.controller.titles, op)
        print(len(self.dic3))
    def unfold(self, input1):
        height = input1.get()
        try: 
            int(height)
            self.controller.maxheight = int(height)
        except:
            pass
        # print(self.controller.maxheight)
        self.run(op = True, fo = False)
    def askrule(self):
        diag = Rule(self.controller)
    
        self.wait_window(diag) # 这一句很重要！！！
        
        if diag.userinfo != None:
            print(self.controller.titles)
            self.run(True, False)
            print(self.controller.titles)
    def askrule2(self):
        diag = Rule2(self.controller)
    
        self.wait_window(diag) # 这一句很重要！！！
        
        if diag.userinfo != None:
            self.run(True, False)
    #implement a regular expression search
    def regsearch(self, i, j, s, p, cache):
        if (i, j) in cache:
            return cache[(i,j)]
        if i >= len(s) and j >= len(p):  #abc^     abc^
            return True
        if i < len(s) and j >= len(p):   #a^a        a^
            return False                 # i > len(s) and j < len(p): ab^  ab^c* might be true

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')     #ab ab/.b
        if (j + 1)< len(p) and p[j + 1] == '*':   #most annoying *
            cache[(i,j)] =  (self.regsearch(i, j + 2, s, p, cache) #ignore char 
                or (match and self.regsearch(i + 1, j, s, p, cache))) #repeat char
            return cache[(i,j)]
        #no * now
        if match:
            cache[(i,j)] = self.regsearch(i + 1, j + 1, s, p, cache)
            return cache[(i,j)]
        cache[(i,j)] = False
        return False
    #implement a smith search: * stand for unknown string of unknown length
    def search(self, i, j, s, p, cache):
        if (i, j) in cache:
            return cache[(i,j)]
        if i >= len(s) and j >= len(p):  #abc^     abc^
            return True
        if i < len(s) and j >= len(p):   #a^a        a^
            return False                 # i > len(s) and j < len(p): ab^  ab^c* might be true
        if i >= len(s):
            if j == len(p) - 1 and p[j] == "*":
                return True
            else:
                return False
        if p[j] == "*":
            cache[(i, j)] = self.search(i + 1, j, s, p, cache) or self.search(i + 1, j + 1, s, p, cache)
            return cache[(i, j)]
        if i < len(s) and s[i] == p[j]:
            cache[(i,j)] = self.search(i + 1, j + 1, s, p, cache)
            return cache[(i,j)]
        cache[(i, j)] = False
        return False
        

