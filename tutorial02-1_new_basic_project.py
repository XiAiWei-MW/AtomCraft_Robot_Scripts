# --Description:[教程]基本回放数据的创建和存储

import sys
import os
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# 项目名称
project_name = "Project_Tutorial"

# 项目保存位置
projects_dir = os.path.expanduser('~/Documents/CRIWARE/CriAtomCraft/projects')
if not os.path.isdir(projects_dir):
    os.makedirs(projects_dir)

# 教程用声音素材的位置
data_dir = os.path.dirname(os.path.dirname(__file__)) + '/tutorial_data'

# 创建项目
result = acproject.create_project(projects_dir, project_name, True)
if not result["succeed"]:
    acdebug.warning("Failed Create Project")
    sys.exit()

# 创建工作单元
result = acproject.create_workunit("WorkUnit_Tutorial", True, None)
if not result["succeed"]:
    acdebug.warning("Failed Create WorkUnit")
    sys.exit()

# 取得工作单元的信息
workunit = result["data"]

# 获取素材根文件夹
material_root_folder = acproject.get_material_rootfolder(workunit)["data"]

# 将波形文件注册到素材根文件夹中
material = acproject.register_material(material_root_folder, data_dir+"/tutorial_data01/gun1_High.wav")["data"]


# ----- CueSheet的创建 -----
# 获取CueSheet文件夹
cuesheet_rootfolder = acproject.get_cuesheet_rootfolder(workunit)["data"]

# 获取CueSheet文件夹“WorkUnit_Tutorial”
cuesheet_folder = acproject.get_child_object(cuesheet_rootfolder, "CueSheetFolder", "WorkUnit_Tutorial")["data"]

# 在CueSheet文件夹中创建CueSheet
cuesheet = acproject.create_object(cuesheet_folder, "CueSheet", "Tutorial")["data"]


# ----- Cue，音轨和波形区域的创建 -----
# 创建Cue
cue = acproject.create_object(cuesheet, "Cue", "gun1_High")["data"]

# 创建音轨
track = acproject.create_object(cue, "Track", "Track")["data"]

# 用指定素材创建波形区域
waveform_region = acproject.create_waveform_region(track, material)["data"]


# ----- 保存项目 -----
result = acproject.save_project_all()

# 如果保存失败，则输出一个警告信息
if not result["succeed"]:
    acdebug.warning("项目保存失败")