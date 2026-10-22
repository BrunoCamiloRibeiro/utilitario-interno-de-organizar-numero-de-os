import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(options=options)
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "index.html"))
    driver.get(f"file://{html_path}")
    yield driver
    driver.quit()


def test_initial_page_state(driver):
    assert driver.title == "Formatador de OS"

    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")
    btn_format = driver.find_element(By.ID, "btnFormat")
    btn_copy = driver.find_element(By.ID, "btnCopy")
    btn_clear = driver.find_element(By.ID, "btnClear")
    badge = driver.find_element(By.ID, "countBadge")

    assert input_el.get_attribute("value") == ""
    assert output_el.get_attribute("value") == ""
    assert output_el.get_attribute("readOnly") in ["true", "True", True, ""]
    assert badge.text == "0 OSs"
    assert btn_format.text == "Formatar"
    assert btn_copy.text == "Copiar"
    assert btn_clear.text == "Limpar"

    # Screenshot initial
    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    os.makedirs(assets_dir, exist_ok=True)
    driver.save_screenshot(os.path.join(assets_dir, "screenshot_initial.png"))


def test_extraction_on_input_event(driver):
    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")
    badge = driver.find_element(By.ID, "countBadge")

    # Enter mixed text with three 6-digit OS numbers
    raw_text = "Notificação OS 739241 gerada, seguida da OS 739710 e multa 739813 finalizada."
    driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));", input_el, raw_text)

    assert output_el.get_attribute("value") == "739241;739710;739813"
    assert badge.text == "3 OSs"

    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    driver.save_screenshot(os.path.join(assets_dir, "screenshot_filled.png"))


def test_singular_plural_badge(driver):
    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")
    badge = driver.find_element(By.ID, "countBadge")

    # Exactly 1 OS: singular "1 OS"
    driver.execute_script("arguments[0].value = 'Processo 739241 arquivado'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == "739241"
    assert badge.text == "1 OS"

    # 2 OSs: plural "2 OSs"
    driver.execute_script("arguments[0].value = '739241 739710'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == "739241;739710"
    assert badge.text == "2 OSs"


def test_regex_boundary_and_length_rules(driver):
    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")
    badge = driver.find_element(By.ID, "countBadge")

    # 5 digits (12345) and 7 digits (1234567) should NOT match
    driver.execute_script("arguments[0].value = 'OS 12345 e OS 1234567'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == ""
    assert badge.text == "0 OSs"

    # Alphanumeric adjacent boundary: ABC123456, 123456DEF should NOT match
    driver.execute_script("arguments[0].value = 'ABC123456 e 123456DEF'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == ""
    assert badge.text == "0 OSs"

    # Punctuation boundaries: (739241), [739710], {739813} SHOULD match
    driver.execute_script("arguments[0].value = '(739241), [739710], {739813}!'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == "739241;739710;739813"
    assert badge.text == "3 OSs"


def test_non_sorting_and_non_deduplication(driver):
    """
    CRITICAL BEHAVIOR:
    The tool is named 'Projeto Ordenação OS', but in code it does NOT sort and does NOT deduplicate.
    """
    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")

    # Unordered input
    driver.execute_script("arguments[0].value = '999999 111111 555555'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == "999999;111111;555555", "Code does not sort numbers"

    # Duplicate input
    driver.execute_script("arguments[0].value = '739241 739241 739710'; arguments[0].dispatchEvent(new Event('input'));", input_el)
    assert output_el.get_attribute("value") == "739241;739241;739710", "Code does not deduplicate numbers"


def test_format_button_click(driver):
    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")
    btn_format = driver.find_element(By.ID, "btnFormat")
    badge = driver.find_element(By.ID, "countBadge")

    # Set value without firing input event
    driver.execute_script("arguments[0].value = '739241 739710';", input_el)
    # Output still empty or previous until clicked
    btn_format.click()
    assert output_el.get_attribute("value") == "739241;739710"
    assert badge.text == "2 OSs"


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_copy_button_and_feedback(driver):
    btn_copy = driver.find_element(By.ID, "btnCopy")
    output_el = driver.find_element(By.ID, "outputData")

    # When output has value
    assert output_el.get_attribute("value") != ""
    btn_copy.click()

    # Visual feedback: Copiado! and class 'copied' (wait for promise resolution)
    WebDriverWait(driver, 3).until(lambda d: "copied" in btn_copy.get_attribute("class"))
    assert btn_copy.text == "Copiado!"

    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    driver.save_screenshot(os.path.join(assets_dir, "screenshot_copied.png"))

    # After 1.5 seconds timeout reverts
    WebDriverWait(driver, 3).until(lambda d: "copied" not in btn_copy.get_attribute("class"))
    assert btn_copy.text == "Copiar"


def test_clear_button(driver):
    input_el = driver.find_element(By.ID, "inputData")
    output_el = driver.find_element(By.ID, "outputData")
    btn_clear = driver.find_element(By.ID, "btnClear")
    badge = driver.find_element(By.ID, "countBadge")

    btn_clear.click()

    assert input_el.get_attribute("value") == ""
    assert output_el.get_attribute("value") == ""
    assert badge.text == "0 OSs"

    active_el = driver.switch_to.active_element
    assert active_el.get_attribute("id") == "inputData"


def test_responsive_mobile_viewport(driver):
    driver.set_window_size(480, 800)
    btn_clear = driver.find_element(By.ID, "btnClear")
    # In mobile media query (@media max-width: 680px), btn-clear width is 100% or margins adjusted
    assets_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets"))
    driver.save_screenshot(os.path.join(assets_dir, "screenshot_mobile.png"))
    driver.set_window_size(1280, 800)
