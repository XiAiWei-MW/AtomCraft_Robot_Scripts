# --Description:[教程]使用CSV创建CueSheet

import sys
import os
import csv
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# 设置音频数据文件夹和要导入的CSV文件的路径
# 音频数据文件夹路径
data_dir = os.path.dirname(os.path.dirname(__file__)) + '/tutorial_data/tutorial_data03'

# CSV文件路径
csv_path = data_dir + "/tutorial_data3.csv"

# CSV文件路径检查
if os.path.isfile(csv_path) == False:
    acdebug.log("CSV文件未找到: " + csv_path)
    sys.exit()

# 获取Work Unit
workunit = acproject.get_workunit("WorkUnit_Tutorial")["data"]
material_root_folder = acproject.get_material_rootfolder(workunit)["data"]

# CueSheet根目录文件夹
cuesheet_rootfolder = acproject.get_cuesheet_rootfolder(workunit)["data"]

# 创建CueSheet
cuesheet_name = os.path.splitext(os.path.basename(csv_path))[0]
cuesheet = acproject.create_object(cuesheet_rootfolder, "CueSheet", cuesheet_name)["data"]

# 打开并读取CSV文件
with open(csv_path) as f:
    reader = csv.reader(f)
    for row in reader:
        wave_file_path = "" # 储存波形文件路径
        row_params = {}     # 储存Cue的参数信息

        # 获取CSV的列
        wave_file_path = data_dir + "/" + row[0]  # 波形文件名
        row_params["Name"] = row[1]               # Cue名称
        row_params["CueID"] = row[2]              # Cue ID
        row_params["Comment"] = row[3]            # 备注

        # 注册波形文件并新建素材
        material = acproject.register_material(material_root_folder, wave_file_path)["data"]
        # 生成Cue
        cue = acproject.create_simple_cue(cuesheet, material)["data"]
        # 设定Cue的Cue名，Cue ID和备注
        acproject.set_values(cue, row_params)
acdebug.log("[教程]CueSheet生成结束")

# 保存项目
result = acproject.save_project_all()
if not result["succeed"]:
    acdebug.warning("工程保存失败。")
