from abc import ABC, abstractmethod


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def __str__(self):
        return format(str(self._address), str(self._name))
w