import numpy as np
from control import matlab
from matplotlib import pyplot as plt
from matplotlib import animation

m = 1000
c = 100
G = matlab.tf([1], [m, c])

t_delay = 0.5
n_pade = 10
(num_pade, den_pade) = matlab.pade(t_delay, n_pade)
G_delay = matlab.tf(num_pade, den_pade)

G = matlab.series(G_delay, G)

# Kp = 2000
# Ki = 0
# Kd = 0
# num = [Kd, Kp, Ki]
# den = [1, 0]
# K = matlab.tf(num, den)
# 
# sys = matlab.feedback(K*G, 1)

t = np.linspace(0, 20, 2000)
target = []
for i in t:
    if i < 2.0:
        target.append(0.0)
    else:
        target.append(10.0)

fig, ax = plt.subplots()

ims = []
kp = 500
ki = 0
kd = 0
for ki in np.arange(0, 500, 100):
    num = [kd, kp, ki]
    den = [1, 0]
    K = matlab.tf(num, den)

    sys = matlab.feedback(K*G, 1)

    (Y, t, X) = matlab.lsim(sys, target, t)
    ax.legend()
    ax.set_xlim(0, 20)
    ax.set_xlabel('time [sec]')
    ax.set_ylabel('velocity [m/s]')
    im = ax.plot(t, Y, label='Ki='+str(ki))
    im += ax.plot(t, target, color='r')
    ims.append(im)

# ani = animation.ArtistAnimation(fig, ims, interval=100)
# ani.save('kp.gif', writer='pillow')

    
# (Y, T) = matlab.step(sys, t)
# (Y, t, X) = matlab.lsim(sys, target, t)
# plt.plot(t, Y)
# plt.plot(t, target)
# plt.grid()
# plt.xlim(0, 20)
plt.title('Kp=500, Ki=??')
plt.legend()

fig.savefig('ki.png', dpi=300)
plt.show()
