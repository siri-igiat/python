#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def isprime(n):
    status=0
    for i in range(2,n//2):
        if n%i==0:
            status=1
    if status==0:
         print("n is prime")
    else:
        print("n is not prime")
n=int(input("enter a number"))
isprime(n)

