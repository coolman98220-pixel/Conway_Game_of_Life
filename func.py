

def check_cell_(field, x, y):
    neighbors= 0
    height =  len(field)
    width = len(field[0])

    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if dx == 0 and dy == 0:
                continue

            nx, ny = (x + dx)%height, (y+dy)%width

            if 0 <= nx < height and 0 <= ny < width:
                neighbors += field[nx][ny]

    return neighbors 

def next_generation(field):
    height =  len(field)
    width = len(field[0])
    new_field=[[0]*width for _ in range(height)]

    for x in range(height):
        for y in range(width):
            live = check_cell_(field, x, y)

            if field[x][y] == 1:
                if live in (2,3):
                    new_field[x][y] = 1
            else:
                if live == 3:
                    new_field[x][y] = 1
    return new_field