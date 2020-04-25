# def hint_username(username):
#     if len(username) <3:
#         print('Invalid username')
#     elif len(usernam) > 15:
#         print('Invalid username')
#     else:
#         print('logged in')

def is_positive(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)

# print(is_positive(10))

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

# print(greeting("Taylor"))
# print(greeting("John"))

# print("A dog" < "A mouse")
# print(9999+8888 > 100*100)


x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
# print("x=" + str(x))

# def test_while(num):
#     while num < 5:
#         print('Print num', num)
#         num= num+1
# test_while(0)

def letters(word):
    for letter in list(word):
        print(letter+'\n')

# letters('hello')

for i in range(7):
  for j in range(i,7):
    print(j, end=' ')
  # print()

name = 'the new sentence with long name'

print(name[1])


