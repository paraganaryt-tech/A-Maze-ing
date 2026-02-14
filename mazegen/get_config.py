def ft_exit(error_str):
    print(f"Error: {error_str}")
    exit(1)


def ft_get_config(file_name):
    try:
        try:
            file = open(file_name, "r")
            all_config = file.read()
            file.close()
        except Exception:
            ft_exit("Sorry Can't Open File")

        config_list = []
        for line in all_config.splitlines():
            if "#" not in line and "=" in line:
                config_list.append(line)
            else:
                tmp_spt = line.split("#")
                config_list.append(tmp_spt[0])

        item_list = []
        i = 0
        for item in config_list:
            item_list.append(item.split("="))
            try:
                item_list[i][0] = item_list[i][0].upper().strip(" ")
                item_list[i][1] = item_list[i][1].strip(" ")
            except Exception:
                continue
            i += 1

        c_dic = {
            "WIDTH": 20, "HEIGHT": 20,
            "ENTRY": [0, 0], "EXIT": [20, 20],
            "OUTPUT_FILE": "output_maze.txt", "PERFECT": True,
            "SEED": False, "ALGO": 1
            }

        validation_list = []
        for item in item_list:

            if item[0] == "WIDTH":
                c_dic['WIDTH'] = int(item[1])
                validation_list.append("WIDTH")

            elif item[0] == "HEIGHT":
                c_dic['HEIGHT'] = int(item[1])
                validation_list.append("HEIGHT")

            elif item[0] == "ENTRY":
                c_dic['ENTRY'] = item[1].split(",")
                c_dic['ENTRY'][0] = int(c_dic['ENTRY'][0])
                c_dic['ENTRY'][1] = int(c_dic['ENTRY'][1])
                validation_list.append("ENTRY")

            elif item[0] == "EXIT":
                c_dic['EXIT'] = item[1].split(",")
                c_dic['EXIT'][0] = int(c_dic['EXIT'][0])
                c_dic['EXIT'][1] = int(c_dic['EXIT'][1])
                validation_list.append("EXIT")

            elif item[0] == "OUTPUT_FILE":
                c_dic['OUTPUT_FILE'] = item[1]
                validation_list.append("OUTPUT_FILE")

            elif item[0] == "PERFECT":
                validation_list.append("PERFECT")
                if item[1].upper() == "TRUE":
                    c_dic['PERFECT'] = True
                elif item[1].upper() == "FALSE":
                    c_dic['PERFECT'] = False

            elif item[0] == "SEED":
                if item[1].upper() == "TRUE":
                    c_dic["SEED"] = True

            elif item[0] == "ALGO":
                if item[1].upper() == "PRIM":
                    c_dic["ALGO"] = 0

        if c_dic["ENTRY"][0] < 0:
            c_dic["ENTRY"][0] = 0

        if c_dic["ENTRY"][1] < 0:
            c_dic["ENTRY"][1] = 0

        if c_dic["EXIT"][1] >= c_dic["WIDTH"]:
            c_dic["EXIT"][1] = c_dic["WIDTH"] - 1

        if c_dic["EXIT"][0] >= c_dic["HEIGHT"]:
            c_dic["EXIT"][0] = c_dic["HEIGHT"] - 1

        if c_dic["WIDTH"] <= 0 or c_dic["HEIGHT"] <= 0:
            raise ValueError

        return c_dic
    except Exception as e:
        ft_exit(f"Sorry Somthing wrong pleas check your config :{e}")
