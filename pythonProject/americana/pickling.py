import pickle

data = {'name': 'Wyeben', 'age': 23, 'city': 'Lagos'}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
