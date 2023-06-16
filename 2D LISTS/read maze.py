def read_maze(file_name):
    try:
        with open(file_name) as f:
            maze = [[char for char in line.strip("\n")] for line in f]
            '''mtx = []
            for line in f:
                row = []
                for char in line.strip("\n"):
                    row.append(char)
                mtx.append(row)'''

            top_row_size = len(maze[0])
            for row in maze:
                if len(row) != top_row_size:
                    print("Not rectangular!")
                    raise SystemExit
            return maze
    except OSError:
        print("Problem with the file")
        raise SystemExit


if __name__ == "__main__":
    active_maze = read_maze("maze.txt")
    for r in active_maze:
        print(r)
