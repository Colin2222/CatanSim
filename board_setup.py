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
        for tile_x in range(width + 1):
            # add vertical edges
            if tile_y % 2 == 0:
                edge4 = ResourceTileEdge(baseX - 3 + 104 * tile_x, baseY + 48 + 74 * tile_y)
            else:
                edge4 = ResourceTileEdge(baseX - 3 + 54 + 104 * tile_x, baseY + 48 + 74 * tile_y)
            if tile_x < width:
                board.resource_tiles[tile_y][tile_x].edges[4] = edge4
            if tile_x - 1 > 0:
                board.resource_tiles[tile_y][tile_x - 1].edges[1] = edge4

        for tile_x in range(width):
            # add diagonal edges
            if tile_y % 2 == 0:
                edge3 = ResourceTileEdge(baseX + 21 + 104 * tile_x, baseY + 85 + 74 * tile_y)
                edge2 = ResourceTileEdge(baseX + 76 + 104 * tile_x, baseY + 85 + 74 * tile_y)

                # handle edge case of open facing edge on end of array
                if tile_x == 0 and tile_y != 0:
                    edge5 = ResourceTileEdge(baseX + 21 + 104 * tile_x, baseY + 11 + 74 * tile_y)
                    board.resource_tiles[tile_y][tile_x].edges[5] = edge5

                # set tile edges
                board.resource_tiles[tile_y][tile_x].edges[2] = edge2
                board.resource_tiles[tile_y][tile_x].edges[3] = edge3

                # set adjacent tile edges
                if tile_y != height - 1:
                    board.resource_tiles[tile_y + 1][tile_x].edges[5] = edge2
                    if tile_x != 0:
                        board.resource_tiles[tile_y + 1][tile_x - 1].edges[0] = edge3
            else:
                edge3 = ResourceTileEdge(baseX + 76 + 104 * tile_x, baseY + 85 + 74 * tile_y)
                edge2 = ResourceTileEdge(baseX + 131 + 104 * tile_x, baseY + 85 + 74 * tile_y)

                # handle edge case of open facing edge on end of array
                if tile_x == width - 1:
                    edge0 = ResourceTileEdge(baseX + 131 + 104 * tile_x, baseY + 9 + 74 * tile_y)
                    board.resource_tiles[tile_y][tile_x].edges[0] = edge0

                # set tile edges
                board.resource_tiles[tile_y][tile_x].edges[2] = edge2
                board.resource_tiles[tile_y][tile_x].edges[3] = edge3

                # set adjacent tile edges
                if tile_y != height - 1:
                    board.resource_tiles[tile_y + 1][tile_x].edges[0] = edge3
                    if tile_x != width - 1:
                        board.resource_tiles[tile_y + 1][tile_x + 1].edges[5] = edge2