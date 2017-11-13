x=int(input('输入一个数字'))
y=int(input('输入一个数字'))
c=max(x,y)
while True:

    if c%x==0 and c%y==0:
        print(c)
        break
    c+=1
    # print(c)