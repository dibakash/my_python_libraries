import datetime


def main():
    a = [1, 2, 3, 4, [5, ["656", ["a"]]]]

    for _ in range(20):
        a.extend(a)

    print(len(a))

    minC = 100
    minD = 100

    for _ in range(5):
        start1 = datetime.datetime.now()
        c = flatten(a, [])
        stop1 = datetime.datetime.now()
        time1_min = (stop1 - start1).total_seconds()
        if minC > time1_min:
            minC = time1_min

        start2 = datetime.datetime.now()
        d = flatten_v2(a, [])
        stop2 = datetime.datetime.now()
        time2_min = (stop2 - start2).total_seconds()
        if minD > time2_min:
            minD = time2_min

        print("c", stop1 - start1)
        print("d", stop2 - start2)

    print("c", minC, "d", minD)


def flatten(obj, arr):
    for i in obj:
        if hasattr(i, "__iter__") and not type(i) == str:
            flatten(i, arr)
        else:
            arr.extend([i])

    return arr


def flatten_v2(obj, arr):
    for i in obj:
        if isinstance(i, (list, dict, tuple)):
            flatten_v2(i, arr)
        else:
            arr.extend([i])

    return arr


if __name__ == "__main__":
    main()
