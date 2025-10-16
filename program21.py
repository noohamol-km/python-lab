def modifyValue(a):
    print("Value received in function",a)
    a=10
    print("Value inside function after change",a)
#main
a=5
modifyValue(a)
print("Value outside the function",a)
