""" False Position Method """
import matplotlib.pyplot as plt
import math as m
def fx(x):
    return ((1.65*0.71*0.87*1.02*m.e**((-x)*0.03))/(1+0.0094009*x))-0.99 # Equation in the report --> f(Bg²)

F = [] # list to store value of f(Bg²)
B = []
c = -10
Iter = []
for i in range(100001):
    B.append(c)
    c += 0.001 # Geometric Buckling B from -10 to 90 m⁻² with a step size of 0.001 m⁻² is created

for i in B:
    F.append(fx(i))

plt.figure(1)
plt.plot(B,F,'r-')
plt.xlabel("Geometric Buckling Bg² (in m⁻²)")
plt.ylabel("f(Bg²)")
plt.legend(["f(Bg²)"],loc="best")
plt.title("f(Bg²) vs Geometric Buckling (Bg²) graph")
plt.grid()
plt.show()

# Applying False-Position Method from graphical observation of xl and xu
xl = -5
xu = 5
while round(fx(xl)*fx(xu),10) != 0.0:
    xr = xu - ((fx(xu)*(xl-xu))/(fx(xl)-fx(xu)))
    Iter.append(xr)
    if fx(xl)*fx(xr) < 0:
        xu = xr
    elif fx(xl)*fx(xr) > 0:
        xl = xr
    else:
        print(f"The root is approximately {xr} m⁻²")
        break
print("\nFalse-Position Method: ")
print(f"\nThe Geometric Buckling (Bg²) is approximately {xr} m⁻²\n")
print(f"For verification we can see f(Bg²) is {fx(xr)}\n")

plt.figure(2)
plt.plot(list(range(len(Iter))),Iter,'r-')
plt.xlabel("No: of iterations")
plt.ylabel("(Bg²)")
plt.title("Value of Geometric Buckling (Bg²) vs Iterations")
plt.grid()
plt.show()