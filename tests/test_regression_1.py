import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)


def test_regression_1():
 """Regression guard for a notify edge case discovered earlier."""
 from templatelib.features.feature-notify-1 import run_notify
 result = run_notify("sample-1", timeout=5)
 assert result["ok"] is True
 assert "value" in result