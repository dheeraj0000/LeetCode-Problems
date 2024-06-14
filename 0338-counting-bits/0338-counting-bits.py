class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count_ones = bin(i).count('1')
            ans.append(count_ones)
        return ans