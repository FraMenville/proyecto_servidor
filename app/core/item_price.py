class ItemPrice:
    """Clase para representar un producto con su precio."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name}: {self.price if self.price is not None else 'No disponible'}"