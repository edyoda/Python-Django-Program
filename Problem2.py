#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Code for Algorithm to identify start point
def find_starting_location(travel_dict):
    start_points = travel_dict.keys()
    stop_points  = travel_dict.values()
    
    #Only one start point expected. Getting first value
    return (set(start_points) - set(stop_points)).pop()
   
#Code for identifying stop point given a start point    
def find_stop_location_from_start_location(start_location,travel_dict):
    journey = []
    
    while True:
        journey.append(start_location)
        if start_location in travel_dict:
            stop_location = travel_dict[start_location]
            start_location = stop_location
        else:
            return journey

def travel_sequence(travel_dict):
    #find the starting point
    start_location = find_starting_location(travel_dict)
    
    #find the stops & put them in list
    journey = find_stop_location_from_start_location(start_location, travel_dict)
    
    iternary = []
    
    for location_id in range(len(journey)):
        if location_id + 1 < len(journey):
            iternary.append(journey[location_id]+'->'+journey[location_id+1])
    
    return iternary
        
travel_dict = {"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}    
iternary = travel_sequence(travel_dict)

for start_stop in iternary:
    print (start_stop,end=', ')


# In[ ]:




