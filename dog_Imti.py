import csv


class Dog:
    all_dogs = [] 
    def __init__(self, breed: str, age: float, weight: float, name: str = "n/a", breedgroup: str = "n/a"): 
        self.breed = breed
        self.age = age
        self.weight = weight
        self.name = name
        self.breedgroup = breedgroup
        Dog.all_dogs.append(self)
    def __repr__(self):  
        return f"{self.name}: ({self.breed} | {self.breedgroup} | {self.age} | {self.weight})" 
    def get_age(self): 
        return self.age
    @classmethod
    def sum_ages(cls):
        total = 0
        for dog in Dog.all_dogs:
            total += dog.age
        return total
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
    @classmethod
    def get_dog(cls, breed):
        for dog in Dog.all_dogs:
            if breed == dog.breed: 
                return dog
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
    