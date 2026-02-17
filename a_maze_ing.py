"""
Main program entry point.
"""
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
    maze.ft_run()
    path_show = 1

    while 1:
        try:
            print("\n\n=== A-Maze-Ing ===\n")
            print("1) Re-generate a new maze")
            print("2) Show/Hide path from entry to exit")
            print("3) Rotate maze colors")
            print("4) Quit")
            while 1:
                try:
                    choice: int = int(input("Choice? (1-4):"))
                    if choice < 1 or choice > 4:
                        raise ValueError
                    break
                except Exception:
                    print("Please enter a valid number")
        except BaseException:
            exit()
        try:
            if choice == 1:
                os.system("clear")
                maze.amazing_gen()
            elif choice == 2:
                os.system("clear")
                maze.print_path(path_show)
                path_show += 1
            elif choice == 3:
                os.system("clear")
                maze.change_colors(maze.maze_base)
            else:
                break
        except BaseException as e:
            print(e)
            exit()
