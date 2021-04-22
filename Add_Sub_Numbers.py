#!/usr/bin/env python
# coding: utf-8

# In[3]:


terminate = False

while not terminate:
    number1 = input('Enter a number:')
    number1 = int(number1)
    number2 = input('Enter another number:')
    number2 = int(number2)
    
    while True:
        operation = input("Please enter add/sub or quit to exit:")
        if operation == 'quit':
            terminate = True
            break
        
        if operation not in ["add","sub"]:
            print("Unknown Operation!")
            continue
        
        if operation == "add":
            print("Result is : ", number1 + number2)
            break
        
        if operation == "sub":
            print("Result is : ", number1 -number2)
            break


# In[ ]:




