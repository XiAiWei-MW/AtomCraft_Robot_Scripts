# --Description:[教程]使用用户变量来改变Cue的“音高”参数

import cri.atomcraft.project
import cri.atomcraft.project as acproject
import cri.atomcraft.debug as acdebug

# --BeginUserVariable
"""
VARIABLE_CUE:
  type:object
  comment:将要改变参数的Cue
VARIABLE_PARAMETER_NAME:
  type:string
  comment:参数名
VARIABLE_PARAMETER_VALUE:
  type:number
  comment:参数值
"""
VARIABLE_CUE = cri.atomcraft.project.get_object_from_path("/WorkUnits/WorkUnit_Tutorial/CueSheetFolder/WorkUnit_Tutorial/Tutorial/gun1_High")["data"]
VARIABLE_PARAMETER_NAME = "Pitch"
VARIABLE_PARAMETER_VALUE = 100
# --EndUserVariable

acproject.set_value(VARIABLE_CUE, VARIABLE_PARAMETER_NAME, VARIABLE_PARAMETER_VALUE)

acdebug.log("音高参数的更改已结束")
