#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import csv
conn = sqlite3.connect('megapharma.db')
print("Megapharma Database Created successfully")


# In[10]:


conn = sqlite3.connect('Company1.db')
cursor = conn.cursor()
cursor.execute('SELECT SQLITE_VERSION()')
data = cursor.fetchone()[0]
print(f"SQLite version: {data}")


# In[11]:


cursor.execute('CREATE TABLE Hospital(Hospital_Id INT NOT NULL UNIQUE,Hospital_Name TEXT NOT NULL,Bed_Count INT NOT NULL)')
print("Hospital Database")


# In[33]:


import csv
conn = sqlite3.connect('Company1.db')
cursor = conn.cursor()
bfile = open("C:\\Users\brenda.onyango\Downloads\\Hospital.csv",'r')
rows = csv.reader(bfile)
next(rows, None)
cursor.executemany("INSERT INTO Hospital VALUES(?,?,?)", rows)
cursor.execute("SELECT * FROM Hospital")
company1 = cursor.fetchall()
for company1 in company1: 
    print(company1)
conn.commit()


# In[ ]:




