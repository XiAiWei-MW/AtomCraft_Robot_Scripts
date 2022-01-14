# --Description:[教程]检索当前选中的Cue，并批量改变它们的音量

import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# 获取选中的Cue
selected_cues = acproject.get_selected_objects("Cue")["data"]

# 获取Cue的当前音量值，并设置一个新的音量
for cue in selected_cues:
    # 取得Cue的音量
    val = acproject.get_value(cue, "Volume")["data"]
    volume = float(val)
    # 将音量设定为增加了0.5之后的新值
    acproject.set_value(cue, "Volume", volume + 0.5)

acdebug.log("音量变更完毕")
