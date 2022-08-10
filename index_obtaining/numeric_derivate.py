import numpy as np
import matplotlib.pyplot as plt

def get_numerical_second_derivative(x, y):
    """Return the second derivative of y with respect to x at x_0"""
    dy=np.diff(y,1)
    dx=np.diff(x,1)
    yfirst=dy/dx
    xfirst=0.5*(x[:-1]+x[1:])
    dyfirst=np.diff(yfirst,1)
    dxfirst=np.diff(xfirst,1)
    ysecond=dyfirst/dxfirst

    xsecond=0.5*(xfirst[:-1]+xfirst[1:])
    # print("Second derivative x:", xsecond)
    print("Second derivative y:", ysecond)
    print("Second derivative sum y:", sum(ysecond))
    print("Second derivative mean y:", sum(ysecond)/len(ysecond))
    print("Second derivative max y:", max(ysecond))
    print("Second derivative min y:", min(ysecond))
    ysecond.sort()
    print("Second derivative median y:", ysecond[len(ysecond)//2])
    plt.hist(ysecond, bins=20)
    plt.show()


if __name__ == "__main__":
    x = np.array([x for x in range(200)])
    y = np.array([x*x for x in range(100)] + [-x*x for x in range(100)])
    y2 = np.array([3*x**2 for x in range(100)] + [-3*x**2 for x in range(100)])
    get_numerical_second_derivative(x, y)
    get_numerical_second_derivative(x, y2)

