from Apriori import *

if __name__ == "__main__":

    path = r'Data/ticdata2000.txt'
    minSupport = 0.2
    minCofidence = 0.15
    aprioriAlgorithm(path, minSupport, minCofidence)
