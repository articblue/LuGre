#!/usr/bin/env python
import math

def lugref(z, v, Fc, Fs, vs, sigma_0, sigma_1, sigma_2, ts):
    r = -1.0*math.pow(v/vs,2)
    g = (Fc + (Fs - Fc) * math.exp(r)) / sigma_0;
    z_dot = v - abs(v) * z / g;
    z = z + z_dot * ts;

    F = sigma_0 * z + sigma_1 * z_dot + sigma_2 * v;
    return F,z

