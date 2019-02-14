import numpy as np
import matplotlib.pyplot as plt

#equation of one side
n1=np.array([1,-1])
p1=-1

#equation of side 2
n2=np.array([7,-1])
p2=5

#intersection of 2 sides-A
N=np.vstack((n1,n2))
P=np.vstack((p1,p2))
A1=np.matmul(np.linalg.inv(N),P)
print("P=",P)
print("NT=",N)
print('NT^-1',np.linalg.inv(N))


def array(A):
    a=np.zeros(2)
    a[0]=A[0,:]
    a[1]=A[1,:]
    return a

A=array(A1)

def dvec(A,B):
    t=(B-A)
    return t

#omat=np.array([[0,1],[-1,0]])
#def normvec(A,B):
#    t=np.matmul(omat,dvec(A,B))
#    return t

#diagonal intersect at
O1=np.vstack([-1,-2])
O=array(O1)

#distance between A,O
#D=np.linalg.norm(A-O)

#pt B opp to A
B = A + 2*(O-A)

print("A=",A)


print("B=",B)


#equation of diagonal perp to AB
#nd=normvec(A,O)
#o=np.zeros(2)
#o[0]=O1[0,:]
#o[1]=O1[1,:]

nd=dvec(A,O)
print("ndT=",nd)

#for BC
#nbc=n2
pd=np.matmul(nd,O)
print("pd=",pd)
#for BD
#nbd=n1
#pbd=np.matmul(nd,O)

#Pd=np.matmul(nd,O)

#for C take intersention with either side
N1=np.vstack((n1,nd))
P1=np.vstack((p1,pd))
C1=np.matmul(np.linalg.inv(N1),P1)
C=array(C1)

print("P1=",P1)
print("N1T=",N1)
print('N1T^-1',np.linalg.inv(N1))
print("C=",C)

#N2=np.vstack((nd,n2))
#P2=np.vstack((pbc,p2))
#D1=np.matmul(np.linalg.inv(N2),P2)
#D=array(D1)


#alternate method
D= C + 2*(O-C)
print("D=",D)


#d1=A-B
#d2=C-O
#dp=np.matmul(d1,d2)
#print(d1)
#print(d2)
#print("dot product",dp)

normac=np.linalg.norm(C-A)
normcb=np.linalg.norm(B-C)
normbd=np.linalg.norm(D-B)
normda=np.linalg.norm(D-A)

print("Lengths of sides are:\nAC=",normac,"\nCB=",normcb,'\nBD=',normbd,'\nDA=',normda)


len=20
l=np.linspace(0,1,len)

ab=np.zeros((2,len))
bc=np.zeros((2,len))
cd=np.zeros((2,len))
da=np.zeros((2,len))
ac=np.zeros((2,len))
bd=np.zeros((2,len))

for i in range(len):
    t1=A+l[i]*(B-A)
    ab[:,i]=t1.T
    t2=B+l[i]*(C-B)
    bc[:,i]=t2.T
    t3=C+l[i]*(D-C)
    cd[:,i]=t3.T
    t4=D+l[i]*(A-D)
    da[:,i]=t4.T
    t5=A+l[i]*(C-A)
    ac[:,i]=t5.T
    t6=B+l[i]*(D-B)
    bd[:,i]=t6.T


plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'o')
plt.text(B[0]*(1-0.03),B[1]*(1+0.05),'B')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1+0.03),C[1]*(1-0.1),'C')
plt.plot(D[0],D[1],'o')
plt.text(D[0]*(1+0.2),D[1],'D')
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1+0.05),O[1]*(1-0.1),'O')
plt.xlabel('$x$')
plt.ylabel('$y$')



plt.plot(ab[0,:],ab[1,:],label='$AB$')
plt.plot(bc[0,:],bc[1,:],label='$BC$')
plt.plot(cd[0,:],cd[1,:],label='$CD$')
plt.plot(da[0,:],da[1,:],label='$DA$')
plt.plot(ac[0,:],ac[1,:],label='$AC$')
plt.plot(bd[0,:],bd[1,:],label='$BD$')
plt.legend(loc='best')
plt.grid()
plt.plot()
plt.show()
