
#This is a code wars exercise. It deals with the problem of finding out maximum length substring 
#in alphabetical order


import timeit

s="abcdeffffdefghcdefhghgiiiiiiiiggggggiik"
index = 0
max_string=s[0]
buffer_string=""


#let's time this 



#get initial time

start_time = timeit.default_timer()

while index < len(s)-1:
    
    if s[index]<=s[index+1]:

        max_string+=s[index+1]

    else:

        if len(max_string) > len(buffer_string):
            buffer_string = max_string
        max_string = s[index+1]

    index+=1


if len(max_string) <= len(buffer_string):

    print("Longest substring in alphabetical order is: " + buffer_string)

else:

    print("Longest substring in alphabetical order is: " + max_string)


#get final time and substract

print(timeit.default_timer() - start_time)


    