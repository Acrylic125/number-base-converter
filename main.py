import PySimpleGUI as Gui
import elements as e


KEY_BTN_CONVERT = "btn_CONVERT"
KEY_BTN_FLIP = "btn_CONVERT"
KEY_BTN_FLIP_INPUT = "btn_FLIP_INPUT"
KEY_BTN_FLIP_BASE = "btn_FLIP_BASE"

input_Value = e.create_Input("", size=(50, 10))
input_BaseInput = e.create_Input("", size=(5, 10))
box_Output = e.create_OutputBox("", size=(44, 4))
input_BaseOutput = e.create_Input("", size=(5, 10))


def run_Convert():
    pass


def run_ButtonAction(key) -> bool:
    if key == KEY_BTN_CONVERT:
        run_Convert()
        return True
    return False


section = [
    [
        e.create_Text("Key in the value (n):")
    ],
    [
        input_Value
    ],
    [
        e.create_Text("Key in the base (Input):")
    ],
    [
        input_BaseInput
    ],
    [
        e.create_Text("Key in the base (Output):")
    ],
    [
        input_BaseOutput
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
        box_Output
    ]
]

image_viewer_column = [
    [Gui.Text("Choose an image from list on left:")],
    [Gui.Text(size=(40, 1), key="-TOUT-")],
    [Gui.Image(key="-IMAGE-")],
]

layout = [
    [
        Gui.Column(section,
                   background_color=e.BASE_COLOR,
                   pad=(3, 3))
    ]
]

window = Gui.Window("Image Viewer",
                    layout,
                    background_color=e.BASE_COLOR)

while True:
    event, values = window.read()
    if event == "Exit" or event == Gui.WIN_CLOSED:
        break
    run_ButtonAction(event)
    print(event)


window.close()

