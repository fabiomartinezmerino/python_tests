"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following
line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person 
who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
list_of_emails = []
counter = 0
file_handler = open("/Users/Alicia/Documents/mbox-short.txt","r")
for line in file_handler:
    buffer = line.strip()
    if buffer.startswith("From") and not buffer.startswith("From:"):
        counter += 1
        new_item = (buffer.split())[1]
        #if new_item not in list_of_emails:
        list_of_emails.append(new_item)
for email in list_of_emails:
    print(email.strip())
print("There were {0} lines in the file with From as the first word".format(len(list_of_emails)))
