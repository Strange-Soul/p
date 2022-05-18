# Functions
def computepay(hrs, rate):
  if hrs>40:
    pay=rate*40+(hrs-40)*rate*1.5
    print(pay)
  else:
    pay=rate*hrs
    print(pay)
    
hrs = float(input("Enter hours:"))
rate = float(input("Enter rate per hour:"))

p = computepay(hrs, rate)
print("Pay", p)
