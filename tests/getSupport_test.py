import pandas as pd 
import numpy as np
	
# List1 
# 2,8,0,5,1,3,7,0,2,1,2,6
# 2,8,1,4,1,4,6,2,2,0,4,5
# 2,8,0,4,2,4,3,2,4,4,4,2
# 3,3,2,3,2,4,5,2,2,2,3,4
	
lst = {'1':[2,8,0,5,1,3,7,0,2,1,2,6],
       '2':[2,8,1,4,1,4,6,2,2,0,4,5],
       '3':[2,8,0,4,2,4,3,2,4,4,4,2],
       '4':[3,3,2,3,2,4,5,2,2,2,3,4]}
df = pd.DataFrame(lst)
df=df.T
df.columns=columns=['a','b','c','d','e','f','g','h','i','j','k','l']

def getSupport(df,data):
    """calculates support from the data table
    
        Args:
            data (list): list of data to calculate it's support in the data table
            
        Returns:
            support (float): the support
    """
    #make an array with the number of transactions
    ans=np.ones(4)
    for i in range(len(data)):
        arr=np.array(df[data[i][0]])
        num=(arr==data[i][1])
        ans=np.logical_and(ans,num)
    print(sum(ans))
    ans=np.ones(4)

data_in=[('a',2),('b',8),('c',0)]
getSupport(df,data_in)
