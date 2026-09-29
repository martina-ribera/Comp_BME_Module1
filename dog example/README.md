# Module #1: Introduction to data and objects in Python
## Shayn Peirce-Cottler
### BME 2315: Computational BME


### Computers are just data reading and writing machines; we give input data to the computer, and it gives us back output data.

Before we get started, make a folder for this class titled "BME_2315" on your desktop. Within that folder, make a subfolder called "Module_1_Dog_Practice". 

Then, make two python files in this folder: 
1) main.py 
2) dog.py 

The main.py file is your main method where you will run your code. 

The dog.py file and all the other python files that you make will contain code to be executed in main.py. You should only have *ONE* main.py file in any given python project. 

## 1) Data Types

    Here are examples of the 5 primitive data types in python:

    1. This is an integer: 1020
    2. This is a float (floating point): 33.1
    3. This is a character: 'A' 
    4. This is a boolean: True
    5. This is a nonetype: None
    
    and, (last but not least)...

    6. This is a string (a sequence of characters, as if they are tied together in a STRING): "Hello, World!"
    (Note: a string is not a primitive data type, characters are.)

## 2) Now that we know what data is, what can we do with it? We can show it to ourselves by printing it!

Let's print this in the main.py file:

    print(1020)           
    
    print(33.1)          
    
    print('A')          
    
    print(True)

    print("Hello, World!")          

## 3) We can use these data types to define variables.

Here are variables for each data type:

    my_int = 1020
    my_float = 33.1
    my_char = 'A' 
    my_bool = True
    my_string = "Hello, World!"

For fun, let's print these variables in the main.py file:

    print (my_int)
    print (my_float)
    print (my_char)
    print (my_string)
    print (my_bool)

## 4) Define a class of objects: Dog Class. Do this in your file called: dog.py (i.e., not in the main.py file). 
 
 First, we need to construct a "class" for our dog objects. Each dog in our class will have the following attributes: breed, age, weight, name, and breedgroup (like "Working", "Sporting", "Terrier", etc.).    

 Define the dog class with a class header:
    
    class Dog:
   
## 5) Make a "constructor" (__init__) that lists the different attributes that a dog can have. A constructor is considered a "special method".

Type the following code in dog.py. Make sure the indentation is lined up with the line above and inside the "class Dog:" line. Note that "self" is the object itself.

    def __init__(self, breed: str, age: float, weight: float, name: str = "n/a", breedgroup: str = "n/a"): 
        self.breed = breed
        self.age = age
        self.weight = weight
        self.name = name
        self.breedgroup = breedgroup

## 6) To be able to call this constructor in main.py, we need to tell python to import everything ("*") from dog.py into main.py.

 Do this by typing the following at the top of main.py:

    from dog import *

## 7) Now, lets make some dog-type objects using our constructor. Do this in the main.py file.

Use the constructor to construct each dog according to the attributes we specified in the constructor. Note that dog4 and dog5 below are nameless, so they will be given the default string that we made in the constructor, which was ("n/a"). 

    dog1 = Dog("German Pinscher", 1, 43.0, "Rizzo")  

    dog2 = Dog("Golden Retriever", 3, 64.0, "Callypso")

    dog3 = Dog("Chihuahua", 2, 15.6, "Cheeto")

    dog4 = Dog("Blue Tick Hound", 4, 52.5)

    dog5 = Dog("Black Laborator Retriever", 6, 73.0)

## 8) Make a "representer" (__repr__) in dog.py that defines what is shown to us when we print a "dog" type object. A representer is considered a "special method".

"Representers" are special methods that are called when we print. As always, be mindful of your indentation. 

    def __repr__(self):  
        return f"{self.name}: ({self.breed} | {self.breedgroup} | {self.age} | {self.weight})" 

## 9) Call the "representer" (__repr__) in main.py file by printing an object in our dog Class. 

    print(dog1)

## 10) Next, let's ask python to return a specific attribute from one of our dog objects. 

For example, we want to return the age of dog2. In main.py, type:

    print(dog2.age)

## 11) Let's turn this code into a "getter" method, which is considered an "instance method" because it is called on a single object, in dog.py.

Define a "getter" that finds the dog's age and returns it when we ask for it. But note that "return" does not print. Even if you "return" informtation, if you want to see it, you will need to still print it. And, as always, be mindful of your indentation. 

    def get_age(self): 
        return self.age
   
## 12) Now, let's call the getter in main.py. 

In main.py, type:

    print(dog2.get_age())

## 13) Next, let's sum the ages of all the dogs we've created thus far using a "for loop". But first we need to make a list of our dogs.

In order to accomplish this, we need to create a list of every dog object that we construct. Let's call this list: "all_dogs". Put it right under the first line, where you typed "class Dog:" but be sure to indent this code inside the "class Dog:" line in the dog.py file. 

    all_dogs = []  

This is a class variable, or static variable. It is associated with a class. Unlike object attributes, this class variable does not change between objects. 

To build this list, we need to add the following line of code to the bottom of your dog constructor:

    Dog.all_dogs.append(self)

