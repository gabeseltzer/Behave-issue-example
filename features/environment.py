from __future__ import annotations


from behave.model import Tag
from behave.runner import Context


def before_tag(context: Context, tag: Tag) -> None:
  print(f"THE TAG IS: {tag}")