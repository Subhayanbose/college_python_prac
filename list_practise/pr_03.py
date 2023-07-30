a = ['my','name','is','bose']
b = a[-1]
a[-1]=a[0]
a[0]=b
print(a)