Dog.all_dogs is the class variable that we just created. We have to specify Dog.all_dogs because the "all_dogs" list resides in the Dog class. We point python to the Dog class to retrieve this list. 

Even though we're in the same file, we still need to do this. 

Next, in our main.py file, we will use a for loop to sum the ages of all the dogs in the all_dogs list, and we will print (output) the result.  

    total = 0

    for dog in Dog.all_dogs:
        total += dog.age
    print(total)
    print(f"Total age of all dogs is: {total}")

Note that "total += dog.age" is a shorthand way of saying "total = total + dog.age"

## 14) Let's turn this code into a class method in the dog.py file:

Make sure the class method is indented inside the "Class Dog:" line.

    @classmethod
    def sum_ages(cls):
        total = 0
        for dog in Dog.all_dogs:
            total += dog.age
        return total

## 15) Now, call this method in the main.py file:

    print(Dog.sum_ages())

## 16) Instead of typing out each dog, let's import our dogs from a .csv file. We will make a class method to do this.

First, at the top of dog.py, tell python to "import csv" by typing the following on the very first line (i.e., above the "Class Dog:" line):

    import csv

We may want to inspect this .csv file to see what the column headers are, so we know what these data describe. We can do this in the main.py file by typing what you see below, and the way to find the filepath for this data file is to right-click on the file name in the Explorer (menu on the left side of this window) and select "Copy Path".

    with open("/Users/smp6p/Documents/TEACHING/Teaching - BME 2315/Module_1/Intro_Code_for_Module_1/dog data set.csv", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)

Next, tell Python to open the .csv file by making the following class method. As always, make sure this is indented inside the "Class Dog:" line.

    @classmethod 
    def instantiate_from_csv(cls, filename: str):

        #the code below will open the .csv file and create a list of all the rows in your spreadsheet
        
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_dogs = list(reader)
        
        #the code below will create a dog object for each row, based on the data: 
        
            for row in rows_of_dogs:
                    Dog(
                    breed = row['Name'],
                    age = (int(row['Minimum Life Span']) + int(row['Maximum Life Span'])/2),
                    weight = (int(row['Minimum Weight']) + int(row['Maximum Weight'])/2),
                    breedgroup = row['Breed Group']
                )

Note that "age" in this data set is really referring to the avearge lifespan of the breed. We are calculating it by adding the minimum and maximum lifespan and dividing by two. Similarly, to get "weight", we are averaging the minimum and maximum weights that are provided in this data set.  

## 17) Let's do something with the dog objects we created from the .csv file. As one example, let's make a "getter" to get (or retrieve) a specific breed from the spreadsheet that we're interested in. Type this code in your dog.py file, making sure it's indented inside the "Class Dog:" line.

    @classmethod
    def get_dog(cls, breed):
        for dog in Dog.all_dogs:
            if breed == dog.breed: 
                return dog

## 18) Now, let's use this class method by going to our main.py file and calling it from there. 

In main.py, type the following code, and you will need to identify the correct filepath for your file and paste it between the quotes. The way to find the filepath is to right-click on the file name in the Explorer (menu on the left side of this window) and select "Copy Path".

    Dog.instantiate_from_csv("/Users/smp6p/Documents/TEACHING/Teaching - BME 2315/Module_1/Intro_Code_for_Module_1/dog data set.csv")

    print(Dog.get_dog("Pug"))

When you run this code, you should see it "got" the object with the breed of "Pug" from the .csv file, with these attributes: 

n/a: (Pug | Toy | 19.0 | 23.0)

Note that Pug is the breed, Toy is the breedgroup, and 19.0 and 23.0 were calculated above according to the average age and average weight: (min + max) / 2, respectively. We had to do that because this .csv file doesn't contain a list of specific dogs; it only contains information about different dog breeds in general. 

## 19) Let's sort our list of dogs based on their average lifespan (i.e., "age") and then print the sorted list.

In main.py, we will use our getter that we made in Step 11 (in dog.py) to sort by "age", or lifespan, from shortest to longest lifespan:

    Dog.all_dogs.sort(key=Dog.get_age, reverse=False)

    for dog in Dog.all_dogs:
        print(dog)

## 20) Let's make a filter to select dog objects that have a specific common attribute. 

Make a new class method, as follows in dog.py:

    @classmethod
    def filter(cls, list, breed:str ="any", age:int ="any", weight:int ="any", name:str ="any", breedgroup:str ="any"):
            all_dogs = list
            remove_list = []
            attr_list = (
                        breed,
                        age,
                        weight,
                        name,
                        breedgroup
                        )
            attr_name = (
                        "breed",
                        "age",
                        "weight",
                        "name",
                        "breedgroup"
                        )
            for attr in range(len(attr_list)):
                if attr_list[attr] != "any":
                    for dog in all_dogs:
                        if getattr(dog,attr_name[attr]) != attr_list[attr]:
                            remove_list.append(dog)
                    all_dogs = [dog for dog in all_dogs if dog not in remove_list]
                    remove_list.clear()

            return all_dogs

## 21) Let's use our filter to select out -- and count -- the number of dogs with a specific attribute. 

In this example, we are filtering out, counting, and then printing the total number of dogs in the "Working" breedgroup.

