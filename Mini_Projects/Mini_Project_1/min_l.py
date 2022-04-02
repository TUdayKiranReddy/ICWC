import numpy as np
import matplotlib.pyplot as plt


R = np.linspace(50, 250, 1000)
R_h = 250
R_l = 50
f = 1e9

w = 2*np.pi*f

def Q1(R):
	return np.sqrt(R_h/R - 1)

def Q2(R):
	return np.sqrt(R/R_l - 1)

def Q(R):
	return Q1(R) + Q2(R)

def Q1_bar(R):
	return -1*R_h/(2 * np.power(R, 2) * np.sqrt(R_h/R - 1))

def Q2_bar(R):
	return 1/(2*R_l*np.sqrt(R/R_l - 1))

def Q_bar(R):
	return Q1_bar(R) + Q2_bar(R)

def L1(R):
	return Q1(R)*R/w

def L2(R):
	return Q2(R)*R_l/w

def L1_bar(R):
	return (R*Q1_bar(R) + Q1(R))/w

def L2_bar(R):
	return Q2(R)*R_l/w

def cost(R):
	return L1(R) + L2(R)

def cost_bar(R):
	return L1_bar(R) + L2_bar(R)

def C1(R):
	return Q1(R)/(R_h * w)

def C2(R):
	return Q2(R)/(R * w)

def get_params(r):
	print("R:- {} ohm".format(r))
	print("L1:- {}H".format(L1(r)))
	print("C1:- {}F".format(C1(r)))
	print("L2:- {}H".format(L2(r)))
	print("C2:- {}F".format(C2(r)))
	print("Q1:- {}".format(Q1(r)))
	print("Q2:- {}".format(Q2(r)))
	print("Q :- {}".format(Q1(r) + Q2(r)))
r = 195

max_itr = 800
eta = w*1e-3

rs = [r]

for i in range(max_itr):
	# print(r)
	r -= eta*cost_bar(r)
	rs.append(r)

rs = np.array(rs)

get_params(rs[0])
# print("Optimal values")


plt.figure()
plt.title("Q")
plt.plot(R, Q1(R), label="Q1")
plt.plot(rs, Q1(rs), ".")
plt.plot(R, Q2(R), label="Q2")
plt.plot(rs, Q2(rs), ".")
plt.grid()
plt.legend()

plt.figure()
plt.title("L1")
plt.plot(R, L1(R), label="L1")
plt.plot(rs, L1(rs), ".")
plt.plot(R, L2(R), label="L2")
plt.plot(rs, L2(rs), ".")
plt.grid()
plt.legend()

plt.figure()
plt.title("L1 + L2")
plt.plot(R, cost(R))
plt.plot(rs, cost(rs), "r*")
plt.grid()

plt.show()