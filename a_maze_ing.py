import time
import sys
import os
import random
import get_config


def open_path(place_w, place_h, next_w, next_h, tmp_maze):
    dw = next_w - place_w
    dh = next_h - place_h

    place_w = place_w * 2 + 1
    place_h = place_h * 2 + 1

    next_w = next_w * 2 + 1
    next_h = next_h * 2 + 1

    tmp_maze[next_h][next_w] = " "

    tmp_maze[place_h + dh][place_w + dw] = " "


def print_maze(tmp_maze, entry_w, entry_h, exit_w, exit_h):
    BLACK_BG = "\033[40m"
    WHITE_BG = "\033[47m"
    GREEN_BG = "\033[42m"
    BLUE_BG = "\033[45m"
    RED_BG   = "\033[41m"
    RESET    = "\033[0m"
    for h in range(len(tmp_maze)):
        maze_str = ""
        for w in range(len(tmp_maze[0])):
            if tmp_maze[h][w] == "#":
                maze_str += f"{WHITE_BG}  {RESET}"
            elif tmp_maze[h][w] == "@":
                maze_str += f"{BLUE_BG}  {RESET}"
            elif h == entry_h and w == entry_w:
                maze_str += f"{GREEN_BG}  {RESET}"
            elif h == exit_h and w == exit_w:
                maze_str += f"{RED_BG}  {RESET}"
            else:
                maze_str += f"{BLACK_BG}  {RESET}"
        print(maze_str)


def create_tmp_maze(width, height):
    w = width * 2 + 1
    h = height * 2 + 1

    maze = []
    for y in range(h):
        maze.append([])
        for x in range(w):
            maze[y].append("#")

    return maze

def visited_list(width, height):
    visited = []
    for y in range(height):
        visited.append([])
        for x in range(width):
            visited[y].append(False)
    return visited


def set_42_in_maze(is_visited, tmp_maze, width, height):
    is_visited[int(height / 2) - 2][int(width / 2) - 3] = True
    is_visited[int(height / 2) - 1][int(width / 2) - 3] = True
    is_visited[int(height / 2) - 0][int(width / 2) - 3] = True
    is_visited[int(height / 2) - 0][int(width / 2) - 2] = True
    is_visited[int(height / 2) - 0][int(width / 2) - 1] = True
    is_visited[int(height / 2) + 1][int(width / 2) - 1] = True
    is_visited[int(height / 2) + 2][int(width / 2) - 1] = True

    is_visited[int(height / 2) - 2][int(width / 2) + 1] = True
    is_visited[int(height / 2) - 2][int(width / 2) + 2] = True
    is_visited[int(height / 2) - 1][int(width / 2) + 2] = True
    is_visited[int(height / 2) - 0][int(width / 2) + 2] = True
    is_visited[int(height / 2) - 0][int(width / 2) + 2] = True
    is_visited[int(height / 2) - 0][int(width / 2) + 1] = True
    is_visited[int(height / 2) + 1][int(width / 2) + 1] = True
    is_visited[int(height / 2) + 2][int(width / 2) + 1] = True
    is_visited[int(height / 2) + 2][int(width / 2) + 2] = True

    for y in range(len(is_visited)):
        for x in range(len(is_visited[0])):
            if is_visited[y][x] == True:
                tmp_maze[y * 2 + 1][x * 2 + 1] = "@"



def maze_generater(entry, tmp_maze, is_visited, width, height, entry_w, entry_h, exit_w, exit_h):
    start_w = entry[0]
    start_h = entry[1]

    is_visited[start_h][start_w] = True

    reminder = []
    reminder.append((start_w, start_h))


    direction = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

    while len(reminder) > 0:
        place_w, place_h = reminder.pop()

        dir_n = []
        for nw, nh in direction:
            nw += place_w
            nh += place_h

            if 0 <= nw < width and 0 <= nh < height:
                if is_visited[nh][nw] == False:
                    dir_n.append((nw, nh))

        if len(dir_n) > 0:
            reminder.append((place_w, place_h))

            next_w, next_h  = random.choice(dir_n)

            open_path(place_w, place_h, next_w, next_h, tmp_maze)

            is_visited[next_h][next_w] = True

            reminder.append((next_w, next_h))

            os.system("clear")
            print_maze(tmp_maze, entry_w, entry_h, exit_w, exit_h)
            time.sleep(0.05)

    

def amazeing_dfs():
    file_name = sys.argv[1]
    config = get_config.ft_get_config(file_name)

    width  = config['WIDTH']
    height = config['HEIGHT']
    entry  = config['ENTRY']
    exit_p = config['EXIT']
    out_file = config['OUTPUT_FILE']

    tmp_maze = create_tmp_maze(width, height)
    is_visited = visited_list(width, height)
    set_42_in_maze(is_visited, tmp_maze, width, height)
    print(tmp_maze)

    entry_w = entry[0] * 2 + 1
    entry_h = entry[1] * 2 + 1
    exit_w = exit_p[0] * 2 + 1
    exit_h = exit_p[1] * 2 + 1

    tmp_maze[entry_h][entry_w] = " "
    tmp_maze[exit_h][exit_w] = "  "

    maze_generater(entry, tmp_maze, is_visited, width, height, entry_w, entry_h, exit_w, exit_h)

if __name__ == "__main__":
    amazeing_dfs()
    os.system("rm -rf __pycache__")