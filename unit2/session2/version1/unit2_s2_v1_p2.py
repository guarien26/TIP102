def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    total_sum = 0

    for chr in observed_species:
        if chr in endangered_species:
            total_sum+=1
    
    return total_sum



endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2)) 

"""
inputs: 
endangered_species (str) containing characters of species
observed_species (str) all species in the population

output: total number of occurences of the endangered species

constraints: characters only and case sensitive

edges: string is empty

"""