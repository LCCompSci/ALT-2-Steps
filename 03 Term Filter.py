''' This code also filters out unwanted columns from our files but it also only prints out
the key words we've identified in a specific column (i.e. Donegal in column 1) '''

# File that contains my raw data
file = open("RawData.csv","r")

# File that I will write my processed data to
file2 = open("CleanedData03.csv","w")

# Write some headings to the CSV file
file2.write("Town Name"+","+"Phone Numbers"+"\n")


# Loop until the entry is blank
while True:
    
    # Read a line of data from CSV file
    readdata = file.readline()

    # Split the file into an array based on comma seperator 
    ResultList = readdata.split(',')

    # Break from while loop when we hit an empty line
    if (ResultList[0] == ""):
        break
    
    # We search for 'Donegal' in the first column
    if(ResultList[0]=="Donegal"):
        print("Found Donegal!")
        # Write to our clean file the second and fifth column if the search result is found
        file2.write( str(ResultList[1] + "," + ResultList[4]) )
    

# Close the files
file.close()
file2.close()
