#logical operators - used to conbine conditions
# logical operators are: and, or and not

#do we want to give a person a loan?

high_income = True
good_credit = False

if high_income and good_credit:
    print('loan approved')
elif high_income or good_credit:
    print('requires more review')
else:
    print('denied')

    student_working = False

    if not student_working:
        print('get to work buster :broken_heart:')
    else:
        print('good job')

user_role = 'guest'

if not user_role == 'admin':
    print('access denied')
else:print('you have access')


my_ln = input('type \'a\'')
if True or my_ln == a:
    print('holy guacamole')


def return_a_boolean():
    print('in function')
    return True