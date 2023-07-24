# --- Init file ---
import sys

import_paths = [
    "/pyscript_modules",
    "/device_info"
]

for p in import_paths:
    full_path = "/config" + p

    if full_path not in sys.path:
        sys.path.append(full_path)