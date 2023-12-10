from behave import given, when, then


@given("log in page is opened")
def navigate_to_log_in(context):
    context.app.ob_page.click_skip_ob()
    context.app.page.open_saved_tab()
    context.app.saved_page.log_in_or_join_wiki()
    context.app.saved_page.open_login()


@when("log in (User: {username} Password: {password})")
def log_in(context, username, password):
    context.app.saved_page.log_in(username, password)


@when("turn off reading sync")
def turn_off_reading_sync(context):
    context.app.page.warn_reading_list_sync_no()


@then("verify {username} is logged in")
def verify_user_logged_in(context, username):
    context.app.page.open_more_tab()
    context.app.saved_page.verify_logged_in(username)




