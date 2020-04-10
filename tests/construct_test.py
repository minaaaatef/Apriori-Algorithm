import pandas as pd
from itertools import combinations 

sets = {}
sets[1] = {
    ('A',1):0,
    ('A',2):0,
    ('B',1):0,
    ('B',2):0,
}

def constract(currentSet = 1):
        """constracts the next level elements, 
            updates self._sets with a new key and a new set
            update self._currentSet
            
        
            Args:
                none            
            Returns:
                none
        """
        newSet = {}
        current_index = 0
        for key_1, value_1 in sets[currentSet].items():
            current_index +=1
            for key_2,value_2 in list(sets[currentSet].items())[current_index:]:  
                # join the 2 tuples
                join = key_1 + key_2
                # remove duplicates
                join = tuple(set(join))
                # get combinations
                combined = tuple(combinations(join, currentSet+1))

                # append new combination to dict
                if len(combined) != 0 :
                    newSet[combined[0]] = 0
        
        currentSet += 1
        # append the new itemset in the sets dict 
        sets[currentSet] = newSet
    
        return

currentSet = 1
while currentSet <= 3:

    constract(currentSet)
    currentSet +=1