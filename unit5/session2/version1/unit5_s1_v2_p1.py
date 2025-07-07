class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def add_item(self, item_name):
        if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]:
            self.furniture.append(item_name)

    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory empty")
            return
        res = ""
        dct = {}
        for furn in self.furniture:
            if furn not in dct:
                dct[furn] = 1
            else:
                dct[furn] += 1
        
        # print(dct.items())
        lst = []
        for key,value in dct.items():
            lst.append(f"{key}: {value}")
        
        print(", ".join(lst))
            
            

    


alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()