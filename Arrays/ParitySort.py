class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        def fun(e):
            return e%2
        return sorted(A, key = fun)
#This is my solution

class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1

        return A
#This is the leetcode quicksort solution to modify in place.