from fastapi import APIRouter
import subprocess
import sys
import os

router = APIRouter()

LAB_BASE = "python_course/labs"

def run_lab(path: str):
    """Run a lab's main.py and return output."""
    full = os.path.join(LAB_BASE, path, "main.py")
    if not os.path.exists(full):
        return {"error": f"Lab not found: {full}"}

    try:
        result = subprocess.run(
            [sys.executable, full],
            capture_output=True,
            text=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return {"error": str(e)}

@router.get("/labs")
def list_labs():
    """Return a list of available labs."""
    labs = sorted(os.listdir(LAB_BASE))
    return {"labs": labs}

@router.get("/run/{lab_name}")
def run_lab_endpoint(lab_name: str):
    """Run a specific lab."""
    return run_lab(lab_name)
