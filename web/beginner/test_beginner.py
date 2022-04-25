"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestBegginner:

    def test_begginner(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("http://litemall.hogwarts.ceshiren.com/vue/index.html#/login?redirect=user")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='user']").send_keys("user123")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys("user123")
        self.driver.find_element(By.CSS_SELECTOR, ".van-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".van-tabbar-item").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".van-field__control").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".van-field__control").send_keys("火焰杯测试商品")
        self.driver.find_element(By.CSS_SELECTOR, ".van-field__control").send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".van-card__title").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".van-goods-action-button--first").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".van-button--warning").click()
        self.driver.find_element(By.CSS_SELECTOR, ".van-goods-action-icon").click()
        res = self.driver.find_elements(By.XPATH, "//*[text()='火焰杯测试商品']")
        print(res[0].text)
        self.driver.quit()
        assert res != []




