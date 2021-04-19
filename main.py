import PySimpleGUI as Gui
import layout


def run_Convert():
    pass


def run_ButtonAction(key) -> bool:
    if key == layout.KEY_BTN_CONVERT:
        run_Convert()
        return True
    return False


while True:
    event, values = layout.window.read()
    if event == "Exit" or event == Gui.WIN_CLOSED:
        break
    run_ButtonAction(event)
    print(event)


layout.window.close()

