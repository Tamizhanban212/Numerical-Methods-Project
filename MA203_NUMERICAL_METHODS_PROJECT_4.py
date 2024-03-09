import matplotlib.pyplot as plt
from math import e
def func(w):
	a=(0.99+(0.0094009)*(w)+((-1.0395891)*(e)**(-(w)*0.03)))
	b=(0.0094009+(1.0395891*0.03*(e**(-0.03*w))))
	return (a,b)
	
def rec(w,l):
	t=func(w)
	l.append(w)
	if t[0]<10**(-27) and t[0]>-(10)**(-27):
		return w,func(w)[0]
	w=w-(t[0]/t[1])
	return rec(w,l)
l=[]
k=[]
print("Newton-Raphson Method:\n")
m=rec(-100,l)
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
