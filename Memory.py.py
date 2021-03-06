#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import csv
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
print("Python Code resides in Memory")


# In[4]:


cursor.execute('CREATE TABLE Company(ID INT NOT NULL,NAME TEXT NOT NULL, AGE INT NOT NULL,SALARY REAL)')
print("Company Data")


# In[5]:


conn = sqlite3.connect('Company.db')
cursor = conn.cursor()
cursor.execute('SELECT SQLITE_VERSION()')
data = cursor.fetchone()[0]
print(f"SQLite version: {data}")


# In[7]:


cursor.execute('CREATE TABLE Hospital(Hospital_Id INT NOT NULL,Hospital_Name TEXT NOT NULL,Bed_Count INT NOT NULL)')
print("Hospital Database")


# In[21]:


cursor.execute('CREATE TABLE Doctors(Doctor_Id INT NOT NULL,Doctor_Name TEXT NOT NULL,Hospital_Id INT NOT NULL,Date_Joined REAL NOT NULL,Specialty TEXT NOT NULL,Salary REAL NOT NULL,Experience INT NOT NULL)')
print("Doctors Database")


# In[2]:


conn = sqlite3.connect('Company.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Hospital")
rows = cursor.fetchall()


# In[ ]:




