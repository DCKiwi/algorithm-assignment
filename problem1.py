# David Cockerill
# 16163090
# Assignment 3
# Problem 1

# initiate and setup variables
input_file = open("prob1.in")
first_line_bool = True
file_lines = 0
line_number = 0
temp_string = ""

# write file to list, omit first line from list and any blank lines.
for line in input_file:

    if not line.strip():
        continue

    else:
        if first_line_bool:
            first_line_bool = False
            line_number = line

            if int(line_number) < 2:
                raise SystemExit("Incorrect input - line count must be 2 or greater")

            continue

        file_lines += 1

    temp_string += line.strip(" ")

# check first int equals line count
if file_lines != int(line_number):
    raise SystemExit("Incorrect input - first line number does not match line count")

input_file.close()
files_list = temp_string.split()


# sorting algorithm.
def selection_sort(char_list):

    for i in range(len(char_list)):
        min_pos = i

        for j in range(i+1, len(char_list)):

            if int(char_list[j]) < int(char_list[min_pos]):
                min_pos = j

        temp = char_list[min_pos]
        char_list[min_pos] = char_list[i]
        char_list[i] = temp


# call function, create new file and write list to it.
selection_sort(files_list)
output_file = open("prob1.out", "w")

for char in files_list:
    output_file.write(char + " ")

output_file.write("\n")
output_file.close()
