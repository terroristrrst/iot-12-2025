def can_place_cows(cell, C, dist):
    count = 1
    last_position = cell[0]

    for i in range(1, len(cell)):
        if cell[i] - last_position >= dist:
            count += 1
            last_position = cell[i]
            if count == C:
                return True

    return False


def max_min_distance(N, C, free_sections):
    free_sections.sort()

    left = 1
    right = free_sections[-1] - free_sections[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place_cows(free_sections, C, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer