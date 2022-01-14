# --Description:[教程]输出游戏数据（ACF，ACB）

import cri.atomcraft.project as acproject
import cri.atomcraft.build as acbuild

# 获取工作单元
workunit = acproject.get_workunit("WorkUnit_Tutorial")["data"]

# 获取CueSheet
cuesheet_rootfolder = acproject.get_cuesheet_rootfolder(workunit)["data"]

# 获取CueSheet文件夹“WorkUnit_Tutorial”
cuesheet_folder = acproject.get_child_object(cuesheet_rootfolder, "CueSheetFolder", "WorkUnit_Tutorial")["data"]

# 获取CueSheet
cue_sheet = acproject.get_child_object(cuesheet_folder, "CueSheet", "Tutorial")["data"]

# 获取目标配置文件夹
target_config_folder = acproject.get_global_folder("TargetConfigFolder")["data"]

# 获取PC平台的设置
target_config_pc = acproject.get_child_object(target_config_folder, "TargetConfigPc", "PC")["data"]

print("CueSheet“Tutorial”开始构建")
result = acbuild.build_cuesheet(cuesheet, target_config_pc, None)["succeed"]

if result == True:
    print("Script Msg：CueSheet“Tutorial”构建完毕")
else:
    print("Script Msg：CueSheet“Tutorial”构建失败")