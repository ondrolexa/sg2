import numpy as np
import matplotlib.pyplot as plt

def def_ellipse(F):
    # Draw unit circle transformed to strain ellipse
    theta = np.linspace(0, 2*np.pi, 180)
    xc, yc = np.cos(theta), np.sin(theta)
    x,y = np.dot(F, [xc,yc])
    plt.plot(xc, yc, 'r', x, y, 'g')
    plt.axis('equal')

def dis_field(J):
    # Visualize displacement gradient field
    Xg, Yg = np.meshgrid(np.linspace(-3, 3, 21),
                         np.linspace(-2, 2, 17))
    X, Y = Xg.flatten(), Yg.flatten()
    u, v = np.dot(J, [X, Y])
    plt.quiver(X, Y, u, v, angles='xy')
    plt.axis('equal')

def dis_ellipse(J):
    # Draw ellipse from displacement gradient
    J = np.asarray(J)
    F = J + np.eye(J.ndim)
    def_ellipse(F)

def def_field(F):
    # Visualize deformation gradient
    F = np.asarray(F)
    J = F - np.eye(F.ndim)
    dis_field(J)

class Tensor(np.ndarray):

    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    @property
    def I(self):
        return np.linalg.inv(self)

    @property
    def evals(self):
        evals, evecs = np.linalg.eig(self)
        six = np.argsort(evals)[::-1]
        return evals[six]

    @property
    def evecs(self):
        evals, evecs = np.linalg.eig(self)
        six = np.argsort(evals)[::-1]
        return np.asarray(evecs[:,six].T)

    def powm(self, n):
        return np.linalg.matrix_power(self, n)

    def sqrtm(self):
        from scipy.linalg import sqrtm
        return sqrtm(self).view(Tensor)

    def plot(self):
        theta = np.linspace(0, 2*np.pi, 180)
        xc, yc = np.cos(theta), np.sin(theta)
        x, y = self.dot([xc, yc])
        u, s, v = np.linalg.svd(self)
        plt.plot(x, y, 'k', lw=2)
        plt.quiver(np.zeros(2*self.ndim),
                   np.zeros(2*self.ndim),
                   np.hstack((s*u[0],-s*u[0])),
                   np.hstack((s*u[1],-s*u[1])),
                   scale=1, units='xy')
        plt.axis('equal')

    def show(self):
        self.plot()
        plt.show()

