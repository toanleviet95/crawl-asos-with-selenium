from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListing:
  def __init__(self, driver):
    self.driver = driver
    self.XPATH =  {
      "load_more": "//a[@data-auto-id='loadMoreProducts']",
      "product_item": "//article[@data-auto-id='productTile']",
      "product_link": ".//a",
    }
    self.TIME_TO_WAIT = 2 # seconds

  def open_browser_with_link(self, link):
    self.driver.get(link)

  def close_browser(self):
    self.driver.quit()

  def click_load_more(self):
    while True:
      try:
        loadMore = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
          EC.presence_of_element_located((By.XPATH, self.XPATH['load_more'])))
        loadMore.click()
      except:
        break

  def crawl_links_from_product_list(self):
    result = []
    productList = self.driver.find_elements(By.XPATH, self.XPATH['product_item'])
    if len(productList) > 0:
      for product in productList:
        url = product.find_element(By.XPATH, self.XPATH['product_link']).get_attribute('href')
        result.append(url)
    return result
