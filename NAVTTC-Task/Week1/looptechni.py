#loop using enumerate function
words = ['The', 'Big', 'Bang', 'Theory']

for index, value in enumerate(words):
    print(index, value)

#Loop using Zip function
names = ['Leo', 'Kendall', 'Harry']
ages = (24, 27, 25)

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")