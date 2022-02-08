# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

from typing import List, Optional


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        shipCount = 0
        callCount = 0
        # q for regions with a ship
        region_q = [[topRight, bottomLeft]]
        # while there are still regions to examine and we don't go over 400 calls
        # Also if len region_q is ever 10 that means there are 10 ships
        # Because each region is disjoint and only added if hasShips is true there
        while region_q and callCount < 396 and len(region_q) < 10:
            tr, bl = region_q.pop()
            regions = self.computeRegions(tr, bl)
            # No smaller subregions available
            # So this region must be a 1:1 square with a ship
            if not regions:
                shipCount += 1
                continue
            
            for tr, bl in regions:
                callCount += 1
                if sea.hasShips(tr, bl):
                    region_q.append([tr, bl])
        
        # Add len(region_q) in case we know there are 10 ships and stop early
        # or in case we hit call count limit and need to best guess number left
        return shipCount + len(region_q)
    
    def computeRegions(self, topRight: 'Point', bottomLeft: 'Point') -> Optional[List[List['Point']]]:
        """
        Computes the (up to) 4 subregions to divide and conquer from
        the region bounded by the passed in points
        """
        if topRight.x <= bottomLeft.x and topRight.y <= bottomLeft.y:
            return None
        
        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        regions = []
        
        # Can be split into 4 regions cuz is at least 2x2
        if topRight.x != bottomLeft.x and topRight.y != bottomLeft.y:
            # Lower left subregion
            regions.append([Point(midX, midY), bottomLeft])
            # Upper right subregion
            regions.append([topRight, Point(midX+1, midY+1)])
            # Lower right subregion
            regions.append([Point(topRight.x, midY), Point(midX+1, bottomLeft.y)])
            # Upper Left subregion
            regions.append([Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)])
        # Is purely vertical so only 2 regions split on y
        elif topRight.x == bottomLeft.x:
            # Lower subregion
            regions.append([Point(midX, midY), Point(midX, bottomLeft.y)])
            # Upper subregion
            regions.append([Point(midX, topRight.y), Point(midX, midY + 1)])
        # Is purely horizontal so only 2 regions split on x
        else:
            # Left subregion
            regions.append([Point(midX, midY), Point(bottomLeft.x, midY)])
            # right subregion
            regions.append([Point(topRight.x, midY), Point(midX + 1, midY)])
        
        return regions

    def countShipsCleaner(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # If the current rectangle does not contain any ships, return 0.         
        if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y):
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # If the rectangle represents a single point, a ship is located.
        if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
            return 1

        # Recursively check each of the 4 sub-rectangles for ships.
        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2
        return self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + \
               self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1)) + \
               self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + \
               self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))