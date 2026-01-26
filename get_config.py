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
            "OUTPUT_FILE": "", "PERFECT": ""
            }
        for item in item_list:

            if item[0] == "WIDTH":
                config_dic['WIDTH'] = item[1]

            elif item[0] == "HEIGHT":
                config_dic['HEIGHT'] = item[1]

            elif item[0] == "ENTRY":
                config_dic['ENTRY'] = item[1]

            elif item[0] == "EXIT":
                config_dic['EXIT'] = item[1]

            elif item[0] == "OUTPUT_FILE":
                config_dic['OUTPUT_FILE'] = item[1]

            elif item[0] == "PERFECT":
                config_dic['PERFECT'] = item[1]

    except Exception:
        ft_exit("Sorry Somthing wrong")
