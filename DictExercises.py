###### List To Dictionary exercise

# keys = ['Ten', 'Twenty', 'Thirty','Ten','g']
# values = [10, 20, 30, 40,50,90]
# n1 = len(keys)
# d = dict()
# # for i in range(n1):
# #     d[keys[i]] = values[i]


# for i,j in zip(keys,values):
#     d[i] = j

# for k in d:
#     print(k,"-->",d[k])

##### Merge two dictionaries to one

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# d3 = dict(dict1)
# for k in dict2:
#     if(d3.get(k) == None):
#         d3[k] = dict2[k]

# for k in d3:
#     print(k,"--->",d3[k])

#### Nested dictioanry , printa  a value

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict['class']['student']['marks']['history'])


###### Default initalization

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# newDict = dict()
# for e in employees:
#     newDict[e] = defaults

# print(newDict)

##### delete a list of keys from dict
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]

# for k in keys:
#     del sample_dict[k]

# print(sample_dict)


########## minimum value key
# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }

# mini = 99999999999
# for k in sample_dict:
#     mini = min(mini,sample_dict[k])

# print("minimum value is", mini)



#########
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

for k in sample_dict:
    if(sample_dict[k]['name'] == "Brad"):
        sample_dict[k]['salary'] = 8500

for k in sample_dict:
    print(sample_dict[k])

del sample_dict['emp2']

print(sample_dict.items())

#sorted dictionary

newD = dict(sorted(sample_dict.items()))

for k in newD.keys():
    print(newD[k])

some_dict = {"John":(1,25000, "EE"),"Brad":(5,35000, "SC"),"Swetha":(4,1000,"ME")}

#sort based on first element( the name)
print(some_dict.items())
newD2= dict(sorted(some_dict.items(), key=lambda x: x[1][0]))
for k in newD2.items():
    print(k)