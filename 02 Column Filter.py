''' This code reads in a row at a time of the CSV file. If the row has an empty first cell then we finish the program.
We write out each row to our 'clean file', but only from columns 2 and 5. This code thus filters out unwanted columns'''

# File that contains my raw data
file = open("RawData.csv","r")

# File that I will write my processed data to
file2 = open("CleanedData02.csv","w")

# Loop until the entry is blank
while True:
    # Read a line of data from CSV file
    readdata = file.readline()

    # Split the file into an array based on comma seperator 
    DataList = readdata.split(',')

    # Break from while loop when we hit an empty line
    if (DataList[0] == ""):
        break
    
    # Write just the 2nd and 5th columns to the cleaned file
    file2.write (str( DataList[1] + "," + DataList[4] ))
        


print ("Cleaning Complete. Filtered out Columns.")




file.close()
file2.close()

