class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y=0,0
        direction=[(0,1),(1,0),(0,-1),(-1,-0)]
        d=0
        max_result=0
        obstacles = set(map(tuple, obstacles))
        for c in commands:
            if c==-1:
                d=(d+1)%4
            elif c==-2:
                d=(d-1)%4
            else:
                #move forward
                for _ in range(c):
                    #check for next direction 
                    dx=x+direction[d][0]
                    dy=y+direction[d][1]
                    #check if there is break or not 
                    if (dx,dy) in obstacles:
                        break
                    x=dx
                    y=dy
                    #return the max_result
                    max_result=max(max_result,x**2+y**2)
               
        return max_result