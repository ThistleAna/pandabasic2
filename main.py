# Panda can merge two tables together
# Call Pandas before you use it
import pandas as pd
food1= {'number':[1,2,3,4,5],'name':['corn','banana','chips','popcorn','pizza'],'price':[1,2,1,2,1]}
food2= {'number':[1,2,3,4,5],'name':['apple','cinnamon','watermelon','bread','pita'],'price':[1,2,1,2,1]}
# Create tables
table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)
# Merge two tables using merge when the same attribute is number
fusion = pd.merge(table1,table2,on='number')
print(fusion)


# Join two tables using join
food3= {'number':[1,2,3,4,5],'name':['corn','banana','chips','popcorn','pizza'],'price':[1,2,1,2,1]}
food4= {'color':['yellow','yellow','yellow','white','brown'],'weight':[50,45,30,20,15],'qty':[1,2,1,2,1]}
# Create tables
table3 = pd.DataFrame(food3)
table4 = pd.DataFrame(food4)
fusion2 = table3.join(table4)
print(fusion2)
