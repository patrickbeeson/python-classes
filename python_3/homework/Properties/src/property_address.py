"""
property_address.py
"""
import re


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
        self._state = state
        self._zip_code = zip_code

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
        "Validate that states are abbreviated as US Postal style."
        state_valid = re.compile(r'[A-Z]{2}$')
        if re.match(state_valid, value):
            self._state = value
        else:
            raise StateError()

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        "Validate zip codes are five digits."
        zip_valid = re.compile(r'\d{5}$')
        if re.match(zip_valid, value):
            self._zip_code = value
        else:
            raise ZipCodeError()

    def __str__(self):
        return self._name
