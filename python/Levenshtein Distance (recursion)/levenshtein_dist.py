# 두 문자열을 인자로 받아, Levenshtein Distance값을 계산하여 반환하는 함수를 작성하시오. (단, 반드시 Recursion을 활용하여 구현할 것)
# ※ 호출 예시 : getLevenshteinDistance(“apple”, “people”) → 3을 결과값으로 반환
# hint: https://en.wikipedia.org/wiki/Levenshtein_distance

def getLevenshteinDistance(input1, input2, length1, length2):
    cost = None

    # base case:
    if min(length1, length2) == 0:
        return max(length1, length2)

    ## test if the last characters of the strings match
    if input1[length1-1] == input2[length2-1]:
        cost = 0
    else:
        cost = 1

    return min(getLevenshteinDistance(input1, input2, length1-1, length2) + 1,
               getLevenshteinDistance(input1, input2, length1, length2-1) + 1,
               getLevenshteinDistance(input1, input2, length1-1, length2-1) + cost)


# def lev(i, j):
#     if min(i, j) == 0:
#         return max(i, j)
#     else:
#         _  = lev(i-1, j) + 1
#         __ = lev(i, j-1) + 1
#
#         if a[i-1] != b[j-1]: # i-1, j-1 are last index of each string
#             ___ = lev(i-1, j-1) + 1
#         else:
#             ___ = lev(i - 1, j - 1)
#
#         return min(_, __, ___)

def main():
    str1, str2 = input("input strings: ").split()
    print("Input strings:", str1, ", ", str2)

    print("Calculate Levenshtein distance")
    res = getLevenshteinDistance(str1, str2, len(str1), len(str2))

    print("Levenshtein distance between ", str1, ",", str2, "is : ", res)


if __name__ == "__main__":
    main()