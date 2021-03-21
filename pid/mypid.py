import numpy as np
from matplotlib import pyplot as plt

class Vehicle():
    def __init__(self):
        self.x = 0
        self.v = 0
        self.a = 0
        self.m = 1000
        self.c = 100
        self.k = 0

    def run(self, f, dt):
        self.a = (f - self.c * self.v) / self.m
        self.v = self.v + self.a * dt

    def get_v(self):
        return self.v

class PID():
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.i = 0
        self.prev = None

    def control(self, target, current, dt):
        error = target - current
        self.i = self.i + error * dt
        if self.prev == None:
            d = 0
            self.prev = error
        else:
            d = (error - self.prev) / dt
            self.prev = error

        return self.kp * error + self.ki * self.i + self.kd * d

        
dt = 0.01
t_max = 10
t = []
for i in np.arange(0, t_max, dt):
    t.append(i)

kp = 10000
ki = 0
kd = 0
pid = PID(kp, ki, kd)

vehicle = Vehicle()

target = []
for i in t:
    if i < 2.0:
        target.append(0.0)
    else:
        target.append(10.0)

u = []
y = []
for i in range(len(t)):
    current_v = vehicle.get_v()
    target_v = target[i]
    current_u = pid.control(target_v, current_v, dt)
    vehicle.run(current_u, dt)
    u.append(current_u)
    y.append(vehicle.get_v())

print(t)
print(y)
print(u)

plt.plot(t, y)
plt.plot(t, target)
plt.grid()
plt.xlim(0, t_max)
plt.show()

