import sys


def parsing_input(file_path):

    input_text = open(file_path).read()
    input_list = input_text.split('\n')
    new_input_list = []

    for string in input_list: 
        string = string.split()
        string = [int(num) for num in string]
        new_input_list.append(string)
        
    return new_input_list

input_list = parsing_input(sys.argv[1])
# print input_list



def check_triangle(input_list):

    triangle_count = 0
    for triangle in input_list:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            triangle_count += 1

    return triangle_count

#print check_triangle(input_list)


def check_triangle_2(input_list):
    
    triangle_count = 0

    new_list_1 = []
    new_list_2 = []
    new_list_3 = []

    for triangle in input_list:
        print triangle
        new_list_1.append(triangle[0])
        new_list_2.append(triangle[1])
        new_list_3.append(triangle[2])

        # import pdb; pdb.set_trace()


    combine_list = new_list_1 + new_list_2 + new_list_3

    new_list = [combine_list[i:i+3] for i in range(0, len(combine_list), 3)]

    for triangle in new_list:
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            triangle_count += 1

    return triangle_count



print check_triangle_2(input_list)

