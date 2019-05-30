"""
Sakar Michel
March 24, 2019

"""


'''
Assignment: 
DATA ENGINEER INTERN ASSIGNMENT
The goal of this assignment is to demonstrate your ability to capture unconventional datasets, clean and store them.
Write a scraper in either python or NodeJS to collect data from Wikipedia about the top cities in the United States.
The fields you collect, as well as the volume of data is up to you, but ideally you add additional data beyond the initial table, such as data found on the individual city pages, or other sources of your choice.
The final format should be a CSV file that is ready to be uploaded to a BigQuery table.
Please read Bigquery’s Manual to prepare your CSV in the right format.
Intermediary steps, environments or processes necessary to run the scraper should be documented in code as well as a Readme.md and hosted on github in a repo devoted to this assignment. 

'''

#Install beatifulSoup in the command line for windows
#pip install requests
#pip install beautifulsoup4
#Import the beautifulSoup library
import requests
from bs4 import BeautifulSoup
from csv import writer

#opening up the file
#need to specific encoding or the beautiful soup constructor will complain

#inF = open('C:\\Users\\Sakar\\Desktop\\List of United States cities by population - Wikipedia.html','r', encoding="UTF-8") <- Used for testing purposes
inF = requests.get('https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population')
inF = inF.text

#Creating the soup object using the BeautifulSoup constructor
# pip install html5lib
##soup = BeautifulSoup(inF, "html.parser", from_encoding="utf-8")
soup = BeautifulSoup(inF, "html.parser")


#Getting the header
#The information I want from the table is nested insided a class called class='wikitable sortable'.
#I want to print out to the excel file,  the headers for the columns first.

#find_all returns a list.
#find returns the first element with the specific search string
tag = soup.find(class_='wikitable sortable').find_all("th")

Headers = []

#Their are nine headers in the table from Wikipedia.

header1= '' #Rank
header2= '' #City
header3= '' #State
header4= '' #2018 estimate
header5= '' #2010 Census
header6= '' #Change
header7= '' #2016 land area
header8= '' #2016 population density
header9= '' #Location

for eachHeader in tag:
   #The elmement in the list end with a \n. I have to remove using strip.
   Headers.append(eachHeader.get_text().strip())


header1= Headers[0]     
header2= Headers[1]
header3= Headers[2]
header4= Headers[3]
header5= Headers[4]
header6= Headers[5]
header7= Headers[6]
header8= Headers[7]
header9= Headers[8]








#https://stackoverflow.com/questions/54630105/weird-characters-when-webscraping-using-beautiful-soup
#https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row/3348664

#Creating the Excel document
with open('webParser.csv','w', newline='', encoding="utf-8-sig") as csv_file:

    #Creating the writer object. 
    csv_writer = writer(csv_file,lineterminator = '\n')
    headers = [header1, header2,header3, header4, header5, header6, header7, header8, header9]

    #Writing to the excel file
    csv_writer.writerow(headers)


    



#Getting the columns
    tag = soup.find(class_='wikitable sortable').find_all("tr")
    for eachTableRow in tag:
        result = eachTableRow.find_all("td")
        List = []
        for tableData in result:
            List.append(tableData.get_text())


        #There are nine table rows data.
        rank =''
        City=''
        State=''
        estimate=''
        Census=''
        Change=''
        a2016_land_area=''
        a2016_population_density=''
        Location=''

        #If the len of list is zero or the first index of list is empty, the data wasn't found and go to the next iteration.
        for i in range(len(List)):
            if (len(List)) == 0 or List[i] == '':
                continue
            else:
                if i == 0:
                    rank = List[i].strip()
                elif i == 1:
                    City = List[i].strip()
                elif i ==  2:
                    State = List[i].strip()
                elif i ==  3:
                    estimate = List[i].strip()
                elif i ==  4:
                    Census = List[i].strip()
                elif i ==  5:
                    Change = List[i].strip()
                elif i ==  6:
                    a2016_land_area = List[i].strip()
                elif i == 7:
                    a2016_land_area = a2016_land_area + ' ' + List[i].strip()
                elif i ==  8:
                    a2016_population_density = List[i].strip()
                elif i == 9:
                    a2016_population_density = a2016_population_density + ' ' + List[i].strip()
                elif i ==  10:
                    Location = List[i].strip()
                else:
                   continue
                  
        #If the first field is blank, that means the first information was not found.        
        if rank != '':
           csv_writer.writerow([rank,City,State,estimate,Census,Change,a2016_land_area,a2016_population_density,Location])

