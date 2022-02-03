def add(P,Q):
#this fuction is used to add the no.
 return P+Q

def subtract(P,Q):
#this func is used to subtract two no.
 return P-Q

def multiply(P,Q):
#This func is used to multiply the no.
 return P*Q

def divide(P,Q):
#this func is used to divide two no.
 return P/Q

#now we will take inputs from the user
print("Please select the operation.")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")

Choice = input("Please enter your choice(a/b/c/d):")

num_1=int(input("Please enter the first number : "))
num_2 = int(input("Please enter second no : "))

if Choice=='a':
    print(num_1,"+",num_2,"=",add(num_1,num_2))

elif Choice=='b':
    print(num_1,"-",num_2,"=",subtract(num_1,num_2))

elif Choice=='c':
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))

elif Choice=='d':
    print(num_1,"/",num_2,"=",divide(num_1,num_2))

else:
    print("This is an invalid input")


