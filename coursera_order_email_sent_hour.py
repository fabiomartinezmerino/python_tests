"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

"""

hour_dict = {}
hour = ""

file_handle = open("mbox-short.txt","r")

for file_line in file_handle:
    if file_line.startswith("From") and not file_line.startswith("From:"):
        location_of_colon = file_line.index(":")
        hour = file_line[location_of_colon-2:location_of_colon]
        hour_dict[hour] = hour_dict.get(hour,0)+1
#print(hour_dict)

list_of_tuples = [(hour,number) for hour,number in sorted(hour_dict.items())]

for my_tuple in list_of_tuples:
    print(str(my_tuple[0]) + " " + str(my_tuple[1]))
        