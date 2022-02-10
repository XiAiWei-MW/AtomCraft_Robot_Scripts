# --Description: Output the project tree information to a CSV file

import csv
import sys
import cri.atomcraft.debug as acdebug
import cri.atomcraft.project as acproject

# --BeginUserVariable
"""
OUTPUT_FOLDER:
  type:string
  comment:Output CSV folder path.
"""
OUTPUT_FOLDER = "D:/"
# --EndUserVariable

if __name__ == "__main__":
    # Get all global folders
    global_folder = acproject.get_global_folder("GlobalFolder")["data"]
    target_config_folder = acproject.get_global_folder("TargetConfigFolder")["data"]
    language_settings_folder = acproject.get_global_folder("LanguageSettingsFolder")["data"]
    mixer_folder = acproject.get_global_folder("MixerFolder")["data"]
    category_folder = acproject.get_global_folder("CategoryFolder")["data"]
    react_folder = acproject.get_global_folder("ReactFolder")["data"]
    voice_limit_group_folder = acproject.get_global_folder("VoiceLimitGroupFolder")["data"]
    aisac_control_folder = acproject.get_global_folder("AisacControlFolder")["data"]
    global_aisac_folder = acproject.get_global_folder("GlobalAisacFolder")["data"]
    game_variable_folder = acproject.get_global_folder("GameVariableFolder")["data"]
    selector_folder = acproject.get_global_folder("SelectorFolder")["data"]

    # Open CSV file
    with open(OUTPUT_FOLDER + "project_tree_output_result.csv", "w", encoding="UTF8", newline="") as file:
        # Header
        writer = csv.writer(file)

        # Target Config
        tc = [
            "TargetConfigPc",
            "TargetConfigPs4",
            "TargetConfigXboxOne",
            "TargetConfigSwitch",
            "TargetConfigiPhone",
            "TargetConfigAndroid",
            "TargetConfigWebGl",
            "TargetConfigPublic"
        ]
        for tc_type in tc:
            tc_result = acproject.get_child_objects(target_config_folder, tc_type)["data"]
            if tc_result:
                for item in tc_result:
                    writer.writerow(["TargetConfigFolder", item, tc_type])

        # Language Settings
        ls_result = acproject.get_child_objects(language_settings_folder, "LanguageSettings")["data"]
        for item in ls_result:
            writer.writerow(["LanguageSettings", item])

        # Mixer Folder
        mf_result = acproject.get_child_objects(mixer_folder, "Mixer")["data"]
        for item in mf_result:
            mixer_name = acproject.get_value(item, "Name")["data"]
            snapshots = acproject.get_child_objects(item, "MixerSnapshot")["data"]
            for ss in snapshots:
                writer.writerow(["MixerSnapshot", ss, mixer_name, acproject.get_value(ss, "Name")["data"]])

        ## BusMap
        #bm_result = acproject.get_child_objects(global_folder, "BusMap")["data"]
        # TODO

        # Category Folder
        cf_result = acproject.get_child_objects(category_folder, "CategoryGroup")["data"]
        for group in cf_result:
            group_name = acproject.get_value(group, "Name")['data']
            categories = acproject.get_child_objects(group, "Category")["data"]
            for category in categories:
                writer.writerow(["Category", category, group_name, acproject.get_value(category, "Name")["data"]])

        # REACT Folder
        react_result = acproject.get_child_objects(react_folder, "React")["data"]
        for react in react_result:
            writer.writerow(["REACT", react, acproject.get_value(react, "Name")["data"]])

        # Voice Limit Group
        vlg_result = acproject.get_child_objects(voice_limit_group_folder, "VoiceLimitGroup")["data"]
        for vlg in vlg_result:
            writer.writerow(["VoiceLimitGroup", vlg, acproject.get_value(vlg, "Name")["data"]])

        # AISAC Control Folder
        asf_result = acproject.get_child_objects(aisac_control_folder, "AisacControl")["data"]
        for aisac in asf_result:
            writer.writerow(["AisacControl", aisac, acproject.get_value(aisac, "Name")["data"]])

        # Global Aisac Folder
        gaf_result = acproject.get_child_objects(global_aisac_folder, "Aisac")["data"]
        for item in gaf_result:
            writer.writerow(["Global AISACs", item, acproject.get_value(item, "Name")["data"]])

        # Game Variables
        gvar_result = acproject.get_child_objects(game_variable_folder, "GameVariable")["data"]
        for item in gvar_result:
            writer.writerow(["GameVariable", item, acproject.get_value(item, "Name")["data"]])

        # Selector
        sel_result = acproject.get_child_objects(selector_folder, "Selector")["data"]
        for item in sel_result:
            sel_name = acproject.get_value(item, "Name")["data"]
            labels = acproject.get_child_objects(item, "SelectorLabel")["data"]
            for label in labels:
                writer.writerow(["SelectorLabel", label, sel_name, acproject.get_value(label, "Name")["data"]])
