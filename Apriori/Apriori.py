import pandas as pd
import numpy as np
from itertools import combinations 
from itertools import permutations 
from math import floor 

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
        _confidence=_intersection/_LHS
        return (_confidence)

    def getlift(self,LeftTup,RightTup):
        """calculates lift for each rule from the data table
        
            Args:
                LeftTup,RightTup : Tuple of Tuples to calculate it's Lift
                
            Returns:
                lift (float): the lift
        """
        tup=LeftTup+RightTup
        _nom=self.getSupport(tup)
        _den=self.getSupport(LeftTup) * self.getSupport(RightTup)
        _lift=_nom/_den
        return (_lift)

    def getLeverage(self,LeftTup,RightTup):
        """calculates Leverage for each rule from the data table
        
            Args:
                LeftTup,RightTup : Tuple of Tuples to calculate it's Leverage
                
            Returns:
                Leverage (float): the Leverage
        """
        tup=LeftTup+RightTup
        _nom=self.getSupport(tup)
        _den=self.getSupport(LeftTup) * self.getSupport(RightTup)
        _leverage=_nom - _den
        return (_leverage)
    

    def eliminate(self):
        """eliminates the data elements that are less than the min-support 
           or the min-confidence, uses self._sets , and self._currentSet
        
            Args:
                none

            Returns:
                none
        """
        deleteKey = []
        for key,value in self._sets[self._currentSet].items():
            if value < self._minSupport:
                deleteKey.append(key)
        
        for key in deleteKey:
            del self._sets[self._currentSet][key]

    
    def eliminateRules(self):
        """eliminates the data elements that are less than the min-support 
           or the min-confidence, uses self._sets , and self._currentSet
        
            Args:
                none

            Returns:
                none
        """
        deleteKey = []
        for key,value in self._rules.items():
            if value < self._minConfidence:
                deleteKey.append(key)
        
        for key in deleteKey:
            del self._rules[key]


    def calculateAllSupport(self):
        """calculates Support for the current set
         
            Args:
                none

            Returns:
                none
        """

        for key, value in self._sets[self._currentSet].items():
            val = self.getSupport(key)
            self._sets[self._currentSet][key] = self.getSupport(key)
    


    def calculateAllConfidence(self):
        """calculates Support for the current set
         
            Args:
                none

            Returns:
                none
        """

        for key, value in self._rules.items():
            val = self.getConfidence(key[0],key[1])
            self._rules[key] = val
    



    def construct(self):
        """constructs the next level elements, 
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
                # sort combination
                combined = tuple(sorted(combined[0]))

                # append new combination to dict
                if len(combined) != 0 :
                    newSet[combined] = 0

        self._currentSet += 1
        # append the new itemset in the sets dict 
        self._sets[self._currentSet] = newSet


    def getRules(self):
        """constructs the Rules set
            Args:
                none            
            Returns:
                none
        """
        self._rules = {}
        _RuleSet = self._sets[self._currentSet - 1 ]
        for oneSet in _RuleSet :
           
            if len(oneSet) < 2 : 
                pass 
             
            for x in range(1, max(floor(len(oneSet) / 2),2) ):
                
                comb = combinations(oneSet, x)
                for item in comb:
                    remaining = tuple(x for x in oneSet if x not in item)
                    self._rules[(item,remaining)] = 0
                    self._rules[(remaining,item)] = 0
    
     def ArrangeRules(self):
        count={}
        for key, value in self._rules.items():
             lev=self.getLeverage(key[0],key[1])
             count[key]=lev
        sortedList=sorted(count.items(), key=lambda x: x[1], reverse=True)
        
    def printRules(self):
        for key, value in self._rules.items():
            print (f"{key[0]} ----> {key[1]}  with confidence = {value:3f}")
         
            



def aprioriAlgorithm(path, minSuppor, minConfidence):
    """runs Apriori algorithm & prints the rules after
        
            Args:
                path (string): 
            
            Returns:
                none
    """

    apriori = Apriori(minSuppor, minConfidence)
    print("Loading Data...")
    apriori.readFile(path)
    apriori.unique() 
    apriori.calculateAllSupport()
    apriori.eliminate()
    if (apriori._sets[1].__len__() == 0):
            print("There is No rules")
            return

    print("Constructing Itemsets...")
    while (len(apriori._sets[apriori._currentSet]) != 0):
        apriori.construct()
        apriori.calculateAllSupport()
        apriori.eliminate()
    
    if apriori._currentSet == 2:
        print("There is No rules")
        return

    print("Getting Association Rules...")
    apriori.getRules()
    print("Calculating the Confidence... \n")
    apriori.calculateAllConfidence()
    apriori.eliminateRules()
    print("Association Rules are:")
    print(len("Association Rules are:") * ".",'\n')
    apriori.printRules()