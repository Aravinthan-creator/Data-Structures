class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxi=(0,0,0)

        for x,y in dimensions:
            sumofsquare=x**2+y**2
            d=math.sqrt(sumofsquare)
            maxi = max(maxi,(d,x,y))


        return maxi[1] * maxi[2]