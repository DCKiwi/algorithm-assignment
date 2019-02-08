# David Cockerill
# 16163090
# Assignment 3
# Problem 2

# initiate and setup variables
input_file = open("prob2.in")
files_list = []
first_line_bool = True
line_number = 0
file_lines = 0
working_list = []
output_list = []

# write file to list, omit first line from list and any blank lines.
for line in input_file:

    if not line.strip():
        continue

    elif first_line_bool:
        first_line_bool = False
        line_number = line

        if int(line_number) < 1:
            raise SystemExit("Incorrect input - line count must be 1 or greater")

        continue

    else:
        files_list.append(line.strip().split())
        file_lines += 1

# check first int equals line count
if file_lines != int(line_number):
    raise SystemExit("Incorrect input - first line number does not match line count")

input_file.close()


# remove tuple from list with the highest priority
def remove(tuple_list):
    max_k = 0
    max_p = 0
    element = None

    for tuples in tuple_list:
        if int(tuples[1]) > max_p or (int(tuples[1]) == max_p and int(tuples[0]) > max_k):
            max_k = int(tuples[0])
            max_p = int(tuples[1])
            element = tuples

    if element is not None:
        working_list.remove(element)

    output_list.append((max_k, max_p))

# iterate through list from file performing instruction
for lines in files_list:

    if lines[0] == "insert":
        working_list.append((lines[1], lines[2]))
        continue

    if len(working_list) > 1 and lines[0] == "remove":
        remove(working_list)
    else:
        raise SystemExit("Incorrect input - remove instruction greater than input.")


# write removed tuples to file
output_file = open("prob2.out", "w")

for tup in output_list:
    output_file.write(str(tup[0]) + " " + str(tup[1]) + "\n")

output_file.close()
