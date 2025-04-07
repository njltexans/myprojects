#map() function applies a givien function to all the items in a collection
# map(function, collection)


def celcius_to_fahrenheit(temp): # Converts celcius to fahrenheit
    return (temp * 9/5) + 32

celcius_temps = [0, 22.5, 40, 100]

fahrenheit_temps = map(celcius_to_fahrenheit, celcius_temps) # uses map function to apply celcius_to_fahrenheit function to all items in celcius_temps list

print(list(fahrenheit_temps)) # Converts the map object to a list and prints it

