from connection import get_serial_connection
import logging
import argparse


logging.basicConfig(format='%(message)s', level=logging.INFO)
log = logging.getLogger(__name__)


def get_info(serial):
    log.info('getting info')


def parse_arguments():
    parser = argparse.ArgumentParser(description="Utility for QS-S4")
    parser.add_argument(
        '--info', help='General information from controller', action='store_true')
    return vars(parser.parse_args())


serial = None
try:
    args = parse_arguments()
    serial = get_serial_connection()
    if args['info']:
        get_info(serial)
finally:
    if serial:
        log.info('closing serial connection')
        serial.close()
