class Student:
    '''
        Student class with name and marks as attributes
        Methods: calc_avg
    '''
    def __init__(self, name: str, marks: list) -> None:
        '''
            Initializes the class attributes and also calls the 'calc_avg' to initialize 'avg_marks' attribute
        '''
        self.name = name
        self.marks = marks
        self.avg_marks = self.calc_avg()

    def calc_avg(self) -> float:
        '''
            Calculates the average marks of the student
        '''
        return sum(self.marks) / len(self.marks)


def identify_top(stds: Student) -> Student:
    '''
        Identifies the top performing student
        Returns: Top performer
    '''
    top_performer = max(stds, key=lambda std: std.avg_marks)
    return top_performer

stds = []
stds.append(Student(name='John', marks=[85, 78, 92]))
stds.append(Student('Alice', [88, 79, 95]))
stds.append(Student('Bob', [70, 75, 80]))

# Average marks of students
print('Average Marks')
for std in stds:
    print(f'{std.name}: {round(std.avg_marks, 2)}')

print('-'*30)
top_std = identify_top(stds)
print(f'Top Performer: {top_std.name}')
