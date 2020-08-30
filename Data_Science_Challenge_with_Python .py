#!/usr/bin/env python
# coding: utf-8

# In[1]:


dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print (dic4)


# In[2]:


def calculateSum(n):
	if n==1:
		return 0
	fibo=[0]*(n+1)
	fibo[1]=1
    # Initialisasi hasil ke dalam variabel sm
	sm = fibo[0]+fibo[1]
    # Tambahkan suku-suku berikutnya
	for i in range(2,n+1):
		fibo[i]=fibo[i-1]+ fibo[i-2]
		sm+=fibo[i]
	return sm
# Evaluasi hasil deret untuk n = 7    
print(calculateSum(7))


# In[ ]:




