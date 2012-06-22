groceries=['bananas','strawberries','apples','bread']
groceries.append('champagne')
for grocery_list in groceries:
    print grocery_list
print'-----------------'
groceries.remove('bread')
for grocery_list in groceries:
    print grocery_list
print'------------------'
aisles={'apple':'a','banana':'b','champagne':'c','strawberies':'s'}
print aisles['apple']
print'------------------'
catalog={'Apples':7.3,'Bananas':5.5,'Bread':1.0,'Carrots':10.0,'Champagne':20.90,'Strawberries':32.6}
print catalog['Carrots']
catalog['Strawberries'] = 63.43
print catalog['Strawberries']
catalog['Chicken']=6.5
print catalog['Chicken']
print'--------------------'
in_stock=['Apples','Bananas','Bread','Carrots','Champagne','Strawberries']
always_in_stock=('Apples','Bananas','Bread','Carrots','Champagne','Strawberries')

print "Come to Shoprite! We always sell:"
for i in always_in_stock:
    print i
