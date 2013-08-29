#!/usr/bin/env python
# coding:utf-8
# startfirefox.py
# Author: Wang Wei Qiang <wwqgtxx@gmail.com>

import os
import sys
import shutil
from common import FileUtil

def main():
	dir = FileUtil.cur_file_dir()
	os.chdir(dir)
	if FileUtil.has_file('FirefoxPortable/FirefoxPortable.exe'):
		os.system('start ./FirefoxPortable/FirefoxPortable.exe  -no-remote "https://greatagent-ifanqiang.googlecode.com/git-history/web/ifanqiang2.htm"')
	else:
		print "Don't Have FirefoxPortable"
		FileUtil.delete_dir("FirefoxPortable")



if __name__ == '__main__':
	main()