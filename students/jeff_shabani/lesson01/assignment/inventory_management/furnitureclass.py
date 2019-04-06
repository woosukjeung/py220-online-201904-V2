"""
Furniture class module"""

from students.jeff_shabani.lesson01.assignment.inventory_management.inventoryclass import *


class Furniture(Inventory):
    """
    framework for furniture"""

    def __init__(self, productcode, description, marketprice, rentalprice
                 , material, size):
        super().__init__(productcode, description, marketprice,
                         rentalprice)

        self.material = material
        self.size = size

    def returnasdictionary(self):
        """
        returns dictionary of furniture items"""
        outputdict = super().returnasdictionary()
        outputdict['material'] = self.material
        outputdict['size'] = self.size

        return outputdict
