import time
import sys
import os
import random
import get_config


class MazeGenerator():
    def __init__(self, config: dict):
        self.width = config['WIDTH']
        self.height = config['HEIGHT']
        self.entry = config['ENTRY']
        self.exit_p = config['EXIT']
        self.out_file = config['OUTPUT_FILE']

    def open_path(self, place_w, place_h, next_w, next_h, tmp_maze):
        dw = next_w - place_w
        dh = next_h - place_h

        place_w = place_w * 2 + 1
        place_h = place_h * 2 + 1

        next_w = next_w * 2 + 1
        next_h = next_h * 2 + 1

        tmp_maze[next_h][next_w] = " "

        tmp_maze[place_h + dh][place_w + dw] = " "

    def print_maze(self, tmp_maze):
        colors = {
            "BLACK_BG": "\033[40m",
            "WHITE_BG": "\033[47m",
            "GREEN_BG": "\033[42m",
            "BL_BG": "\033[44m",
            "BLUE_BG": "\033[45m",
            "RED_BG": "\033[41m"}

        RESET = "\033[0m"
        for h in range(len(tmp_maze)):
            maze_str = ""
            for w in range(len(tmp_maze[0])):
                if tmp_maze[h][w] == "#":
                    maze_str += f'{colors["WHITE_BG"]}  {RESET}'
                elif tmp_maze[h][w] == "@":
                    maze_str += f'{colors["BLUE_BG"]}  {RESET}'
                elif h == self.entry[1]*2+1 and w == self.entry[1]*2+1:
                    maze_str += f'{colors["GREEN_BG"]}  {RESET}'
                elif h == self.exit_p[1]*2+1 and w == self.exit_p[1]*2+1:
                        maze_str += f'{colors["RED_BG"]}  {RESET}'
                else:
                    maze_str += f'{colors["BLACK_BG"]}  {RESET}'
            print(maze_str)

    def print_intro(self, tmp_maze):
        colors = {
            "BLACK_BG": "\033[40m",
            "AMM_BG": "\033[45m"}

        RESET = "\033[0m"
        for h in range(len(tmp_maze)):
            maze_str = ""
            for w in range(len(tmp_maze[0])):
                if tmp_maze[h][w] == "#":
                    maze_str += f'{colors["BLACK_BG"]}  {RESET}'
                else:
                    maze_str += f'{colors["AMM_BG"]}  {RESET}'
            print(maze_str)

    def create_tmp_maze(self) -> list:
        w = self.width * 2 + 1
        h = self.height * 2 + 1

        maze = []
        for y in range(h):
            maze.append([])
            for x in range(w):
                maze[y].append("#")
            os.system("clear")
            self.print_intro(maze)
            time.sleep(0.03)

        return maze

    def visited_list(self) -> list:
        visited = []
        for y in range(self.height):
            visited.append([])
            for x in range(self.width):
                visited[y].append(False)
        return visited

    def set_42_in_maze(self, is_visited, tmp_maze) -> None:
        is_visited[int(self.height / 2) - 2][int(self.width / 2) - 3] = True
        is_visited[int(self.height / 2) - 2][int(self.width / 2) - 3] = True
        is_visited[int(self.height / 2) - 1][int(self.width / 2) - 3] = True
        is_visited[int(self.height / 2) - 0][int(self.width / 2) - 3] = True
        is_visited[int(self.height / 2) - 0][int(self.width / 2) - 2] = True
        is_visited[int(self.height / 2) - 0][int(self.width / 2) - 1] = True
        is_visited[int(self.height / 2) + 1][int(self.width / 2) - 1] = True
        is_visited[int(self.height / 2) + 2][int(self.width / 2) - 1] = True

        is_visited[int(self.height / 2) - 2][int(self.width / 2) + 1] = True
        is_visited[int(self.height / 2) - 2][int(self.width / 2) + 2] = True
        is_visited[int(self.height / 2) - 1][int(self.width / 2) + 2] = True
        is_visited[int(self.height / 2) - 0][int(self.width / 2) + 2] = True
        is_visited[int(self.height / 2) - 0][int(self.width / 2) + 2] = True
        is_visited[int(self.height / 2) - 0][int(self.width / 2) + 1] = True
        is_visited[int(self.height / 2) + 1][int(self.width / 2) + 1] = True
        is_visited[int(self.height / 2) + 2][int(self.width / 2) + 1] = True
        is_visited[int(self.height / 2) + 2][int(self.width / 2) + 2] = True

        for y in range(len(is_visited)):
            for x in range(len(is_visited[0])):

                if is_visited[y][x]:
                    tmp_maze[y * 2 + 1][x * 2 + 1] = "@"

                    os.system("clear")
                    self.print_intro(tmp_maze)
                    time.sleep(0.08)

    def maze_generater(self, tmp_maze, is_visited) -> None:
        start_w = self.entry[0]
        start_h = self.entry[1]

        is_visited[start_h][start_w] = True
        walls = []

        direction = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        for dx, dy in direction:
            nx, ny = start_w + dx, start_h + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                walls.append((start_w, start_h, nx, ny))
        while len(walls) > 0:
            rand_ind = random.randint(0, len(walls) - 1)
            place_w, place_h, next_w, next_h = walls.pop(rand_ind)
            if is_visited[next_h][next_w]:
                continue
            self.open_path(place_w, place_h, next_w, next_h, tmp_maze)
            is_visited[next_h][next_w] = True
            for dx, dy in direction:
                nnx, nny = next_w + dx, next_h + dy
                if 0 <= nnx < self.width and 0 <= nny < self.height:
                    if not is_visited[nny][nnx]:
                        walls.append((next_w, next_h, nnx, nny))
            os.system("clear")
            self.print_maze(tmp_maze)
            time.sleep(0.056)

    def ft_output_file(self, tmp_maze: list,):
        o_list = [[15 for h in range(self.height)] for w in range(self.width)]
        N = 1
        E = 2
        S = 4
        W = 8
        for h in range(len(o_list)):
            for w in range(len(o_list[0])):
                if tmp_maze[h*2+1][w*2+2] == " ":
                    o_list[h][w] -= E
                if tmp_maze[h*2+1][w*2] == " ":
                    o_list[h][w] -= W
                if tmp_maze[h*2][w*2+1] == " ":
                    o_list[h][w] -= N
                if tmp_maze[h*2+2][w*2+1] == " ":
                    o_list[h][w] -= S
        
        hex_list = ["A", "B", "C", "D", "E", "F"]
        with open(self.out_file, "w") as o_file:
            j = 0
            i = 0
            for h in o_list:
                for w in o_list[j]:
                    if w < 10:
                        o_file.write(str(w))
                    else:
                        i = w - 9
                        o_file.write(hex_list[i - 1])
                o_file.write("\n")
                j += 1


    def amazeing_dfs(self) -> None:
        tmp_maze = self.create_tmp_maze()
        is_visited = self.visited_list()
        self.set_42_in_maze(is_visited, tmp_maze)

        try:
            if tmp_maze[self.entry[0]*2+1][self.entry[1]*2+1] == "@":
                raise ValueError("Is in 42 area")
            if tmp_maze[self.exit_p[0]*2+1][self.exit_p[1]*2+1] == "@":
                raise ValueError("Is in 42 area")

            tmp_maze[self.entry[0]*2+1][self.entry[1]*2+1] = " "

        except ValueError as e:
            print(e)

        self.maze_generater(tmp_maze, is_visited,)
        self.ft_output_file(tmp_maze)

    def ft_run(self) -> None:
        os.system("clear")
        print("\n\n\n\n\n")

        print_list = [
            "    █████╗    ███╗   ███╗ █████╗ ███████╗███████╗   ██╗███╗   ██╗"
            " ██████╗ ",
            "   ██╔══██╗   ████╗ ████║██╔══██╗╚══███╔╝██╔════╝   ██║████╗"
            "  ██║██╔════╝ ",
            "   ███████║   ██╔████╔██║███████║  ███╔╝ █████╗     ██║██╔██╗ "
            "██║██║  ███╗",
            "   ██╔══██║   ██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝     ██║██║╚██╗██"
            "║██║   ██║",
            "   ██║  ██║   ██║ ╚═╝ ██║██║  ██║███████╗███████╗   ██║██║ "
            "╚████║╚██████╔╝",
            "   ╚═╝  ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝╚═╝"
            "  ╚═══╝ ╚═════╝ ",
            "                                                    "
            "By: @nel-adao, @mjabri"
        ]

        for s in print_list:
            print(s)
            time.sleep(0.08)
        print("\n\n\n\n\n")
        time.sleep(0.08)

        input("Run ==>")
        self.amazeing_dfs()


if __name__ == "__main__":
    file_name = sys.argv[1]
    config = get_config.ft_get_config(file_name)
    dfs = MazeGenerator(config)
    dfs.ft_run()
    os.system("rm -rf __pycache__")
