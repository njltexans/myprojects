# filter(function, collection) returns all the elements that pass a condition

def passing_grade(grade):
    return int(grade) > 60

grades = ['78', '89', '90', '67', '45', '56', '78', '89', '90', '67', '45', '56']


passing_grades = filter(lambda grade: int(grade) >= 60, grades)
print(list(passing_grades)) # ['78', '89', '90', '67', '78', '89', '90', '67']

