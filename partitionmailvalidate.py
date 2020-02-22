a=input()
b=a.count("@")
if b==1:
    d=a.partition('@')
    if len(d[0])>=6 and len(d[2])>=3 and a[-4:]==".com":
        print("Valid")
    else:
        print("InValid")
else:
    print("inValid")
