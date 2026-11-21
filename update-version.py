#!/usr/bin/env python3
import re
import sys
from datetime import datetime
from pathlib import Path

for name in sys.argv[1:]:
    path = Path(name)
    text = path.read_text()
    version = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y%m%d%H%M%S")
    updated, count = re.subn(r"(?m)^([#!] Version: ).*$", rf"\g<1>{version}", text)
    if count != 1:
        raise SystemExit(f"{path}: expected one Version line, found {count}")
    path.write_text(updated)
