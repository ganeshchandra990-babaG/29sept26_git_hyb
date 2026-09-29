import time
import webbrowser
a=float(input("Enter Num1: "))
b=float(input("Enter Num2: "))
c=float(input("Enter Num3: "))

url1=("www.google.com")
url2=("www.github.com")
url3=("www.apple.in")

sum=(a+b+c)
print (f"Sum={sum}")

time.sleep(2)

multi=(a*b*c)
print (f"Multiply= {multi}")
time.sleep(2)

div=((a+b)/c)
print (f"This DIV= {div}")


if (sum >= multi):
    webbrowser.open(url1)

elif (multi <= sum):
    webbrowser.open(url2)
else:
    webbrowser.open(url3)


