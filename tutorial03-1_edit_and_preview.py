# --Description:[教程]参数值的变更和Cue预览

import cri.atomcraft.project as acproject
import cri.atomcraft.preview as acpreview

# 获取工作单元
workunit = acproject.get_workunit("WorkUnit_Tutorial")["data"]

# 获取CueSheet根文件夹
cuesheet_rootfolder = acproject.get_cuesheet_rootfolder(workunit)["data"]

# 获取CueSheet文件夹“WorkUnit_Tutorial”
cuesheet_folder = acproject.get_child_object(cuesheet_rootfolder, "CueSheetFolder", "WorkUnit_Tutorial")["data"]

# 获取CueSheet
cue_sheet = acproject.get_child_object(cuesheet_folder, "CueSheet", "Tutorial")["data"]

# 获取Cue
cue = acproject.get_child_object(cue_sheet, "Cue", "gun1_High")["data"]

# 变更Cue的音量
acproject.set_value(cue, "Volume", 0.5)

# 播放Cue
acpreview.start_playback_cue(cue)