# --Description:[教程]使用CSV检查未注册的Cue

import sys
import os
import csv
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# CSV文件地址
csv_path = os.path.dirname(os.path.dirname(__file__)) + '/tutorial_data/tutorial_data03/tutorial_data3.csv'

# 检查CSV文件是否存在
if os.path.isfile(csv_path) == False:
    acdebug.warning("无法找到CSV文件: " + csv_path)
    sys.exit()

# 获取CueSheet内已经注册的Cue
cuesheet = acproject.find_object(workunit, "CueSheet", "tutorial_data3")["data"]
cues = acproject.get_child_objects(cuesheet, "Cue")["data"]
registered_cue_name_list = [acproject.get_value(cue, "Name")["data"] for cue in cues]

# 打开CSV文件并检查CueSheet中的Cue
acdebug.log("正在使用tutorial_data3.csv检查Cue")
unregistered_cue_name_list = []
with open(csv_path) as f:
    reader = csv.reader(f)
    for row in reader:
        # 获取CSV的Cue列表
        cue_name = row[1]
        # 检查CSV中记录的Cue是否已经被注册完毕
        if not cue_name in registered_cue_name_list:
            # 如果没有被注册的话
            unregistered_cue_name_list.append(cue_name)

# 检查
if len(unregistered_cue_name_list) > 0:
    acdebug.warning(cuesheet_name + "中有未注册的Cue")
    for cue_name in unregistered_cue_name_list:
        acdebug.warning("Cue " + cue_name + "未找到")
else:
    acdebug.log("检查完毕，没有异常")
acdebug.log("[教程]Cue的注册情况检查完毕")
