import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]



def test_get_employees_by_age_range():
    min_age = 20
    max_age = 30

    value = [
    {'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000},
    {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}
    ]

    result = employee_info.get_employees_by_age_range(min_age, max_age)


    assert (result == value)



def test_calculate_average_salary():

    average = 60166.666666666664

    result = employee_info.calculate_average_salary()

    assert(result == average)



def test_get_employees_by_dept():
    dept = "Sales"

    value = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]

    result = employee_info.get_employees_by_dept(dept)

    assert(result == value)