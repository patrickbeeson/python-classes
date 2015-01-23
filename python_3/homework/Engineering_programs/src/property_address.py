"""
property_address.py
"""
import re
import logging
import argparse
import configparser

config = configparser.RawConfigParser()
config.read('V:/workspace/Python3_Homework12/src/property_address.cfg')

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
DEFAULT_LOG_LEVEL = "debug"
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
         }

def start_logging(filename=LOG_FILENAME, level=None):
    logging.basicConfig(filename=filename, level=level, format=LOG_FORMAT)
    logging.info('Starting up the property address program')

class ZipCodeError(Exception):
    "Custom exception for invalid zip codes."
    pass


class StateError(Exception):
    "Custom exception for invalid state abbreviation."
    pass


class Address(object):
    """
    An address object.
    """

    def __init__(self, name, street_address, city, state, zip_code):
        self._name = name
        self._street_address = street_address
        self._city = city
        self.state = state
        self.zip_code = zip_code
        logging.info('Instantiated an address')

    @property
    def name(self):
        return self._name

    @property
    def street_address(self):
        return self._street_address

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        "Validate that states are abbreviated correctly."
        state_valid = re.compile(config.get('validators', 'state'))
        if re.match(state_valid, value):
            self._state = value
        else:
            message = 'STATE Exception: State not in correct format'
            logging.error(message)
            raise StateError(message)

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        "Validate zip codes are nine digits." 
        zip_valid = re.compile(config.get('validators', 'zip_code'))
        if re.match(zip_valid, value):
            self._zip_code = value
        else:
            message = 'ZIP CODE Exception: Zip code not in correct format'
            logging.error(message)
            raise ZipCodeError(message)

    def __str__(self):
        return self._name

def main(args):
    # Start the logger with the default level
    start_logging(level=args.level)

    # Try to create our address object, with validation on state and zip fields
    try:
        address = Address(args.name, args.address, args.city, args.state, args.zip_code)
    except ZipCodeError:
        parser.error('option -z requires a valid 9-digit US zip code')
    except StateError:
        parser.error('option -s requires a valid US state abbreviation')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Set attributes for property address.')
    parser.add_argument(
                        '-l',
                        '--level',
                        dest='level',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='INFO',
                        help='Sets the log level to DEBUG, INFO, WARNING, ERROR, and CRITICAL')
    parser.add_argument(
                        '-n',
                        '--name',
                        dest='name',
                        action='store',
                        required=True,
                        help='Sets the name value of the Address object')
    parser.add_argument(
                        '-a',
                        '--address',
                        dest='address',
                        action='store',
                        required=True,
                        help='Sets the street_address value of the Address object')
    parser.add_argument(
                        '-c',
                        '--city',
                        dest='city',
                        action='store',
                        required=True,
                        help='Sets the city value of the Address object')
    parser.add_argument(
                        '-s',
                        '--state',
                        dest='state',
                        action='store',
                        required=True,
                        help='Sets the state value of the Address object')
    parser.add_argument(
                        '-z',
                        '--zip_code',
                        dest='zip_code',
                        action='store',
                        required=True,
                        help='Sets the zip_code value of the Address object')
    args = parser.parse_args()
    main(args)