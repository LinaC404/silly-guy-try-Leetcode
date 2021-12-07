# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        https://www.youtube.com/watch?v=-1P3VP7LH0I&ab_channel=HappyCoding
        Time complexity: (4^N)
        """
        # The robot cannot move freely in all four directions, 
        # so return to the previous position and restore the orientation of the previous position
    
        def goback(robot):
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def dfs(x,y,d):
            robot.clean()
            
            for i in range(len(directions)):
                # deciede the direction, then move based on the direction
                next_d = (d+i)%4
                next_x = x + directions[next_d][0]
                next_y = y + directions[next_d][1]

                
                if (next_x,next_y) not in visited and robot.move():
                    visited.add((next_x,next_y))
                    dfs(next_x,next_y,next_d)
                    goback(robot)
                    
                robot.turnLeft()

        #               0:↑   1:→　 2:↓　　3:←
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        dfs(0,0,0)
            
            
        