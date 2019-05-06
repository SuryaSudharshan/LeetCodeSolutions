class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})

#It's the Leetcode solution.
#Its a very poorly worded question imo. After an hour of trying to figure out what to do. I just gave up trying to understand it.