def isSet(arg_set):  #list가 set이면 True, set이 아니면 False를 반환
    n = 0
    for i in range(len(arg_set) - 1):
        for j in range(i + 1, len(arg_set)):
            if arg_set[i] == arg_set[j]:
                n += 1
    if n >= 1:
        return False
    else:
        return True


def toSet(arg_set):  #list를 set으로 변환
    #집합 자료형 이용
    toSet = set(arg_set)
    return toSet
    #반복문 이용
    # new_list = []
    # for i in arg_set:
    #     if i not in new_list:
    #         new_list.append(i)
    # return new_list


def unionSet(arg_set1, arg_set2):  #ist1과 list2의 모든 원소를 포함하는 set을 반환(합집합)
    union = toSet(arg_set1) | toSet(arg_set2)
    return union


def intersectionSet(arg_set1,
                    arg_set2):  #list1과  list2에서 중복되는 원소들을 모은 set을 반환(교집합)
    inter = toSet(arg_set1) & toSet(arg_set2)
    return inter


def main():
    arg1 = [1, 2, 2, 3, 4, 'list']
    arg2 = [3, 5, 7, 'lis', 'list']
    print("set1:", arg1, ", set2:", arg2, "\n")
    print("set1 is set?", isSet(arg1), ", set2 is set?", isSet(arg2), "\n")
    print("to set1:", toSet(arg1), ", to set2:", toSet(arg2), "\n")
    print("Union:", unionSet(arg1, arg2), "\n")
    print("Intersection:", intersectionSet(arg1, arg2), "\n")


if __name__ == "__main__":
    main()