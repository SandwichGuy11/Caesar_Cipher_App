import PySimpleGUI as sg
import functions

FONTS = {
    "HEADER_1": ("Arial", 20),
    "HEADER_2": ("Arial", 16),
    "BODY": ("Helvetica", 12),
    "BUTTON": ("Courier New", 10),
    "WINDOW": ("Helvetica", 15)
}

TEXT_BOX_SIZE = (50, 8)
BUTTON_SIZE = (12, 1)

sg.theme("DarkBlue")
# ------------------------------ WIDGETS ------------------------------
header_text = sg.Text(text="Caesar Cipher Program",
                      font=FONTS["HEADER_1"],
                      )
input_box_label = sg.Text(text="Input Text:",
                          font=FONTS["BODY"]
                          )

text_input_box = sg.Multiline(default_text="Something interesting..",
                              font=FONTS["BODY"],
                              size=TEXT_BOX_SIZE,
                              key="-INPUT-"
                              )

output_text_label = sg.Text(text="Output Text:",
                            font=FONTS["BODY"],
                            )

text_output_box = sg.Multiline(default_text="",
                               font=FONTS["BODY"],
                               size=TEXT_BOX_SIZE,
                               key="-OUTPUT-"
                               )

cipher_button = sg.Button(button_text="Cipher",
                          button_color="LightGreen",
                          size=BUTTON_SIZE,
                          key="-CIPHER-"
                          )

decipher_button = sg.Button(button_text="Decipher",
                            button_color="Gray",
                            size=BUTTON_SIZE,
                            key="-DECIPHER-"
                            )

options_header = sg.Text(text="Options:",
                         font=FONTS["BODY"]
                         )

shift_label = sg.Text(text="Shift amount:",
                      font=("Helvetica", 10)
                      )

shift_input = sg.Input(default_text="1",
                       size=(5, 1),
                       key="-SHIFT-"
                       )

# ------------------------------ WINDOW LAYOUT ------------------------------
layout = [
    [header_text],

    [sg.Line()],

    [input_box_label],
    [text_input_box],

    [sg.Line()],

    [options_header],
    [shift_label, shift_input, cipher_button, decipher_button],

    [sg.Line()],

    [output_text_label],
    [text_output_box]

]

window = sg.Window(title="Caesar Cipher", layout=layout)
# ------------------------------ MAIN LOOP ------------------------------

running = True
while running:
    event, values = window.read()
    print(f"event: {event}, values: {values}")

    if event == sg.WINDOW_CLOSED:
        running = False

    if event in ["-CIPHER-", "-DECIPHER-"]:
        try:
            to_cipher = values["-INPUT-"]
            shift_amount = int(values["-SHIFT-"])
            direction = "E" if event == "-CIPHER-" else "D"

            cipher_result = functions.caesar(direction=direction, text=to_cipher, shift=shift_amount)

            window["-OUTPUT-"].update(cipher_result)
        except ValueError:
            sg.PopupOK("Please enter a number!")


print("Program closed.")
