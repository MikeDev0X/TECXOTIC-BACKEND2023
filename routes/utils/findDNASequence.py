import re
from routes.utils.fish_species import fishSpecies, name_cytochrome
import json


#eDNA_array = ['ggcattcccccgaatgaataacataagcttttgacttctccctccctcccttctccttcttctagcatccgctggggtagaagctggggccggaactggatgaacagtttacccacccctagcgggtaatctagc','cacgcattcgtaataattttctttatagtaataccaattatgattggtgggttcggaaattgattaattc']

def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)

    return obj



def searchSpecies(eDNA_array):

    index = -1

    foundSpeciesSuper = []
    foundSpeciesDict = {}

    # searches each substring in every element inside species dictionary
    for x in range(len(eDNA_array)):
        for key in fishSpecies:
            currentKey = str(fishSpecies[key])
            currentKey = currentKey.replace(r'\n', '')
            currentKey = currentKey.replace('{','')
            currentKey = currentKey.replace('}','')
            
            #print(currentKey)

            index = currentKey.find(eDNA_array[x])
            if index != -1:
                #foundSpeciesArray.append(str(key))
                print('key', key)
                foundSpeciesDict[str(key)] = {str(name_cytochrome[key])}
                foundSpeciesSuper.append(foundSpeciesDict)
                foundSpeciesDict = {}

                break

    print(foundSpeciesSuper)
    return foundSpeciesSuper

#searchSpecies(eDNA_array)
