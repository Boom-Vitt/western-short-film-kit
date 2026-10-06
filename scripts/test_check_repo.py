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
]
for filename, before, after, expected in cases:
    with TemporaryDirectory() as temp:
        target = Path(temp) / "kit"
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(".git", ".superpowers", "__pycache__"))
        path = target / filename
        if before == "DELETE":
            path.unlink()
        else:
            content = path.read_text(encoding="utf-8")
            if before is None:
                content += after
            else:
                assert before in content, (filename, before)
                content = content.replace(before, after, 1)
            path.write_text(content, encoding="utf-8")
        errors, _, _ = checker.check(target)
        assert any(expected in error for error in errors), (filename, expected, errors)
print("PASS: valid kit + 8 invalid-content regression cases")
