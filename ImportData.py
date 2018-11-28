import urllib3
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs

yearFiles = '/Users/sanjith/Documents/Projects/ScorigamiCFB/YearFiles/'

def is_int(s):
    try:
        num = int(s)
    except ValueError:
        return False
    return True

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
                if len(line) > 5:
                    skip = False
                    stuff = line.split(' ')
                    fs = list(filter(lambda x: x != '', stuff))
                    date = fs[0]
                    homeTeamList = list()
                    visitorTeamList = list()
                    homeScore = 0
                    visitorScore = 0
                    count = 1
                    while is_int(fs[count]) == False:
                        homeTeamList.append(fs[count])
                        count += 1
                    homeScore = fs[count]
                    count += 1
                    print(fs, count)
                    while count < len(fs) and is_int(fs[count]) == False :
                        print(count)
                        if fs[count] == "Institute136":
                            visitorTeamList.append("Institute")
                            visitorScore = 136
                            skip = True
                        else:
                            visitorTeamList.append(fs[count])
                        count += 1
                    if skip == False:
                        visitorScore = fs[count]
                    homeTeam = " ".join(homeTeamList)
                    visitorTeam = " ".join(visitorTeamList)
                    fs = [date, homeTeam, int(homeScore), visitorTeam, int(visitorScore)]
                    print(fs)
                    dataRows.append(fs)
            yearDF = pd.DataFrame(dataRows, columns=("Date", "Home", "HomeScore", "Visitor", "VisitorScore"))[:-1]
            yearDF.to_excel(yearFiles + str(year) + ".xlsx", index = False)

if __name__ == '__main__':
    importData()
