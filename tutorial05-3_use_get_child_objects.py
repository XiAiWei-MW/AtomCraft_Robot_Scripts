# --Description:[教程]使用get_child_objects函数来获取Cue，并根据命名规则设置类别

import sys
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# 为Cue准备将要设定的类别
# 获取类别文件夹
category_folder = acproject.get_global_folder("CategoryFolder")["data"]

# 获取类别
category = acproject.find_object(category_folder, "Category", "Category_0")["data"]

# 变更类别名
acproject.set_value(category, "Name", "sfx")

# 获取工作单元
workunit = acproject.get_workunit("WorkUnit_Tutorial")["data"]

# 获取CueSheet
cuesheet = acproject.find_object(workunit, "CueSheet", "Tutorial")["data"]

# 获取CueSheet正下方的多个Cue
cues = acproject.get_child_objects(cuesheet, "Cue")["data"]

# 需要设定类别的Cue列表

# 包含了名称以 "sfx "开头的Cue的列表
cues_for_set_categories = []

## 检查对象的Cue
for cue in cues:
    # 获取Cue名称
    cue_name = acproject.get_value(cue, "Name")["data"]
    # 使用字符串函数startswith来检查字符串的开头是否包含sfx字符
    if cue_name.startswith('sfx') == True:  # Cue名称包含“sfx”
        # 添加到列表中
        cues_for_set_categories.append(cue)

# 设定类别
# 批量更改类别的情况下使用add_category_to_cues
acproject.add_category_to_cues(cues_for_set_categories, category)

acdebug.log("[教程]使用get_child_objects函数获得Cue，并根据命名规则设定了类别")
