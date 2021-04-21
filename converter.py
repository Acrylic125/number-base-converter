import PySimpleGUI as Gui
import layout
import re as regex

NEGATIVE_SIGN = "-"
SPACING_PATTERN = "[ _,]"
MAX_BASE = 35

# Table to convert from char -> number
CharNumericsTable = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35
}
NumericsCharTable = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
    17: "H",
    18: "I",
    19: "J",
    20: "K",
    21: "L",
    22: "M",
    23: "N",
    24: "O",
    25: "P",
    26: "Q",
    27: "R",
    28: "S",
    29: "T",
    30: "U",
    31: "V",
    32: "W",
    33: "X",
    34: "Y",
    35: "Z"
}


def toNum(char: str) -> int:
    output = CharNumericsTable.get(char)
    return output if output is not None else 0


def toChar(val: int) -> str:
    output = NumericsCharTable.get(val)
    return output if output is not None else 0


def __markInputAs(inp: Gui.Input, valid: bool):
    if valid:
        layout.resetInputColor(inp)
    else:
        inp.update(background_color="#f2506b")


def __testInputForInt(val: str) -> bool:
    return len(val) > 0 and not val.__contains__(".")


def validateInputValue(inp: Gui.Input) -> bool:
    val = str(inp.get())
    result = __testInputForInt(val)
    __markInputAs(inp, result)
    return result


def validateInputBase(inp: Gui.Input) -> bool:
    val = str(inp.get())
    result = __testInputForInt(val)
    if result:
        val = int(val)
        result = 0 < val <= MAX_BASE
    __markInputAs(inp, result)
    return result


def validateForConversion() -> bool:
    valid_Value, valid_InputBase, valid_OutputBase = \
        validateInputValue(layout.e.input_Value), \
        validateInputBase(layout.e.input_BaseInput), \
        validateInputBase(layout.e.input_BaseOutput)
    return valid_Value and valid_InputBase and valid_OutputBase


def _recursiveConverter(quotient: int,
                        tail: str,
                        base: int) -> str:
    remainder = quotient % base
    newQuotient = (quotient - remainder) / base
    rTail = toChar(remainder)
    if rTail is not None:
        tail = rTail + tail
    return tail if newQuotient <= 0 else _recursiveConverter(int(newQuotient), tail, base)


class Converter:
    def __init__(self,
                 inputBase: int = 10,
                 outputBase: int = 10,
                 inputValue: str = "0"):
        self.inputBase = inputBase
        self.outputBase = outputBase
        self.inputValue = regex.sub(SPACING_PATTERN, "", inputValue).upper()
        self.warnings = []

    def convertToOutput(self) -> str:
        b_10 = self.__toBase10()
        if b_10 < 0:
            return "-" + _recursiveConverter(b_10 * -1, "", self.outputBase)
        return _recursiveConverter(b_10, "", self.outputBase)

    def __toBase10(self) -> int:
        # Error handling
        warn_OutOfBase = False

        # Conversion
        arr = list(self.inputValue)
        i = len(arr)
        acc = 0
        isNegative = arr[0] == NEGATIVE_SIGN
        for c in arr:
            i -= 1
            num = toNum(c)
            acc += (num * pow(self.inputBase, i)) if num != 0 else 0
            # Error handling
            if not warn_OutOfBase and num >= self.inputBase:
                warn_OutOfBase = True
                self.warnings.append("The given input is out of base! This may resort in unwanted results.")
        if isNegative:
            acc *= -1
        return acc
