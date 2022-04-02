import numpy as np
import matplotlib.pyplot as plt



f = 1e9
w = 2*np.pi*f

R_h = 250
R_l = 50

n = np.arange(3) + 1
n = n.astype(int)


def Q(n):
	return np.sqrt(np.power(R_h/R_l, 1/n) - 1)

def R(n, i):
	x = np.power(R_h/R_l, 1/n)
	return R_h/(np.power(x, i))

def L(n, i):
	return Q(n)*R(n, i)/w


for i in n:
	plt.figure()
	plt.title("L{}".format(i))
	plt.plot(n, L(n, i)*1e9)
	plt.grid()

	print("L{}:- {}nH".format(i, L(n[-1], i)*1e9))
	# plt.figure()
	# plt.title("R{}".format(i))
	# plt.plot(n, R(n, i))
	# plt.grid()
print("Q:- {}".format(Q(n[-1])))
plt.figure()
plt.title("Q")
plt.plot(n, Q(n))
plt.grid()
plt.show()

