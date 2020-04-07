


class Apriori:
    def init(self,minSupport,minConfidence):
        self._minSupport = minSupport
        self._minConfidence = minConfidence


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


    def getSupport(self,data):
        """calculates support from the data table
        
            Args:
                data (list): list of data to calculate it's support in the data table
                
            Returns:
                support (float): the support
        """


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


    def eliminate(self,datadic):
        """eliminates the data elements that are less than the min-support 
           or the min-confidence
        
            Args:
                datadic (dic): dic of data elements with the key ---> the support & confidence
            
            Returns:
                datadic (dic): after eliminating the elements
            
        """


    def constract(self, datadic):
        """constracts the next level elements
        
            Args:
                datadic (dic): dic of data elements with the key ---> the support & confidence
            
            Returns:
                datadic (dic): after constacting the new combinations 
        """

    def Apriori(self):
        """runs Apriori algorithm & prints the rules after
        
            Args:
                none
            
            Returns:
                none
        """