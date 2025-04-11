from __future__ import annotations
import logging


from behave.model import Tag
from behave.runner import Context

def before_tag(context: Context, tag: Tag) -> None:
  logging.error(f"Tag is: {tag}")