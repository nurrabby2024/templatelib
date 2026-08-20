import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_0():
 """Regression guard for a preview edge case discovered earlier."""
 from templatelib.features.feature-preview-0 import run_preview
 result = run_preview("sample-0", timeout=5)
 assert result["ok"] is True
 assert "value" in result