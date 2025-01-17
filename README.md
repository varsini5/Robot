 Robot Movement Simulation

This project is a Python-based simulation that manages multiple robots on a grid terrain. Each robot can move according to specified commands while avoiding collisions and staying within the grid boundaries. The program demonstrates object-oriented programming principles and includes unit tests to ensure proper functionality.

Features

- Grid Representation: The terrain is represented as a grid of customizable size.
- Robot Management: Multiple robots can be added to the grid, each with a unique identifier.
- **Movement Commands**: Robots can move in four directions:
  - N<number>: Move North (up) by the specified number of steps.
  - S<number>: Move South (down).
  - E<number>: Move East (right).
  - W<number>: Move West (left).
- Collision Avoidance: Robots stop before entering an occupied cell to prevent collisions.
- Boundary Enforcement: Robots cannot move outside the defined grid.
- Unit Testing: Comprehensive tests verify various scenarios, ensuring code robustness.

Installation

1. Clone the Repository:

   bash
   git clone https://github.com/varsini5/Robot.git
   

2. Navigate to the Project Directory:

   bash
   cd Robot
   

3. Ensure Python is Installed:

   Make sure you have Python 3.7 or higher installed on your system.

Usage

1. Run the Simulation:

   Execute the `robot_movement.py` script to start the simulation.

   bash
   python robot_movement.py
   

2. Run Unit Tests:

   To verify the functionality, run the `unit_test.py` script.

   bash
   python unit_test.py
   

Project Structure

plaintext
Robot/
robot.py             # Contains the Robot class definition
robot_movement.py    # Manages the terrain and robot movements
unit_test.py         # Unit tests for the simulation


Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Acknowledgments

This project was inspired by the need to simulate robot movements on a grid while ensuring collision avoidance and boundary enforcement. 
