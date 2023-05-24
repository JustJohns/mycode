#!/usr/bin/env python3

# The following line will create the directory if it does not exist already

# import additional code
import shutil
import os

def main():
    # move into working directory
    os.chdir("/home/student/mycode/")

    # copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copy entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

    main()

