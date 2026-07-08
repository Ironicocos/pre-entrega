import pytest 
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.dataReader import read_users_csv
import pathlib
import pytest_html
BASE = 'https://jsonplaceholder.typicode.com'
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Edge(options=options)

    yield driver

    driver.quit()
@pytest.fixture
def login_in_driver(driver):
    loginPage = LoginPage(driver)
    user = read_users_csv()[0]
    loginPage.login(user["username"], user["password"])
    return driver
@pytest.fixture(scope="module")
def posts_url():
    return f"{BASE}/posts"
@pytest.fixture(scope="module")
def post_by_id_url():
    def _get_url(post_id):
        return f"{BASE}/posts/{post_id}"
    return _get_url

@pytest.hookimpl(tryfirst=True,hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    #when = setup, call, teardown
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents = True, exist_ok = True)

            fileName = target / f"{item.name}.png"

            driver.save_screenshot(str(fileName))
            
            if hasattr(report, "extra"):
                report.extra.append({
                    "name" : "screenshot",
                    "format" : "img",
                    "content" : str(fileName)
                })
                
            extras = getattr(report, "extras",[])
            extras.append(pytest_html.extras.png(str(fileName)))

            report.extras = extras