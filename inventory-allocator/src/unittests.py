import unittest
from InventoryAllocator import inventory_allocator


class TestInventoryAllocator(unittest.TestCase):
    """
    A class to test inventory_allocator.py module
    """

    def test_simple_case(self):
        """
        A simple test case
        """

        order = {"apple": 10}
        warehouses = [{"name": "owd", "inventory": {"apple": 10}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [{"owd": {"apple": 10}}])
        self.assertEqual(pending_order, {})

    def test_multiple_warehouse(self):
        """
        A test case with multiple order items being in multiple warehouses
        """

        order = {"apple": 5, "banana": 5, "orange": 5}
        warehouses = [{"name": "owd", "inventory": {"apple": 5, "orange": 10}}, {
            "name": "dm", "inventory": {"banana": 5, "orange": 10}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [
                         {'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}])
        self.assertEqual(pending_order, {})

    def test_item_in_multiple_warehouse(self):
        """
        A test case where whole order cannot be fulfilled from single warehouse
        """

        order = {"apple": 10}
        warehouses = [{"name": "owd", "inventory": {"apple": 5}},
                      {"name": "dm", "inventory": {"apple": 5}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [
                         {'owd': {'apple': 5}}, {'dm': {'apple': 5}}])
        self.assertEqual(pending_order, {})

    def test_no_inventory(self):
        """
        A test case where inventory is zero
        """

        order = {"apple": 10}
        warehouses = [{"name": "owd", "inventory": {"apple": 0}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [])
        self.assertEqual(pending_order, {'apple': 10})

    def test_not_enough_inventory(self):
        """
        A test case where order can only be partially fulfilled 
        """

        order = {"apple": 10}
        warehouses = [{"name": "owd", "inventory": {"apple": 0}},
                      {"name": "abc", "inventory": {"apple": 5, "orange": 2}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [{'abc': {'apple': 5}}])
        self.assertEqual(pending_order, {'apple': 5})

    def test_jumbled_item_inventory(self):
        """
        A test case where item can be in multiple warehouses and 
        partial order can be fulfilled
        """

        order = {"apple": 10, "grapes": 10, "banana": 4, "orange": 6}
        warehouses = [{"name": "owd", "inventory": {"apple": 5}},
                      {"name": "dm", "inventory": {"apple": 5, "banana": 10}},
                      {"name": "abc", "inventory": {
                          "apple": 5, "banana": 2, "orange": 5}},
                      {"name": "xyz", "inventory": {"grapes": 5, "orange": 2}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [{'owd': {'apple': 5}}, {'dm': {'apple': 5, 'banana': 4}}, {
                         'abc': {'orange': 5}}, {'xyz': {'grapes': 5, 'orange': 1}}])
        self.assertEqual(pending_order, {'grapes': 5})

    def test_no_order(self):
        """
        A test case for empty order
        """

        order = {}
        warehouses = [{"name": "owd", "inventory": {"apple": 5}},
                      {"name": "dm", "inventory": {"apple": 5, "banana": 10}}]
        inventoryallocator = inventory_allocator.InventoryAllocator(
            order, warehouses)
        fulfilled_order, pending_order = inventoryallocator.order_shipment()
        self.assertEqual(fulfilled_order, [])
        self.assertEqual(pending_order, {})


if __name__ == '__main__':
    unittest.main()
