# Base class
class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Price: Ksh{self.price}"

    def make_call(self, number):
        return f"Dialing {number} from {self.model}..."

# Subclass with inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, price, battery_life):
        super().__init__(brand, model, storage, price)
        self.battery_life = battery_life

    def display_details(self):
        return f"{super().display_details()}, Battery Life: {self.battery_life} hours"

    def track_steps(self, steps):
        return f"Tracked {steps} steps today on {self.model}."

# Example usage
phone = Smartphone("Tecno", "Camon 20", 256, 30000)
watch = Smartwatch("Infinix", "Q30", 32, 3999, 47)

print(phone.display_details())
print(phone.make_call("123-456-7890"))

print(watch.display_details())
print(watch.track_steps(10000))
