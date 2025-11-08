import pandas as pd

data = {
    'Name': ['Anushka', 'Ayush', 'Riddhi'],
    'Age': [20, 21, 19],
    'City': ['Delhi', 'Jaipur', 'Chandigarh']
}

df = pd.DataFrame(data)
print(df)
