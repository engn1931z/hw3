# Homework 3 Template Code
#
# This file will begin by creating a string called userGuideText using the pdfminer library.
# This string userGuideText will be saved into a separate file userGuideText.txt to speed up your subsequent testing.
# 
# Your assignment is to programmatically analyze the userGuideText string using regular expressions to find all the unique SCPI Query Commands.
# Once you find all the query commands, you should pass them as a single long queryString to pass to our virtual E3631A system.
# queryString should be a single string that has all the queries concatenated (joined) together with the appropriate terminators.
#
# When you have a final answer, you can submit your assignment to the autograder by running the submit.py script 

##################################################################
### HELPER CODE TO IMPORT PDFMINER LIBRARY AND PRODUCE TEXT STRING
##################################################################
import pdfminerToText
import re
import requests

try: 
	with open('userGuideText.txt','r') as f1: userGuideText=f1.read()
except:
	userGuideText=pdfminerToText.convert("E3631-90002.pdf")
	with open('userGuideText.txt','wb') as f2: f2.write(userGuideText)

##################################################################
### YOUR CODE TO FIND & CONCATENATE ALL SCPI QUERIES GOES HERE
##################################################################

email= "YOUR_EMAIL_GOES_HERE@brown.edu" #REPLACE THIS




queryString='???' # UPDATE THIS LINE TO INCLUDE YOUR CONCATENATE SERIES OF QUERY COMMANDS AS ONE LONG STRING
##################################################################
### HELPER CODE TO SAVE YOUR ANSWER and THE RESPONSE YOU RECEIVE
##################################################################
with open('queryString.txt','w') as f3:
    test=f3.write(queryString)

response=requests.get('https://script.google.com/macros/s/AKfycbxKmFUGdc3iQtn4s_Hng1aOzpuY7JU3Cyo9upIMGk_2V9BJO1U/exec',params={'queryString':queryString}).text
with open('response.txt','w') as f4:
    test=f4.write(response)
print response
##################################################################
### DO NOT CHANGE THE FOLLOWING - Used in submission process
##################################################################
def yourSubmission():
	return {'email':email,'hw':3,'queryString':queryString,'response':response}