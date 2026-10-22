import sys
import math

# Named constants for unit conversions
L_SUN = 3.8e26
AU_METERS = 1.496e11

def t_eq(L, d):
    """Calculate equilibrium temperature given L in Watts and d in Meters."""
    sigma = 5.670374419e-8 
    return (L / (16.0 * math.pi * sigma * (d ** 2))) ** 0.25
planets = [   # name, luminosity (solar units), distance (AU)
    ["Earth",        1.0,     1.000],
    ["Mars",         1.0,     1.524],
    ["HD 209458 b",  1.6,     0.047],
    ["51 Peg b",     1.3,     0.052],
    ["TRAPPIST-1 e", 0.00055, 0.029],
    ["Kepler-22 b",  0.79,    0.85],
    ["55 Cnc e",     0.58,    0.0154],
    ["HD 189733 b",  0.34,    0.031],
    ["Kepler-452 b", 1.2,     1.046],
    ["Proxima b",    0.0016,  0.0485],
]
if __name__ == '__main__':
    if len(sys.argv) >= 3:
        print(f"{t_eq(float(sys.argv[1]), float(sys.argv[2])):.1f} K")
    else:
        for i in range(len(planets)):
            name = planets[i][0]
            lum = planets[i][1] * L_SUN
            dist = planets[i][2] * AU_METERS
            temp = t_eq(lum, dist)
            print(f"{name:<14} {temp:.0f} K")
