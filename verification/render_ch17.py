import subprocess
subprocess.run(["pdftoppm", "-png", "-r", "200", "docs/scans/ch17.pdf", "verification/ch17_pages/page"], check=True)
print("done")
