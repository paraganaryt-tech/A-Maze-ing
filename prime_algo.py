"""
Hadi hya lprime algo a nasser bdel lmaze_generater method
bhadi o runi lcode matzide matn9es
"""

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
        time.sleep(0.03)
