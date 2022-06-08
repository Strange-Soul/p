# Lists

filename = "dataset/romeo.txt"
#fname = input("Enter file name: ")
fh = open("dataset/romeo.txt")
lst = list()
for line in fh:
    line=line.rstrip()
    word=line.split()
    for w in word:
        if w not in lst:
            lst.append(w)
lst.sort()
print(lst)

