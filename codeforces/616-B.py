n, m = map(lambda x: int(x), raw_input().split())
input_list = []

for i in range(n):
    input_list.append(raw_input().split())

def find_minima(ls):
    return min(map(lambda x: int(x), ls))

def find_maxima(ls):
    return max(map(lambda x: int(x), ls))

def find_max_minima_in_list_of_lists(ls_of_ls):
    maxima_list = map(find_minima, ls_of_ls)
    return find_maxima(maxima_list)
        
print find_max_minima_in_list_of_lists(input_list)