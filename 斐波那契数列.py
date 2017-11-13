#比较简单的一个方法
a=1
b=1
for i in range(1,1000):
    a,b=b,a+b
print(a)

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(30))