num_lines = int(raw_input())
input = []
for i in range(num_lines):
    input.append(raw_input())

counter = 0
prev_state = input[0]
c = 0
for curr_state in input:
    if curr_state != prev_state:
        c += 1
        prev_state = curr_state
    else:
        prev_state = curr_state

print c + 1
