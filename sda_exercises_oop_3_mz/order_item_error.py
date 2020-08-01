class OrderItemError(ValueError):

    def __init__(self, info='final prices equals or below zero!'):
        super().__init__(info)
