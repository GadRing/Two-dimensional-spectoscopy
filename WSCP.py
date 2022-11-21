import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
import sys 
np.set_printoptions(threshold=sys.maxsize)

Hamiltonian = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 14000, 70, 6, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 70, 14000, 13, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 6, 13, 14000, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 13, 6, 70, 14000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 28000, 13, 6, 13, 6, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 13, 28000, 70, 0, 70, 13, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 6, 70, 28000, 70, 0, 6, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 13, 0, 70, 28000, 70, 13, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 6, 70, 0, 70, 28000, 6, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0,  13, 6, 13, 6, 28000, 0, 0, 0, 0, 0],
                       [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42000, 13, 70, 6, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 42000, 6, 70, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 6, 42000, 13, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 70, 13, 42000, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56000]])

Dipolio_matrica = np.array([[0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                           [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                           [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                           [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                           [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                           [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                           [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                           [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
                           [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                           [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]])


w, v = LA.eigh(Hamiltonian)

eigv = np.zeros((16, 16))

for i in range(len(w)):
    eigv[i, i] = w[i]
    
Dipol_matrix_in_base_ham = Ham_Evec_tr@Dipolio_matrica@Ham_Evec
D_M_H = Dipol_matrix_in_base_ham


x = np.linspace(27800,28300, num=500)
y = np.linspace(13800,14300, num=500)
X, Y = np.meshgrid(x,y)
Z = np.zeros((500, 500))

for i in range(len(Z[0:])):
    for j in range(len(Z[0:])):
        for n in np.arange(1,5):
            for m in np.arange(5,12):
                for s in np.arange(1,5):
                    H_1 = eigv[m, m] - eigv[0,0]
                    H_2 = eigv[s, s] - eigv[0,0]
                    H_3 = eigv[m, m] - eigv[s,s]
                    
                    Z[i, j] = Z[i, j] + ((((D_M_H[0,s]*D_M_H[s, m]*D_M_H[m, n]*D_M_H[n,0])/
                                          (((1j*X[i,j] - 1j*H_1) - 20)*((1j*Y[i,j] - 1j*H_2)-20))) 
                                          -((D_M_H[0,s]*D_M_H[s,1]*D_M_H[m,n]*D_M_H[n,1])/
                                           (((1j*X[i,j] - 1j*H_1) - 20)*((1j*Y[i,j] - 1j*H_3)-20)))))
                    
maxG = np.max(np.max(np.abs(Z)))
plt.contourf(X, Y, np.arcsinh(Z/maxG)*100)
plt.show()
