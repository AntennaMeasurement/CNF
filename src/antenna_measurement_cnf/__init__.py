from importlib.metadata import version

from antenna_measurement_cnf.core import wavelength, measurementDistance, probeRadius

__version__ = version("antenna-measurement-cnf")

__all__ = ["wavelength", "measurementDistance", "probeRadius"]
