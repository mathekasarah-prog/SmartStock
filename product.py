class Product:
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def info(self):
        print(f"Product: {self.name}")
        print(f"Price:Ksh {self.price}")
        print(f"Quantity: {self.quantity}")
        
    def is_valid(self):
        if not isinstance(self.name, str) or not self.name.strip():
            return False

        if isinstance(self.price, bool) or not isinstance(self.price, (int, float)) or self.price <= 0:
            return False

        if isinstance(self.quantity, bool) or not isinstance(self.quantity, int) or self.quantity < 0:
            return False

        return True

    def inventory_value(self):
        return self.price * self.quantity


        
products = [
    Product("Shea Glow Body Butter", 950, 25),
    Product("African Black Soap", 650, 25),
    Product("Rosemary Hair Oil", 1100, 25),
    Product("Sandalwood Scented Candle", 1500, 25),
    Product("Lavender Bath Set", 1800, 25),
    Product("Chebe & Hibiscus Hair Butter", 1250, 25),
    Product("Aloe & Honey Leave-In Conditioner", 1100, 25),
    Product("Moringa Wellness Capsules", 1500, 25),
    Product("Purify Bath Salts", 950, 25),
    Product("Niacinamide Face Cream", 1350, 25),
    Product("Mango Body Butter", 1200, 32),
    Product("Turmeric & Honey Natural Soap", 650, 18),
    Product("Rose & Aloe Face Mist", 850, 20),
    Product("Moringa Body Scrub", 1100, 33),
    Product("Rosehip Seed Oil", 1350, 30),
    Product("Lavender & Frankincense Candle", 1500, 33),
]
      
        