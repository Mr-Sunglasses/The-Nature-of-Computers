# Impementing for C Style loops using recursion
def For_C_Style_Increment(initial, limit):
    print(initial)
    if limit == 0:
        return
    else:
        For_C_Style_Increment(initial + 1, limit - 1)

print(For_C_Style_Increment(1,10))