def count_hops_to_right(blocks, curr_pos):
    hops = 0
    while curr_pos < len(blocks) - 1:
        if blocks[curr_pos + 1] >= blocks[curr_pos]:
            hops += 1
            curr_pos += 1
        else:
            break

    return hops


def count_hops_to_left(blocks, curr_pos):
    hops = 0
    while curr_pos > 0:
        if blocks[curr_pos - 1] >= blocks[curr_pos]:
            hops += 1
            curr_pos -= 1
        else:
            break

    return hops


def solution(blocks):
    max_hops = 0

    for curr_pos, block in enumerate(blocks):
        hops_to_right = count_hops_to_right(blocks, curr_pos)
        hops_to_left = count_hops_to_left(blocks, curr_pos)

        max_hops = max(max_hops, hops_to_left + hops_to_right)

    return max_hops + 1
