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
            maze.amazing_gen(0)
        elif choice == 2:
            os.system("clear")
            print("Path")
            # dakhel l fucntion dial l path hna ligadi
            # thadha chof labgiti tgadha f class gadha
            # lamabgitich gadha f function lmhm lrah
            # l 2d arry dial lmaze li b # o " " rah smytha:
            # maze.maze_base
        elif choice == 3:
            os.system("clear")
            maze.change_colors(maze.maze_base)
        else:
            break

# rah gadi lflake o kolchi ol interface o lpakages rah msayb
# anchof wach ba9i khasi yzid ytgad ola la b9a gir dakchi
# dlinsstalation b toml o lpath dialk sf ol makefile
