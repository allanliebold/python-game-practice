"""Python adventure game prototype."""


class Room(object):
    """Room class object."""

    def __init__(self):
        """Initialization of Room object."""
        self.name = 'Room'
        self.desc = 'Description'
        self.nsew = [None, None, None, None]
        self.updown = [None]
        self.visited = False


class Map(object):
    """Map class object."""

    def __init__(self):
        """Initialization of Map object."""
        self.name = 'Map'
        self.layout = {}

    def add_room(self):
        """Add a new room to the map."""
        new_room = Room()

    def add_route(self, room1, room2, direction):
        """Create a path from one room to another via the direction passed."""
