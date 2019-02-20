#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

dir_path = os.listdir(os.path.abspath(os.path.dirname(__file__)))

# import所有符合此正则表达式的文件
hander_files = [x for x in dir_path if re.findall('handler_+[A-Za-z]\w+\.py$', x)]

for hander_file in hander_files:
    model_name = hander_file[:-3]
    __import__(model_name, globals(), locals(), [model_name], -1)