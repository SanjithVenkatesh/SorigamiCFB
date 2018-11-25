import urllib3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs

yearFiles = '/Users/sanjith/Documents/Projects/ScorigamiCFB/YearFiles/'

def importData():
    for year in range(1869, 2011):
        if year != 1871:
            url = "http://homepages.cae.wisc.edu/~dwilson/rsfc/history/howell/cf" + str(year) + "gms.txt"
            http = urllib3.PoolManager()
            response = http.request('GET', url)
            dataLines = response.data.decode("utf-8").split('\n')
            print()
            dataRows = list()
            for line in dataLines:
                stuff = line.split(' ')
                fs = list(filter(lambda x: x != '', stuff))
                dataRows.append(fs[0:-1])
            print(dataRows)
            yearDF = pd.DataFrame(dataRows, columns=("Date", "Home", "HomeScore", "Visitor", "VisitorScore"))[:-1]
            print(yearDF)
            yearDF.to_excel(yearFiles + str(year) + ".xlsx")

if __name__ == '__main__':
    importData()
