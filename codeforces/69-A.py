number_of_forces = int(raw_input())

list_of_forces = []

for i in range(0, number_of_forces):
    list_of_forces.append(str(raw_input()))

restructure_list = map ((lambda x: x.split()), list_of_forces)

sum_col_0 = sum(map (lambda x: int(x[0]), restructure_list))

if sum_col_0 != 0:
    print "NO"
    exit()

sum_col_1 = sum(map (lambda x: int(x[1]), restructure_list))

if sum_col_1 != 0:
    print "NO"
    exit()

sum_col_2 = sum(map (lambda x: int(x[2]), restructure_list))

if sum_col_2 != 0:
    print "NO"
    exit()
else:
    print "YES"
    exit()