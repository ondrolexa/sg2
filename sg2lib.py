# Library of routines for 2D deformation visualization
#
# Ondrej Lexa 2017

from pylab import *
from scipy import linalg as la

def def_ellipse(F):
    # Draw strain ellipse from deformation gradient
    theta = linspace(0, 2*pi, 180)
    xc, yc = cos(theta), sin(theta)
    x,y = dot(F, [xc,yc])
    plot(xc, yc, 'r', x, y, 'g')
    u, s, v = svd(F)
    quiver(zeros(2), zeros(2),
               hstack((s*u[0],-s*u[0])), hstack((s*u[1],-s*u[1])),
               scale=1, units='xy')

def def_square(F):
    # Draw square
    xc, yc = [-1, -1, 1, 1, -1], [-1, 1, 1, -1, -1]
    x,y = dot(F, [xc,yc])
    plot(xc, yc, 'r', x, y, 'g')

def dis_ellipse(J):
    # Draw strain ellipse from displacement gradient
    J = asarray(J)
    F = J + eye(2)
    def_ellipse(F)

def dis_square(J):
    # Draw square
    J = asarray(J)
    F = J + eye(2)
    def_square(F)

def dis_field(J):
    # Visualize displacement field from
    # displacement gradient
    X, Y = meshgrid(linspace(-3, 3, 21),
                    linspace(-2, 2, 17))
    u, v = tensordot(J, [X, Y], axes=1)
    quiver(X, Y, u, v, angles='xy')

def def_field(F):
    # Visualize displacement field from
    # deformation gradient
    F = asarray(F)
    J = F - eye(2)
    dis_field(J)

def dis_show(J):
    # Draw displacement field and deformation ellipse
    # from displacement gradient
    dis_field(J)
    dis_square(J)
    dis_ellipse(J)
    title(f"J = [[{J[0,0]:g}, {J[0,1]:g}], [{J[1,0]:g}, {J[1,1]:g}]]")
    axis('equal')
    show()

def def_show(F):
    # Draw displacement field and deformation ellipse
    # from deformation gradient
    def_field(F)
    def_square(F)
    def_ellipse(F)
    axis('equal')
    title(f"F = [[{F[0,0]:g}, {F[0,1]:g}], [{F[1,0]:g}, {F[1,1]:g}]]")
    show()

def vel_field(L, t=None):
    # Visualize velocity field from
    # spatial velocity gradient
    X, Y = meshgrid(linspace(-2, 2, 17),
                    linspace(-2, 2, 17))
    u, v = tensordot(L, [X, Y], axes=1)
    quiver(X, Y, u, v, angles='xy')
    if t is not None:
        F = la.expm(L*t)
        def_square(F)
        def_ellipse(F)
    axis('equal', adjustable='box')
    title('Spatial velocity gradient')
    show()

def densify_list_xy(x, y, n=500, per=True):
    from scipy import interpolate
    if per and (x[0] != x[-1]) and (x[0] != x[-1]):
        x.append(x[0])
        y.append(y[0])
    tck, u = interpolate.splprep([x, y], s=0, k=1, per=per)
    return interpolate.splev(np.linspace(0, 1, n), tck)
    
