"""Run a lens-design script with a working optiland import.

If the environment's optiland install is an editable package pointing at a
stale path, the import fails; this launcher falls back to a local checkout
(set OPTILAND_SRC to override the default location).

    env -u PYTHONPATH python3 build/lens_designs/run.py \
        build/lens_designs/ch23_microscope/ch23_microscope_system.py
"""
import os
import runpy
import sys
from pathlib import Path

try:
    import optiland  # noqa: F401
except ModuleNotFoundError:
    if "OPTILAND_SRC" not in os.environ:
        sys.exit("optiland not importable; set OPTILAND_SRC to a local optiland checkout")
    sys.path.insert(0, os.environ["OPTILAND_SRC"])
    import optiland  # noqa: F401

script = Path(sys.argv[1]).resolve()
sys.argv = sys.argv[1:]
sys.path.insert(0, str(script.parent))
runpy.run_path(str(script), run_name="__main__")
