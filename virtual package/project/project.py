from openpyxl import Workbook
import queue
wb = Workbook()
ws = wb.active

class Node:
    def __init__(self, height, name, number, info):
        self.height = int(height)
        self.name = name
        self.number = int(number)
        self.info = info
        self.children = []
        self.color = 0
    def addchildren(self, child) :
        self.children.append(child)
    def equal(self, other) :
        if self.name == other.name :
            return True
        return False
    def numberEq (self, other):
        if self.number == other.number :
            return True
        return False

def dfs(node) :
    print(node.name)
    if node.children == []:
        return
    for i in node.children:
        dfs(i)
def dfs2(node, map) :
    print("%d %s" % (node.height, node.name))
    if map.get(node.name) == None:
        return
    for i in map[node.name]:
        i.height = node.height + 1
        dfs2(i, map)

def bfs(queue):
    while queue.empty() == False:
        node = queue.get()
        print(node.name)
        for i in node.children:
            queue.put(i)

def check(node):
    if node.children == []:
        return
    for i in node.children:
        check(i)

def compare():
    pass
data1 = {}
hierachy1 = {}
root1 = Node(0,"default",0,"default")

with open('35G0F-t38V0bom.txt','r') as f:
    count = 0
    for line in f:
        if count == 0:
            count += 1
            continue;
        firstindex = line.find("\t")
        height = line[:firstindex];
        if height == "":
            break
        line = line[firstindex:];
        line = line.lstrip();
        secondindex = line.find("\t")
        name = line[0 : secondindex]

        line = line[secondindex:];
        line = line.lstrip();
        thirdindex = line.find("\t")
        number = line[0 : thirdindex]

        line = line[thirdindex:];
        line = line.lstrip();
        index = line.find("\t")
        project = line[0 : index]

        line = line[index:];
        line = line.lstrip();
        index = line.find("\t")
        sign = line[0 : index]

        line = line[index:];
        line = line.lstrip();
        condition = line.find("\t")
        condition = line[0 : index]

        info = project + "\t" + sign + "\t" + condition
        node = Node(height, name, number, info)
        height = int(height)
        if height == 0:
            root1 = node
        hierachy1[height] = node
        parent = hierachy1.get(height - 1)
        if parent != None:
            parent.children.append(node)
# dfs(root1)

data2 = {}
parent = Node(-1,"default",0,"default")
root2 = Node(0,"default",0,"default")
parentname = ""
with open('3506001-t38v0_asm00_pre.txt','r') as f:
    count = 0
    for line in f:
        firstindex = line.find("\t") 
        line = line[firstindex:]
        line = line.lstrip();
        if firstindex != 0:
            secondindex = line.find("\t")
            parentname = line[0 : secondindex]
            data2[parentname] = []
            parent.name = parentname
            if count == 0:
                root2 = Node(0, parentname, 1, "default")
                count+=1
        else:
            secondindex = line.find("\t")
            number = line[0 : secondindex]
            if number == "":
                continue
            line = line[secondindex:]
            line = line.lstrip();
            secondindex = line.find("\t")
            info = line[0 : secondindex]

            line = line[secondindex:]
            name = line.strip();
            if info == "零件":
                name = name + "*"
            node = Node(-1, name, number, info)
            data2[parentname].append(node)
            parent.children.append(node)
dfs2(root2, data2)
            
# q1 = queue.Queue()
# q1.put(root1)
# bfs(q1)

