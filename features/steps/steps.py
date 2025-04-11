from __future__ import annotations


from behave import given, then, when
from behave.runner import Context



@given("a thing")
def starter(context: Context) -> None:
  pass
  
@when("{something} is printed")
def outlined_when_step(context: Context, something: str) -> None:
  pass
  
@then("nothing")
def nothing(context: Context) -> None:
  pass

@when("nothing")
def when_nothing(context: Context) -> None:
  pass