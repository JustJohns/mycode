#!/usr/bin/env python3

import shutil
import os

def main():
    # this forces python to start in home directory
    os.chdir('/home/student/mycode/')

    # this will move file/folder from source to destination
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for new name for kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj?')

    # this renames the current kerrigan.obj file
    shutil.move('ceph_storage/kerrigon.obj', 'ceph_storage/' + xname)

    main()
