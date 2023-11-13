import math
from enums import props,reqs
class Stozek:
    def __init__(stozek):
        stozek.height = 0
        stozek.side = 0
        stozek.radius = 0
        stozek.volume = 0
        stozek.mass = 0
        stozek.density = 0
        stozek.area = 0

    def getRadius(stozek):
        return stozek.radius
    def getSide(stozek):
        return stozek.side
    def getHeight(stozek):
        return stozek.height
    def getVolume(stozek):
        stozek.volume = (math.pi*(stozek.radius**2)**stozek.height)/3
        return stozek.volume
    def getMass(stozek):
        stozek.volume = stozek.getVolume()
        stozek.mass = stozek.volume*stozek.density
        return stozek.mass
    def getArea(stozek):
        stozek.area = math.pi*stozek.radius*(stozek.radius + stozek.side)
        return stozek.area
    
    def getRequirenments(stozek, req):
        match(req):
            case reqs.VOLUME:
                return [props.RADIUS, props.HEIGHT]
            case reqs.MASS:
                return [props.RADIUS, props.HEIGHT, props.DENSITY]
            case reqs.AREA:
                return [props.RADIUS, props.SIDE]
    def setProps(stozek, prop, value):
        match(prop):
            case props.SIDE:
                stozek.side = value
            case props.RADIUS:
                stozek.radius = value
            case props.HEIGHT:
                stozek.height = value
            case props.DENSITY:
                stozek.density = value