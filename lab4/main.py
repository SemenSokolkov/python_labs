def OverrideMap(func, iterable : list) -> list:
    resultList = list();
    for obj in iterable:
        resultList.append(func(obj));
    return resultList;

def OverrideReduce(func, iterable : list):
    index : int = 2;
    length : int = len(iterable);
    result = func(iterable[0], iterable[1]);
    while(index < length):
        result = func(result, iterable[index]);
        index += 1;
    return result;

if __name__ == "__main__":
    print(OverrideMap(lambda x: x * 2 + 3, [10, 15, 21, 33, 42, 55]))
    print(OverrideReduce(lambda x, y: x + y, [1]))