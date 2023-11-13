from enums import props,reqs

class Ostroslup:
    def __init__(ostroslup):
        ostroslup.sidea = 0
        ostroslup.sideb = 0
        ostroslup.height = 0
        ostroslup.volume = 0
        ostroslup.mass = 0
        ostroslup.density = 0
        ostroslup.area = 0

    def getSideA(ostroslup):
        return ostroslup.sidea
    def getSideB(ostroslup):
        return ostroslup.sideb
    def getHeight(ostroslup):       
        return ostroslup.height
    def getVolume(ostroslup):
        ostroslup.volume = (1/3)*(ostroslup.sidea*ostroslup.sideb)*ostroslup.height
        return ostroslup.volume
    def getMass(ostroslup):
        ostroslup.volume = ostroslup.getVolume()
        ostroslup.mass = ostroslup.volume*ostroslup.density
        return ostroslup.mass
    def getArea(ostroslup):
        ostroslup.area = ostroslup.sidea*ostroslup.sideb + ostroslup.sidea*heightHelper(ostroslup.sidea/2, ostroslup.height) + ostroslup.sideb*heightHelper(ostroslup.sideb/2, ostroslup.height)
        return ostroslup.area
    
    def getRequirenments(ostroslup, req):
        match(req):
            case reqs.VOLUME:
                return [props.SIDEA, props.SIDEB, props.HEIGHT]
            case reqs.MASS:
                return [props.SIDEA, props.SIDEB, props.HEIGHT, props.DENSITY]
            case reqs.AREA:
                return [props.SIDEA, props.SIDEB, props.HEIGHT]
    def setProps(ostroslup, prop, value):
        match(prop):
            case props.SIDEA:
                ostroslup.sidea = value
            case props.SIDEB:
                ostroslup.sideb = value
            case props.HEIGHT:
                ostroslup.height = value
            case props.DENSITY:
                ostroslup.density = value
    
def heightHelper(a, b):
    return (a**2 + b**2)**0.5