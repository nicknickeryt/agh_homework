from enums import props,reqs

class Czworoscian:
    def __init__(czworoscian):
        czworoscian.side = 0
        czworoscian.volume = 0
        czworoscian.mass = 0
        czworoscian.density = 0
        czworoscian.area = 0

    def getSide(czworoscian):
        return czworoscian.side
    def getVolume(czworoscian):
        czworoscian.volume = (czworoscian.side**3*(2**0.5))/12
        return czworoscian.volume
    def getMass(czworoscian):
        czworoscian.volume = czworoscian.getVolume()
        czworoscian.mass = czworoscian.volume*czworoscian.density
        return czworoscian.mass
    def getArea(czworoscian):
        czworoscian.area = czworoscian.side**2*(3**0.5)
        return czworoscian.area
    
    def getRequirenments(czworoscian, req):
        match(req):
            case reqs.VOLUME:
                return [props.SIDE]
            case reqs.MASS:
                return [props.SIDE, props.DENSITY]
            case reqs.AREA:
                return [props.SIDE]
    def setProps(czworoscian, prop, value):
        match(prop):
            case props.SIDE:
                czworoscian.side = value
            case props.DENSITY:
                czworoscian.density = value