class InventoryAllocator:
    """
    A class to find cheapest shipment for given inventory
    """

    def __init__(self, order, warehouses):
        """
        Parameters
        ----------
        order : dict
            Order to be fulfilled
        warehouses : array of dict
            Storages from where orders can be fulfilled
        """

        self.order = order
        self.warehouses = warehouses

    def order_shipment(self):
        """
        Finds the cheapest way to fulfill the order

        Parameters
        ----------
        None

        Returns
        -------
        shipment : array of dict
            A cheapest shipment 
        self.order : dict
            Pending order 
            i.e. items that cannot be shipped due to shortage in stock
        """

        # An output array called shipment
        shipment = []
        # Iterate through each warehouse
        for warehouse in self.warehouses:
            # Get names and inventory of a particular warehouse
            name = warehouse["name"]
            inventory = warehouse["inventory"]
            # Initialize storage dict to store the intermediate output
            storage = {name: {}}
            # Iterate through inventory of the warehouse
            for item in inventory:
                # Check if item is in order
                if item in self.order:
                    # Check if inventory has enough items in it
                    # Update the order and inventory items
                    if inventory[item] >= self.order[item]:
                        storage[name][item] = self.order[item]
                        inventory[item] -= self.order[item]
                        self.order.pop(item)
                    elif inventory[item] == 0:
                        continue
                    else:
                        storage[name][item] = inventory[item]
                        self.order[item] -= inventory[item]
                        inventory[item] = 0
            # Check if intermediate result is not empty
            if storage[name]:
                shipment.append(storage)
            # If no items left in order then return
            if not self.order:
                return shipment, self.order

        return shipment, self.order


if __name__ == "__main__":
    """
    A block of code to test the InventoryAllocator class
    """

    # Defining order and warehouse inventory (Happy case)
    order = {"apple": 10}
    warehouses = [{"name": "owd", "inventory": {"apple": 10}}]

    # Print input
    print("Order: ", order)
    print("Warehuses: ", warehouses)

    # Create object of "InventoryAllocator" class
    inventoryallocator = InventoryAllocator(order, warehouses)
    # Call "order_shipment" to get fulfilled order and pending order (if any)
    fulfilled_order, pending_order = inventoryallocator.order_shipment()

    # Print output
    if pending_order:
        print("Fulfilled Order: ", fulfilled_order)
        print("Pending Order: ", pending_order)
    else:
        print("Fulfilled Order: ", fulfilled_order)
