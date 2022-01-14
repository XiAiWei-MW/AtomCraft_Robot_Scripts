# --Description: Import CueSheet, Cue, Track and Block from a CSV file

### To use the read_excel function, please install openpyxl

import sys
import os
import pandas as pd
import cri.atomcraft.project
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# --BeginUserVariable
"""
XLSX_PATH:
  type:string
  comment:File Location
CURR_WORKUNIT:
  type:object
  comment:Current Work Unit
"""
XLSX_PATH = ""
CURR_WORKUNIT = None
# --EndUserVariable

# Check CSV Path
if not os.path.isfile(XLSX_PATH):
    acdebug.log('XLSX file not found：' + XLSX_PATH)
    sys.exit()


material_rootfolder = acproject.get_material_rootfolder(CURR_WORKUNIT)['data']
cuesheet_rootfolder = acproject.get_cuesheet_rootfolder(CURR_WORKUNIT)['data']
cuesheet_name = os.path.splitext(os.path.basename(XLSX_PATH))[0]
cuesheet = acproject.create_object(cuesheet_rootfolder, 'CueSheet', cuesheet_name)['data']

data = pd.read_excel(XLSX_PATH, sheet_name=None)

for cue_name, cue_data in data.items():
    cue = acproject.create_object(cuesheet, 'Cue', cue_name)['data']
    pre_length = 0.0
    for row in cue_data.iterrows():
        track_name, location, is_loop, divisions = row[1][0], row[1][1], row[1][2], row[1][3]

        if not os.path.isfile(location):
            acdebug.log('Material file not found: ' + location)
            sys.exit()

        acdebug.log('Now processing: ' + track_name)
        material = acproject.register_material(material_rootfolder, location)['data']
        sample_frames = int(acproject.get_value(material, 'SampleFrames')['data'])
        sampling_rate = int(acproject.get_value(material, 'SamplingRate')['data'])
        curr_length = sample_frames / sampling_rate * 1000

        track = acproject.create_object(cue, 'Track', track_name)['data']
        wave = acproject.create_waveform_region(track, material)['data']
        acproject.set_value(wave, 'DelayTimeMS', pre_length)

        block = acproject.create_object(cue, 'Block', 'B' + track_name)['data']
        if is_loop == 'T':
            acproject.set_value(block, 'BlockTransitionTiming', 'Division')
            acproject.set_value(block, 'BlockPlaybackLoopNum', -1)
            acproject.set_value(block, 'BlockDivisionNum', divisions)

        pre_length += curr_length

acdebug.log('All finished')
