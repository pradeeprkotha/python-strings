fruits = ["pinapple", "apple", "banana"]
fruits.append("kaya")
sortedList = fruits.sort()
print(sortedList)
fruits.insert(0, 'orange')
print(fruits)
fruits.insert(25, 'green apple')
print(fruits)
fruits.remove('apple')

for fruit in fruits:
    if(fruits.index(fruit)%2 == 0):
        print(fruit)
    
