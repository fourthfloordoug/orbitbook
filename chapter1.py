import numpy as np

xs = np.ones((5,1)) * 1.0
ys = np.ones((5,1)) * 1.0

def getXTerm(x0,vx,t):
    return np.square(x0 - xs + vx * t)

def getYTerm(y0,vy,g,t):
    return np.square(y0 - ys + vy * t + 0.5*g*t*t)

def getRho(xterm,yterm):
    return np.sqrt(xterm + yterm)

def getDX0(rho,xterm):
    return xterm/rho

def getDVx(rho,xterm,t):
    num = xterm * t
    return num/rho

def getDY0(rho,yterm):
    return yterm/rho

def getDVy(rho,yterm,t):
    num = yterm * t
    return num/rho

def getDG(rhow,yterm,g,t):
    num = yterm * (-1*g*t)
    return num/rho

def getJMatrix(xterm,yterm,t):

    dx0 = getDX0(xterm,yterm)
    dvx = getDVx(xterm,yterm)
    dy0 = getDVy()



x0 = np.ones((5,1)) * 1.5
vx = np.ones((5,1)) * 2.2
y0 = np.ones((5,1)) * 10.0
vy = np.ones((5,1)) * 0.5
g = np.ones((5,1)) * 0.3
t = np.array([[0,1,2,3,4]]).T

rhos = rhoEquation(x0,vx,y0,vy,g,t)

print(rhos.shape)
print(rhos)
print()

drhodx = dRhodX0(x0,vx,y0,vy,g,t)
print(drhodx.shape)
print(drhodx)
