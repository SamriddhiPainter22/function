print("Please Enter the String : ",end="")
string = input()
string_length=len(string)
for k in string:
    ascii = ord(k)
    print(k,"\t",ascii)