# import os
# from settings import db_path
# def AbtolutePath(table):
#     return os.path.join(db_path,table)

import os
from settings import db_path
def getAbtolutePath(table):
    return os.path.join(db_path,table)