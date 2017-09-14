# SupervisedLearning
Collection of python code to do supervised learning using decision tree classifier.

Following are the files 

File : README.md
=================
This file

File : livelogAna.py
=====================
This is a sample data cleaning file that extracts the essential data from Server live logs to generate keywords

File : ml8_oneHotEncSk.py
==========================
This is the main source code that demonstrates how can we convert the keywords to Numbers and to One hot encoded Matrix. Further, fit the data and train the classifier and test the data

File : ml8_oneHotEncSk.png
==========================
This file shows the Decision tree developed by the algorithem in pictorial format

How to run these scripts
=========================
1. Set up the environment by installing sklearn using pip install - sudo pip install sklearn
2. Install numpy - sudo pip install numpy
3. Keep the logs h2-001-Livelogs.log in the same directory as livelogAna.py and run the command to display the keywords
4. Frame the Input Features and output lables and populate in inputData and outputData matrix of ml8_oneHotEncSk.py
5. Run ml8_oneHotEncSk.png and see the Decision tree generated in same directory as  ml8_oneHotEncSk.png
6. Now you can check if the algorithem is able to predict by populating any knon data from input one hot encoded matrix val = clf.predict([1,0,0,0])


Note
=====
This was code developd for POC purpose and lot of optimizations are pending
