import math
from enums import props,reqs

class Kula:
    def __init__(kula):
        kula.radius = 0
        kula.volume = 0
        kula.mass = 0
        kula.density = 0
        kula.area = 0

    def getRadius(kula):
        return kula.radius
    def getVolume(kula):
        kula.volume = (4/3)*math.pi*kula.radius**3
        return kula.volume
    def getMass(kula):
        kula.volume = kula.getVolume()
        kula.mass = kula.volume*kula.density
        return kula.mass
    def getArea(kula):
        kula.area = 4*math.pi*kula.radius**2
        return kula.area
    
    def getRequirenments(kula, req):
        match(req):
            case reqs.VOLUME:
                return [props.RADIUS]
            case reqs.MASS:
                return [props.DENSITY, props.RADIUS]
            case reqs.AREA:
                return [props.RADIUS]
    def setProps(kula, prop, value):
        match(prop):
            case props.RADIUS:
                kula.radius = value
            case props.DENSITY:
                kula.density = value
    