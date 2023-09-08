class Element:
    # coordinates of the element
    x = 0
    y = 0

    # list of icon objects to be drawn for the element
    icons = []
    ownIcons = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ownIcons = []

class Icon:
    # string location of image in file explorer
    image_location = None
    localX = 0
    localY = 0

    def __init__(self, location, x, y):
        self.image_location = location
        self.localX = x
        self.localY = y

class CatanBoard:
    # 2d array of hexagon grid of ResourceTile
    resource_tiles = []

    # ordered list of the players in the game
    players = []

    def __init__(self):
        # self.resource_tiles = [[None for i in range(height)] for j in range(width)]
        pass

class ResourceTile(Element):
    # type of the tile (wood, sheep, rock, brick, wheat, desert, etc)
    type = "water"

    # ref to the ResourceTileNumber object of the tile
    number = None

    # list of refs to the adjacent edges
    edges = []

    # list of refs to the adjacent intersections
    intersections = []

    def __init__(self, x, y):
        Element.__init__(self, x, y)
        icon_insertion = Icon("images/hexagon_empty.png", x, y)
        self.icons.append(icon_insertion)
        self.ownIcons.append(icon_insertion)
        self.edges = [None for i in range(6)]

    def GetEdges(self):
        return self.edges

class ResourceTileNumber:
    # integer value of the dice roll associated with the resource tile (2-12)
    number = None;

class ResourceTileEdge(Element):
    # this will hold a reference to a road object when a player builds on it
    road = None

    # array of the adjacent edges (used for calculating possible road placements and longest road)
    adjacent_edges = None

    # array of adjacent resource tiles
    adjacent_tiles = None

    def __init__(self, x, y):
        Element.__init__(self, x, y)
        self.adjacent_tiles = []
        self.adjacent_edges = []
        icon_insertion = Icon("images/placeholder_6.png", x, y)
        self.icons.append(icon_insertion)
        self.ownIcons.append(icon_insertion)

class ResourceTileIntersection:
    # reference to a settlement or city built on this intersection
    building = None

    # list of references to adjacent resource tiles
    adjacent_tiles = []

    # list of references to adjacent edges
    adjacent_edges = []

class Player:
    color = "cornsilk4"

    resource_hand = []

    dc_hand = []

    roads = []

class ResourceCard:
    type = None

class DevelopmentCard:
    type = None

class CardDeck:
    cards = []