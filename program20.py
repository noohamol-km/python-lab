def sum(a,b):  #Function header with 2 parameters a & b
    """This function finds the sum of 2 numbers""" #Docstring
    total=a + b
    return total
#main function
a=int(input("enter a "))
b=int(input("enter b "))
s=sum(a,b)
print(a,"+",b,"=",s)
