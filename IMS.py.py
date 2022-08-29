#!/usr/bin/env python
# coding: utf-8

# In[2]:


dct = { 'ME101' : {'name': 'coca cola'     , 'description': 'energy drink' ,  'supplier': 'cola company'       , 'amount': 50 , 'qty on hand': 60   , 'customer orders' : 38 , 'qty available': 22 } ,
        'ME102' : {'name': 'mountain dew'  , 'description': 'energy drink'  , 'supplier': 'pepsiCo company'    , 'amount': 80 , 'qty on hand': 46   , 'customer orders' : 25 , 'qty available': 21 } ,
        'ME103' : {'name': '7up'           , 'description': 'energy drink'  , 'supplier': '7 up company'       , 'amount': 70,  'qty on hand': 71   , 'customer orders' : 59 , 'qty available': 12 } ,
        'ME104' : {'name': 'pepsi'         , 'description': 'energy drink'  , 'supplier': 'pepsi company'      , 'amount': 40 , 'qty on hand': 32   , 'customer orders' : 26 , 'qty available': 6  } ,
        'ME105' : {'name': 'maaza'         , 'description': 'energy drink'  , 'supplier': 'maa company'        , 'amount': 20 , 'qty on hand': 55   , 'customer orders' : 34 , 'qty available': 21 } ,
        'ME106' : {'name': 'bovonto'       , 'description': 'energy drink'  , 'supplier': 'bovonto company'    , 'amount': 90 , 'qty on hand': 110  , 'customer orders' : 82 , 'qty available': 28 } ,
        'ME107' : {'name': 'milk'          , 'description': 'energy drink'  , 'supplier': 'arokya company'     , 'amount': 30 , 'qty on hand': 220  , 'customer orders' : 114, 'qty available': 106} ,
        'ME108' : {'name': 'sprite'        , 'description': 'energy drink'  , 'supplier': 'sprite company'     , 'amount': 110, 'qty on hand': 105  , 'customer orders' : 90 , 'qty available': 9  } ,
        'ME109' : {'name': 'red bull'      , 'description': 'energy drink'  , 'supplier': 'red bull company'   , 'amount': 150, 'qty on hand': 24   , 'customer orders' : 15 , 'qty available': 9  } ,
        'ME110' : {'name': 'fizz'          , 'description': 'energy drink'  , 'supplier': 'apple fizz company' , 'amount': 60 , 'qty on hand': 75   , 'customer orders' : 66 , 'qty available': 9  } , }


# In[3]:


dct


# ### 1. Product Details Based on their ID :

# In[4]:


product_id = (input("Enter the product id :"))
print('-'*35)
print('Name            :' , dct[product_id]['name'])
print('Description     :' , dct[product_id]['description'])
print('Supplier        :' , dct[product_id]['supplier'])
print('Amount          :' , dct[product_id]['amount'])
print('Qty on hand     :' , dct[product_id]['qty on hand'])
print('Customer orders :' , dct[product_id]['customer orders'])
print('Qty available   :' , dct[product_id]['qty available'])
print('-'*35)


# ### 2.Product Details based on their Name :

# In[5]:


name = input("Enter the name :")
for key in dct.keys():
    if(dct[key]['name'].lower() == name.lower()):
        print('-'*35)
        print('product_id      :' , key)
        print('Name            :' , dct[key]['name'])
        print('Description     :' , dct[key]['description'])
        print('Supplier        :' , dct[key]['supplier'])
        print('Amount          :' , dct[key]['amount'])
        print('Qty on hand     :' , dct[key]['qty on hand'])
        print('Customer orders :' , dct[key]['customer orders'])
        print('Qty available   :' , dct[key]['qty available'])
        print('-'*35)


# ### 3. Finding Costliest Product :

# In[6]:


price = []
for key in dct.keys():
    price.append(dct[key]['amount'])
    
cost = max(price)


for key in dct.keys():
    if (dct[key]['amount'] == cost):
        print(dct[key]['name'])


# ### 4.Finding Cheapest Product :

# In[7]:


price = []
for key in dct.keys():
    price.append(dct[key]['amount'])
    
cost = min(price)


for key in dct.keys():
    if (dct[key]['amount'] == cost):
        print(dct[key]['name'])


# In[ ]:





# In[ ]:




