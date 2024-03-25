def Leader(T: list[int]) -> int | None:
    maks = T[0]
    ile = 1
    for i in range(1, len(T)):
        if ile == 0:
            maks = T[i]
            ile = 1
        else:
            if T[i] == maks:
                ile += 1
            else:
                ile -= 1
    if ile == 0:
        return None
    else:
        iloscMaksow = 0
        for i in range(1, len(T)):
            if T[i] == maks:
                iloscMaksow += 1
    if iloscMaksow > len(T) / 2:
        return maks


T1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 1, 1]
T2 = [1, 2, 2, 3, 3, 3, 3, 2, 3]
print(Leader(T1))
print(Leader(T2))
