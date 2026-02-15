import sys
from typing import Dict, Any


def ft_exit(error_str: str) -> None:
    print(f"Error: {error_str}")
    sys.exit(1)


def ft_get_config(file_name: str) -> Dict[str, Any]:
    try:
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
        except (OSError, PermissionError):
            ft_exit("Sorry Can't Open File")

        c_dic: Dict[str, Any] = {
            "WIDTH": 20, "HEIGHT": 20,
            "ENTRY": [0, 0], "EXIT": [20, 20],
            "OUTPUT_FILE": "output_maze.txt", "PERFECT": True,
            "SEED": False, "ALGO": 1
        }

        for line in lines:
            line = line.split("#")[0].strip()
            if not line or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip().upper()
            val = value.strip()

            if key == "WIDTH":
                c_dic['WIDTH'] = int(val)
            elif key == "HEIGHT":
                c_dic['HEIGHT'] = int(val)
            elif key == "ENTRY":
                coords = val.split(",")
                c_dic['ENTRY'] = [int(coords[0]), int(coords[1])]
            elif key == "EXIT":
                coords = val.split(",")
                c_dic['EXIT'] = [int(coords[0]), int(coords[1])]
            elif key == "OUTPUT_FILE":
                c_dic['OUTPUT_FILE'] = val
            elif key == "PERFECT":
                c_dic['PERFECT'] = (val.upper() == "TRUE")
            elif key == "SEED":
                c_dic["SEED"] = (val.upper() == "TRUE")
            elif key == "ALGO":
                if val.upper() == "PRIM":
                    c_dic["ALGO"] = 0
                else:
                    c_dic["ALGO"] = 1

        if c_dic["WIDTH"] <= 0 or c_dic["HEIGHT"] <= 0:
            raise ValueError("Dimensions must be positive")

        w, h = c_dic["WIDTH"], c_dic["HEIGHT"]
        c_dic["ENTRY"][0] = max(0, min(c_dic["ENTRY"][0], h - 1))
        c_dic["ENTRY"][1] = max(0, min(c_dic["ENTRY"][1], w - 1))
        c_dic["EXIT"][0] = max(0, min(c_dic["EXIT"][0], h - 1))
        c_dic["EXIT"][1] = max(0, min(c_dic["EXIT"][1], w - 1))

        entry_cordt = (c_dic["ENTRY"][0], c_dic["ENTRY"][1])
        exit_cordt = (c_dic["EXIT"][0], c_dic["EXIT"][1])
        if entry_cordt == exit_cordt:
            raise ValueError("Cordinates combined!")

        return c_dic

    except ValueError as e:
        ft_exit(f"Config Error: {e}")
        return {}
    except Exception as e:
        ft_exit(f"Unexpected Error: {e}")
        return {}
