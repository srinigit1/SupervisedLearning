from nltk.tokenize import line_tokenize,word_tokenize
from sklearn import tree
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


'''
NORMAL BOOT SEQUENCE INPUT LABLES
1. POWER OFF
2. POWER ON
3. MICRO CODE DETECTION
4. CPU SOCKET & CORE DETECTION
5. MEMORY DETECTION
6. CPU CORES ACTIVATION
7. NPAR FOR IO CARDS
8. ACPI TABLES
9. EXIT EFI BOOT
'''


readLiveLogFile = []
# DATA INITIALIZATION AND CLEANING
#readLiveLogFile = open('h2-001-LiveLogs.log','r').readline()
keywordCount = 0
lineCount = 0



with open('h2-001-LiveLogs.log') as f:
    readLiveLogFile = f.readlines()
# remove whitespace characters like `\n` at the end of each line
readLiveLogFile = [x.strip() for x in readLiveLogFile]
# Check from where relavent keywords start
for line in readLiveLogFile:
    lineCount = lineCount+1
    if "Date" in line :
        for word in word_tokenize(line):
            keywordCount = keywordCount + 1
            if "Keyword" in word:
                break
        break

listOfKeyWords = []

for lineNum in range(lineCount, len(readLiveLogFile)):
    print(word_tokenize(readLiveLogFile[lineNum])[keywordCount-1])





