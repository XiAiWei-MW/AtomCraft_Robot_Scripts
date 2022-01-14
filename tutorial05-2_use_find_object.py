# --Description:[教程]使用find_object函数＆批量设置波形区域的Voice限数组

import sys
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# 获取Voice限数组文件夹
voicelimit_group_folder  = acproject.get_global_folder("VoiceLimitGroupFolder")["data"]

# 获取Voice限数组“VoiceLimitGroup_0”
voicelimit_group = acproject.get_child_object(voicelimit_group_folder, "VoiceLimitGroup", "VoiceLimitGroup_0")["data"]

# 获取工作单元
workunit = acproject.get_workunit("WorkUnit_Tutorial")["data"]

# 使用find_objects来获得CueSheet中的波形区域列表
waveformRegions = acproject.find_objects(workunit, "WaveformRegion")["data"]

# 用for循环从波形区域列表中逐一获取波形区域
for region in waveformRegions:
    # 在波形区域设置Voice限数组
    acproject.set_value(region, "VoiceLimitGroup", voicelimit_group)

acdebug.log("[教程]使用find_objects函数&波形区域设置Voice限数组运行完毕")
