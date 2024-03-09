""" Simple Fixed Point Iteration """
import matplotlib.pyplot as plt
import math as m
def fx(x):
    return x + ((1.65*0.71*0.87*1.02*m.e**((-x)*0.03))/(1+0.0094009*x))-0.99 # Equation in the report --> f(Bg²)

G = [] # list to store value of fx(Bg²)
B = []
F = [] # list to store value of f(Bg²)
c = -10
Iter = []
for i in range(20001):
    B.append(c)
    c += 0.001 # Geometric Buckling B from -10 to 10 m⁻² with a step size of 0.001 m⁻² is created

for i in B:
    G.append(fx(i))
    F.append(fx(i)-i)

plt.figure(1)
plt.plot(B,F,'b-')
plt.plot(B,G,'r-')
plt.xlabel("Geometric Buckling Bg² (in m⁻²)")
plt.ylabel("f(Bg²)")
plt.title("f(Bg²) vs Geometric Buckling (Bg²) graph")
plt.legend(["g(Bg²)","x"],loc="best")
plt.grid()
plt.show()

# Applying Simple Fixed Point Iteration from graphical observation of xu
xu = 5
SCrit = 1
while round(SCrit,10) != 0.0:
    xr = fx(xu)
    SCrit = (xr - xu)/xr
    xu = xr
    Iter.append(xr)
print("\nSimple Fixed-Point Iteration Method: ")
print(f"\nThe Geometric Buckling (Bg²) is approximately {xr} m⁻²\n")
print(f"For verification we can see f(Bg²) is {SCrit}\n")

plt.figure(2)
plt.plot(list(range(len(Iter))),Iter,'r-')
plt.xlabel("No: of iterations")
plt.ylabel("(Bg²)")
plt.title("Value of Geometric Buckling (Bg²) vs Iterations")
plt.grid()
plt.show()