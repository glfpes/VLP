import pretty_logger
from aoa import aoa
Zf = 2271
logger = pretty_logger.get_logger()
w = 10
l = 10

print 'x'
positions_of_lights = [(-450,450),(-450,450),(-450,450)]
transmitters = [(-w/2,  l/2, 0),(w/2,  l/2, 0),(-w/2,  -l/2, 0)]
#positions_of_lights
lights = [
			(
				positions_of_lights[i],
				transmitters[i]
			) for i in xrange(3)]
logger.debug('Raw lights information: {}'.format(lights))

tries_method = ['static']
rx_location, rx_rotation, location_error = aoa(lights, Zf, k_init_method=tries_method)
logger.info('location estimate = {}'.format(rx_location))