# #2
# print(1020)             
# print(33.1)           
# print('A')          
# print(True)
# print("Hello, World!")          
# #3
# my_int = 1020
# my_float = 33.1
# my_char = 'A' 
# my_bool = True
# my_string = "Hello, World!"

# print (my_int)
# print (my_float)
# print (my_char)
# print (my_string)
# print (my_bool)

#4

from dog_Imti import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 


dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  

dog2 = Dog("Golden Retriever", 3, 64.0, "Callypso")

dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")

print(dog1)

print(dog2.age)

print(dog2.get_age())

total = 0

for dog in Dog.all_dogs:
    total += dog.age
print(total)
print(f"Total age of all dogs is: {total}")

print(Dog.sum_ages())

with open("/Users/imtiagea./Desktop/BME 2315/Mod 1/Comp_BME_Module1/dog data set.csv", newline="") as f:
    reader = csv.reader(f)
    headers = next(reader) # Get the first row
    for h in headers:
        print(h)

Dog.instantiate_from_csv("/Users/imtiagea./Desktop/BME 2315/Mod 1/Comp_BME_Module1/dog data set.csv")

print(Dog.get_dog("Pug"))

Dog.all_dogs.sort(key=Dog.get_age, reverse=False)

for dog in Dog.all_dogs:
     print(dog)

working_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Working")))
print(f'Number of Working Dog breeds = {len(working_dogs)}')

toy_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Toy")))
print(f'Number of Toy Dog breeds = {len(toy_dogs)}')

age_Working_dogs = []
age_Toy_dogs = []

for dog in Dog.filter(Dog.all_dogs, breedgroup = "Working"):
    age_Working_dogs.append(dog.age)
for dog in Dog.filter(Dog.all_dogs, breedgroup = "Toy"):
    age_Toy_dogs.append(dog.age)

x_Working_dog_bar = (statistics.mean(age_Working_dogs))
x_Toy_dog_bar = (statistics.mean(age_Toy_dogs))

age_Working_dog_stdev = (statistics.stdev(age_Working_dogs))
age_Toy_dog_stdev = (statistics.stdev(age_Toy_dogs))

print(f'x_Working_dog_bar = {x_Working_dog_bar}, age_Working_dog_stdev {age_Working_dog_stdev}')
print(f'x_Toy_dog_bar = {x_Toy_dog_bar}, age_Toy_dog_stdev {age_Toy_dog_stdev}')

Dog_breedgroup_cols = ['Working Dogs', 'Toy Dogs']
mean_breedgroup = [x_Working_dog_bar, x_Toy_dog_bar]
stdev_breedgroup = [age_Working_dog_stdev, age_Toy_dog_stdev]
yerr = [np.zeros(len(mean_breedgroup)), stdev_breedgroup]

plt.bar(Dog_breedgroup_cols, mean_breedgroup, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Lifespan of Breedgroups")
plt.xlabel("Breedgroup")
plt.ylabel("Average Lifespan (age)")
plt.show()

breed_age = []
breed_weight = []

for dog in Dog.all_dogs:
    breed_age.append(dog.age)

for dog in Dog.all_dogs:
    breed_weight.append(dog.weight)

X = [breed_age]  # Independent variable
y = [breed_weight]   # Dependent variable

plt.scatter(X, y, color='blue')
plt.xlabel('Average Lifespan')
plt.ylabel('Average Weight')
plt.title('Scatter Plot of Average Lifespan vs Average Weight')
plt.show()








