import pandas as pd
import numpy as np

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
                unique_entry = (col,i)
                self._uniqueValue[unique_entry] = 0                                 

        self._sets[self._currentSet] = self._uniqueValue 


    def getSupport(self,data):
        """calculates support from the data table
        
            Args:
                data (list): list of data to calculate it's support in the data table
                
            Returns:
                support (float): the support
        """
        #make an array with the number of transactions
        num_of_values=1 # to calculate totla numbers of values multiplied in each others
        num_of_col=len(data)# number of columns in data list
        num_of_trans=5822 #total number of transactions
        arr=np.zeros((num_of_col,num_of_trans))#array to get the specific rows from global data
        lists=np.array(num_of_col)
        for i in range(len(data)):#loop for tuples in the list
            arr[i]=(np.array(self._dataTable[data[i][0]]))#get specific rows from global data
            num_of_values*=len(data[i][1])
        ###################################################### this section to merge values in all lists and generate onle list
        merged_array=np.zeros([len(data),num_of_values])############## this array to merge all values in lists
        for i in range(len(data)):
            list_len=(int(num_of_values/len(data[i][1])))
            arr1=np.full((list_len,len(data[i][1])),data[i][1])
            arr1=arr1.flatten()
            merged_array[i]=(arr1)
        merged_array=merged_array.T
        ##############################################################################
        ans=np.ones(num_of_trans)
        k=0
        for i in range(len(merged_array)):
            for j in range(len(merged_array[i])):
                if(k==num_of_col):
                    k=0
                num=(arr[k]==merged_array[i][j])
                ans=np.logical_and(ans,num)
                k+=1
            print(sum(ans))
            ans=np.ones(num_of_trans)


    def getConfidence(self,data):
        """calculates Confidence from the data table
        
            Args:
                data (list): list of data to calculate it's Confidence in the data table
                
            Returns:
                confidence (float): the Confidence
        """


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

    def calculateSupportAndConfidence(self):
        """calculates Support And Confidence for the current set
         
            Args:
                none

            Returns:
                none
        """

        for key, value in self._sets[self._currentSet].items():
            value = (self.getSupport(key),self.getConfidence(key))
    


    def constract(self):
        """constracts the next level elements, 
            updates self._sets with a new key and a new set
            update self._currentSet
            
        
            Args:
                none            
            Returns:
                none
        """



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
    apriori.calculateSupportAndConfidence()
    apriori.eliminate() 
   
    while (len(apriori._sets[apriori._currentSet]) != 0):

        apriori.constract()
        apriori.calculateSupportAndConfidence()
        apriori.eliminate()


    # function to print last set
        