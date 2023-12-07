from behave import given, when, then


@when("Open Customize Explore Feed")
def customize_feed(context):
    context.app.explore_page.customize_explore_feed()