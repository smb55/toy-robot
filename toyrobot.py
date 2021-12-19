import sys

class Robot:
    '''define a class to represent the robot. methods are:
        place(x,y,facing)
        move()
        left()
        right()
        report()'''
 
    def __init__(self):
        '''set the location and direction to None, set placed to False. Create direction conversion tables
            to convert written directions to numbers.'''
        self.placed = False
        self.location = None
        self.direction = None
        self.direction_table = {1:'EAST',
                                2:'SOUTH',
                                3:'WEST',
                                4:'NORTH'}
        
        self.direction_table_reversed = {value:key for key, value in self.direction_table.items()}

    def place(self, x, y, facing):
        '''place the robot on coordinates x,y with direction facing as direction faced.'''
        self.location = (x, y)
        # convert the written direction to a number that can be used by the left() and right() methods
        self.direction = self.direction_table_reversed[facing]
        self.placed = True
                                                       
    def move(self):
        '''moves the robot one unit in the current direction, unless this would result in falling off the table.'''
        if self.placed:
            if self.direction == 1:
                # East. Check the robot is not on the East edge before proceeding:
                if self.location[0] < 4:
                    self.location = (self.location[0] + 1, self.location[1])     

            if self.direction == 2:
                # South. Check the robot is not on the South edge before proceeding:
                if self.location[1] > 0:
                    self.location = (self.location[0], self.location[1] - 1)

            if self.direction == 3:
                # West. Check the robot is not on the West edge before proceeding:
                if self.location[0] > 0:
                    self.location = (self.location[0] - 1, self.location[1])

            if self.direction == 4:
                # North. Check the robot is not on the North edge before proceeding:
                if self.location[1] < 4:
                    self.location = (self.location[0], self.location[1] + 1)
                    
    def left(self):
        if self.placed:
            # reducing direction by 1 rotates anti-clockwise / left. If the direction is 0, next direction is 4
            if self.direction > 1:
                self.direction -= 1
                
            else:
                self.direction = 4


    def right(self):
        if self.placed:
            # increasing direction by 1 rotates clockwise / right. If the direction is 4, next direction is 0
            if self.direction < 4:
                self.direction += 1
                
            else:
                self.direction = 1


    def report(self):
        if self.placed:
            # output the coordinates and direction the robot is facing
            output.write(f"{self.location[0]},{self.location[1]},{self.direction_table[self.direction]}" + "\n")

commands = sys.stdin
output = sys.stdout

robot = Robot()

direction_list = ['EAST', 'SOUTH', 'WEST', 'NORTH']
coord_list = ['0','1','2','3','4']

def main():
    print("You have a toy robot and a table top which is a grid of 5 x 5 units. There are no obstructions. You can issue commands to your robot allowing it to roam around the table top.")
    print("Commands:\nPLACE X,Y,FACING\nMOVE\nLEFT\nRIGHT\nREPORT")
    print("You must begin with a valid PLACE command. All invalid commands and commands resulting in the robot falling off the table will be ignored.")
    for line in commands:
        split_command = line.upper().split()   

        if split_command[0] == 'PLACE':
            if len(split_command) != 2:
                continue

            place_info = split_command[1].split(',')
            if len(place_info) != 3:
                continue

            if place_info[0] not in coord_list:
                continue
            if place_info[1] not in coord_list:
                continue
            if place_info[2] not in direction_list:
                continue
                
            robot.place(int(place_info[0]), int(place_info[1]), place_info[2])

        else:
            if len(split_command) != 1:
                continue

            if split_command[0] == 'MOVE':
                robot.move()

            elif split_command[0] == 'LEFT':
                robot.left()

            elif split_command[0] == 'RIGHT':
                robot.right()

            elif split_command[0] == 'REPORT':
                robot.report()

if __name__ == "__main__":
    main()

        

    
                



