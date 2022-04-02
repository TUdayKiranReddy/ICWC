import numpy as np
import matplotlib.pyplot as plt


R = np.linspace(50, 250, 1000)
R_h = 250
R_l = 50


def Q(R):
	return np.sqrt(R_h/R - 1) + np.sqrt(R/R_l - 1)

def Q_bar(R):
	return -1*R_h/(2 * np.power(R, 2) * np.sqrt(R_h/R - 1)) + 1/(2*R_l*np.sqrt(R/R_l - 1))

r = 120

max_itr = 500
eta = 1000

rs = [r]

for i in range(max_itr):
	print(r)
	r -= eta*Q_bar(r)
	rs.append(r)

rs = np.array(rs)


plt.figure()
plt.plot(R, Q(R))
plt.plot(rs, Q(rs), "r*")
plt.grid()
plt.show()