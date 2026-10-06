from selenium import webdriver

def test_titulo_pagina():
    driver = webdriver.Firefox()
    driver.get("https://inefarium.github.io/erizos/")
    assert "Example" in driver.title
    driver.quit()