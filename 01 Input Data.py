# File that contains my raw data
file = open("InputFile.csv","r")

# File that I will write my processed data to
file2 = open("OutputFile.csv","w")

# Read all data from the Input File and store in myData variable
myData = file.read()

print(myData)

# Write data to the output file 
result = file2.write(myData)

# Close the files
file.close()
file2.close()
