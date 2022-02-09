# --Description: Output all REACT information to a CSV file

import csv
import sys
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# --BeginUserVariable
"""
OUTPUT_FOLDER:
  type: string
  comment: Output CSV folder path.
"""
OUTPUT_FOLDER = ""
# --EndUserVariable

if __name__ == "__main__":
	basic = ["Name", "ReactType", "ChangeCategory", "TriggerCategory"]
	ducker = [
		"ChangeTime",
		"ChangeCurveType",
		"ChangeCurveStrength",
		"HoldType",
		"HoldTime",
		"ReturnTime",
		"ReturnCurveType",
		"ReturnCurveStrength",
		"ChangeParameter",
		"Level"
	]
	aisac = [
		"ChangeAisacModKeyFlag",
		"ChangeAisacModKey",
		"ReturnAisacModKeyFlag",
		"ReturnAisacModKey"
	]
	content = []

	# Get all REACT objects
	react_folder  = acproject.get_global_folder("ReactFolder")["data"]
	objs = acproject.get_child_objects(react_folder, "React")["data"]

	# Write data to CSV file
	with open(OUTPUT_FOLDER + "react_output_result.csv", "w", encoding="UTF8", newline="") as file:
		# Header
		writer = csv.writer(file)
		writer.writerow(basic + ducker + aisac)

		# Get values
		for obj in objs:
			result_basic = acproject.get_values(obj, basic)["data"]
			value_basic = [val for _, val in result_basic.items()]
			value_ducker = [val for _, val in acproject.get_values(obj, ducker)["data"].items()] \
				if result_basic["ReactType"] == "Ducker" \
				else ["" for _ in range(10)]
			value_aisac = [val for _, val in acproject.get_values(obj, aisac)["data"].items()] \
				if result_basic["ReactType"] == "AisacModTrigger" \
				else ["" for _ in range(4)]

			writer.writerow(value_basic + value_ducker + value_aisac)
