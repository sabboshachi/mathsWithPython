#!/usr/bin/env python
# coding: utf-8

# In[ ]:


year = input("Enter a Year:")
year = int(year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print ( year, " is a Leap Year")
        else:
            print ( year, " isn't a Leap Year")
    else:
        print ( year, " is a Leap Year")
else:
    print( year, " isn't a Leap Year")

