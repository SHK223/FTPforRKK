import os
import time
import ruamel.yaml
import sys

def analyse():
    yaml = ruamel.yaml.YAML()
    with open("ini.yaml") as iniFile:
        yamlF = yaml.load(iniFile)
        for sysId in yamlF["LoadList"]:
            listsys.append(sysId)
        print(sysId)

        if yamlF[sysId]["Ip"] != '127.0.0.1':
            yamlF[sysId]["Ip"] = '127.0.0.1'
        if yamlF[sysId]["Port"] != 7777:
            yamlF[sysId]["Port"] = 7777
    with open("ini.yaml","w") as iniFile:
        yaml.dump(yamlF, iniFile)

    path_to_watch = yamlF[sysId]["LogDir"]
    before = dict ([(f, None) for f in os.listdir (path_to_watch)])

    while 1:
        time.sleep (5)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]

        if added:
            with open("answer.txt", "a") as file:
                file.write("Completed /n")
            break
        if removed:
            file.write("Removed: ", ", ".join(removed))
        before = after
