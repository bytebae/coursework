n, m = raw_input().split()
ls = []
for i in range(int(n)):
    ls.append(list(raw_input()))

for i in range(int(n)):
    print ls[i]

coordinate_component_map = []
visited_list = []
comp_id = 0
comp_dict = {}
# def find_all_components(ls, visited_list):
#     i, j = 0, 0
#     while some_base_condition:
#         if (ls[i])[j] == '*':
#             coordinate_component_map.append([(i,j), comp_id+1])
            
def find_all_components_given_i_j(ls, i, j, comp_id, visited_list):
    to_check = get_coord_of_adj_cells(i, j, n, m)
    for coord in to_check:
        if return_byte_given_coord(coord, ls) == '.':
            comp_dict[(i,j)] = comp_id+1]) # can this DS can be improved?
        visited_list.append()
        
        

def get_coord_of_adj_cells(i, j, n, m):
    coord_list = []
    if i + 1 < n:
        coord_list.append((i+1, j))
    if i > 0:
            coord_list.append((i-1, j))
    if j + 1 < m:
        coord_list.append((i, j+1))
    if j > 0:
        coord_list.append((i, j-1))
    return coord_list

def return_byte_given_coord((i, j), ls):
    return ls[int(i)][int(j)]
    
