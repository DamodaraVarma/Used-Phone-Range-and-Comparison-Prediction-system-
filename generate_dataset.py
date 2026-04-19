import pandas as pd
import random

brands = ["Samsung", "Apple", "Xiaomi", "Realme", "Vivo", "Oppo", "OnePlus", "Asus"]

data = []

for _ in range(10000):
    brand = random.choice(brands)

    ram = random.choice([4, 6, 8, 12])
    storage = random.choice([64, 128, 256])
    camera = random.choice([12, 16, 32, 48, 64, 108])
    battery = random.randint(3500, 6000)
    display = round(random.uniform(6.1, 6.9), 1)
    age = random.randint(0, 5)

    base_price = {
        "Apple": 60000,
        "Samsung": 35000,
        "OnePlus": 32000,
        "Xiaomi": 25000,
        "Realme": 22000,
        "Vivo": 23000,
        "Oppo": 24000,
        "Asus": 30000
    }[brand]

    depreciation = age * random.randint(4000, 7000)
    price = max(5000, base_price + (ram * 1000) + (camera * 50) - depreciation)

    data.append([
        brand, ram, storage, camera, battery, display, age, int(price)
    ])

df = pd.DataFrame(data, columns=[
    "Brand", "RAM", "Storage", "Camera", "Battery", "Display", "Age", "Price"
])

df.to_csv("used_phone_data.csv", index=False)

print("Dataset generated: used_phone_data.csv")
