def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    result = []
    last_finish = 0
    for s, f in activities:
        if s >= last_finish:
            result.append((s, f))
            last_finish = f

    return result
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
print(activity_selection(start, finish))