#!/usr/bin/env python
# coding: utf-8

# # functions for titanic.csv practice

# In[1]:


# Importing the Libraries
import csv


# ### opening the file 

# In[26]:


# A function that gets the relative path of a CSV file from the user and returns a list where each item represents a line in the file
#user_mistakes can be given to handle some common mistakes made by the user 
def my_csv_reader ( encoding = 'UTF-8' , user_mistakes = [] ) :
    print ('\n','welcome to my_file_reader.','\n','please enter the files name and press enter','\n')
    file_name = input ()
    records = []
    while True:
        try :
            if file_name.lower().strip() in user_mistakes :
                if file_name != user_mistakes[0]:
                    print (f'I think you mean {user_mistakes[0]} file ')
                file_name = user_mistakes[0]       
            with open (file_name , 'r' , encoding = encoding) as file:
                file_reader = csv.reader (file)
                for line in file_reader:
                    records.append(line)
            break
        except FileNotFoundError:
            file_name = input (f'sorry {file_name} could not be found please make sure your file location is correct and you entered the correct name: ')
        
    return records


# ### checking numbers entered by the user

# In[3]:


## this function checks is the number user inputs is integer and also in the range we want and returns it
## we can also costumise the massege it shows
def number_check (range , massege = '__default__' ) :
    if massege == '__default__' :
        massege = f'please enter a number in range (0,{range})'
    while True :
        number =input(massege)
        try :
            number = int(number)
            if number > range or number <0:
                print (f'{number} is not in range, try a number between (0 ,{range})')
            else :
                break
        except ValueError:
            print (f'{number} is not a number, please enter a number')
    return number


# ### check if item exists

# In[4]:


## this function makes sure the item user inputs is in the list we want 
## it is not sensitive to upper or lower and will ignore spaces before and after the word user inputs 
def item_check ( list , massege = '__default__' ):
    if massege == '__default__' :
        massege = ('\n','please enter a name from list above')
    # first make a copy of our list and make sure they are all lower and strip
    list_copy = []
    for i in list :
        i = i.lower().strip()
        list_copy.append (i)
    # now get an item name from user and check if we can find a match in our coppy, we wont break until we get the right answer 
    while True :
                #print (list)
                item = (input (massege)).lower().strip()
                if item in list_copy :
                    #if its not in the original list means it either has space or is not the same in case of lower or upper, here we fix that 
                    if item not in list :
                        item_position = list_copy.index(item)
                        item = list [item_position]
                    break
                else :
                    print (f'i cant find this {item} in the list, please try again')
    return item


# ### get features from the file 

# In[36]:


def get_heading (file):
    heading = file [0]
    file = file[1:]
    return heading , file


# In[37]:


## this function gets a list where item[0] is the heading then asks the user witch ones should be extracted and puts them in a dictionary 
def get_features (heading , file):
    len_heading = len(heading)
    print ('how many different features you want?')
    number = number_check (len_heading)
    features = {}
    if number != 0:
        for i in range (number):
            feature_name = item_check(heading)
            feature_items = []
            feature_position = heading.index(feature_name)
            for j in file : 
                        feature_items.append (j[feature_position])
            features[feature_name] = feature_items
            
    return features


# ## handling features

# #### display

# In[57]:


#a function to display any feature from given dictionary
def display_features (dic):
    dic_keys = list(dic.keys())
    feature_name = item_check (dic_keys)
    return dic[feature_name]


# In[7]:


def value_count (list):
    counts = {}
    for item in list :
        if item in counts.keys():
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


# In[62]:


def value_count2 (list , item):
    counts = 0
    for i in list :
        if i == item:
            counts += 1
    return counts


# In[63]:


def value_count3 (list , item):
    counts = 0
    for i in list :
        if i > item:
            counts += 1
    return counts


# In[64]:


def value_count4 (list , item):
    counts = 0
    for i in list :
        if i < item:
            counts += 1
    return counts


# ## menu

# In[71]:


