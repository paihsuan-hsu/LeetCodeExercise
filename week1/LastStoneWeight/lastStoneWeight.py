import heapq

class Solution:
    @classmethod
    def lastStoneWeight(self, stones: list[int])->int:
        heapq._heapify_max(stones)
        print(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            print('x: %d',x)
            y = heapq.heappop(stones)
            print('y: %d',y)
            if(x!=y):
                heapq.heappush(stones, abs(x-y))

        if len(stones) == 0:
            return 0
        else:
            return heapq.heappop(stones)

stones = [2,7,4,1,8,1]
output = Solution.lastStoneWeight(stones)
print(output)