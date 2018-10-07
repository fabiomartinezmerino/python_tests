#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:34:05 2018

@author: Alicia


def majority(arr):
  #your code here!
  
  intermediate_map = {}
  
  print ("Lista al comienzo: " + str(arr))
  
  for letter_in_arr in arr:
      
      #Identify letter and count occurences - update a map with that info
  
      print("La letra es: %s y ocurre %d veces" % \
            (letter_in_arr, arr.count(letter_in_arr)))




      intermediate_map.update({letter_in_arr:arr.count(letter_in_arr)})
      

      
      print ("El estado del mapa es: " + str(intermediate_map))
      


      #Once we have dealt with an item we remove it from initial array
      
      print("Quitamos %s " % (letter_in_arr))
      
      for i in range (0,arr.count(letter_in_arr)):
          arr.remove(letter_in_arr)
      
      #We print array status y de nuevo estado del mapa
      
      print("El estado de la lista despues de la remocion: " + str(arr))
      print("El estado del mapa despues de la remoción: " \
            + str(intermediate_map))
      print("Items despues de la remocion: " + \
      str("*".join(str(x) for x in arr)))
        
  return intermediate_map


print(majority(["A","B","A","A","B","C","D"]))

"""

def majority(arr):

    work_map = {}
    print(work_map)
    
    for item_in_arr in arr:
        work_map.update({item_in_arr: arr.count(item_in_arr)})
    
    list_of_sorted_values = sorted(work_map.values(),reverse=True)    
    
    print("El mapa en este punto se parece a esto: " + str(work_map))
    print("Los valores en orden son estos: " + str(list_of_sorted_values))

    if len(list_of_sorted_values) > 1 \
    and list_of_sorted_values[0]==list_of_sorted_values[1]:
        return None
    for letter, counter in work_map.items():
        if counter == list_of_sorted_values[0]:
            return letter
        
    
print(majority(["A"]))    
        
        
        
        
        