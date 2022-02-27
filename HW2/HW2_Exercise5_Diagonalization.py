''' HW2_Exercise5_Diagonalization '''
import numpy as np
from scipy.signal import dlti

''' Using python programming to solve Exercise 5. Diagonalization '''
# define control parameters
Ad = np.asarray([[0., 1.], 
                [1., 1.]])
Bd = np.asarray([[0.],
                [0.]])
Cd = np.asarray([[1., 0.]])
Dd = np.asarray([[0.]])
T = 1 
x0 = np.asarray([[0.],
                 [1.]])

# define control system
dtSystem = dlti(Ad,Bd,Cd,Dd)

# simulate
t_max=20.
t_dt = np.arange(0, t_max+T, T)
u_dt = np.zeros(t_dt.size)

# by simulation
t_dt, y_dt, x_dt = dlsim(dtSystem, u_dt, t_dt,  x0.T)
print("F(20) = \n{}".format(y_dt[t_dt==20]))

# by calculation
M = np.asmatrix([[1,1],[(1-np.sqrt(5))/2,(1+np.sqrt(5))/2]])
MI = M.I
A_hat = np.asmatrix([[((1-np.sqrt(5))/2)**20,0],[0,((1+np.sqrt(5))/2)**20]])
F_20 = Cd@M@A_hat@MI@x0
print("F(20) = \n{}\n".format(F_20))