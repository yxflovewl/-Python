
x=int(input('输入一个数字'))
y=int(input('输入一个数字'))

for i in range(1,min(x,y)+1):
    if y%i==0 and x%i==0:
        a=i
print(a)
#print(min(2,12))

























