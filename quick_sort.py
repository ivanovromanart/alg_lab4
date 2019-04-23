
def quicksort(a):
    if not a:
        return []

    pivots = [x for x in a if x == a[0]]
    lesser = quicksort([x for x in a if x < a[0]])
    greater = quicksort([x for x in a if x > a[0]])

    return lesser + pivots + greater

