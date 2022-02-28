import PySimpleGUI as psg

def GUI():
    psg.theme("Red")

    layoutA=[[psg.Text("Send til nr", size=10, font="Lucida", justification="left"), psg.InputText(size=10)],
              [psg.Text("Melding:", size=10, font="Lucida", justification="left"), psg.Multiline(size=(60, 6), key="textbox")],
              [psg.Radio("Send nå", "Naa", font="Lucida", key="send_naa"), psg.Radio("Send nå", "Naa", font="Lucida", key="send_naa")],
              [psg.Text("Velg tid", size=10, font="Lucida", justification="left"), psg.InputText(size=5), psg.InputText(size=5)],
              [psg.Button("Send Melding", font=("Times New Roman", 14)), psg.Button("Glem det", font=("Times New Roman", 14))]]

    window = psg.Window("Pokémon Encounters", layoutA)
    e, v = window.read()
    window.close()

    svar = list(v.values())
    return svar


GUI()   