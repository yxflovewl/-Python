a=eval(input('请输入a:'))
b=eval(input('请输入a:'))
c=eval(input('请输入a:'))
if b**2-4*a*c<0:
    print('对不起，没有根')
elif b**2-4*a*c==0:
    print('只有一个根，根值为',-b/(2*a))
else:
    # x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    # x2=(- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('有两个根，分别为{}{}'.format((-b+(b**2-4*a*c)**0.5)/(2*a),(-b-(b**2-4*a*c)**0.5)/(2*a)))
    print('有两个根，分别为%f和%d'%((-b+(b**2-4*a*c)**0.5)/(2*a),(-b-(b**2-4*a*c)**0.5)/(2*a)))#%d和%f的区别
#    print('有两个根，分别为',((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)), (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))






