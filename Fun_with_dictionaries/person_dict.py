person = person = {
    "name": "Alice",
    "age": 30,
    "city": "Boston",
    "occupation": "Engineer",
    "salary": 95000,
    "is_employed": True
}

def main():
    if get_occupation(person):
        occupation = get_occupation(person)
        print(f'{occupation[0]}: {occupation[1]}')
    if get_name(person):
        name = get_name(person)
        print(f'{name[0]}: {name[1]}')


def get_occupation(person):
    for key, value in person.items():
        if key.lower() == 'occupation':
            return key, value
        
def get_name(person):
    for key, value in person.items():
        if key.lower() == 'name':
            return key, value

def get_age(person):
    for key, value in person.items():
        if key.lower() == 'age':
            return key, value

def get_salary(person):
    for key, value in person.items():
        if key.lower() == 'salary':
            return key, value

    
if __name__=='__main__':
    # get_occupation(person)
    main()