class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.position = (0, 0)  

    def move(self, command, occupied_positions, grid_size):
        direction, steps = command[0], int(command[1:])
        x, y = self.position
        new_position = x, y

        for _ in range(steps):
            if direction == 'N':
                new_position = (x - 1, y)
            elif direction == 'S':
                new_position = (x + 1, y)
            elif direction == 'E':
                new_position = (x, y + 1)
            elif direction == 'W':
                new_position = (x, y - 1)

            # Check boundaries
            if 0 <= new_position[0] < grid_size[0] and 0 <= new_position[1] < grid_size[1]:
                if new_position in occupied_positions:
                    break  
                x, y = new_position
            else:
                break  

        self.position = (x, y)
        return self.position


class Terrain:
    def __init__(self, rows, cols):
        self.grid_size = (rows, cols)
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot with ID {robot_id} already exists.")
        self.robots[robot_id] = Robot(robot_id)

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            raise ValueError(f"Robot with ID {robot_id} does not exist.")

        occupied_positions = {robot.position for robot in self.robots.values() if robot.robot_id != robot_id}
        return self.robots[robot_id].move(command, occupied_positions, self.grid_size)

    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError(f"Robot with ID {robot_id} does not exist.")
        return self.robots[robot_id].position


# Unit Tests
import unittest

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        self.terrain = Terrain(5, 5)  # 5x5 grid
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)

    def test_initial_position(self):
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))
        self.assertEqual(self.terrain.get_robot_position(2), (0, 0))

    def test_robot_movement(self):
        self.terrain.move_robot(1, 'N1')  
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))

        self.terrain.move_robot(1, 'E2')  # Move East by 2 steps
        self.assertEqual(self.terrain.get_robot_position(1), (0, 2))

    def test_collision_avoidance(self):
        self.terrain.move_robot(1, 'E2')  # Robot 1 moves East to (0, 2)
        self.terrain.move_robot(2, 'E3')  # Robot 2 moves East but stops at (0, 1)
        self.assertEqual(self.terrain.get_robot_position(2), (0, 1))

    def test_out_of_bounds(self):
        self.terrain.move_robot(1, 'S6')  # Attempt to move South out of bounds
        self.assertEqual(self.terrain.get_robot_position(1), (4, 0))  # Stops at the boundary

    def test_multiple_commands(self):
        self.terrain.move_robot(1, 'E2')  # Move to (0, 2)
        self.terrain.move_robot(1, 'S3')  # Move to (3, 2)
        self.assertEqual(self.terrain.get_robot_position(1), (3, 2))


if __name__ == "__main__":
    # Remove exit=False
     unittest.main(argv=['first-arg-is-ignored'], exit=False)
