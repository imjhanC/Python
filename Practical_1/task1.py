import csv

with open('data.csv','r') as file:
    reader = csv.reader(file)

    for row in reader:
        name = row[0]
        age = row[1]
        gender = row[2]
        city = row[3]

        print(name, age, gender, city)

    # if gender = 'Male'
    #    print(f"{name} us {age} years old")
        
