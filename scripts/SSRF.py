from __future__ import annotations
from enum import Enum, auto
from typing import List, Iterable

class Decorum:
    class Colour(Enum):
        NONE = auto()
        YELLOW = auto()
        RED = auto()
        GREEN = auto()
        BLUE = auto()
    
    class ObjStyle(Enum):
        NONE = auto()
        MODERN = auto()
        ANTIQUE = auto()
        RETRO = auto()
        UNUSUAL = auto()
    
    class ObjType(Enum):
        CURIO = auto()
        WALL_HANGING = auto()
        LAMP = auto()
    
    class ObjPosition(Enum):
        LEFT = 0
        MIDDLE = 1
        RIGHT = 2
    
    class Room(Enum):
        BATHROOM = 0
        BEDROOM = 1
        LIVING_ROOM = 2
        KITCHEN = 3

    class Arrangement:
        def __init__(
            self,
            objectColours: List[Decorum.Colour],
            wallColours: List[Decorum.Colour]
        ):
            assert len(objectColours) == 12
            assert len(wallColours) == 4
            assert Decorum.Colour.NONE not in wallColours

            self._objectColours = objectColours.copy()
            self._wallColours = wallColours.copy()
        
        def __str__(self):
            return str(self._objectColours) + "\n" + str(self._wallColours)
        
        def getObjectTypes() -> List[Decorum.ObjType]:
            return [
                Decorum.ObjType.CURIO,
                Decorum.ObjType.WALL_HANGING,
                Decorum.ObjType.LAMP,
                Decorum.ObjType.WALL_HANGING,
                Decorum.ObjType.LAMP,
                Decorum.ObjType.CURIO,
                Decorum.ObjType.CURIO,
                Decorum.ObjType.LAMP,
                Decorum.ObjType.WALL_HANGING,
                Decorum.ObjType.LAMP,
                Decorum.ObjType.WALL_HANGING,
                Decorum.ObjType.CURIO,
            ]
        
        def getObjectTypesOfRoom(room: Decorum.Room) -> List[Decorum.ObjType]:
            return Decorum.Arrangement.getObjectTypes()[room.value*3:(room.value+1)*3]
        
        def getObjectPosition(
            room: Decorum.Room,
            objType: Decorum.ObjType
        ) -> int:
            objTypes: List[Decorum.ObjType] = Decorum.Arrangement.getObjectTypesOfRoom(room)
            
            return Decorum.ObjPosition[objTypes.index(objType)]
            
        def getObjectType(
            room: Decorum.Room,
            objPosition: Decorum.ObjPosition
        ):
            objTypes: List[Decorum.ObjType] = Decorum.Arrangement.getObjectTypesOfRoom(room)
            
            return objTypes[objPosition.value]
        
        def getObjectIndexFromType(
            room: Decorum.Room,
            objPosition: Decorum.ObjPosition
        ):           
            return room.value*3 + objPosition.value
        
        def getObjectIndexFromPosition(
            room: Decorum.Room,
            objType: Decorum.ObjType
        ):
            objTypes: List[Decorum.ObjType] = Decorum.Arrangement.getObjectTypesOfRoom(room)
            return room.value*3 + objTypes.index(objType)
        
        def getObjectColourFromType(
            self,
            room: Decorum.Room,
            objType: Decorum.ObjType
        ):
            return self._objectColours[self.getObjectIndexFromType(room, objType)]
        
        def getObjectColourFromPosition(
            self,
            room: Decorum.Room,
            objPosition: Decorum.ObjPosition
        ):
            return self._objectColours[self.getObjectIndexFromPosition(room, objPosition)]

        def getWallColour(
            self,
            room: Decorum.Room
        ):
            return self._wallColours[room.value]
        
    def generateAllArrangements() -> Iterable[Decorum.Arrangement]:
        objectColours: List[Decorum.Colour] = [Decorum.Colour.NONE]*12
        wallColours: List[Decorum.Colour] = [Decorum.Colour.YELLOW]*4
        
        def getNextObjectColour(colour: Decorum.Colour) -> Decorum.Colour:
            if colour == Decorum.Colour.NONE:
                return Decorum.Colour.YELLOW
            elif colour == Decorum.Colour.YELLOW:
                return Decorum.Colour.RED
            elif colour == Decorum.Colour.RED:
                return Decorum.Colour.GREEN
            elif colour == Decorum.Colour.GREEN:
                return Decorum.Colour.BLUE
            
            return Decorum.Colour.NONE
        
        def getNextWallColour(colour: Decorum.Colour) -> Decorum.Colour:
            if colour == Decorum.Colour.YELLOW:
                return Decorum.Colour.RED
            elif colour == Decorum.Colour.RED:
                return Decorum.Colour.GREEN
            elif colour == Decorum.Colour.GREEN:
                return Decorum.Colour.BLUE
            
            return Decorum.Colour.YELLOW
        
        total = pow(5, 12) * pow(4, 4)
        
        for arrangementNum in range(1, total + 1):
            yield Decorum.Arrangement(objectColours, wallColours)
            
            goNextArrangementNum = False
            currentModChecker = total
            
            for i in range(4):
                currentModChecker /= 4
                if arrangementNum % currentModChecker == 0:
                    wallColours[i] = getNextWallColour(wallColours[i])
                    goNextArrangementNum = True
                    break
            
            if goNextArrangementNum:
                continue
            
            for i in range(12):
                currentModChecker /= 5
                if arrangementNum % currentModChecker == 0:
                    objectColours[i] = getNextObjectColour(objectColours[i])
                    break         

    def calculateSSRF(isValid: callable = lambda x: True):
        total = pow(5, 12) * pow(4, 4)
        invTotal = 1.0/total
        perc = 0.0
        limitToPrint = 0.00001
        for arrangement in Decorum.generateAllArrangements():
            perc += invTotal
            if perc > limitToPrint:
                print(limitToPrint)
                limitToPrint += 0.00001
            
            

def main():
    Decorum.calculateSSRF()

if __name__ == "__main__":
    main()