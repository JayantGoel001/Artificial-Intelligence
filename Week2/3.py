def mergeSort(ml):
    if len(ml) > 1:
        mid = len(ml) // 2

        left = ml[:mid]
        right = ml[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ml[k] = left[i]
                i += 1
            else:
                ml[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            ml[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            ml[k] = right[j]
            k += 1
            j += 1


def insertSort(il):
    for i in range(1, len(il)):
        key = il[i]

        j = i - 1
        while j >= 0 and key < il[j]:
            il[j + 1] = il[j]
            j -= 1

        il[j + 1] = key


def selectionSort(sl):
    for i in range(len(sl)):
        min_idx = i
        for j in range(i + 1, len(sl)):
            if sl[min_idx] > sl[j]:
                min_idx = j
        sl[min_idx], sl[i] = sl[i], sl[min_idx]


if __name__ == '__main__':
    l = list(map(int, input("Enter a list:\n").split()))

    ml = l.copy()
    il = l.copy()
    sl = l.copy()

    print("Merge Sort")
    mergeSort(ml)
    print(ml)

    print("Insertion Sort")
    insertSort(il)
    print(il)

    print("Selection Sort")
    selectionSort(sl)
    print(sl)
