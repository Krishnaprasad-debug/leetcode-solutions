class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = []
        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)
        ans = []
        for i in range(len(s)):
            mind= float('inf')
            for pos in positions:
                mind = min(mind, abs(i - pos))
            ans.append(mind)
        return ans