
class EmptyTileFilter:
    """ Filter that only returns Empty Tiles """
    
    def filter(self, tiles):
        """ Filter the given list of tiles """
        return [tile for tile in tiles if tile.piece is None]