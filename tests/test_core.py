
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

