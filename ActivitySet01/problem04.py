# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=float(input("Enter rate:"))
if h>40:
    pay=rate*40+(h-40)*rate*1.5
    print(pay)
else:
    pay=rate*h
    print(pay)