def menu (mistakes = []):
    text_ = """
hello welcome to csv review 

   this application is for opening and checking information of any csv file you have
"""
    text =""" 
   please choose one of these options below (simply put in the number and enter)

       [0]Exit  
       [1]Open csv file
              """
    
    print (text_)
    while True:
        print (text)
        chosen = number_check(1)
        if chosen == 0 :
            print ('Bye Bye')
            break
        elif chosen == 1 :
            #read csv 
            csv_file = my_csv_reader(user_mistakes = mistakes)
            text_1 = 'Done!, here are the headings'
            print ('\n',text_1,'\n')
            heading , file = get_heading (csv_file)
            print (heading)
            chosen_features = get_features (heading , file)
            while True:
                        text_2 = '''
Done!, now choose one of the options below (simply put in the number and enter)
                
                
     [0]Exit 
     [1]Display 
     [2]Count 
'''
                        print (text_2)
                        chosen_2 = number_check(2)
                        if chosen_2 == 0:
                            break
                        elif chosen_2 == 1:
                            #display
                            text_3 = '''
choose one of the options below (simply put in the number and enter)
     [0]Exit 
     [1]Display all
     [2]Choose one and display
'''
                            print (text_3)
                            chosen_3 = number_check(2)
                            if chosen_3 == 0:
                                break
                            if chosen_3 == 1:
                                for key,value in chosen_features.items() :
                                    print ('\n', f'here are all the values for {key}' ,'\n')
                                    print (value,'\n')
                            if chosen_3 == 2:
                                value_chosen = display_features (chosen_features)
                                print (value_chosen)
                        elif chosen_2 == 2:
                            #count
                            text_4 = '''
choose one of the options below (simply put in the number and enter)
     [0]Exit 
     [1]Count numerical values (all >,<,= a number) 
     [2]Count words (gender,name,profesion)
'''
                            print (text_4)
                            chosen_4 = number_check(2)
                            
                            if chosen_4 == 0 :
                                break
                            elif chosen_4 == 1:
                                while True:
                                    value_chosen1 = display_features (chosen_features)
                                    try :
                                        value_number = []
                                        for item in value_chosen1 :
                                            if item == '':
                                                item = 0
                                            value_number.append(float(item)) 
                                        break
                                    except :
                                        print ('this is not a numerical feature')
                                text_5 = '''
choose one of the options below (simply put in the number and enter)
     [0]Exit 
     [1]Count numerical values that are equal to something (=)
     [2]Count numerical values that are greater than something (>)
     [3]Count numerical values that are lesser than something (<)
'''
                                print (text_5)
                                chosen_5 = number_check(2) 
                                if chosen_5 == 0 :
                                    break
                                elif chosen_5 == 1:
                                    number_entered = number_check (10000000000 , massege = 'please enter the number u wanna find')
                                    answer = value_count2 (value_number , number_entered)
                                    print ('\n',f'there are total of {answer} results found equal to {number_entered}', '\n')
                                elif chosen_5 == 2:
                                    number_entered = number_check (10000000000 , massege = 'please enter the number u want values to be greater than')
                                    answer = value_count3 (value_number , number_entered)
                                    print ('\n',f'there are total of {answer} results found greater than {number_entered}', '\n')
                                elif chosen_5 == 3:
                                    number_entered = number_check (10000000000 , massege = 'please enter the number u want values to be lesser than')
                                    answer = value_count4 (value_number , number_entered)
                                    print ('\n',f'there are total of {answer} results found lesser than {number_entered}', '\n')
                            elif chosen_4 == 2:
                                value_chosen1 = display_features (chosen_features)
                                word_entered = input ('please enter the word you are trying to count')
                                answer = value_count2 (value_chosen1 , word_entered)
                                print ('\n',f'there are total of {answer},{word_entered} results found', '\n')


# In[70]:


if __name__ == '__main__':
    #### some common mistakes for titanic.csv
    users_mistakes_titanic = ['titanic.csv','titanic','titanik','titanik.csv','titaniccsv','titanicsv','titani.csv','titanek.csv']
    menu(users_mistakes_titanic)

