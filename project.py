class Node:
    def __init__(self, height, name, number, info):
        self.height = int(height)
        self.name = name
        self.number = int(number)
        self.info = info
        self.children = []
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

def buildFirst(root, before):
    if data1.__len__ == 0:
        return
    toinsert = data1[0]
    while toinsert.height == root.height + 1:
        root.addchildren(toinsert)
        print("xx " + toinsert.name + " 1")
        before = toinsert
        data1.pop(0)
        toinsert = data1[0]

    if toinsert.height <= root.height:
        print("xx " + toinsert.name + " 2")
        return
    if toinsert.height > root.height + 1:
        before.addchildren(toinsert)
        data1.pop(0)
        print("xx " + toinsert.name + " 3")
        buildFirst(before, toinsert)
    



def dfs(node) :
    print(node.name)
    if node.children == []:
        return
    for i in node.children:
        dfs(i)

data1 = []
data2 = []
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
        data1.append(node)
# for i in data1:
#     print(i.name)
# print("dfs")
root = data1[0]
data1.pop(0)
buildFirst(root, root)
dfs(root)
print(len(root.children))
