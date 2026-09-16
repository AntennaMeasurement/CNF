import math

################################################################################
# Physical constants 
################################################################################

# speed of light in vacuum (m/s)
c = 299792458

################################################################################
# Functions
################################################################################
def wavelength(frequency: float) -> float:
    r"""Calculate the wavelength for a given frequency.

    Parameters
    ----------
    frequency : float
        Frequency in hertz.

    Returns
    -------
    float
        Wavelength in meters.

    Notes
    -----
    The wavelength is calculated as:

    .. math::

        \lambda = \frac{c}{f}

    where :math:`c` is the speed of light in vacuum and :math:`f` is the
    frequency.
    """
    return c / frequency


def measurementDistance(frequency: float, coefficient: float = 5) -> float:
    r"""Calculate the required measurement distance for a given frequency in terms of the wavelength.

    Parameters
    ----------
    frequency : float
        Frequency in hertz.
    coefficient : float, optional
        Coefficient to multiply the wavelength by, default 5

    Returns
    -------
    float
        Measurement distance in meters.

    Notes
    -----
    The measurement distance is calculated as:

    .. math::

        d = \text{coefficient} \cdot \lambda

    where :math:`\lambda` is the wavelength corresponding to the frequency :math:`f`.
    """
    return coefficient * wavelength(frequency)
  
  
def probeRadius(ref_distance: float, lengths: list[float]) -> float:
  r"""Calculate the probe radius based on a reference distance and a list of lengths.

  Parameters
  ----------
  ref_distance : float
      Reference distance in meters.
  lengths : list[float]
      List of lengths in meters.

  Returns
  -------
  float
      Probe radius in meters.

  Notes
  -----
  The probe radius is calculated reference distance minus sum of the other lengths.
  
  .. math::

      r = R_ref - \sum_i \text{l}_i
      
  where :math:`R_ref` is the reference distance and :math:`l_i` are the individual lengths in the list.
  
  """
  return ref_distance - sum(lengths)


def scanSizeY(D: float, P: float, Z: float, R: float, Az_max: float, El_max: float ) -> float:
    r"""Calculate the scan size in the Y direction based distances and desired far-field angle spans.

    Parameters
    ----------
    D : float
        Antenna height in meters.
    P : float
        Probe longest edge length in meters.
    Z : float
        Probe radius in meters.
    R : float
        Maximum radial extent in meters.
    Az_max : float
        Desired maximum azimuth angle in degrees.
    El_max : float
        Desired maximum elevation angle in degrees. Should be equal or less than 60

    Returns
    -------
    float
        Scan size in the Y direction in meters.

    Notes
    -----
    The scan size in the Y direction is calculated based on the given parameters.
    
    .. math::

        L_Y = D + P + 2 \cdot (Z - R \cdot \cos(\text{Az_max})) \cdot \tan(\text{El_max})

    References
    ----------
    .. [1] *NSI 2000 (Near-field Edition), Version 4, Software Operating Manual*
     
    """
    
    # First validate the input parameters
    if El_max > 60:
      raise ValueError("El_max should be equal or less than 60 degrees.")
    
    # Z distance must greater than R (MRE)
    if Z <= R:
      raise ValueError("Z distance must be greater than R (MRE).")
    
    return D + P + 2*(Z-R*math.cos(math.radians(Az_max)))*math.tan(math.radians(El_max))

