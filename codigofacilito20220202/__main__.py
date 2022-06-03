import logging

from codigofacilito20220202 import unreleased

"""
INFO - 10
DEBUG - 20
WARNING - 30
ERROR - 40
CRITICAL - 50
"""

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    logging.debug('Estamos iniciando la ejecución del paquete')
    workshops = unreleased()
    logging.debug(workshops)
    logging.debug('Estamos finalizando la ejecución del paquete')
