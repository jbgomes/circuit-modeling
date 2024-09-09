from laplace_inverse import i_laplace
from frequency_response import bode2

k = 10
R1 = 1e5
R2 = k*R1
Cl = 1e-12
Cg = 0.5e-12
gm = 100e-6
r0 = 1e7

num = [-R2*r0*(gm*R2 - 1)]
den = [(-r0*R1*Cg*Cl*R2**2), (r0*Cl*R2**2 + R1*Cg*R2**2 + r0*R1*R2*Cg + r0*R1*R2*Cl), (R2**2 + R1*R2 + r0*R2 + R1*r0*gm*R2)]

bode2(num, den, 1e5, 1e9, 1000)
#i_laplace(num, den)