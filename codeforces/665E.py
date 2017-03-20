n, k = raw_input().split()
lst = raw_input().split()
k = int(k)

def _xor(arr):
    return int(reduce(lambda x, y: int(x) ^ int(y), arr))

# operate on lst with a sliding window?

def generate_list_of_list(arr):
    range_len = 1
    pointer = 0
    arr_len = len(arr)
    output_list = []
    while pointer < arr_len:
        output_list.append(arr[pointer:pointer+range_len])
        range_len += 1
        if pointer + range_len > arr_len:
            pointer += 1
            range_len = 1
    return output_list

def no_of_b_arrays(ls_o_ls, thrshld):
    s = 0
    for ls in ls_o_ls:
        if _xor(ls) >= thrshld:
            s += 1
    return s

print no_of_b_arrays(generate_list_of_list(lst), k)
   
