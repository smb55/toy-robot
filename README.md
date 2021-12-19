# toy-robot
Toy Robot Task

Task Instructions:

You have a toy robot on a table top, a grid of 5 x 5 units, there are no obstructions. You can issue commands to your robot allowing it to roam around the table top. But be careful, don't let it fall off!

Commands

The robot should be able to process the following commands.
PLACE X,Y,FACING

    Puts the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.
    The origin (0,0) can be considered to be the SOUTH WEST most corner.
    The first valid command to the robot is a PLACE command, after that, any sequence of commands may be issued, in any order, including another PLACE command.
    The application should discard all commands in the sequence until a valid PLACE command has been executed.

MOVE
Moves the toy robot one unit forward in the direction it is currently facing.

LEFT
Will rotate the robot 90° anticlockwise without changing the position of the robot.

RIGHT
Rotate the robot 90° clockwise without changing the position of the robot.

REPORT
Outputs the X,Y and F of the robot. This can be in any form, but standard output is sufficient.

Constraints

    The robot is free to roam around the surface of the table, but must be prevented from falling to destruction.
    Any movement that would result in the robot falling from the table must be prevented, however further valid movement commands must still be allowed.
    Input can be from a file, or from standard input, as the developer chooses.
    You need to provide test data/results for the app & its logic.

Example Input & Output

    place 0,0,NORTH
    move
    report => Output:0, 1, NORTH
    place 0, 0, NORTH
    left
    report => Output:0, 0, WEST
    place 1,2,EAST
    move
    move
    left
    move
    report => Output:3, 3, NORTH
    
Files:
    
toyrobot.py is a program that meets these specifications.
    
robot_test.py imports toyrobot.py and runs two tests:

1) A file of valid commands is loaded and run. This file uses all of the commands and attempts to push the robot off all 4 sides of the table, the final command is REPORT. The location reported should match the known result for the test to pass.

2) A file of mixed valid and invalid commands is loaded and run. The final command is a valid REPORT command and the location reported should match the known result for the test to pass.

test1.txt and test2.txt are these lists of commands.

Improvements to be made:

Both tests redirect the standard output of the report command to a text file, before then opening and comparing the contents of the text file to known values.
Ideally this standard output should be saved in a variable instead of a file.


