my_dict = {'Iron': ['Avengers: Endgame', "One", 'A cave'], 'World': ['One', 'What If', "Two"]}
graph_value = my_dict.values()
list_of_graphs = list(graph_value)

graph_values = my_dict.keys()
list_of_keys = list(graph_values)

for item in list_of_graphs:
    newlist = item[0] + item[1]
print (newlist)
# # for key in my_dict:
# #     print (my_dict[key])



# my_dict = {2:3, 5:6, 8:9}

# new_dict = {}
# for k, v in my_dict.items():
#     new_dict[v] = k
# print (new_dict)