from pylab import *

def defgrad(F):
    X,Y = meshgrid(linspace(-5,5,16), linspace(-5,5,12))
    x = F[0,0]*X + F[0,1]*Y
    y = F[1,0]*X + F[1,1]*Y
    quiver(X, Y, x-X, y-Y)
    axis('equal')
    show()

def disgrad(J):
    X,Y = meshgrid(linspace(-5,5,16), linspace(-5,5,12))
    u = J[0,0]*X + J[0,1]*Y
    v = J[1,0]*X + J[1,1]*Y
    quiver(X, Y, u, v)
    axis('equal')
    show()

def steps(D,n):
    R = eye(2)
    for i in range(n):
        R = dot(D, R)
    return R

def strain(D):
    u,s,v = svd(D)
    ar = s[0]/s[1]
    theta = rad2deg(arccos(u[0,0]))
    return ar, theta

