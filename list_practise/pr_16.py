a=[1,2,3,4]
if a[0]>a[2]:
    f1=a[0]
else:
    f1=a[2]

if a[1]>a[3]:
    f2=a[1]
else:
    f2=a[3]

if f1>f2:
    print(str(f1) + " is largest")
else:
    print(str(f2) + " is largest")