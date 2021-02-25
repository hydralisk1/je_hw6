from selenium.webdriver.common.by import By
from behave import given, then, when

BEST_SELLERS = (By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
TOP_LINKS = (By.XPATH, "//div[@id='zg_tabs']//li//a")


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')


@when('Click on the best sellers link')
def check_products(context):
    context.driver.find_element(*BEST_SELLERS).click()


@then('Click on every top link, and verify pages get properly open')
def click_top_link(context):
    num_of_links = len(context.driver.find_elements(*TOP_LINKS))
    for i in range(num_of_links):
        link = context.driver.find_elements(*TOP_LINKS)[i]
        # Get the text from the button
        button_text = link.text
        link.click()
        # Get the text from the header
        header_text = context.driver.find_element(By.XPATH, "//div[@id='zg_banner_text_wrapper']").text
        assert button_text in header_text, f"{button_text} page didn't open"
