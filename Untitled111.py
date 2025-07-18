#!/usr/bin/env python
# coding: utf-8

# In[1]:


IFSC_CODE = "HDFC0004567"
print(IFSC_CODE[6:])


# In[2]:


PAN = input("enter the PAN : ")

if(len(PAN) ==10):
    if(PAN[0:5].isalpha() and PAN[5:9].isdigit() and PAN[-1].isalpha()):
        print("valid")
    else:
        print("not valid")

else:
    print("length of PAN should be 10 ")


# In[3]:


name = input("enter your name : ")
name.title()


# In[6]:


Acc_No = input("enter the  acc no : ")
Acc_No.replace(Acc_No[:8],"XXXXXXXX")


# In[9]:


name = input("Enter your name : ")
phone = input("Enter your mobile : ")

Customer_id = name[0:3].upper() + phone[-4:]
print("your customer_id is : ",Customer_id)


# In[16]:


email = input("enter your email : ")
if("icicibank.com" in email):
        print("Belongs to icici bank")
else:
    print("Other Domain")


# In[17]:


txn_id = "TXN202506"
rev = ""
for i in txn_id:
    rev = i + rev
print(rev)


# In[34]:


Feedback = "Service was slow and response time was high"
count = 0
for i in Feedback:
    count = count + 1
print(count)


# In[30]:


len(Feedback)


# In[36]:


Feedback = "Service was slow and response time was high"
count = 0
for i in Feedback:
    count = count + 1
    if i.isspace():
        count = count-1
print(count)


# In[29]:


li = [1,2,3,4,5,6,7,8,9,10]
[i**2 for i in li if i%2 != 0 ]


# In[25]:


li = ["himanshu","chaman","abhijeet","abhishek","superman"]
[i for i in li if not i.startswith("ab")]


# In[20]:


basket = ["apple","guava","cherry","banana"]
my_fruits = ["apple","Kiwi","grapes","banana"]

result = [i for i in my_fruits if i in basket and i.startswith("a")]
print(result)


# In[13]:


L1 = [1,2,3,4]
L2 = [5,6,7,8]
L1.extend(L2)
print(L1)


# In[16]:


L1 = [1,2,3,4]
L2 = [5,6,7,8]
cartesian_product = [(x,y) for x in L1 for y in L2]
print(cartesian_product)


# In[21]:


basket = ["apple","guava","cherry","banana"]
my_fruits = ["apple","Kiwi","grapes","banana"]

for i in my_fruits:
    if i in basket and i.startswith("a"):
        print(i)


# In[27]:


L1 = [1,2,3,4]
L2 = [5,6,7,8]

for x in L1:
    for y in L2:
        print((x,y) , end=" ")


# In[28]:





# In[ ]:




