from __future__ import annotations
import logging


from behave.model import Tag
from behave.runner import Context

logger = logging.getLogger("environment")


def before_tag(context: Context, tag: Tag) -> None:
  logger.error(f"Tag is: {tag}")