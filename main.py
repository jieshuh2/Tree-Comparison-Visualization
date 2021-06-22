from ui import * 
def main():
    window = UI()
    window.mainloop()

if __name__ == '__main__':
    main()


# def openfile1():
#     filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
#     f = open(filename, 'r')
#     hierachy1 = {}
#     count = 0
#     #convert form 1 into tree
#     for line in f:
#         if count == 0:
#             count += 1
#             continue;
#         firstindex = line.find("\t")
#         height = line[:firstindex];
#         if height == "":
#             break
#         line = line[firstindex:];
#         line = line.lstrip();
#         secondindex = line.find("\t")
#         name = line[0 : secondindex]

#         line = line[secondindex:];
#         line = line.lstrip();
#         thirdindex = line.find("\t")
#         number = line[0 : thirdindex]

#         line = line[thirdindex:];
#         line = line.lstrip();
#         index = line.find("\t")
#         project = line[0 : index]

#         line = line[index:];
#         line = line.lstrip();
#         index = line.find("\t")
#         sign = line[0 : index]

#         line = line[index:];
#         line = line.lstrip();
#         condition = line.find("\t")
#         condition = line[0 : index]

#         info = project + "\t" + sign + "\t" + condition
#         node = Node(height, name, number, info)
#         height = int(height)
#         if height == 0:
#             root1 = node
#         hierachy1[height] = node
#         parent = hierachy1.get(height - 1)
#         if parent != None:
#             parent.children.append(node)
#     f.close()
#     wb1 = Workbook()
#     ws1 = wb1.active
#     buildform(root1, ws1)
#     wb1.save("output/form1.xlsx")
#     f1 = 1

#     # dfs(root1)
# def openfile2():
#     filename = filedialog.askopenfilename(initialdir= "F:\computer\tree-project")
#     f = open(filename, 'r')
#     data2 = {}
#     rootname = ""
#     parentname = ""
#     for line in f:
#         firstindex = line.find("\t")

#         if firstindex != 0:
#             title = line[:firstindex]
#             if (title == "装配零件的总数"):
#                 break
#             line = line[firstindex:]
#             line = line.lstrip();
#             secondindex = line.find("\t")
#             parentname = line[0 : secondindex]
#             data2[parentname] = []
#             if rootname == "":
#                 rootname = parentname
#         else:
#             line = line.lstrip();
#             secondindex = line.find("\t")
#             number = line[0 : secondindex]
#             if number == "":
#                 continue
#             line = line[secondindex:]
#             line = line.lstrip();
#             secondindex = line.find("\t")
#             info = line[0 : secondindex]

#             line = line[secondindex:]
#             name = line.strip();
#             if (info == "零件"):
#                 name = name + "*"
#             node = Node(-1, name, number, info)
#             data2[parentname].append(node)
#     f.close()
#     root2 = Node(0, rootname, 1, "")
#     #tree two into tree
#     buildtree(data2, root2)

#     wb2 = Workbook()
#     ws2 = wb2.active
#     buildform(root2, ws2)
#     wb2.save("output/form2.xlsx")
#     f2 = 1

# #convert form 1 into tree
# hierachy1 = {}
# root1 = Node(0,"default",0,"default")
# with open('35G0F-t38V0bom.txt','r') as f:
#     count = 0
#     for line in f:
#         if count == 0:
#             count += 1
#             continue;
#         firstindex = line.find("\t")
#         height = line[:firstindex];
#         if height == "":
#             break
#         line = line[firstindex:];
#         line = line.lstrip();
#         secondindex = line.find("\t")
#         name = line[0 : secondindex]

#         line = line[secondindex:];
#         line = line.lstrip();
#         thirdindex = line.find("\t")
#         number = line[0 : thirdindex]

#         line = line[thirdindex:];
#         line = line.lstrip();
#         index = line.find("\t")
#         project = line[0 : index]

#         line = line[index:];
#         line = line.lstrip();
#         index = line.find("\t")
#         sign = line[0 : index]

#         line = line[index:];
#         line = line.lstrip();
#         condition = line.find("\t")
#         condition = line[0 : index]

#         info = project + "\t" + sign + "\t" + condition
#         node = Node(height, name, number, info)
#         height = int(height)
#         if height == 0:
#             root1 = node
#         hierachy1[height] = node
#         parent = hierachy1.get(height - 1)
#         if parent != None:
#             parent.children.append(node)
       
# data2 = {}
# rootname = ""
# #convert tree two into dic
# with open('3506001-t38v0_asm00_pre.txt','r') as f:
#     parentname = ""
#     for line in f:
#         firstindex = line.find("\t")

#         if firstindex != 0:
#             title = line[:firstindex]
#             if (title == "装配零件的总数"):
#                 break
#             line = line[firstindex:]
#             line = line.lstrip();
#             secondindex = line.find("\t")
#             parentname = line[0 : secondindex]
#             data2[parentname] = []
#             if rootname == "":
#                 rootname = parentname
#         else:
#             line = line.lstrip();
#             secondindex = line.find("\t")
#             number = line[0 : secondindex]
#             if number == "":
#                 continue
#             line = line[secondindex:]
#             line = line.lstrip();
#             secondindex = line.find("\t")
#             info = line[0 : secondindex]

#             line = line[secondindex:]
#             name = line.strip();
#             if (info == "零件"):
#                 name = name + "*"
#             node = Node(-1, name, number, info)
#             data2[parentname].append(node)
# root2 = Node(0, rootname, 1, "")
# #tree two into tree
# buildtree(data2, root2)


# wb1 = Workbook()
# ws1 = wb1.active
# buildform(root1, ws1)
# wb1.save("output/form1.xlsx")

# wb2 = Workbook()
# ws2 = wb2.active
# buildform(root2, ws2)
# wb2.save("output/form2.xlsx")

# wb3 = Workbook()
# ws3 = wb3.active
# compare(root1, root2, ws3, -1)
# wb3.save("output/form3.xlsx")
