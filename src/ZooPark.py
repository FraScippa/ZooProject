#Francesca Scippa
#08-05-2024

class Animal:

    def __init__(self, name: str, species: str,
                 age: int, height: float, 
                 width: float, preferred_habitat: str, 
                 health:float = None, dimention: int = 0):
        
        self.name: str = name
        self.species: str = species
        self.age: int = age
        if self.age <= 0:
            print("### The animal can't have this age! ###")   
        else:
            self.age: int = age
        
        self.height: float = height
        if self.height <= 0:
            print("### The animal can't have this height!###")
        self.width: float = width
        if self.width <= 0:
            print("### The animal can't have this width! ###")
        self.preferred_habitat: str = preferred_habitat
        self.health: float = health
        try:
            self.health: float = round(100*(1/age),3)
            if self.health < 0:
                print("### The health can be negative! ###")
        except ZeroDivisionError:
            print("### Can't calculete the health. ###")
        self.dimention: int = width*height
        self.animals: list[str] = []
        self.current_fence: str = None
    
    def get_animal_species(self) -> str:
        return self.species
    
    def get_dimention(self) -> float:
        return self.dimention
    
    def get_animal_name(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return f"Animal's name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nHeight: {self.height}\nWidth: {self.width}\nHabitat: {self.preferred_habitat}\nHealth: {self.health}\nDimention: {self.dimention}"

class Fence:
    
    def __init__(self, area: float, temperature: float, 
                 habitat: str,  animals: list[Animal] = None, animal: Animal = 0):
        
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[str] = []
        
        if animals is None:
            pass
        else:
           animals.append(animal)

    def get_area(self):
        return self.area  
    
    def __str__(self):
        animal_info = ''
        for animal in self.animals:
            animal_info += f"{animal.name} ({animal.species}) - Health: {animal.health} - Dimention: {animal.dimention}\n"
        if not animal_info:
            animal_info = 'Empty fence\n'
        
        return "#"*30+f"\nEmpty Area: {self.area}\nTemperature: {self.temperature}\nHabitat: {self.habitat}\nAnimals:\n{animal_info}"+'#'*30
  
class ZooKeeper:

    def __init__(self, name: str, surname: str, ID: int):
        
        self.fence: Fence = Fence
        self.name: str = name
        self.surname: str = surname
        self.ID = ID
    
    def get_animal_species(self, species_name: str, animals: Animal):
        for animal in animals:
            if animal.species == species_name:
                return animal
        return None
    
    def add_animal(self, animal: Animal, fence: Fence):
        
        if not isinstance(fence, Fence):
            print("### Type mismatch: 'fence' type not supported ###")
        
        if not isinstance(animal, Animal):
            print("### Type mismatch: 'animal' type not supported ###")
        
        if animal.preferred_habitat.title() != fence.habitat:
            print(f"### {animal.species}: This animal isn't appropiriate for {fence.habitat}. ###")
        
        try:
            if fence.area >= animal.dimention:
                
                fence.area -= animal.dimention
                fence.animals.append(animal)
                animal.current_fence = fence
            
            else:
                print(f"#### OH NO! You can't add the {animal.species}! Your fence is full! Remove an\some animal\s! ###")
        
        except AttributeError:
            print("### Wrong input order! The second parament doesn't have an area! ###")
            
    def remove_animal(self, animal: Animal, fence: Fence):
       
        if animal in fence.animals:
            fence.area += animal.dimention
            fence.animals.remove(animal)
        
    def feed(self, animal: Animal, fence: Fence = None):
        
        if animal.health < 100:
            new_animal_health = animal.health * 1.01  
            new_animal_dimention = animal.dimention * 1.02  
            
            if fence is None:
                fence = animal.current_fence
            
            try:
                if new_animal_dimention <= fence.area:
                  fence.area += animal.dimention
                  animal.dimention = new_animal_dimention
                  animal.health = min(new_animal_health, 100)
                  fence.area -= animal.dimention
            
            except AttributeError:
                print("### OH NO! You don't have enough space in this fance for feed this animal! ###")
        
        else:
            print("### Your animal is full health! ###")
    
    def clean(self, fence : Fence) -> float: 
        total_dimention = 0
        
        for animal in fence.animals:
            total_dimention += animal.get_dimention()
        try:
            if animal is not None:
                total_dimention += animal.dimention
            
            empty_area = fence.area - total_dimention
            
            if total_dimention == 0:
                cleaning_time = fence.area
            
            elif empty_area == 0:
                cleaning_time = total_dimention
            
            elif fence.area == 0:
                cleaning_time = 0
            else:
                cleaning_time = total_dimention / empty_area
            
            fence.animals.clear()
            print(f'The cleaning time is: {cleaning_time}')
        
        except UnboundLocalError:
            print(f'The cleaning time is: {fence.area}')     
        
        
    def __str__(self) -> str:
        return f"\nZooKeeper: {self.name} {self.surname}ID: {self.ID}\n"+"_"*30
        
class Zoo:
    
    def __init__(self, guardians: list[ZooKeeper], fence: list[Fence],):
        
        self.fence: list[Fence] = fence
        self.guardians: list[ZooKeeper] = guardians
        
    
    def __str__(self) -> str:
        try:
            g: str = ''
            for guardian in self.guardians:
                g += f'ZooKeeper(name = {guardian.name}, surname = {guardian.surname}, ID = {guardian.ID})\n\n'
            
            f: str = ''
            for fence in self.fence:
                if fence.animals:
                    f += '#'*30+f'\n\nFences:\n\nFence(area = {fence.area}'+f' temperature = {fence.temperature}'+f' habitat = {fence.habitat})'+f'\n\nwith animals:\n\n'    
                for animal in fence.animals:
                   f += f'\nAnimal(name = {animal.name}, species = {animal.species}, age = {animal.age}, health = {animal.health}, height = {animal.height}, width = {animal.width}, preferred habitat = {animal.preferred_habitat})\n\n'
                    
            return f"\nGuardians:\n\n{g}{f}"
        except TypeError:
            print('Please, insert the ZooKeeper/Fence in lists with []')
    
    def describe_zoo(self):
        return self.__str__()
 