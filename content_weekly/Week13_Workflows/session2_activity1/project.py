from darcy_functions import darcy_circular
import numpy as np
# Assign argument values
k_sat = 0.5    # saturated hydraulic conductivity (m/day)
r     = 0.1    # radius (m)
dh_dl = 0.02   # hydraulic gradient (m/m)

# Call the function
Q = darcy_circular(k_sat=k_sat, r=r, dh_dl=dh_dl)

# Print result
print(f"Hydraulic conductivity (k_sat): {k_sat} m/day")
print(f"Radius (r):                     {r} m")
print(f"Hydraulic gradient (dh/dl):     {dh_dl} m/m")
print(f"Cross-sectional area:           {np.pi * r**2:.4f} m²")
print(f"Volumetric flow rate (Q):       {Q:.6f} m³/day")