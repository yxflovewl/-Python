''''''
'''
如果一个n位正整数等于其各位数字的n次方之和,
  则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。
1000以内的阿姆斯特朗数： 
1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
以下代码用于检测用户输入的数字是否为阿姆斯特朗数：
'''
#如何判断
'''
for i in range(1,10000):
    list1=[]
    i=str(i);len1=len(i)
    for j in range(0,len1):
        a1=int(i[j])**len1
        list1.append(a1)
    if int(i)==sum(list1):
        print(i)
'''
'''
for i in range(1,10000):
    list1=[]
    i=str(i);len1=len(i)
    for j in range(0,len1):
        a1=int(i[j])**len1
        list1.append(a1)
    if int(i)==sum(list1):
        print(i,end=' ')
        print(list1)
'''
#判断一个数字是不是阿姆斯特朗数字
a=input('请输入一个数字')
len1=len(a)
sum=0
for i in range(0,len1):
    sum+=int(a[i])**len1
if sum==int(a):
    print('true')
else:
    print('false')











