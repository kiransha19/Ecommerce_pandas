"""
pandas project 


To perform data analysis, I have mentioned 15 questions that we are going to solve one by one. Questions are as follows.
1. Display Top 10 Rows of The Dataset
2. Check Last 10 Rows of The Dataset
3. Check Datatype of Each Column
4. Check null values in the dataset
5. How many rows and columns are there in our Dataset? 
6. Highest and Lowest Purchase Prices.
7. Average Purchase Price
8. How many people have French 'fr' as their Language?
9. Job Title Contains Engineer
10. Find The Email of the person with the following IP Address: 132.207.160.22
11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
12. Find the email of the person with the following Credit Card Number: 4664825258997302
13. How many people purchase during the AM and how many people purchase during PM?
14. How many people have a credit card that expires in 2020?
15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 
"""

import pandas as pd

data = pd.read_csv(r"C:\Users\KIRAN BABU\OneDrive\Desktop\pandas project\Ecommerce Purchases.csv")


#1.1. Display Top 10 Rows of The Dataset

data.head(10)

#2.2. Check Last 10 Rows of The Dataset

data.tail(10)

#3. Check Datatype of Each Column

data.dtypes

#4. Check null values in the dataset

data.isnull().sum()

#5. How many rows and columns are there in our Dataset? 

data.info()
data.columns
len(data.columns)


#6. Highest and Lowest Purchase Prices.

data.columns #see the name of the prize column 
data['Purchase Price'].max()
data['Purchase Price'].min()


#7.Average Purchase Price

data['Purchase Price'].mean()

#8. How many people have French 'fr' as their Language?

data.columns
len(data[data['Language']=='fr'])
data[data['Language']=='fr']


#9. Job Title Contains Engineer
data.columns
data[data['Job'].str.contains('enginerr',case=False)]
data[data['Job']=='engnieer']

#10. Find The Email of the person with the following IP Address: 132.207.160.22
data.columns
data[data['IP Address']=='132.207.160.22']['Email']

#11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
data.columns

len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)])

#12. Find the email of the person with the following Credit Card Number: 4664825258997302

data.columns
data[data['Credit Card']== '4664825258997302']['Email']

#13. How many people purchase during the AM and how many people purchase during PM?

data.columns
data['AM or PM'].value_counts()                     # new point


#14. How many people have a credit card that expires in 2020?

data.columns
data['CC Exp Date']
len(data[data['CC Exp Date'].apply(lambda x:x[4:]=='20')])


#15. What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...) 
data.columns
data['Email']
top = data['Email'].apply(lambda x:x.split('@')[1]).value_counts


