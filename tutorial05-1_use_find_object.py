# --Description:[教程]使用find_object函数＆批量注册复数波形文件

import os
import glob
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# 获取波形文件列表
# 获取教程波形素材文件夹'tutorial_data/tutorial_data02'的路径
data_dir = os.path.dirname(os.path.dirname(__file__)) + '/tutorial_data/tutorial_data02'

# 使用glob获取data_dir内的文件
files = glob.glob(data_dir + '/*')
if len(files) == 0:
    acdebug.warning(data_dir + "内没有文件")
    sys.exit()

# 获取注册了音频文件的工作单元
workunit = acproject.get_workunit("WorkUnit_Tutorial")["data"]

# 获取注册了音频文件的素材文件夹
material_root_folder = acproject.get_material_rootfolder(workunit)["data"]

# 获取创建了Cue的CueSheet
cuesheet = acproject.find_object(workunit, "CueSheet", "Tutorial")["data"]

for file in files:
    # 在素材根目录下注册波形文件，并创建一个素材
    material = acproject.register_material(material_root_folder, file)["data"]
    # 从素材信息中创建一个Cue
    acproject.create_simple_cue(cuesheet, material)

# 保存项目
result = acproject.save_project_all()
if not result["succeed"]:
    acdebug.warning("项目文件保存失败。")

acdebug.log("[教程]使用find_object函数完成了文件夹中多个音频文件的批量注册。")
