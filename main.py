import PySimpleGUI as Gui
import layout
import converter as c

while True:
    base = int(input("Key in a base to convert from."))
    val = input("Key in a value.")
    print(c.Converter(base, inputValue=val).toBase10())

#
# def run_Convert():
#     inp = layout.e.input_Value.get()
#     layout.e.box_Output.update(inp)
#     print(inp)
#
#
# def run_Flip():
#     run_FlipBase()
#     run_FlipValues()
#
#
# def run_FlipValues():
#     inp = layout.e.input_Value
#     out = layout.e.box_Output
#     flip(inp, out)
#
#
# def run_FlipBase():
#     inp = layout.e.input_BaseInput
#     out = layout.e.input_BaseOutput
#     flip(inp, out)
#
#
# def flip(inp, out):
#     v_Inp = inp.get()
#     v_Out = out.get()
#     inp.update(v_Out)
#     out.update(v_Inp)
#
#
# def run_ButtonAction(key, values) -> bool:
#     if key == layout.KEY_BTN_CONVERT:
#         run_Convert()
#         return True
#     if key == layout.KEY_BTN_FLIP:
#         run_Flip()
#         return True
#     if key == layout.KEY_BTN_FLIP_BASE:
#         run_FlipBase()
#         return True
#     if key == layout.KEY_BTN_FLIP_INPUT:
#         run_FlipValues()
#         return True
#     return False
#
#
# while True:
#     event, values = layout.window.read()
#     if event == "Exit" or event == Gui.WIN_CLOSED:
#         break
#     if run_ButtonAction(event, values):
#         continue
#     print(event)
#
#
# layout.window.close()
#
