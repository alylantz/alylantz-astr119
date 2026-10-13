# What it does: Estimates how much mass and radius of a comet changes
#               on a path past the sun from solar energy
# How to run:   conda activate astr119
#               python3 cometlife.py
#               Then enter radius in meters whne prompted



import math 
from math import sqrt, pi
import numpy as np

# Constants
pi = 3.14
R = 2000 # Radius of the comet in meters 
AU = 1.49e11 # Astronomical unit in meters
a = 3.12*AU # Semi-major axis of the comet's orbit in meters
p = 500 # Perihelion distance of the comet in meters
A = 0 # Aphelion distance of the comet in meters
e = 0.5 # Eccentricity of the comet's orbit
L = 3.8e26 # Luminosity of the Sun in watts
GM = 1.3271e20 # Gravitational parameter of the Sun in m^3/s^2
h_ice = 2.5e6 # Energy sublimating ice

R_input = input("Enter comet radius in meters: ")
R = float(R_input) # Radius in meters

# Formula for total solar energy
H_sol = (pi/2)*(1-A)*R**2*(L/sqrt(GM))*(1/(sqrt(a*(1-e**2))))
print(H_sol)

# Mass
M = (4/3)*pi*(R**3)*p #Lifetime in orbits
dM = H_sol/h_ice #Mass lost per orbit
dr = (dM/p)/(4*pi*R**3) #Volume of ice lost in m^3

n_orbits = R/dr #Lifetime in orbits
y_orbits = sqrt((a/AU)**3) # Years per orbit
lifetime_years = n_orbits * y_orbits

print(f"A {R:.0f} = radius a comet loses about {dM:.2e} kg and{dr:.3f} a^3 of raduis per orbit, so it can survive about {n_orbits:.0f} orbits, which si about {lifetime_years:.0f} years")
