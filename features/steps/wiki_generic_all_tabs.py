from behave import given, when, then


@when("Go back")
def go_back(context):
    context.app.page.go_back()


@given('Click to Skip onboarding')
def click_skip_ob(context):
    context.app.ob_page.click_skip_ob()
