def computepay(h,r):
    if h > 40:
        pay = (40*r)+((h-40)*(r*1.5))
        return pay
    elif h < 40:
        pay = h*r
        return pay
        

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float(rate)
pay = 0
p = computepay(hrs,rate)
print("Pay",p)
