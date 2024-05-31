import unittest 
from unittest import TestCase
from src.ZooPark import Zoo, ZooKeeper, Animal, Fence

class TestZoo(TestCase):

    def setUp(self) -> None:  #è una funzione ereditata da TestCase, ma è vuota. La sovrascrivo
        
        #self.zoo_1: Zoo = Zoo() #con il self possono avere l'accesso anche alle altre funzioni
        self.zookeeper_1: ZooKeeper = ZooKeeper(name = 'Gianni', surname = 'Rossi', ID = 1) #stiamo creando delle istanze che ci permetteranno di fare dei test
        self.fence_1: Fence = Fence(area = 100, temperature = 25.0, habitat = "Savana")
        self.animal_1: Animal = Animal(name = 'Pluto', species = 'Canide', age = 5, height = 3.0, width = 1.0, preferred_habitat = 'Savana') 

    def test_animal_dimention(self):
        """ 
        Questo test controlla che animali troppo grandi non vengano aggiunti alla fance
        """
        
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result: int = len(self.fence_1.animals)
        msg: str = f"Error: the function add_animal should not add self.animal_1 in to self.fance_1"
        self.assertEqual(result, 1, msg) 

    def test_animal_add(self):
        """
        Questo test controlla che l'animale sia aggiunto correttamente alla fence
        """
        self.zookeeper_1.add_animal(self.animal_1, self.fence_1)
        result: float = len(self.fence_1.animals)
        msg: str = f"Error: the function add_animal should add self.animal_1 in to self.fence_1"
        self.assertEqual(result,1 , msg)
        
    def test_clean_fence(self):
        """
        Questo test controlla, se la fence è vuota allora ridà l'area
        """
        self.zookeeper_1.clean(self.fence_1)
        result: int = len(self.fence_1.animals)
        msg: str = f"Errore: the function clean should remove all the animals"
        self.assertEqual(result, 0, msg)
    
    def test_animal_remove(self):
        """
        Questo test controlla se l'animale viene rimosso correttamente
        """
        self.zookeeper_1.remove_animal(self.animal_1, self.fence_1)
        result: int = len(self.fence_1.animals)
        msg: str = f"Errore: the function remove_animal should remove the animal"
        self.assertEqual(result, 0, msg)
    

    


if __name__ == '__main__':  

    unittest.main()