Type the following code in main.py.

    working_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Working")))

    print(f'Number of Working Dog breeds = {len(working_dogs)}')

How do we filter, count, and print the total number of dogs in the "Toy" breedgroup?

    toy_dogs = range(len(Dog.filter(Dog.all_dogs, breedgroup = "Toy")))

    print(f'Number of Toy Dog breeds = {len(toy_dogs)}')

## 22) Let's make a bar graph that compares the mean (+/- standard deviation) of an attribute that we are interested in between Working dogs and Toy dogs.

In this example, we are intersted in making a bar graph that compares the mean (+/- standard deviation) lifespan (which we are calling 'age') in Working vs. Toy dogs.

Do all of this in main.py.

First, type the following in main.py under the first line, which reads: "from dog import Dog":

    import matplotlib.pyplot as plt
    from scipy import stats
    import numpy as np
    import statistics 

Next, be sure that you're still creating your dog objects from the .csv data file. 

    Dog.instantiate_from_csv("/Users/smp6p/Documents/TEACHING/Teaching - BME 2315/Module_1/Intro_Code_for_Module_1/dog data set.csv")
	
Next, make two (empty) lists that will be populated by the ages of all the Working dog breeds and Toy dog breeds, respectively:

    age_Working_dogs = []
    age_Toy_dogs = []

Next, populate these two lists with the ages of the different breeds in each breedgroup (Working and Toy) that you want to filter:

    for dog in Dog.filter(Dog.all_dogs, breedgroup = "Working"):
        age_Working_dogs.append(dog.age)
    for dog in Dog.filter(Dog.all_dogs, breedgroup = "Toy"):
        age_Toy_dogs.append(dog.age)

Next, define the bars for your bar graph as the means of the ages of the different Working dog and Toy dog breeds:

    x_Working_dog_bar = (statistics.mean(age_Working_dogs))
    x_Toy_dog_bar = (statistics.mean(age_Toy_dogs))

    age_Working_dog_stdev = (statistics.stdev(age_Working_dogs))
    age_Toy_dog_stdev = (statistics.stdev(age_Toy_dogs))

Next, define the standard deviations for your bar graph as the standard deviations of the ages of the different Working dog and Toy dog breeds:

    print(f'x_Working_dog_bar = {x_Working_dog_bar}, age_Working_dog_stdev {age_Working_dog_stdev}')
    print(f'x_Toy_dog_bar = {x_Toy_dog_bar}, age_Toy_dog_stdev {age_Toy_dog_stdev}')

Next, let's make our bar graph (which will have two bars), labeled: Working Dogs and Toy Dogs. Each bar will represent the means of the ages, and the standard deviation will be shown. 

    Dog_breedgroup_cols = ['Working Dogs', 'Toy Dogs']
    mean_breedgroup = [x_Working_dog_bar, x_Toy_dog_bar]
    stdev_breedgroup = [age_Working_dog_stdev, age_Toy_dog_stdev]
    yerr = [np.zeros(len(mean_breedgroup)), stdev_breedgroup]

Lastly, we will plot and show the bar graph with apprpriate labels. 

    plt.bar(Dog_breedgroup_cols, mean_breedgroup, yerr=yerr, capsize=10, color=["blue", "orange"])
    plt.title("Average Lifespan of Breedgroups")
    plt.xlabel("Breedgroup")
    plt.ylabel("Average Lifespan (age)")
    plt.show()

## 23) Next, let's make a scatter plot that compares one dog attribute to another dog attribute in our data set. IMPORTANTLY, these attributes have to be defined as either integer or floating point values and can't represent ordered categories, like a Likert scale (see note below). 

In this example, we will plot average breed weight (on the y-axis) vs. average breed "age", or lifespan (on the x-axis). This is really important...

NEVER plot "Likert data" -- where the data is ordered categories, like "temperment" (if that was provided as a score) -- on a scatter plot. Scatter plots assume the data live on a continuous numerical scale where distances matter. The distance between Thal scores (1, 2, 3, 4, etc..) is arbitrary. This is because a Likert scale (e.g., 1 = strongly disagree … 5 = strongly agree) tells you order, but not meaningful spacing between each level. Always remember: if the numbers in your data are labels (that represent things like "low, medium, high, very high"), not measurements, don’t plot them on a scatter plot!

Type all of this code in the main.py file. 

First, define two empty lists that will hold these data:

    breed_age = []
    breed_weight = []

Next, fill these empty lists with data from the dataset. 

    for dog in Dog.all_dogs:
        breed_age.append(dog.age)

    for dog in Dog.all_dogs:
        breed_weight.append(dog.weight)

Next, define the independent variable (which will be plotted on the x-axis) and the dependent variable (which will be plotted on the y-axis).

    X = [breed_age]  # Independent variable
    y = [breed_weight]   # Dependent variable

Now we can visualize these data on our scatter plot, by typing the following:

    plt.scatter(X, y, color='blue')
    plt.xlabel('Average Lifespan')
    plt.ylabel('Average Weight')
    plt.title('Scatter Plot of Average Lifespan vs Average Weight')
    plt.show()