# --Description: Control the volume of selected Cue or Tracks

import cri.atomcraft.criatomcraft_api_lib as acconnect
# import cri.atomcraft.project
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

import math
import tkinter as tk

BUTTON_PADX = 10
BUTTON_PADY = 3


def db_2_perc(db: float):
    return 10 ** (db / 10)


def perc_2_db(perc: float):
    return 10 * math.log10(perc)


def vol_down(val: int):
    obj = None
    if acproject.get_selected_objects('Cue')['data']:
        obj = acproject.get_selected_objects('Cue')['data']
    elif acproject.get_selected_objects('Track')['data']:
        obj = acproject.get_selected_objects('Track')['data']
    else:
        print('Please select cue or track')

    for item in obj:
        curr_vol = acproject.get_value(item, 'Volume')['data']
        new_vol = max(db_2_perc(perc_2_db(float(curr_vol)) - 0.5 * float(val)), 0.0)
        acproject.set_value(item, 'Volume', new_vol)


def vol_up(val: int):
    obj = None
    if acproject.get_selected_objects('Cue')['data']:
        obj = acproject.get_selected_objects('Cue')['data']
    elif acproject.get_selected_objects('Track')['data']:
        obj = acproject.get_selected_objects('Track')['data']
    else:
        print('Please select cue or track')

    for item in obj:
        curr_vol = acproject.get_value(item, 'Volume')['data']
        new_vol = min(db_2_perc(perc_2_db(float(curr_vol)) + 0.5 * float(val)), 1.0)
        acproject.set_value(item, 'Volume', new_vol)


if __name__ == '__main__':
    acconnect.initialize()
    acconnect.connect('127.0.0.1', 9000)
    acdebug.log('Python remote connected')

    window = tk.Tk()
    window.title('Vol Change')

    lf_volume = tk.LabelFrame(
        window,
        text='Volume'
    )
    lf_volume.pack()

    b13 = tk.Button(
        lf_volume,
        text='+1dB',
        width=20,
        height=2,
        command=lambda: vol_up(1)
    )
    b13.grid(
        row=7,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b14 = tk.Button(
        lf_volume,
        text='-1dB',
        width=20,
        height=2,
        command=lambda: vol_down(1)
    )
    b14.grid(
        row=10,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b15 = tk.Button(
        lf_volume,
        text='+3dB',
        width=20,
        height=2,
        command=lambda: vol_up(3)
    )
    b15.grid(
        row=13,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b16 = tk.Button(
        lf_volume,
        text='-3dB',
        width=20,
        height=2,
        command=lambda: vol_down(3)
    )
    b16.grid(
        row=16,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b17 = tk.Button(
        lf_volume,
        text='+6dB',
        width=20,
        height=2,
        command=lambda: vol_up(6)
    )
    b17.grid(
        row=19,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b18 = tk.Button(
        lf_volume,
        text='-6dB',
        width=20,
        height=2,
        command=lambda: vol_down(6)
    )
    b18.grid(
        row=23,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    window.geometry("200x400")
    window.call('wm', 'attributes', '.', '-topmost', '1')
    window.mainloop()
