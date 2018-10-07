#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:20:42 2018
@author: Alicia

input: a list of arrays
outuput:a list of lists each one of them will contain the number of times user has bought
in all months and user id


A website named "All for Five" sells many products to registered clients
that cost all the same (5 dollars, the price is not relevant).
Every user receives an alphanumeric id code, like D085.
The page tracks all the purchases, that the clients do.
For each purchase of a certain client, his/her id user will be registered once.

You will be given an uncertain number of arrays that contains strings 
(the id code users). Each array will represent the purchases that the users do in a month.
You should find the total number of purchases of the users that have bought
in all the given months (the clients that their id code are present in all the arrays).
e.g.:

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
The result will be:

'A042'---> 5 times
'A025'---> 3 times
'B004'---> 3 times


"""
def intersection_of_lists(list1,list2):
    
    return [item for item in list1 if item in list2]

def cleanUID(*args):
    """
    input: args is a list of lists. for each item in each list we have to check if it is present in every other lists.
    if it is so it is a valid UID - purchase to compute. if not we discard it
    output: a list with every UID present in every list as many times repeated as in the original *args
    """
    
    
    my_args = list(args)
    my_intersection_list = my_args[0]
    
    counter = 0
    
    for list_item in my_args:
        
       
        print("---Preparando las intersecciones---")
        print("My_intersection_list antes del and: {0}".format(my_intersection_list))
        print("list_item antes del and: {0}".format(list_item))
        
        my_intersection_list = intersection_of_lists(my_intersection_list,list_item)
        
        print("my_intersection_list después del and: {0}".format(my_intersection_list))
        print("counter: {0}".format(counter))
        
        if list_item == (my_intersection_list) and counter > 0:
        
            print("No hay nada")
            return [[]]
       
        
        counter+=1
    
    print("Lista de interseccion: {}".format(my_intersection_list))
    """
    now my_intersection_list contains UID's present in all lists
    """
    curated_list_of_lists = [[]]
    
    for list_item in my_args:
        list_item_copied=list_item.copy()
        curated_list_of_lists.append(list_item_copied)
        for item_UID in list_item:
            print("Testeando: {}".format(item_UID))
            if item_UID in my_intersection_list:
                print("esta en todas las listas")
                
            else:
                print("lo elimino")
                list_item_copied.remove(item_UID)
    
    print("Dentro de limpieza la lista de listas queda asi: {0}".format(args))
    return curated_list_of_lists

def computeUID(args):    
    
    
    # iterate throughout all the lists provided and keep track of each time a user id comes up
    # we will use a dictionary with key userID and value the number of times it appears

    user_activity_dict = {}
    number_of_times_dict = {}
    buffer_list=[]
    
    print("Dentro de computo la lista de listas queda asi: {0}".format(args))


            
    for list_item in args:
        for item_of_list in list_item:
            if item_of_list in user_activity_dict:
                user_activity_dict[item_of_list]+=1
            else:
                user_activity_dict[item_of_list]=1
    
   
    
    #now for each user we strore data (times he/she has bought and item) in a list with two items: times and id.
    #then all of this lists are gathered into another list
    
    list_of_times_uid = [[times,uid] for uid,times in user_activity_dict.items()]
    
    print("Escribimos lista de listas [numero de veces, UID]: {0}".format(list_of_times_uid))
    
    #now we create a dictionary whose keys will be number of times and value a list containing all the user id's
    #that have appeared that number of times
    
    for times_uid in list_of_times_uid:
        
        print("Cogemos la pareja: {0}".format(times_uid))
        
        
        if times_uid[0] in number_of_times_dict:#this is number of times
            print("el numero de veces {0} existe - añadimos el uid {1} al diccionario".format(times_uid[0],times_uid[1]))
            
            (number_of_times_dict[times_uid[0]]).append(times_uid[1])#if the number of times already exists we add to the
            #list of user that have appeared that number of times a new user, that has appeared that number of times as well
            
            print("El diccionario esta asi: {0}".format(number_of_times_dict))
        else:
    
            print("el numero de veces {0} no existe - añadimos clave y añadimos el uid {1} al diccionario".format(times_uid[0],times_uid[1]))
            
            buffer_list = []
            buffer_list.append(times_uid[1])
            number_of_times_dict[times_uid[0]] = buffer_list#if the number of times doesn't exists we create a new
            #entry in the dictionary whose value is a dict containing the user id that appears this number of times
            
            print("El diccionario esta asi: {0}".format(number_of_times_dict))
    
    
    #now we turn number_of_times_dict dictionary into a list of lists: each list will contain a first item indicating number
    #of times and a second list with all uid appearing that number of times
    
    list_of_lists_timesUID = [[times,sorted(list_of_UID)] for times, list_of_UID in sorted(number_of_times_dict.items(),reverse=True)]
    

    
    return list_of_lists_timesUID






def id_best_users(*args):
    #first we drop user_id that doesn't appear in all lists
    
    
    #then we call de function that does all the computational job
    return computeUID(cleanUID(*args))
    
    
    


a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'B004', 'A025', 'A042', 'C025', 'B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a4 = ['A042', 'A025', 'B004']
#print (computeUID(cleanUID(a1,a2,a3)))

print (id_best_users(a1,a2,a3,a4))

"""
test.describe("Basic Tests")

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'A025', 'B004']
test.assert_equals(id_best_users(a1, a2, a3), [[5, ['A042']], [3, ['A025', 'B004']]])

a1 = ['A043', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B003', 'A042', 'A027', 'A044']
a3 = ['A041', 'A026', 'B005']
test.assert_equals(id_best_users(a1, a2, a3),  [])

a1 = ['A042', 'B004', 'A025', 'A042', 'C025']
a2 = ['B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a3 = ['A042', 'B004', 'A025', 'A042', 'C025', 'B009', 'B040', 'B004', 'A042', 'A025', 'A042']
a4 = ['A042', 'A025', 'B004']
test.assert_equals(id_best_users(a1, a2, a3, a4), [[9, ['A042']], [5, ['A025', 'B004']]])
"""
