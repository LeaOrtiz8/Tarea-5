def enter_comments(point):
    print('Enter your comments')
    comment = input()
    post = f'point: {point} comment: {comment}'
    file_pc = open("data.txt", 'a')
    file_pc.write(f'{post}\n')
    file_pc.close()

def vrfy_review_pts(point):
    while True:
        point = int(point)
        if point < 1 or point > 5:
            print('Please enter on a scale of 1 to 5')
            point = input()
        else:
            enter_comments(point)
            break

def enter_review():
    while True:
        print('Please enter a rating on a scale of 1 to 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5: 
                vrfy_review_pts(point)
            else:
                enter_comments(point)
                break
        else:
            print('Please enter the number of evaluation points')


def print_saved_reviews():
    print('Results to date')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()

while True:
    print('Please select the process you wish to perform')
    print('1:Enter evaluation points and comments')
    print('2:Check the results so far.')
    print('3:Terminate')
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            enter_review() 
        elif num == 2: 
            print_saved_reviews()
        elif num == 3: 
            print('Termination.')
            break
        else:
            print('Please enter 1 to 3')
    else:
        print('Please enter 1 to 3')
