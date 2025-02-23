decimal=int(input("enter the decimal numer:-"))
convert=int(input("convert into  : [1]binary  [2]octal  [3]hexadecimal :"))

if convert==1:
    print("convert the decimal to binary",bin(decimal))
elif convert==2:
    print("convert decimal to octal ",oct(decimal))
elif convert==3:
    print("convert decimal to hexadecimal",hex(decimal))
else:
    print("nothing")
