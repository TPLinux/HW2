# coding: utf-8

g_p = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0.0}

courses = open('courses.txt', 'r').readlines()
students = open('students.txt', 'r').readlines()

all_courses, all_students = {}, {}
for course in courses:
    c = course.split(':')
    all_courses.update({c[0]: {'name': c[1], 'hrs': int(c[2].replace('\n', ''))}})  # noqa

for student in students:
    s = student.split(':')
    all_students.update({s[0]: {'name': s[1].replace('\n', ''), 'courses': {}}})  # noqa

for c_code in all_courses:
    with open(c_code + '.txt') as f:
        info = f.readlines()
        for student in info:
            s = student.split(':')
            if(len(s) is 2):
                s_g = s[1].replace('\n', '')
                c = all_courses[c_code]
                all_students[s[0]]['courses'].update({c_code: {'grade': s_g, 'hrs': c['hrs'], 'points': g_p[s_g]}})  # noqa


def calculate_all_credits(id):
    total_credit = 0
    total_points = 0
    for c, v in all_students[id]['courses'].items():
        total_credit += v['hrs']
        total_points += v['hrs'] * v['points']

    gpa = total_points / total_credit
    return [total_credit, total_points, '%.3f' % gpa]


def print_final_msg(id):
    s_info = calculate_all_credits(id)
    print('\t' * 8 + 'SULTAN QABOOS UNIVERSITY')
    print('\t' * 7 + 'DEANSHIP OF ADMISSION AND REGISTERATION')
    print('\t' * 8 + '  ACADEMIC TRANSCRIPT')
    print('\t' * 8 + ' ' * 6 + 'SPRING 2017')
    print()
    print('STUDENT NO: %s' % id + '\t' * 7 + 'NAME: %s' % all_students[id]['name'])  # noqa
    print()
    print('COURSE NO', end='\t' * 4)
    print('COURSE NAME', end='\t' * 5)
    print('CREDITS', end='\t' * 4)
    print('GRADE', end='\t' * 3)
    print()
    print('-' * 126)
    for code, row in all_students[id]['courses'].items():
        print(code, end='\t' * 3)
        print(all_courses[code]['name'].ljust(40), end='\t' * 2)
        print(row['hrs'], end='\t' * 4)
        print(row['grade'], end='\t' * 3)
        print()
    print('-' * 126)
    print('TOTAL CREDITS: %0.2f' % s_info[0] + '\t' * 5 + 'TOTAL POINTS: %0.2f' % s_info[1] + '\t' * 4 + 'SEM GPA: %s' % s_info[2])  # noqa
    print()
    print('\t' * 8 + ' ' * 3 + 'END OF TRANSCRIPT')
    print('\t' * 7 + ' ' * 3 + '*' * 32)


while(True):
    inserted_id = input('Please Insert Studen ID [q then enter to close]: ')  # noqa
    if(inserted_id == 'q'):
        print('\nFinish\n')
        exit()
    print_final_msg(inserted_id)
