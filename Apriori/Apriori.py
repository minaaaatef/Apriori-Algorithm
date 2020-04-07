


class Apriori:
    def init(self,minSupport,minConfidence):
        self._minSupport = minSupport
        self._minConfidence = minConfidence


    def readFile(self,path):
        """Reads a text file and constract the base table

            Args:
                path (str): the the pass to the text file

            Returns:
                None
        """


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