hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
pay = 0

if h>40:
    hrs = h - 40
    hrs = float(hrs)
    pay = (40*rate)+((hrs*rate)*1.5)
else:
    pay = (h*rate)
    
print(pay)
