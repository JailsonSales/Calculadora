import PySimpleGUI as sg

sg.theme("Black")

layout = [
    [sg.Input(
        key="display",
        size=(20,1),
        font=("Arial", 24),
        justification="right",
        border_width=0,
        background_color="#1e1e1e",
        text_color="white"
    )],

    [sg.Button("C", size=(5,2), button_color=("white", "#d9534f")),
     sg.Button("(", size=(5,2)),
     sg.Button(")", size=(5,2)),
     sg.Button("/", size=(5,2), button_color=("white", "#f0ad4e"))],

    [sg.Button("7", size=(5,2)),
     sg.Button("8", size=(5,2)),
     sg.Button("9", size=(5,2)),
     sg.Button("*", size=(5,2), button_color=("white", "#f0ad4e"))],

    [sg.Button("4", size=(5,2)),
     sg.Button("5", size=(5,2)),
     sg.Button("6", size=(5,2)),
     sg.Button("-", size=(5,2), button_color=("white", "#f0ad4e"))],

    [sg.Button("1", size=(5,2)),
     sg.Button("2", size=(5,2)),
     sg.Button("3", size=(5,2)),
     sg.Button("+", size=(5,2), button_color=("white", "#f0ad4e"))],

    [sg.Button("0", size=(11,2)),
     sg.Button(".", size=(5,2)),
     sg.Button("=", size=(5,2), button_color=("white", "#5cb85c"))],
]

janela = sg.Window("Calculadora Pro", layout, element_justification="center")

expressao = ""

while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED:
        break

    if evento in "0123456789.+-*/()":
        expressao += evento
        janela["display"].update(expressao)

    if evento == "C":
        expressao = ""
        janela["display"].update("")

    if evento == "=":
        try:
            resultado = str(eval(expressao))
            janela["display"].update(resultado)
            expressao = resultado
        except:
            janela["display"].update("Erro")
            expressao = ""

janela.close()