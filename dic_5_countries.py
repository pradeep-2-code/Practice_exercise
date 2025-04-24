# Create a dictionary that stores the names of 5 countries as keys and their capitals as values.
# Write a program that takes a country name as input and prints its capital. Use string methods to ensure the input is case-insensitive.
country_capitals = {
    "India": "Delhi",
    "China": "Beijing",
    "Nepal": "Kathmandu",
    "Germany": "Berlin",
    "England": "London",
}
country = input("Give a country name").lower()
for key, values in country_capitals.items():
    if country == key.lower():
        print(values)
