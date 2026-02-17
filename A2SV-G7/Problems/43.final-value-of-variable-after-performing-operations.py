def finalValueAfterOperations(operations):
    ops_map = {
        "X++":1, "++X":1,
        "X--":-1, "--X":-1
    }
    sum_ = 0
    for op in operations:
        sum_ += ops_map[op]
    return sum_