from enum import Enum
from utils import *

class ops(Enum):
    ADDITION = "addition"
    MINUS = "minus"
    TIMES = "times"
    DIVISION = "divide"

    SQRT = "square root"
    SIGN = "sign"
    DOT = "dot"
    CLEAR = "clear"

def doOp(operation, first, second):
    match(operation):
        case ops.TIMES:
            return round(first*second, 5)
        case ops.DIVISION:
            try:
                ret = round(first/second, 5)
            except(ZeroDivisionError):
                ret = specialCodes[1]
                showDialogBox()
            return ret
        case ops.ADDITION:
            return first+second
        case ops.MINUS:
            return first-second
