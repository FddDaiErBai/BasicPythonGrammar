# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.04.09
"""

import traceback

try:
    print(10/0)

except:
    traceback.print_exc()