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

# Write another function that prints out all the melon orders that delivered over 10 melons.
def sales_reports_2(log_file):
    for line in log_file:
        line = line.rstrip()
        if line.endswith("10 melons"):
            print(line)
            