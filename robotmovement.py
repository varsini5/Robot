import unittest

class Terrain:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.robots = {}  

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError("Robot ID already exists")
        self.robots[robot_id] = (0, 0)  

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            raise ValueError("Robot ID not found")
        
        direction, steps = command[0], int(command[1:])
        x, y = self.robots[robot_id]
        
        deltas = {
            'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1),
            'NE': (-1, 1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (1, -1)
        }
        
        if direction not in deltas:
            raise ValueError("Invalid direction")
        
        dx, dy = deltas[direction]
        
        for _ in range(steps):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.rows and 0 <= new_y < self.cols and (new_x, new_y) not in self.robots.values():
                x, y = new_x, new_y
            else:
                break
        
        self.robots[robot_id] = (x, y)
        print(f"Robot {robot_id} moved to ({x}, {y})")
    
    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError("Robot ID not found")
        return self.robots[robot_id]

# Unit Tests
class TestTerrain(unittest.TestCase):
    def test_robot_movement(self):
        terrain = Terrain(5, 5)
        terrain.add_robot(1)
        terrain.move_robot(1, 'E2')
        self.assertEqual(terrain.get_robot_position(1), (0, 2))
        
        terrain.move_robot(1, 'S3')
        self.assertEqual(terrain.get_robot_position(1), (3, 2))
    
    def test_collision(self):
        terrain = Terrain(5, 5)
        terrain.add_robot(1)
        terrain.add_robot(2)
        terrain.move_robot(1, 'E3')
        terrain.move_robot(2, 'E2')
        terrain.move_robot(2, 'E2')  
        self.assertEqual(terrain.get_robot_position(2), (0, 2))
    
    def test_diagonal_movement(self):
        terrain = Terrain(5, 5)
        terrain.add_robot(1)
        terrain.move_robot(1, 'SE2')
        self.assertEqual(terrain.get_robot_position(1), (2, 2))
    
    def test_out_of_bounds(self):
        terrain = Terrain(5, 5)
        terrain.add_robot(1)
        terrain.move_robot(1, 'W2')  
        self.assertEqual(terrain.get_robot_position(1), (0, 0))

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
