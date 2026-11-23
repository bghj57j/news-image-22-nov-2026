# Copies the pre-built 1024x1024 news image to the output directory.
# The image sums up Sunday 22 November 2026 world news in six stories.
import os
import shutil

SRC = os.path.join(os.path.dirname(__file__), "entry.png")
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
shutil.copyfile(SRC, os.path.join(out, "entry.png"))
