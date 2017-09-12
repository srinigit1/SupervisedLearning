from sklearn import tree
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# STEP 1 : PREPARE THE INPUT DATA
inputData = ['CHASSIS_POWERED_OFF CHASSIS_POWERED_ON BOOT_START CLUMP_SIZE', \
             'CHASSIS_POWERED_ON CHASSIS_POWERED_OFF BOOT_START CLUMP_SIZE', \
             'CLUMP_SIZE CHASSIS_POWERED_OFF CHASSIS_POWERED_ON BOOT_START', \
             'BOOT_START CHASSIS_POWERED_ON CHASSIS_POWERED_OFF CLUMP_SIZE', \
            ]

inputValues = array(inputData)
print(inputValues)
label_encoder = LabelEncoder()
integer_encoded_input = label_encoder.fit_transform(inputValues)
print(integer_encoded_input)
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded_input = integer_encoded_input.reshape(len(integer_encoded_input), 1)
onehot_encoded_input = onehot_encoder.fit_transform(integer_encoded_input)
print(onehot_encoded_input)

# STEP 2 : PREPARE THE OUTPUT DATA
outputData = ['NORMAL : OFF->ON->BOOT START->CLUMP',\
              'POW SEQ FAULT : ON->OFF->CLUMP->BOOT START->ROM',\
              'POW SEQ FAULT : ON->OFF->CLUMP->ROM->BOOT START',\
              'POW SEQ FAULT : ON->CLUMP->BOOT START->OFF->ROM',\
              ]
outputValues = array(outputData)
print(outputValues)
label_encoder = LabelEncoder()
integer_encoded_output = label_encoder.fit_transform(outputValues)
print(integer_encoded_output)
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded_output = integer_encoded_output.reshape(len(integer_encoded_output), 1)
onehot_encoded_output = onehot_encoder.fit_transform(integer_encoded_output)
print(onehot_encoded_output)

# STEP 3 : TRAIN A DECISION TREE CLASSIFIER
# Initialize a decision tree classifier
clf1 = tree.DecisionTreeClassifier(criterion='gini',splitter='best')
# Fit the input and output lables
#clf = clf1.fit(integer_encoded_input,integer_encoded_output)
clf = clf1.fit(onehot_encoded_input,integer_encoded_output)


# STEP 4 : PREDICT THE OUTPUT
val = clf.predict([0,0,1,0])
print ("PREDICTED OUTPUT IS :")
print(label_encoder.inverse_transform([argmax(onehot_encoded_output[val, :])]))


# STEP 5 : Display the Tree for visualization
from sklearn.externals.six import StringIO
from subprocess import call

dot_data = StringIO()
tree.export_graphviz(clf,out_file="ml8_oneHoyEncSk.dot")
call(["dot","-Tpng","ml8_oneHoyEncSk.dot","-o","ml8_oneHoyEncSk.png"])

