# --Description: Modify the specific value of selected items
import math

import cri.atomcraft.criatomcraft_api_lib as acconnect
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject
import tkinter as tk
from tkinter import messagebox

BUTTON_PADX = 10
BUTTON_PADY = 3
COLOR_MAPPER = {
    'red': '255, 0, 0',
    'orange': '255, 128, 0',
    'yellow': '255, 255, 0',
    'lime green': '0, 255, 0',
    'cyan': '0, 255, 255',
    'blue': '0, 0, 255',
    'magenta': '255, 0, 255'
}


def db_2_perc(db: float):
    return 10 ** (db / 10)


def perc_2_db(perc: float):
    return 10 * math.log10(perc)


def vol_up():
    obj = acproject.get_selected_objects('Cue')['data']
    for item in obj:
        curr_vol = float(acproject.get_value(item, 'Volume')['data'])
        new_vol = perc_2_db(curr_vol) + 1.0 if curr_vol != 0.0 else -40.0
        print(new_vol, db_2_perc(new_vol))
        acproject.set_value(item, 'Volume', min(db_2_perc(new_vol), 1.0))
    return


def vol_down():
    obj = acproject.get_selected_objects('Cue')['data']
    for item in obj:
        curr_vol = float(acproject.get_value(item, 'Volume')['data'])
        new_vol = perc_2_db(curr_vol) + 1.0 if curr_vol != 0.0 else -40.0
        print(new_vol, db_2_perc(new_vol))
        acproject.set_value(item, 'Volume', min(db_2_perc(new_vol), 1.0))
    return


def mute():
    obj = acproject.get_selected_objects('Track')['data']
    for item in obj:
        acproject.set_value(item, 'MuteFlag', True)
    return


def set_color(color: str):
    obj = acproject.get_selected_objects('Track')['data']
    for item in obj:
        acproject.set_color(item, COLOR_MAPPER[color])
    return


def set_volume(vol: str):
    vol = float(vol)
    if vol > 1.0:
        messagebox.showerror('Error', 'Please input a number in (0~1)')
    else:
        obj = acproject.get_selected_objects('Track')['data']
        for item in obj:
            acproject.set_value(item, 'Volume', vol)


def unmute():
    obj = acproject.get_selected_objects('Track')['data']
    for item in obj:
        acproject.set_value(item, 'MuteFlag', False)
    return


def unset_color():
    obj = acproject.get_selected_objects('Track')['data']
    for item in obj:
        acproject.unset_color(item)


def volume_down():
    obj = acproject.get_selected_objects('Track')['data']
    for item in obj:
        curr_vol = acproject.get_value(item, 'Volume')['data']
        new_vol = max(float(curr_vol) - 0.1, 0.0)
        acproject.set_value(item, 'Volume', new_vol)


def volume_up():
    obj = acproject.get_selected_objects('Track')['data']
    for item in obj:
        curr_vol = acproject.get_value(item, 'Volume')['data']
        new_vol = min(float(curr_vol) + 0.1, 1.0)
        acproject.set_value(item, 'Volume', new_vol)


if __name__ == '__main__':
    acconnect.initialize()
    connect_result = acconnect.connect('127.0.0.1', 9000)
    acdebug.log('Python remote connected')

    window = tk.Tk()
    window.title('Track Edit Toolbox')

    lf_volume = tk.LabelFrame(
        window,
        text='Volume'
    )
    lf_volume.grid(
        row=0,
        column=0,
        rowspan=5,
        columnspan=3,
        padx=BUTTON_PADX/2,
        pady=BUTTON_PADY,
        sticky=tk.NW
    )

    b11 = tk.Button(
        lf_volume,
        text='Mute Selected Tracks',
        width=20,
        height=2,
        command=mute
    )
    b11.grid(
        row=0,
        column=0,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b12 = tk.Button(
        lf_volume,
        text='Unmute Selected Tracks',
        width=20,
        height=2,
        command=unmute
    )
    b12.grid(
        row=4,
        column=0,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b13 = tk.Button(
        lf_volume,
        text='Volume +0.10',
        width=20,
        height=2,
        command=volume_up
    )
    b13.grid(
        row=7,
        column=0,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b14 = tk.Button(
        lf_volume,
        text='Volume -0.10',
        width=20,
        height=2,
        command=volume_down
    )
    b14.grid(
        row=10,
        column=0,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    set_vol_str = tk.StringVar()
    set_vol_label = tk.Label(
        lf_volume,
        textvariable=set_vol_str
    )
    set_vol_str.set('Set Vol')
    set_vol_label.grid(
        row=13,
        column=0,
        rowspan=3,
        padx=BUTTON_PADX/2,
        pady=BUTTON_PADY,
    )
    new_vol_update = tk.Spinbox(
        lf_volume,
        from_=0,
        to=1,
        increment=0.1
    )
    new_vol_update.grid(
        row=13,
        column=1,
        rowspan=3,
    )
    b15 = tk.Button(
        lf_volume,
        text='Update',
        width=10,
        height=2,
        command=lambda: set_volume(new_vol_update.get())
    )
    b15.grid(
        row=13,
        column=2,
        rowspan=3,
        columnspan=2,
        padx=BUTTON_PADX/2,
        pady=BUTTON_PADY,
    )

    lf_panning = tk.LabelFrame(
        window,
        text='Panning'
    )
    lf_panning.grid(
        row=0,
        column=5,
        rowspan=5,
        columnspan=5,
        padx=BUTTON_PADX/2,
        pady=BUTTON_PADY,
        sticky=tk.NW
    )

    b21 = tk.Button(
        lf_panning,
        text='Dummy',
        width=20,
        height=2
    )
    b21.grid(
        row=0,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    lf_pitch = tk.LabelFrame(
        window,
        text='Pitch'
    )
    lf_pitch.grid(
        row=0,
        column=15,
        rowspan=5,
        columnspan=5,
        padx=BUTTON_PADX/2,
        pady=BUTTON_PADY,
        sticky=tk.NW
    )

    b31 = tk.Button(
        lf_pitch,
        text='Dummy',
        width=20,
        height=2
    )
    b31.grid(
        row=0,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    lf_color = tk.LabelFrame(
        window,
        text='Color'
    )
    lf_color.grid(
        row=0,
        column=20,
        rowspan=5,
        columnspan=5,
        padx=BUTTON_PADX/2,
        pady=BUTTON_PADY,
        sticky=tk.NW
    )

    color_options = ['red', 'orange', 'yellow', 'lime green', 'cyan', 'blue', 'magenta']
    color_variable = tk.StringVar(lf_color)
    color_variable.set(color_options[0])
    color_menu = tk.OptionMenu(
        lf_color,
        color_variable,
        *color_options
    )
    color_menu.grid(
        row=0,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b41 = tk.Button(
        lf_color,
        text='Set Color',
        width=20,
        height=2,
        command=lambda: set_color(color_variable.get())
    )
    b41.grid(
        row=3,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    b42 = tk.Button(
        lf_color,
        text='Unset Color',
        width=20,
        height=2,
        command=unset_color
    )
    b42.grid(
        row=6,
        column=1,
        padx=BUTTON_PADX,
        pady=BUTTON_PADY,
        rowspan=3,
        columnspan=3
    )

    window.geometry("860x320")
    window.call('wm', 'attributes', '.', '-topmost', '1')
    window.mainloop()
