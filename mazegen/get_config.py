import sys
import os
from typing import Dict, Any


def ft_exit(error_str: str) -> None:
    """
    Prints error and exits.
    """
    print(f"Error: {error_str}")
    sys.exit(1)


def ft_get_config(file_name: str) -> Dict[str, Any]:
    """
    Parses config file.
    """
    try:
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
        except (OSError, PermissionError):
            ft_exit("Sorry Can't Open File")

        c_dic: Dict[str, Any] = {
            "WIDTH": 0, "HEIGHT": 0,
            "ENTRY": [0, 0], "EXIT": [0, 0],
            "OUTPUT_FILE": "output_maze.txt", "PERFECT": True,
            "SEED": [False], "ALGO": 1
        }

        w_check = 0
        h_check = 0
        e_check = 0
        x_check = 0
        o_check = 0

        for line in lines:
            line = line.split("#")[0].strip()
            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip().upper()
            val = value.strip()

            if key == "WIDTH":
                w_check = 1
                c_dic['WIDTH'] = int(val)
            elif key == "HEIGHT":
                h_check = 1
                c_dic['HEIGHT'] = int(val)
            elif key == "ENTRY":
                e_check = 1
                coords = val.split(",")
                c_dic['ENTRY'] = [int(coords[0]), int(coords[1])]
            elif key == "EXIT":
                x_check = 1
                coords = val.split(",")
                c_dic['EXIT'] = [int(coords[0]), int(coords[1])]
            elif key == "OUTPUT_FILE":
                o_check = 1
                c_dic['OUTPUT_FILE'] = val
            elif key == "PERFECT":
                if val.upper() == "TRUE":
                    c_dic['PERFECT'] = True
                elif val.upper() == "FALSE":
                    c_dic['PERFECT'] = False
                else:
                    raise ValueError("invalid input")
            elif key == "SEED":
                c_dic["SEED"] = [True, int(val)]
            elif key == "ALGO":
                if val.upper() == "PRIM":
                    c_dic["ALGO"] = 0
                elif val.upper() == "DFS":
                    c_dic["ALGO"] = 1
                else:
                    raise ValueError("invalid input for algo name")

        check_list = [w_check, h_check, e_check, x_check, o_check]
        for item in check_list:
            if item == 0:
                raise ValueError("the config file are not completed")

        if c_dic["WIDTH"] <= 0 or c_dic["HEIGHT"] <= 0:
            raise ValueError("Dimensions must be positive")

        w, h = c_dic["WIDTH"], c_dic["HEIGHT"]
        if c_dic["ENTRY"][0] >= h or c_dic["ENTRY"][1] >= w:
            raise ValueError("Entry out of range")
        if c_dic["ENTRY"][0] < 0 or c_dic["ENTRY"][1] < 0:
            raise ValueError("Entry out of range")
        if c_dic["EXIT"][0] >= h or c_dic["EXIT"][1] >= w:
            raise ValueError("Entry out of range")
        if c_dic["EXIT"][0] < 0 or c_dic["EXIT"][1] < 0:
            raise ValueError("Entry out of range")

        entry_cordt = (c_dic["ENTRY"][0], c_dic["ENTRY"][1])
        exit_cordt = (c_dic["EXIT"][0], c_dic["EXIT"][1])
        if entry_cordt == exit_cordt:
            raise ValueError("Cordinates wrong!")

        try:
            o_file = open(c_dic["OUTPUT_FILE"], "w")
            o_file.write(" ")
            os.system(f"rm -f {c_dic['OUTPUT_FILE']}")
            os.system("clear")
        except BaseException:
            ft_exit("Sorry can't open the file")
        return c_dic

    except ValueError as e:
        ft_exit(f"Config Error: {e}")
        return {}
    except Exception as e:
        ft_exit(f"Unexpected Error: {e}")
        return {}
