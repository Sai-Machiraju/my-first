N,M=map(int,input().split())
n=(N//2)
p=(M//2)-1
k=1
a=3
b=(M-6)//3
for i in range(n):
  print("-"*(p)+".|."*(k)+"-"*(p))
  k=k+2
  p=p-3
j=(M-7)//2
print("-"*(j)+"WELCOME"+"-"*(j))
for i in range(n):
    print("-"*(a)+".|."*(b)+"-"*(a))
    a=a+3
    b=b-2  
