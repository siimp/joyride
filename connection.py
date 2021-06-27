from serial import Serial
from serial.tools import list_ports
import logging

BAUD_RATE = 1200
COM_PORT_INDEX = 0

logging.basicConfig(format='%(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


def get_serial_connection():
    comports = list_ports.comports()
    log.info(f'available comport devices: { list(map(lambda comport: comport.device, comports)) }')

    if len(comports) == 0:
        log.info('no comport device found')
        exit()

    device = comports[COM_PORT_INDEX].device
    log.info(f'using com port device {device}')

    log.info(f'connecting to serial device using baud rate {BAUD_RATE}')
    return Serial(device, BAUD_RATE, timeout = 1)