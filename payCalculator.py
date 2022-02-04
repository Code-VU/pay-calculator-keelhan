def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = float(input("Enter Hours: "))
    hpay = float(input("Hourly Wage?: "))
    if hrs > 40 :
        gpay =hrs*hpay + (hrs-40)*(0.5*hpay)
        print (str(gpay))
    else:
         gpay =hrs*hpay
         print (str(gpay))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculatePay()