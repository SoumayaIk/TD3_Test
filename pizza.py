class Pizza: 
    def __init__(self,nom,ingredients,prix):
        self.__nom = nom
        self.__ingredients = []
        self.__ingredients = ingredients
        self.__prix = prix
        
    def get_pizza_name(self):
        return self.__nom
    
    def __repr__(self):
        return f"Pizza {self.__nom}, Prix = {self.__prix}, Ingredients = {self.__ingredients}"