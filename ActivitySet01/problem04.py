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

'''score =float(input("Enter Score: "))
if score > 1.0:
    print('Error')
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else: 
    print('F')'''


