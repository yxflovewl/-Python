#判断了！
a=eval(input('请输入一个数字a：'))
b=eval(input('请输入一个数字b：'))
c=eval(input('请输入一个数字c：'))
s=(a+b+c)/2
while a+b<c or a+c<b or b+c<a:
    print ('输入的边构不成三角形，请重新输入！')
    a = float (input ('输入三角形第一边长：'))
    b = float (input ('输入三角形第二边长：'))
    c = float (input ('输入三角形第三边长：'))

mianji=(s*(s-a)*(s-b)*(s-c))**0.5
print(mianji)


