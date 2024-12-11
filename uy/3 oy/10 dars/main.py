class Robot:
    def __init__(self, name, current_x, current_y, direction):
        self.name = name
        self.current_x = current_x
        self.current_y = current_y
        self.direction = direction

    def move(self, steps):
        if self.direction == "up":
            self.current_y += steps
        elif self.direction == "down":
            self.current_y -= steps
        elif self.direction == "left":
            self.current_x -= steps
        elif self.direction == "right":
            self.current_x += steps

    def change_direction(self, new_direction):
        self.direction = new_direction


robot = Robot("MyRobot", 0, 0, "up")

while True:
    command = input("Enter a command (move/change direction/exit): ")

    if command == "move":
        steps = int(input("Enter the number of steps: "))
        robot.move(steps)
        print("Robot moved.")

    elif command == "change direction":
        new_direction = input("Enter the new direction: ")
        robot.change_direction(new_direction)
        print("Robot direction changed.")

    elif command == "exit":
        print("Exiting the program.")
        break

    else:
        print("Invalid command. Please try again.")
