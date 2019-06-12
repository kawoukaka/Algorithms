class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort(reverse=True)
            if stones[0]==stones[1]:
                stones=stones[2:]
            else:
                stones[1]=stones[0]-stones[1]
                stones=stones[1:]
        if stones:
            return stones[0]    
        else:
            return 0