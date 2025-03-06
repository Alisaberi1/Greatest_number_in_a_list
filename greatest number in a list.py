Main_list=[1,2,3,4,9]
Maximum=Main_list[0]
for a in Main_list:
    if a > Maximum:
        Maximum=a
    else:
        Maximum=Main_list[0]

print(Maximum) 
