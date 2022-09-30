from operator import itemgetter

dict = [{'name':'ravi', 'mob':9090 , 'city':'surat', 'country':'India','gyan':'panda'},
            {'name':'gyan', 'mob':9689 , 'city':'ahmedabad', 'country':'PAK','gyan':'conda'},
                {'name':'ravi', 'mob':8755 , 'city':'vadodara', 'country':'BAN','gyan':'awf'},
                    {'name':'ketan', 'mob':7495 , 'city':'bharuch', 'country':'USA','gyan':'etrrt'},
]


# new_list = []
# for i in key_list:
#     for j in dict:
#         new_list.append(j[i])
# print("____________________",new_list)

# new_dict = str(dict)
# print(type(dict))
# print(type(new_dict))

# res = list((map(itemgetter('gyan'),dict)))
# print("________WOW_________",res)

# value = [i for i in dict if i['name']=='gyan']
# print("________________________________",value)

# def get_key(ky):
#     for key, value in dict:
#         for i in dict:
#             if ky == i['name']:
#                 return value

# print(get_key('name'))