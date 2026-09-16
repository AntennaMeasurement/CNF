
import math

from AntennaMeasurementCNF.core import wavelength, c, measurementDistance, probeRadius

def test_wavelength():
    frequency = 299792458  # ~300 MHz
    expected_wavelength = c / frequency
    assert wavelength(frequency) == expected_wavelength
    
def test_measurementDistance():
    frequency = 299792458  # ~300 MHz
    coefficient = 5
    expected_distance = coefficient * wavelength(frequency)
    assert measurementDistance(frequency, coefficient) == expected_distance
    
def test_probeRadius():
    ref_distance = 3
    lengths = [0.4, 0.6, 1.195, 0.2]
    expected_radius = ref_distance - sum(lengths)
    assert probeRadius(ref_distance, lengths) == expected_radius
    

def test_scanSizeY():
    from AntennaMeasurementCNF.core import scanSizeY
    D = 1.5
    P = 0.5
    Z = 2.0
    R = 1.0
    Az_max = 45
    El_max = 60
    expected_scan_size_y = D + P + 2*(Z-R*math.cos(math.radians(Az_max)))*math.tan(math.radians(El_max))
    assert scanSizeY(D, P, Z, R, Az_max, El_max) == expected_scan_size_y


