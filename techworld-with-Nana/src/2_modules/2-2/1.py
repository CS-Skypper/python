import os
import logging # handle error messages or warnings

# to open the files Ctrl+Alt+Click
#  go to the root of os, from where it is imported


print(os.name)


logger = logging.getLogger("MAIN")
logger.error("If you see this know that Task failed successfully!")

