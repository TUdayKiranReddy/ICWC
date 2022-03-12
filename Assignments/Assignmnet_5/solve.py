import numpy as np
import matplotlib.pyplot as plt

def q1(r):
	return np.sqrt(1000/r - 1)

def q2(r):
	return np.sqrt(r/50 - 1)
q = 20
def eta(r):
	return 1/(1 + (q1(r) + q2(r) + q1(r)*q2(r)/q)/q)

R = np.linspace(50, 1000, 1000)
e = eta(R)

r = np.array([223.6, 52.7, 947.213])

plt.figure()
plt.plot(R, e*100)
plt.plot(r, eta(r)*100, "*r")
plt.grid()
plt.ylabel(r'$\eta$ %')
plt.xlabel(r'$R_i$')
plt.title("Efficiency in two stage matching network")
plt.savefig('./figs/plot.jpg')
plt.show()
# r = 223.6
# q1=q1(r)
# q2=q2(r)
# print(1/(1 + 0.05*(q1+q2 + 0.05*q1*q2)))
# print("L1 = ", q1*r/(2 * np.pi * 1e9))
# print("L2 = ", q2*50/(2 * np.pi * 1e9))
# print("C1 = ", q1/(2 * np.pi * 1e9 * 1000))
# print("C2 = ", q2/(2 * np.pi * 1e9 * r))
