class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)

        for current in range(1, len(ratings)):
            if ratings[current] > ratings[current-1]:
                candys[current] = candys[current-1] + 1
        
        for current in range(len(ratings)-2, -1, -1):
            if ratings[current] > ratings[current+1]:
                candys[current] = max(candys[current], candys[current + 1] + 1)
        
        return sum(candys)
