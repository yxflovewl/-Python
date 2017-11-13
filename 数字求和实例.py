#自己编写的
sum=0
while True:
    number=input('请输入一个数字：')
    if number=='q':
        break
    sum+=eval(number)
print(sum)

