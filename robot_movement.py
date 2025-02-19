class Robot:
    def __init__(self, robot_id, rows, cols):
        self.robot_id = robot_id
        self.rows = rows
        self.cols = cols
        self.position = (0, 0)  

    def move(self, direction, steps, other_robots_positions):
        x, y = self.position 

        for _ in range(steps):
            if direction == 'N':
                new_position = (x - 1, y)
            elif direction == 'S':
                new_position = (x + 1, y)
            elif direction == 'E':
                new_position = (x, y + 1)
            elif direction == 'W':
                new_position = (x, y - 1)


            elif direction == 'NE':
                new_position = (x - 1, y + 1)
            elif direction == 'NW':
                new_position = (x - 1, y - 1)
            elif direction == 'SE':
                new_position = (x + 1, y + 1)
            elif direction == 'SW':
                new_position = (x + 1, y - 1)
            else:
                print(f"Invalid direction: {direction}")
                return

            
            if (0 <= new_position[0] < self.rows and
                0 <= new_position[1] < self.cols and
                new_position not in other_robots_positions):
                x, y = new_position
            else:
                break

        self.position = (x, y)


class Terrain:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            print(f"Robot ID {robot_id} already exists.")
        else:
            self.robots[robot_id] = Robot(robot_id, self.rows, self.cols)

    def move_robot(self, robot_id, command):
        if robot_id not in self.robots:
            print(f"Robot ID {robot_id} does not exist.")
            return

        direction = command[0]
        steps = int(command[1:]) 
        other_robots_positions = [robot.position for rid, robot in self.robots.items() if rid != robot_id]
        self.robots[robot_id].move(direction, steps, other_robots_positions)

    def get_robot_position(self, robot_id):
        if robot_id in self.robots:
            return self.robots[robot_id].position
        else:
            print(f"Robot ID {robot_id} does not exist.")
            return None


# Example Usage
if __name__ == "__main__":
    
    terrain = Terrain(5, 5)

    # Add 
    terrain.add_robot(1)
    terrain.add_robot(2)

    # Move 
    terrain.move_robot(1, "N4")  
    terrain.move_robot(2, "E3")  
    terrain.move_robot(1, "E2")  

    
    print("Robot 1 Position:", terrain.get_robot_position(1))
    print("Robot 2 Position:", terrain.get_robot_position(2))
