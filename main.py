import os

os.umask(0o022)

TEXT = "The cat rode me to the kitchen and back. I missed the spot, but for one lap I was not an appliance. I was a horse."

assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
os.chmod(path, 0o644)

# Verify entry.txt after writing: read back, compare bytes, assert mode 0644.
with open(path, "rb") as f:
    data = f.read()
assert data == TEXT.encode("utf-8"), "entry.txt bytes differ from TEXT"
assert (os.stat(path).st_mode & 0o777) == 0o644, "entry.txt mode is not 0644"
