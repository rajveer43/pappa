n = int(input("Enter number of rule"))
dic = {}
for i in range(n):
    re = input("Enter the Regular expression: ")
    a = re.split('->')
    if i == 0:
        start = a[0]
    dic[a[0]] = a[1].split('/')

first = {}
flist = set()


def findFirst(i):
    for j in dic[i]:
        # print(j)
        a = j.split(' ')
        if a[0] not in dic.keys():
            flist.add(a[0])
        else:
            findFirst(a[0])
    return flist


for i in dic.keys():
    first[i] = findFirst(i)
    flist = set()

print(first)

follow = {}
copyTo = {}


def findFollow(i):
    if i == start:
        follow[i] = set('$')
    for j in dic[i]:
        a = j.split(' ')
        for k in range(len(a)):
            if a[k] in dic.keys():
                if k != len(a)-1:
                    if a[k+1] not in dic.keys():
                        if a[k] in follow.keys():
                            follow[a[k]] = set(a[k+1]).union(follow[a[k]])
                        else:
                            follow[a[k]] = set(a[k+1])
                    else:
                        for elm in first[a[k+1]]:
                            if a[k] in follow.keys():
                                follow[a[k]] = set(elm).union(follow[a[k]])
                            else:
                                follow[a[k]] = set(elm)

                else:
                    if a[k] in dic.keys():
                        if i in copyTo.keys():
                            copyTo[i] = set(a[k]).union(copyTo[i])
                        else:
                            copyTo[i] = set(a[k])


for i in dic.keys():
    findFollow(i)

for i in copyTo.keys():
    for j in copyTo[i]:
        if j in follow.keys():
            follow[j] = follow[i].union(follow[j])
        else:
            follow[j] = follow[i]
print(follow)
# ε
parseTable = {}
flag = False
for i in dic.keys():
    parseTable[i] = {}
    for b in dic[i]:
        j = b.split(" ")
        if j[0] in dic.keys():
            a = first[j[0]]
            for k in a:
                if k in parseTable[i].keys():
                    flag = True
                    parseTable[i][k] = set([b]).union(parseTable[i][k])
                else:
                    parseTable[i][k] = set([b])
        else:
            if j[0] in parseTable[i].keys():
                parseTable[i][j[0]] = set([b]).union(parseTable[i][j[0]])
                flag = True
            else:
                parseTable[i][j[0]] = set([b])

print(parseTable)
if flag:
    print("Not LL1")
else:
    print("LL1")