"""Minimal example for TemplateLib."""

from templatelib import templatelib


def main():
 runner = templatelib({"name": "TemplateLib", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()