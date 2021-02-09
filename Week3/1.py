def tree_ref(tree, indexs):
    segment = tree
    try:
        for i in indexs:
            segment = segment[i]
    except:
        print("Error Index Error")
        return

    print(segment)


if __name__ == '__main__':
    tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
    indexs = (0, 0, 0, 0)
    tree_ref(tree, indexs)
