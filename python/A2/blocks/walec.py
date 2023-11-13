import math
from enums import props,reqs
class Walec:
    def __init__(walec):
        walec.height = 0
        walec.radius = 0
        walec.volume = 0
        walec.mass = 0
        walec.density = 0
        walec.area = 0

    def getHeight(walec):
        return walec.height
    def getRadius(walec):
        return walec.radius
    def getVolume(walec):
        walec.volume = math.pi*(walec.radius**2)*walec.height
        return walec.volume
    def getMass(walec):
        walec.volume = walec.getVolume()
        walec.mass = walec.volume*walec.density
        return walec.mass
    def getArea(walec):
        walec.area = 2*math.pi*walec.radius*(walec.radius + walec.height)
        return walec.area
    
    def getRequirenments(walec, req):
        match(req):
            case reqs.VOLUME:
                return [props.RADIUS, props.HEIGHT]
            case reqs.MASS:
                return [props.RADIUS, props.HEIGHT, props.DENSITY]
            case reqs.AREA:
                return [props.RADIUS, props.DENSITY]
    def setProps(walec, prop, value):
        match(prop):
            case props.RADIUS:
                walec.radius = value
            case props.HEIGHT:
                walec.height = value
            case props.DENSITY:
                walec.density = value