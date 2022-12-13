def computepay(hours, rate):
    if h > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = houra * rate
    return pay
sh = input ("Enter Hours: ")
sr = input ("Enter Rate: ")
fh = float (sh)
fr = float (sr)
xp = float (sr)
xp = computepay(fh,fr)
print("Pay",xp)


def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p
    
hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print("Pay",p)

num = 0
largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        numb = int(num)
        except:
            print('Invalid input')
        if smallest is None :
            smallest = numb
        elif numb < smallest :
            smallest = numb
        elif numb > largest :
            largest = numb
print("Maximum is", largest)
print("Minimum is", smallest)

