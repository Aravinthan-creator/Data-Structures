class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
         n = len(gas)
         sum_gas=sum(gas)
         sum_cost=sum(cost)
         if sum_gas<sum_cost:
            return -1 
         current = 0
         start = 0
         for i in range(n):
            current += gas[i] - cost[i]
            if current <0:
                current = 0
                start=i+1
         return start

          








