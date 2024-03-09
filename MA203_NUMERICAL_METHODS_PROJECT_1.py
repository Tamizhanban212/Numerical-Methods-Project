import matplotlib.pyplot as plt
from math import e
def func(d):
	return (0.99+(0.0094009)*(d)+((-1.0395891)*(e)**(-(d)*0.03)))
l=[]
k=[]
def binary_search(func,lis,l):
	if len(lis)>0:
		mid=(lis[0]+lis[1])/2
		#print(func(mid),mid)
		l.append(mid)
		if func(mid)>-(10**(-29)) and func(mid)<(10**(-29)):
			return mid,func(mid)
		elif func(mid)>0:
			lis=[lis[0],mid]
			return binary_search(func,lis,l)
		else:
			lis=[mid,lis[1]]
			return binary_search(func,lis,l)

lis=[-10,10]
print("Bisection Method:\n")
m=binary_search(func,lis,l)
print(f"The Geometric Buckling Value (Bg^2) is approximately {m[0]} m^-2 \n")
print(f"The corresponding f(Bg^2) Value is {m[1]}")
for h in range(len(l)):
	k.append(h)
plt.plot(k,l)
plt.title("The Value of of (Bg)^2 vs Iterations")
plt.ylabel("(Bg)^2")
plt.xlabel("No of Iterations")
plt.grid(True)
plt.show()
