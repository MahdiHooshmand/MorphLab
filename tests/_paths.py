# Adds registry/experiment source folders to sys.path so test files can
# `import` device modules directly, plus the mocks/ folder so `import machine`
# resolves to the host stub instead of failing.
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _p in [
    os.path.join(_ROOT, "tests", "mocks"),
    os.path.join(_ROOT, "registry", "drivers", "esp32_micropython"),
    os.path.join(_ROOT, "registry", "components"),
    os.path.join(_ROOT, "experiments", "project-001", "mechanism"),
]:
    if _p not in sys.path:
        sys.path.insert(0, _p)
