import pandas as pd
import random

data = []

for i in range(500):

    area = random.randint(800, 12000)
    bedrooms = random.randint(1, 6)
    bathrooms = random.randint(1, 5)
    stories = random.randint(1, 4)

    mainroad = random.choice(['yes', 'no'])
    guestroom = random.choice(['yes', 'no'])
    basement = random.choice(['yes', 'no'])
    airconditioning = random.choice(['yes', 'no'])

    parking = random.randint(0, 4)

    furnishingstatus = random.choice([
        'furnished',
        'semi-furnished',
        'unfurnished'
    ])

    price = (
        area * 1200 +
        bedrooms * 500000 +
        bathrooms * 350000 +
        stories * 250000 +
        parking * 150000
    )

    if airconditioning == 'yes':
        price += 400000

    if furnishingstatus == 'furnished':
        price += 600000

    elif furnishingstatus == 'semi-furnished':
        price += 300000

    price += random.randint(-500000, 500000)

    data.append([
        price,
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        airconditioning,
        parking,
        furnishingstatus
    ])

columns = [
    'price',
    'area',
    'bedrooms',
    'bathrooms',
    'stories',
    'mainroad',
    'guestroom',
    'basement',
    'airconditioning',
    'parking',
    'furnishingstatus'
]

df = pd.DataFrame(data, columns=columns)

df.to_csv('Housing.csv', index=False)

print("Housing.csv created successfully!")
