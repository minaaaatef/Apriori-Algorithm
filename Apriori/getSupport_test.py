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
    num_of_values=1 # to calculate totla numbers of values multiplied in each others
    num_of_col=len(data)# number of columns in data list
    num_of_trans=4 #total number of transactions
    arr=np.zeros((num_of_col,num_of_trans))#array to get the spesific rows from global data
    lists=np.array(num_of_col)
    #ans=np.ones((2,4))#####################################################################
    for i in range(len(data)):#loop for tuples in the list
        arr[i]=(np.array(df[data[i][0]]))
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
    ans=np.ones(4)
    k=0
    for i in range(len(merged_array)):
        for j in range(len(merged_array[i])):
            if(k==num_of_col):
                k=0
            num=(arr[k]==merged_array[i][j])
            ans=np.logical_and(ans,num)
            k+=1
        print(merged_array[i],sum(ans))
        ans=np.ones(4)

data=[('a',[1,2,3]),('b',[8,3]),('c',[0,1])]
getSupport(df,data)
