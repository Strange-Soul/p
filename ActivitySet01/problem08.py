# Files

filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(filename)
count = 0
number = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue       
    x= line.find('0')        
    number = number + float(line[x:])
    count = count + 1    
print("Average spam confidence:", float(number/count))
