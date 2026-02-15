import time
import os
import random


class MazeGenerator():
    def __init__(self, config: dict) -> None:
        self.width = config['WIDTH']
        self.height = config['HEIGHT']
        self.entry = config['ENTRY']
        self.exit_p = config['EXIT']
        self.out_file = config['OUTPUT_FILE']
        self.perfect = config['PERFECT']
        self.seed = config["SEED"]
        self.algo = config["ALGO"]

    def test_path_blue(self, tmp_maze):
        try:
            start_h, start_w = self.entry[0], self.entry[1]
            end_h, end_w = self.exit_p[0], self.exit_p[1]
            visited = []
            for y in range(len(tmp_maze)):
                visited.append([])
                for x in range(len(tmp_maze[0])):
                    visited[y].append(False)
            stack = [[[start_h * 2 + 1, start_w * 2 + 1]]]
            colors = {
                "BLACK_BG": "\033[40m",
                "WHITE_BG": "\033[47m",
                "GREEN_BG": "\033[42m",
                "BL_BG": "\033[44m",
                "AMM_BG": "\033[45m",
                "RED_BG": "\033[41m"
            }
            RESET = "\033[0m"
        except BaseException:
            print('Wrong cordinates')
            exit()
        try:
            while len(stack) > 0:
                current_path = stack.pop()
                h, w = current_path[-1]
                if visited[h][w]:
                    continue
                visited[h][w] = True
                os.system("clear")
                for y in range(len(tmp_maze)):
                    maze_str = ""
                    for x in range(len(tmp_maze[0])):
                        if [y, x] in current_path:
                            maze_str += f'{colors["GREEN_BG"]}  {RESET}'
                        elif tmp_maze[y][x] == "#":
                            maze_str += f'{colors["WHITE_BG"]}  {RESET}'
                        elif tmp_maze[y][x] == "@":
                            maze_str += f'{colors["AMM_BG"]}  {RESET}'
                        elif y == start_h * 2 + 1 and x == start_w * 2 + 1:
                            maze_str += f'{colors["GREEN_BG"]}  {RESET}'
                        elif y == end_h * 2 + 1 and x == end_w * 2 + 1:
                            maze_str += f'{colors["RED_BG"]}  {RESET}'
                        else:
                            maze_str += f'{colors["BLACK_BG"]}  {RESET}'
                    print(maze_str)
                time.sleep(0.05)
                if h == end_h * 2 + 1 and w == end_w * 2 + 1:
                    break
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dh, dw in directions:
                    nh, nw = h + dh, w + dw
                    if 0 <= nh < len(tmp_maze) and 0 <= nw < len(tmp_maze[0]):
                        if tmp_maze[nh][nw] != "#" and not visited[nh][nw]:
                            new_path = list(current_path)
                            new_path.append([nh, nw])
                            stack.append(new_path)
        except BaseException:
            exit()

    def open_path(
                self, place_w: int,
                place_h: int,
                next_w: int,
                next_h: int,
                tmp_maze: list
                            ) -> None:

        dw = next_w - place_w
        dh = next_h - place_h

        place_w = place_w * 2 + 1
        place_h = place_h * 2 + 1

        next_w = next_w * 2 + 1
        next_h = next_h * 2 + 1

        tmp_maze[next_h][next_w] = " "

        tmp_maze[place_h + dh][place_w + dw] = " "

    def print_maze(self, tmp_maze) -> None:
        try:
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
                    elif h == self.entry[0]*2+1 and w == self.entry[1]*2+1:
                        maze_str += f'{colors["GREEN_BG"]}  {RESET}'
                    elif h == self.exit_p[0]*2+1 and w == self.exit_p[1]*2+1:
                        maze_str += f'{colors["RED_BG"]}  {RESET}'
                    else:
                        maze_str += f'{colors["BLACK_BG"]}  {RESET}'
                print(maze_str)
        except BaseException as e:
            print(e)
            exit()

    def print_intro(self, tmp_maze: list) -> None:
        try:
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
        except BaseException:
            exit()

    def create_tmp_maze(self) -> list:
        w = self.width * 2 + 1
        h = self.height * 2 + 1

        maze: list = []
        for y in range(h):
            maze.append([])
            for x in range(w):
                maze[y].append("#")
            os.system("clear")
            self.print_intro(maze)
            time.sleep(0.03)

        return maze

    def visited_list(self) -> list:
        visited: list = []
        for y in range(self.height):
            visited.append([])
            for x in range(self.width):
                visited[y].append(False)
        return visited

    def perfect_path(self, tmp_maze: list):
        i = random.randint(1, self.width)
        print(i)
        rnd_list = [(self.entry[0]*2)+1, (self.exit_p[0]*2)+1]
        rd = random.choice(rnd_list)
        print(rd)
        while i < len(tmp_maze[rd]):
            if tmp_maze[rd][i] == "#":
                print(i)
                tmp_maze[rd][i] = " "
                break
            i += 1

    def set_42_in_maze(self, is_visited: list, tmp_maze: list) -> None:
        try:
            is_visited[int(self.height/2) - 2][int(self.width/2) - 3] = True
            is_visited[int(self.height/2) - 2][int(self.width/2) - 3] = True
            is_visited[int(self.height/2) - 1][int(self.width/2) - 3] = True
            is_visited[int(self.height/2) - 0][int(self.width/2) - 3] = True
            is_visited[int(self.height/2) - 0][int(self.width/2) - 2] = True
            is_visited[int(self.height/2) - 0][int(self.width/2) - 1] = True
            is_visited[int(self.height/2) + 1][int(self.width/2) - 1] = True
            is_visited[int(self.height/2) + 2][int(self.width/2) - 1] = True

            is_visited[int(self.height/2) - 2][int(self.width / 2) + 1] = True
            is_visited[int(self.height/2) - 2][int(self.width / 2) + 2] = True
            is_visited[int(self.height/2) - 1][int(self.width / 2) + 2] = True
            is_visited[int(self.height/2) - 0][
                int(self.width / 2) + 2] = True
            is_visited[int(self.height/2) - 0][int(self.width / 2) + 2] = True
            is_visited[int(self.height/2) - 0][int(self.width / 2) + 1] = True
            is_visited[int(self.height/2) + 1][int(self.width / 2) + 1] = True
            is_visited[int(self.height/2) + 2][int(self.width / 2) + 1] = True
            is_visited[int(self.height/2) + 2][int(self.width / 2) + 2] = True
        except IndexError:
            print()

        for y in range(len(is_visited)):
            for x in range(len(is_visited[0])):
                try:
                    if is_visited[y][x]:
                        tmp_maze[y * 2 + 1][x * 2 + 1] = "@"

                        os.system("clear")
                        self.print_intro(tmp_maze)
                        time.sleep(0.05)
                except BaseException:
                    while 1:
                        ex = input("you want to exit ? (y/n): ")
                        if ex.lower() == "y":
                            exit()
                        elif ex.lower() == "n":
                            break
                    continue

    def maze_generater_dfs(self, tmp_maze, is_visited) -> None:
        start_w = self.entry[0]
        start_h = self.entry[1]

        is_visited[start_h][start_w] = True

        reminder = []
        reminder.append((start_w, start_h))

        direction = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        try:
            while len(reminder) > 0:
                try:
                    place_w, place_h = reminder.pop()

                    dir_n = []
                    for nw, nh in direction:
                        nw += place_w
                        nh += place_h

                        if 0 <= nw < self.width and 0 <= nh < self.height:
                            if not is_visited[nh][nw]:
                                dir_n.append((nw, nh))

                    if len(dir_n) > 0:
                        reminder.append((place_w, place_h))

                        next_w, next_h = random.choice(dir_n)

                        self.open_path(place_w, place_h, next_w, next_h, tmp_maze)

                        is_visited[next_h][next_w] = True

                        reminder.append((next_w, next_h))

                        os.system("clear")
                        self.print_maze(tmp_maze)
                        time.sleep(0.05)
                except BaseException:
                    while 1:
                        ex = input("you want to exit ? (y/n): ")
                        if ex.lower() == "y":
                            exit()
                        elif ex.lower() == "n":
                            break
                    continue
        except BaseException:
            exit()
        if not self.perfect:
            os.system("clear")
            self.perfect_path(tmp_maze)
            self.print_maze(tmp_maze)
        self.ft_output_file(tmp_maze)

    def maze_generater_prim(self, tmp_maze, is_visited) -> None:
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
            try:
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
                time.sleep(0.04)
            except BaseException:
                while 1:
                    ex = input("you want to exit ? (y/n): ")
                    if ex.lower() == "y":
                        exit()
                    elif ex.lower() == "n":
                        break
                continue
        if not self.perfect:
            os.system("clear")
            self.perfect_path(tmp_maze)
            self.print_maze(tmp_maze)
        self.ft_output_file(tmp_maze)

    def ft_output_file(self, tmp_maze: list) -> None:
        o_list: list = [[15 for h in range(self.width)]
                        for w in range(self.height)]
        N = 1
        E = 2
        S = 4
        W = 8
        for h in range(self.height):
            for w in range(self.width):
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
            o_file.write(f"\n{str(self.entry[0])},{str(self.entry[1])}\n")
            o_file.write(f"{str(self.exit_p[0])},{str(self.exit_p[1])}")

    def amazing_gen(self):
        try:
            tmp_maze = self.create_tmp_maze()
            is_visited = self.visited_list()
            if self.width > 8 or self.height > 8:
                self.set_42_in_maze(is_visited, tmp_maze)
            try:
                if tmp_maze[self.entry[0]*2+1][self.entry[1]*2+1] == "@":
                    raise ValueError("Is in 42 area")
                if tmp_maze[self.exit_p[0]*2+1][self.exit_p[1]*2+1] == "@":
                    raise ValueError("Is in 42 area")

                tmp_maze[self.entry[0]*2+1][self.entry[1]*2+1] = " "

            except ValueError as e:
                print(e)
                exit(1)
            if self.seed:
                random.seed(1337)
            if self.algo:
                self.maze_generater_dfs(tmp_maze, is_visited)
            else:
                self.maze_generater_prim(tmp_maze, is_visited)
            self.maze_base = tmp_maze
        except BaseException:
            exit()

    def ft_run(self) -> None:
        try:
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
                time.sleep(0.05)
            print("\n\n\n\n\n")
            time.sleep(0.05)
            input("Run ==>")
        except BaseException:
            exit()
        self.amazing_gen()

    def change_colors(self, tmp_maze) -> None:
        GREEN_BG = "\033[42m"
        RED_BG = "\033[41m"
        RESET = "\033[0m"

        colors = [
            "\033[44m",
            "\033[45m",
            "\033[40m",
            "\033[43m",
            "\033[47m",
            "\033[46m"
            ]
        for_wall = random.choice(colors)
        colors.remove(for_wall)

        for_42 = random.choice(colors)
        colors.remove(for_42)

        for_path = random.choice(colors)
        colors.remove(for_path)

        for h in range(len(tmp_maze)):
            maze_str = ""
            for w in range(len(tmp_maze[0])):
                if tmp_maze[h][w] == "#":
                    maze_str += f'{for_wall}  {RESET}'
                elif tmp_maze[h][w] == "@":
                    maze_str += f'{for_42}  {RESET}'
                elif h == self.entry[0]*2+1 and w == self.entry[1]*2+1:
                    maze_str += f'{GREEN_BG}  {RESET}'
                elif h == self.exit_p[0]*2+1 and w == self.exit_p[1]*2+1:
                    maze_str += f'{RED_BG}  {RESET}'
                else:
                    maze_str += f'{for_path}  {RESET}'
            print(maze_str)
