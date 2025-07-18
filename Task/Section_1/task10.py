from Python_learning_module.Day12.Task.Section1.task4_5 import area
import Python_learning_module.Day12.Task.Section1.task4_5 as geo
from Python_learning_module.Day12.Task.Section1.task2 import greet_user

if __name__ == "__main__":
    greet_user("Ragul")
    print("Area of circle:", area("circle", 3))
    print("Area of triangle:", geo.area("triangle", 4, 5))