from game_classes import *


def load_board(board: CatanBoard, setup_file_location, baseX, baseY):
    setup_file = open(setup_file_location, mode='r')
    rows = setup_file.readlines()

    dimensions = rows.pop(0).split()
    width = int(dimensions[1])
    height = int(dimensions[3])
    board.resource_tiles = [[None for i in range(height)] for j in range(width)]

    # create resource tiles
    for row_index, row in enumerate(rows):
        tile_symbols = row.split()
        row_insertion = []

        for symbol_index, symbol in enumerate(tile_symbols):
            insX = baseX + (symbol_index * 104)
            insY = baseY + (row_index * 74)
            if row_index % 2 == 1:
                insX += 52
            insertion = ResourceTile(insX, insY)
            row_insertion.append(insertion)
        board.resource_tiles[row_index] = row_insertion

    # create edges between tiles
    for tile_x in range(width):
        edge5 = ResourceTileEdge(baseX + 21 + 104 * tile_x, baseY + 9)
        edge0 = ResourceTileEdge(baseX + 76 + 104 * tile_x, baseY + 9)
        board.resource_tiles[0][tile_x].edges[5] = edge5
        board.resource_tiles[0][tile_x].edges[0] = edge0
        edge5.adjacent_tiles.append(board.resource_tiles[0][tile_x])
        edge0.adjacent_tiles.append(board.resource_tiles[0][tile_x])
    for tile_y in range(0, height):
        for tile_x in range(width):
            if(tile_y % 2 == 0):
                edge4 = ResourceTileEdge(baseX - 3 + 104 * tile_x, baseY + 48 + 74 * tile_y)
            else:
                edge4 = ResourceTileEdge(baseX - 3 + 54 + 104 * tile_x, baseY + 48 + 74 * tile_y)

