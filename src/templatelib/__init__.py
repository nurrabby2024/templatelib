"""TemplateLib: A minimal text template engine with loops and conditionals."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]