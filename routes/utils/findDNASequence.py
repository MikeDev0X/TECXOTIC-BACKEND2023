from routes.utils.fish_species import fishSpecies, name_cytochrome

def searchSpecies(eDNA_array):

    index = -1

    foundSpeciesDict = {}
    counter = 0

    # searches each substring in every element inside species dictionary
    for x in range(len(eDNA_array)):
        for key in fishSpecies:
            currentKey = str(fishSpecies[key])
            currentKey = currentKey.replace(r'\n', '')
            currentKey = currentKey.replace('{','')
            currentKey = currentKey.replace('}','')

            index = currentKey.find(eDNA_array[x])
            
            if index != -1:

                foundSpeciesDict["fish" + str(counter+1)] = {"scientific_name" : str(name_cytochrome[key]), "common_name" : str(key)}
                break

        counter += 1
    return foundSpeciesDict