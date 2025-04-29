import pickle
data = {"name": "Alice", "age": 25, "city": "New York"}

# Open a file in binary write mode
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

print("Data serialized and saved to data.pkl")


data = [1, 2, 3, 4, 5]

# Serialize the data to a byte stream
serialized_data = pickle.dumps(data)
print(serialized_data)


with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print("Deserialized data:", loaded_data)


deserialized_data = pickle.loads(serialized_data)
print("Deserialized data:", deserialized_data)
