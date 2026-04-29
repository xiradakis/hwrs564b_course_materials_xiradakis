import numpy as np

def darcy_circular(k_sat, r, dh_dl):
    """
    Compute Darcy flow through a circular cross-sectional area.

    Parameters
    ----------
    k_sat : float  Saturated hydraulic conductivity (m/day or cm/s)
    r     : float  Radius of the circular cross section (m)
    dh_dl : float  Hydraulic gradient (m/m)

    Returns
    -------
    Q : float  Volumetric flow rate
    """
    A = np.pi * r**2
    Q = k_sat * A * dh_dl
    return Q
