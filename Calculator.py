def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multi(p,q):
    return p*q
def div(p,q):
    return p/q
print("Please select the operation")
print("a.add")
print("b.sub")
print("c.multi")
print("d.div")
choice=input("Plz enter the choice(a/b/c/d),")
num1=int(input("plz enter the first number"))
num2=int(input("plz enter the second number"))
if choice=='a':
       print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
       print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='c':
       print(num1,"*",num2,"=",multi(num1,num2))
elif choice=='d':
       print(num1,"/",num2,"=",div(num1,num2))
else:
    print("This is invalid input")