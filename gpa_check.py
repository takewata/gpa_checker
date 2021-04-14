float_digit = 2
special_flag = 0
credit_sum, grade_sum, special_credit_sum, special_grade_sum = 0, 0, 0, 0

with open('grade.txt', 'r') as f:
    datalist = [s.split() for s in f.readlines()]

for dataline in datalist:
    credit = 0

    for data in dataline:
        if '学部専門教育科目' in data:
            special_flag = 1
        elif '他学部開講科目' in data:
            special_flag = 0
        
        if 'ＡＡ' in data:
            grade_sum += credit * 4
            special_grade_sum += special_flag * credit * 4
        elif 'Ａ' in data:
            grade_sum += credit * 3
            special_grade_sum += special_flag * credit * 3
        elif 'Ｂ' in data:
            grade_sum += credit * 2
            special_grade_sum += special_flag * credit * 2
        elif 'Ｃ' in data:
            grade_sum += credit
            special_grade_sum += special_flag * credit
        
        credit = 0

        try:
            if float(data) < 10.0:
                credit = float(data)
                credit_sum += credit
                special_credit_sum += special_flag * credit
        except ValueError:
            pass

total_gpa = grade_sum / credit_sum
total_special_gpa = special_grade_sum / special_credit_sum

print(f'全体のGPA:{total_gpa:.{float_digit}f}')
print(f'専門のGPA:{total_special_gpa:.{float_digit}f}')