import pandas as pd
import numpy as np
from itertools import combinations 

class Apriori:
    def __init__(self,minSupport,minConfidence):
        self._minSupport = minSupport
        self._minConfidence = minConfidence
        self._sets = {}
        self._currentSet = 0


    def readFile(self,path):
        """Reads a text file and construct the base table
            Args:
                path (str): the path to the text file
             variables used in another methods:
                _dataTable 
            Returns:
                None
        """
        _file = pd.read_csv(path, sep='\s+', engine='python', header=None)
        self._dataTable = pd.DataFrame(_file.iloc[:, 3:15])
        self._dataTable.columns = ['MGEMLEEF Avg age', 'MOSHOOFD Customer main type', 'MGODRK Roman catholic',
                             'MGODPR Protestant', 'MGODOV Other religion', 'MGODGE No religion', 'MRELGE Married',
                             'MRELSA Living together', 'MRELOV Other relation', 'MFALLEEN Singles',
                             'MFGEKIND Household without children', 'MFWEKIND Household with children']

    def unique(self):
        """Returns all unique values from the data table
        
            Args:
                None
                
            Returns:
                dic with the data as keys
        """
        # variables for uniques 
        self._currentSet = 1
        self._uniqueValue = {}

        pd = self._dataTable
        for col in pd:
            arr = pd[col].unique()
            for i in arr:
                unique_entry = ((col,i),)
                self._uniqueValue[unique_entry] = 0                                 

        self._sets[self._currentSet] = self._uniqueValue 


    def getSupport(self,data):
        """calculates support from the data table
        
            Args:
                data (list): list of data to calculate it's support in the data table
                
            Returns:
                support (float): the support
        """
        ans=np.ones(5822)
        num_of_trans=5822
        for i in range(len(data)):
            arr=np.array(self._dataTable[data[i][0]])
            num=(arr==data[i][1])
            ans=np.logical_and(ans,num)
        return(sum(ans)/num_of_trans)


    def getConfidence(self,LeftTup,RightTup):
        """calculates Confidence from the data table
        
            Args:
                LeftTup,RightTup : Tuple of Tuples to calculate it's Confidence in the data table
                
            Returns:
                confidence (float): the Confidence
        """

        tup=LeftTup+RightTup
        _intersection=self.getSupport(tup)
        _LHS=self.getSupport(LeftTup)
        _confidence=intersection/_LHS
        return (_confidence)

    def getlift(self,data):
        """calculates lift from the data table
        
            Args:
                data (list): list of data to calculate it's lift in the data table
                
            Returns:
                lift (float): the lift
        """

    def getLeverage(self,data):
        """calculates Leverage from the data table
        
            Args:
                data (list): list of data to calculate it's Leverage in the data table
                
            Returns:
                Leverage (float): the Leverage
        """

    

    def eliminate(self):
        """eliminates the data elements that are less than the min-support 
           or the min-confidence, uses self._sets , and self._currentSet
        
            Args:
                none

            Returns:
                none
        """
        for key,value in self._sets[self._currentSet].items():
            if value < self._minSupport:
                del self._sets[self._currentSet][key]

    def calculateAllSupport(self):
        """calculates Support for the current set
         
            Args:
                none

            Returns:
                none
        """

        for key, value in self._sets[self._currentSet].items():
            value = self.getSupport(key)
    


    def constract(self):
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

        for key_1, value_1 in self._sets[self._currentSet].items():
            current_index += 1
            for key_2,value_2 in list(self._sets[self._currentSet].items())[current_index:]:
                # join the 2 tuples
                join = key_1 + key_2
                # remove duplicates
                join = tuple(set(join))
                # get combinations
                combined = tuple(combinations(join, self._currentSet+1))

                # append new combination to dict
                if len(combined) != 0 :
                    newSet[combined[0]] = 0
        
        self._currentSet += 1
        # append the new itemset in the sets dict 
        self._sets[self._currentSet] = newSet





def aprioriAlgorithm(path, minSuppor, minConfidence):
    """runs Apriori algorithm & prints the rules after
        
            Args:
                path (string): 
            
            Returns:
                none
    """

    apriori = Apriori(minSuppor, minConfidence)
    apriori.readFile(path)
    apriori.unique() 
    apriori.calculateAllSupport()
    apriori.eliminate() 
   
    while (len(apriori._sets[apriori._currentSet]) != 0):

        apriori.constract()
        apriori.calculateAllSupport()
        apriori.eliminate()
    
    print(apriori._sets[apriori._currentSet])

    # function to print last set
        
