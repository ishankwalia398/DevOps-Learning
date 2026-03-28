f = open('data.txt', 'r+')  # Open a file in write mode

data = f.read()  # Read the content of the file
print(data)

f.write('\n This is a New Line \n')  # Write a line to the file

f.close()  # Close the file
