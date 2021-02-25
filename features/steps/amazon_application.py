from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then, when

COLORS = (By.XPATH, "//li[starts-with(@id, 'color_name')]")
SELECTED_COLOR = (By.XPATH, "//span[@class='selection']")


@given('Open Amazon T&C page')
def open_amazon_tnc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon applications link')
def click_amazon_applications_link(context):
    context.driver.find_element(By.XPATH, "//a[contains(@href, 'docId=1000625601')]").click()
    context.driver.wait.until(EC.new_window_is_opened)


@when('Switch to the newly opened window')
def switch_to_opened_window(context):
    context.driver.switch_to_window(context.driver.window_handles[1])


@then('Amazon app page is opened')
def amazon_app_page_opened(context):
    # If there's an Apple Appstore button, it would be the amazon app page.
    appstore_button = context.driver.find_elements(By.XPATH, "//a[@aria-label='Download on the Apple App Store']")
    assert appstore_button, "This page isn't the Amazon app page"


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
    assert len(context.driver.window_handles) == 1, "The opened window wasn't closed"
