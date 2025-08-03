def factorial(n):
  if n==0 or n==1:
    return 1
  print(n)
  return n* factorial(n-1)

number=int(input("enter number"))
result = factorial(number)
print ("factorial of", number, "is",result)

def generate_fibonacci (n):
    fib_series=[]
    c,d=0,1
    for _ in range(n):
      fib_series.append(c)
      c,d =d,c+d
    return fib_series

num = int(input("eneter how manynumbers you want:"))
print("fibonacci series:",generate_fibonacci(num))

print("welcome to the Tip Calculator")


bill = float(input("what is the total bill?"))
tip_percent=float(input("how much tip you like to give?"))
people=int(input("how many to split the bill between?"))

tip_amount= (tip_percent / 100)*bill
total_bill=bill+tip_amount
eachperson=total_bill / people

print(f"each individual should pay:{eachperson:.2f} JD(including tip)")