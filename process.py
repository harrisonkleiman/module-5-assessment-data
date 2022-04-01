# Allows us to access data from the "um-server-01.txt" file
log_file = open("um-server-01.txt")

# Prints all the lines that occur on Monday, 5/19/2014
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

 # Calls the function
sales_reports(log_file)
