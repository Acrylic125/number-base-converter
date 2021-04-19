import PySimpleGUI as Gui

# Constants
BASE_COLOR = "#1a1f1f"
INPUT_COLOR = "#414141"
OUTPUT_COLOR = "#5f5f5f"
BUTTON_COLOR = "#2b2e2e"
BASE_TEXT_COLOR = "#ffffff"


# Consist elements (Helper functions)
def create_Text(text: str,
                useEvents: bool = False,
                key: str = None,
                size=(30, 1)) -> Gui.Text:
    return Gui.Text(text,
                    text_color=BASE_TEXT_COLOR,
                    enable_events=useEvents,
                    key=key,
                    size=size,
                    background_color=BASE_COLOR)


def create_Button(text: str,
                  useEvents: bool = True,
                  key: str = None,
                  size=(7, 1)) -> Gui.Button:
    return Gui.Button(text,
                      button_color=BUTTON_COLOR,
                      enable_events=useEvents,
                      key=key,
                      size=size,
                      border_width=0)


def create_Input(text: str,
                 useEvents: bool = True,
                 key: str = None,
                 size=(30, 12)) -> Gui.Input:
    return Gui.Input(text,
                     background_color=INPUT_COLOR,
                     enable_events=useEvents,
                     key=key,
                     size=size,
                     text_color=BASE_TEXT_COLOR,
                     border_width=0)


def create_OutputBox(text: [],
                     size=(30, 10)) -> Gui.Text:
    return Gui.Text(text,
                    background_color=OUTPUT_COLOR,
                    size=size)


input_Value = create_Input("", size=(50, 10))
input_BaseInput = create_Input("", size=(5, 10))
box_Output = create_OutputBox("", size=(44, 4))
input_BaseOutput = create_Input("", size=(5, 10))
