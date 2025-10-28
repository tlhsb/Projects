### 考核 A： 代码重构挑战


def process_data(student_records):
    return sorted([student['name'].upper() for student in student_records if student['grade'] == 'A' and student['active'] == True])
        

# 示例数据
data = [
    {'name': 'Bob', 'grade': 'C', 'active': True},
    {'name': 'Eve', 'grade': 'A', 'active': False},
    {'name': 'Alice', 'grade': 'A', 'active': True},
    {'name': 'Charlie', 'grade': 'A', 'active': True},
]
print(process_data(data))




