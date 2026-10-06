"""Run real checks and prove common content mistakes are rejected; stdlib only."""
import importlib.util
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "scripts/check_repo.py"
assert CHECKER.is_file(), "checker has not been implemented"
spec = importlib.util.spec_from_file_location("check_repo", CHECKER)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
assert checker.check(ROOT)[0] == [], checker.check(ROOT)[0]

cases = [
    ("README.md", None, "\n[Broken](missing.md)\n", "missing/escaping reference"),
    ("README.md", None, '\n<img src="missing.png">\n', "missing/escaping reference"),
    ("examples/one-floor-below-48s.md", "00:00–00:08", "00:01–00:08", "timeline gap"),
    ("examples/one-floor-below-48s.md", '"I know that tune."', '"I forgot that tune."', "changed dialogue"),
    ("examples/one-floor-below-48s.md", "Only Ella speaks", "Only Alex speaks", "speaker does not match"),
    ("examples/one-floor-below-48s.md", "Shot S01. Vertical 9:16", "Shot S01. Horizontal 16:9", "self-contained"),
    ("templates/PRODUCTION.md", "DELETE", "", "missing required file"),
    ("README.md", None, "\n```text\n", "unclosed fenced block"),
    ("examples/one-floor-below-48s.md", "Shot S01. Vertical 9:16, 8-second", "Shot S01. Vertical 9:16, 18-second", "self-contained"),
    ("examples/one-floor-below-48s.md", "### S02 · 00:08–00:16", "### S02 · 00:09–00:19", "heading times/order"),
    ("examples/one-floor-below-48s.md", "SWAP_SHOTS", "", "prompt order"),
    ("scripts/check_repo.py", "DELETE", "", "missing required file"),
    ("assets/hero.png", "CORRUPT_PNG", "", "hero is not a PNG"),
    ("assets/hero.png", "ZERO_HEIGHT", "", "wide high-resolution banner"),
    ("assets/demo.mp4", "DELETE", "", "missing required file"),
]
failures = []
for filename, before, after, expected in cases:
    with TemporaryDirectory() as temp:
        target = Path(temp) / "kit"
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".git", ".superpowers", "__pycache__"))
        path = target / filename
        if before == "DELETE":
            path.unlink()
        elif before == "CORRUPT_PNG":
            path.write_bytes(b"not a PNG")
        elif before == "ZERO_HEIGHT":
            content = bytearray(path.read_bytes())
            content[20:24] = b"\x00" * 4
            path.write_bytes(content)
        else:
            content = path.read_text(encoding="utf-8")
            if before == "SWAP_SHOTS":
                first = content.index("### S01 ·")
                second = content.index("### S02 ·")
                third = content.index("### S03 ·")
                content = content[:first] + content[second:third] + content[first:second] + content[third:]
            elif before is None:
                content += after
            else:
                assert before in content, (filename, before)
                content = content.replace(before, after, 1)
            path.write_text(content, encoding="utf-8")
        errors, _, _ = checker.check(target)
        if not any(expected in error for error in errors):
            failures.append((filename, expected, errors))
assert not failures, failures
print(f"PASS: valid kit + {len(cases)} invalid-content regression cases")
