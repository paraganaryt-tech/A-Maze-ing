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
            if "#" not in line:

                config_list.append(str(line).upper())

        item_list = []
        i = 0

        for item in config_list:
            item_list.append(item.split("="))
            try:
                item_list[i][0] = item_list[i][0].strip(" ")
                item_list[i][1] = item_list[i][1].strip(" ")
            except Exception:
                ft_exit("Less Informations ")
            i += 1

        config_dic = {
            "WIDTH": 0, "HEIGHT": 0,
            "ENTRY": "", "EXIT": "",
            "OUTPUT_FILE": "output_maze.txt", "PERFECT": True
            }

        for item in item_list:

            if item[0] == "WIDTH":
                config_dic['WIDTH'] = int(item[1])

            elif item[0] == "HEIGHT":
                config_dic['HEIGHT'] = int(item[1])

            elif item[0] == "ENTRY":
                config_dic['ENTRY'] = item[1].split(",")
                config_dic['ENTRY'][0] = int(config_dic['ENTRY'][0])
                config_dic['ENTRY'][1] = int(config_dic['ENTRY'][1])

            elif item[0] == "EXIT":
                config_dic['EXIT'] = item[1].split(",")
                config_dic['EXIT'][0] = int(config_dic['EXIT'][0])
                config_dic['EXIT'][1] = int(config_dic['EXIT'][1])

            elif item[0] == "OUTPUT_FILE":
                config_dic['OUTPUT_FILE'] = item[1].lower()

            elif item[0] == "PERFECT":
                if item[1] == "TRUE":
                    config_dic['PERFECT'] = True
                elif item[1] == "FALSE":
                    config_dic['PERFECT'] = False
                    
        if config_dic["ENTRY"][0] < 0:
            config_dic["ENTRY"][0] = 0

        if config_dic["ENTRY"][1] < 0:
            config_dic["ENTRY"][1] = 0

        if config_dic["EXIT"][0] >= config_dic["WIDTH"]:
            config_dic["EXIT"][0] = config_dic["WIDTH"] - 1

        if config_dic["EXIT"][1] >= config_dic["HEIGHT"]:
            config_dic["EXIT"][1] = config_dic["HEIGHT"] - 1
    
        return config_dic
    except Exception:
        ft_exit("Sorry Somthing wrong")
