#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Q1
# an exception in python helps us to raise a type of error in the programme.
# the main difference between exception and syntax error is that exceptions are caused due to some fault in the logic
#of the code whereas syntax error occurs due to fault in language of the command given to the python interpretor.


# In[2]:


#Q2
# the programme stops running at the point where the error is found.
print(3-1)
print(a+b)
print(5+6)


# In[4]:


#Q3
# the try-except block is used to handle exceptions in python.
print(3-1)
try:
    print(a+b)
except Exception as e:
    print(e)
print(5+6)


# In[10]:


#Q4

# try and else: else statement in executed in a try-except block after the try block is successfully executed.
try:
    print(5+6)
except Exception as e:
    print(e)
else:
    print("try executed without error.")
    
# finally: this statement is executed irrespective of the execution of try-except block.
try:
    print(a+b)
except Exception as e:
    print(e)
finally:
    print("doesn't matter.")
    
# raise: it is used to create custom exceptions.
class rno1(Exception):
    def __init__(self,msg):
        self.msg=msg

def rno(no):
    if no<0:
        raise rno1("no. is negative.")
        
try:
    no=int(input("Enter a no.: "))
    rno(no)
except rno1 as e:
    print(e)


# In[12]:


#Q5
#Q6
# they are used to handle exceptions created by the programmers according to their needs.
# we need them because there are times when we don't require certain data but as it is not handled by the exception class so we have to create an exception of our own.
class cuseg(Exception):
    def __init__(self,msg):
        self.msg=msg
def exe(a):
    if (a>100):
        raise cuseg("too big.")

try:
    no=int(input("Enter a no.: "))
    exe(no)
except cuseg as c:
    print(c)


# In[ ]:




