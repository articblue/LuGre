#!/usr/bin/env python
from lugref import *
import numpy as np
import matplotlib.pyplot as plt

# See Table I from the paper
sigma_0 = 1e5
sigma_1  = math.sqrt(1e5)
sigma_2  = 0.4
Fc = 1
Fs = 1.5
vs = 0.001
ts = 1e-6

"""
Plot 1
"""
time_span = 0.1
t = np.linspace(0,time_span,time_span/ts)

# Velocity range
v = np.linspace(-0.005,0.005,100)

F = [] 
Fss = []

for i in range(0,len(v)):
    z = 0.0
    for j in range(0,len(t)):
        fj, z = lugref(z, v[i], Fc, Fs, vs, sigma_0, sigma_1, sigma_2, ts)
        F.append(fj)
    Fss.append(F[-1])

plt.plot(v, Fss)
plt.grid()
plt.xlabel('Velocity (m/s)')
plt.ylabel('Friction force (N)')
plt.title('Friction force at steady state condition')
plt.show()

"""
Plot 2
"""

# Zoom into certain velocity to see its transient behaviour
F = []
v = 0.002
z = 0
for j in range(0,len(t)):
    fj, z = lugref(z, v, Fc, Fs, vs, sigma_0, sigma_1, sigma_2, ts)
    F.append(fj)

plt.figure()
plt.plot(t, F)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Friction force (N)')
plt.title('Friction force for v = 0.002')
plt.show()

"""
Plot 3
"""

# Apply sinusoidal velocity and measure the friction force (Fig. 3 of the paper)
plt.figure()
plt.hold(True)
color = ['r','g','b']

F_omega = []
v = []
t = np.linspace(0,10.0,10.0/ts)
omega = [1,10,25]
legend = ['1 rad/s', '10 rad/s', '25 rad/s']

for i in range(0,len(omega)):
    F_omega.append([])
    z = 0
    v = [0.001 * (math.sin(omega[i]*x)+1.5) for x in t]
    for j in range(0,len(t)):
        fj, z = lugref(z, v[j], Fc, Fs, vs, sigma_0, sigma_1, sigma_2, ts)
        F_omega[i].append(fj)

    # Start from t = 3 up to the end
    plt.plot(v[int(3.0/ts):],F_omega[i][int(3.0/ts):], color[i],label=legend[i])

plt.grid()
plt.xlabel('Velocity (m/s)')
plt.ylabel('Friction force (N)')
plt.title('Hysteresis in friction with varying velocity')
plt.show()
