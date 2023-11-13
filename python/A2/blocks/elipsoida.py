import math
from enums import props,reqs
class Elipsoida:
    def __init__(elipsoida):
        elipsoida.semiaxis = 0
        elipsoida.radius = 0
        elipsoida.volume = 0
        elipsoida.mass = 0
        elipsoida.density = 0
        elipsoida.area = 0

    def getSemiAxis(elipsoida):
        return elipsoida.semiaxis
    def getRadius(elipsoida):
        return elipsoida.radius
    def getVolume(elipsoida):
        elipsoida.volume = (4/3)*math.pi*elipsoida.semiaxis*(elipsoida.radius**2)
        return elipsoida.volume
    def getMass(elipsoida):
        elipsoida.volume = elipsoida.getVolume()
        elipsoida.mass = elipsoida.volume*elipsoida.density
        return elipsoida.mass
    def getArea(elipsoida):
        epsilon = (1-(elipsoida.radius**2)/(elipsoida.semiaxis**2))**0.5
        elipsoida.area = 2*math.pi*elipsoida.radius*(elipsoida.radius + ((elipsoida.semiaxis/epsilon)*math.asin(epsilon)))
        return elipsoida.area
    
    def getRequirenments(elipsoida, req):
        match(req):
            case reqs.VOLUME:
                return [props.SEMIAXIS, props.RADIUS]
            case reqs.MASS:
                return [props.SEMIAXIS, props.RADIUS, props.DENSITY]
            case reqs.AREA:
                return [props.SEMIAXIS, props.RADIUS]
    def setProps(elipsoida, prop, value):
        match(prop):
            case props.RADIUS:
                elipsoida.radius = value
            case props.SEMIAXIS:
                elipsoida.semiaxis = value
            case props.DENSITY:
                elipsoida.density = value