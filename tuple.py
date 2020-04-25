fullname = ('pradeep', 'Reddy', 'kotha', '1220')
print(fullname)

# tuples in list

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
        print(enumerate(result))
    return result
print(enumerate(full_emails([('alex@en.com', 'alex'), ('shay@gn.com','shay')])))
  