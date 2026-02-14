import mazegen
import sys
import os

if __name__ == "__main__":

    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Enter a name of config file !")
        exit()

    config = mazegen.ft_get_config(file_name)
    maze = mazegen.MazeGenerator(config)
    tmp_maze = maze.ft_run()

    while 1:
        print("\n\n=== A-Maze-Ing ===\n")
        print("1) Re-generate a new maze")
        print("2) Show/Hide path from entry to exit")
        print("3) Rotate maze colors")
        print("4) Quit")
        while 1:
            try:
                choice = int(input("Choice? (1-4):"))
                if choice < 1 or choice > 4:
                    raise ValueError
                break
            except Exception:
                print("Please enter a valid number")

        if choice == 1:
            os.system("clear")
            maze.amazing_gen(1)
        elif choice == 2:
            os.system("clear")
            maze.test_path_blue(maze.maze_base)
        elif choice == 3:
            os.system("clear")
            maze.change_colors(maze.maze_base)
        else:
            break
