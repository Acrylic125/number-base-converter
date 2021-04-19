import elements as e
import PySimpleGUI as Gui


KEY_BTN_CONVERT = "btn_CONVERT"
KEY_BTN_FLIP = "btn_FLIP"
KEY_BTN_FLIP_INPUT = "btn_FLIP_INPUT"
KEY_BTN_FLIP_BASE = "btn_FLIP_BASE"


section = [
    [
        e.create_Text("Key in the value (n):")
    ],
    [
        e.input_Value
    ],
    [
        e.create_Text("Key in the base (Input):")
    ],
    [
        e.input_BaseInput
    ],
    [
        e.create_Text("Key in the base (Output):")
    ],
    [
        e.input_BaseOutput
    ],
    [
       Gui.HSeparator()
    ],
    [
        e.create_Button("Convert", key=KEY_BTN_CONVERT),
        e.create_Button("Flip", key=KEY_BTN_FLIP),
        e.create_Button("Flip Base", key=KEY_BTN_FLIP_BASE),
        e.create_Button("Flip Input", key=KEY_BTN_FLIP_INPUT)
    ],
    [
        e.create_Text("Output:"),
    ],
    [
        e.box_Output
    ]
]

layout = [
    [
        Gui.Column(section,
                   background_color=e.BASE_COLOR,
                   pad=(3, 3))
    ]
]

window = Gui.Window("Number Converter",
                    layout,
                    background_color=e.BASE_COLOR)
