''' HW2_Exercise4_CT_and_DT_Dynamics.py '''
import numpy as np
from scipy.signal import StateSpace, lsim, dlsim
import matplotlib.pyplot as plt

''' Using python programming to solve Exercise 4. CT and DT dynamics '''
# define control parameters
A = np.asarray([[0., 1.], 
                [-2., -2.]])
B = np.asarray([[1.],
                [1.]])
C = np.asarray([[2., 3.]])
D = np.asarray([[0.]])
T = 1 

# define control system
ctSystem = StateSpace(A, B, C, D)
dtSystem = ctSystem.to_discrete(T)

# simulate
t_max=6.
t_ct = np.arange(0, t_max, 1e-3)
t_dt = np.arange(0, t_max+T, T)

u_ct = np.ones(t_ct.size)
u_dt = np.ones(t_dt.size)

_, y_ct, x_ct = lsim(ctSystem, u_ct, t_ct, [0.,0.])
t_dt, y_dt, x_dt = dlsim(dtSystem, u_dt, t_dt,  [0.,0.])

''' i) Find y(5) for CT system '''
print("y(5) = \n{}\n".format(y_ct[t_ct==5]))

''' ii) discretized state space representation '''
print("Ad = \n{}".format(dtSystem.A))
print("Bd = \n{}".format(dtSystem.B))
print("Cd = \n{}".format(dtSystem.C))
print("Dd = \n{}\n".format(dtSystem.D))

''' iii) Find y(5) for DT system '''
# by simulation
print("By simulation, y(5) = \n{}".format(y_dt[t_dt==5]))

# by calculation
Ad = np.asmatrix([[np.exp(-T)*(np.sin(T)+np.cos(T)),np.exp(-T)*np.sin(T)],
                  [-2*np.exp(-T)*np.sin(T),np.exp(-T)*(np.cos(T)-np.sin(T))]])
Bd = np.asmatrix([[-np.exp(-T)*(.5*np.sin(T)+1.5*np.cos(T))+1.5],
                  [np.exp(-T)*(2*np.sin(T)+np.cos(T))-1]])
Cd = np.asmatrix([[2.,3.]])
y_cal=0.
for m in range(0,5):
  M = Cd @ (Ad**(4-m)) @ Bd
  y_cal = y_cal + M
print("By calculation, y(5) = \n{}\n".format(y_cal))

# plot y(t) for both CT and DT
plt.figure(dpi=300)
plt.plot(t_ct, y_ct,label='CT')
plt.plot(t_dt, y_dt,label='DT')
plt.legend()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.show()