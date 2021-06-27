from connection import get_serial_connection
import logging


logging.basicConfig(format='%(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


def read_all(serial):
    response = []
    while serial.inWaiting() > 0:
        response.append(serial.read(1))
    log.info(f'read {len(response)} bytes from serial')
    log.info(f'{response}')


try:
    serial = get_serial_connection()
    read_all(serial)
finally:
    log.info('closing serial connection')
    serial.close()
