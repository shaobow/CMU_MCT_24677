import numpy as np
import matplotlib.pyplot as plt

def sim2Mat(power0,gamma):
  ## constant
  gain=np.array([[1,.2,.1],[.1,2,.1],[.3,.1,3]])
  alpha=1.2
  sigma=0.1

  ## control rules
  A_mat=np.zeros([3,3])
  for i in range(3):
    for j in range(3):
        if i==j:
          A_mat[i,j]=0.
        else:
          A_mat[i,j]=alpha*gamma*gain[i,j]/gain[i,i]

  B_mat=np.zeros([3,1])
  for i in range(3):
    B_mat[i]=alpha*gamma/gain[i,i]
  
  ## simulate
  power=power0
  P_mat=np.empty([3,0]) # power through time
  S_mat=np.empty([3,0]) # sinr through time

  k=np.arange(0,20) # time steps
  for n in k:
    sinr=np.array([gain[0,0]*power[0]/(sigma**2+gain[0,1]*power[1]+gain[0,2]*power[2]),gain[1,1]*power[1]/(sigma**2+gain[1,0]*power[0]+gain[1,2]*power[2]),gain[2,2]*power[2]/(sigma**2+gain[2,0]*power[0]+gain[2,1]*power[1])])
    S_mat=np.append(S_mat,sinr,axis=1)
    P_mat=np.append(P_mat,power,axis=1)
    power=A_mat@power+B_mat*(sigma**2)

  return [S_mat,P_mat]

power0_1=np.array([[.1],[.1],[.1]]) # initial power
power0_2=np.array([[.1],[.01],[.02]])
gamma_1=3. # threshold
gamma_2=5.
alpha=1.2
index=1

k=np.arange(0,20) # time steps

for gamma in [gamma_1,gamma_2]: 
  for power in [power0_1,power0_2]:   
    [S_mat,P_mat]=sim2Mat(power,gamma)

    plt.figure(index,dpi=300)
    plt.plot(k,S_mat[0,:],label='S_1')
    plt.plot(k,S_mat[1,:],label='S_2')
    plt.plot(k,S_mat[2,:],label='S_3')
    plt.plot(k,[alpha*gamma for k in range(0,20)],linestyle='dashed',label='alpha*gamma')
    plt.legend()
    plt.xlabel("Time steps(k)")
    plt.ylabel("SINR")
    plt.title("Initial power="+str(power.T)+",Gamma="+str(gamma))

    plt.figure(index+1,dpi=300)
    plt.plot(k,P_mat[0,:],label='p_1')
    plt.plot(k,P_mat[1,:],label='p_2')
    plt.plot(k,P_mat[2,:],label='p_3')
    plt.legend()
    plt.xlabel("Time steps(k)")
    plt.ylabel("Power")
    plt.title("Initial power="+str(power.T)+",Gamma="+str(gamma))

    plt.show()
    index=index+2
