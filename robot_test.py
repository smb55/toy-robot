import toyrobot
import unittest

class RobotTest(unittest.TestCase):
    
    def test_movement(self):
        '''run the list of commands and confirm the robot ends up on the correct square and orientation. The commands
            attempt to push the robot off all four sides, use both rotation directions, and finally reports the final position.
            this should be (4,4,NORTH\n) if the commands have been executed correctly.'''

        with open('test1', 'r') as f:
            toyrobot.commands = [line.strip('\n') for line in f.readlines()]

        with open('test_output1', 'w') as g:
            toyrobot.output = g
            toyrobot.main()

        with open('test_output1', 'r') as h:
            result = h.read()

        self.assertEqual(result, '4,4,NORTH\n')

    def test_invalid_commands(self):
        '''this test is exactly the same as the movement test, except that this time there are invalid commands in the test file.'''

        with open('test2', 'r') as f:
            toyrobot.commands = [line.strip('\n') for line in f.readlines()]

        with open('test_output2', 'w') as g:
            toyrobot.output = g
            toyrobot.main()

        with open('test_output2', 'r') as h:
            result = h.read()

        self.assertEqual(result, '4,4,NORTH\n')

        
if __name__ == '__main__':
    unittest.main()           








