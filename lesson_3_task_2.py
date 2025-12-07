from smartphone import Smartphone

phone_data = [
    ("Samsung", "Galaxy S23", "+7918416093"),
    ("Apple", "iPhone 15", "+79286667776"),
    ("Xiaomy", "Realm 6 Pro", "+79991236616"),
    ("Nokia", "3310", "+79163150034"),
    ("Motorola", "Razen", "+79094493639"),
]

catalog = []

for brand, model, user_number in phone_data:
    new_phone = Smartphone(
        brand=brand,
        model=model,
        user_number=user_number
    )

    catalog.append(new_phone)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.user_number}")
