from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetail:
  def __init__(self, driver):
    self.driver = driver
    self.XPATH =  {
      "thumbnail": "//li[contains(@class, 'image-thumbnail')]/*/img",
      "title": "//div[@class='product-hero']/h1",
      "current_price": "//span[@data-id='current-price']",
      "previous_price": "//span[@data-id='previous-price']",
      "color": "//span[@class='product-colour']",
      "rating": "//div[@class='numeric-rating']",
      "total_reviews": "//div[@class='total-reviews']"
    }
    self.TIME_TO_WAIT = 2 # seconds

  def open_browser_with_link(self, link):
    self.driver.get(link)

  def close_browser(self):
    self.driver.quit()

  def crawl_product_title(self):
    title = self.driver.find_element(By.XPATH, self.XPATH['title'])
    return title.text

  def crawl_product_current_price(self):
    current_price = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.XPATH, self.XPATH['current_price'])))
    return current_price.text.replace("Now ", "")

  def crawl_product_previous_price(self):
    previous_price = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.XPATH, self.XPATH['previous_price'])))
    return previous_price.text.replace("Was ", "")

  def crawl_product_color(self):
    color = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.XPATH, self.XPATH['color'])))
    return color.text

  def crawl_product_rating(self):
    try:
      rating = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
          EC.presence_of_element_located((By.XPATH, self.XPATH['rating'])))
      return rating.text
    except:
      return ''

  def crawl_product_total_reviews(self):
    try:
      total_reviews = WebDriverWait(self.driver, self.TIME_TO_WAIT).until(
          EC.presence_of_element_located((By.XPATH, self.XPATH['total_reviews'])))
      return total_reviews.text.replace("(", "").replace(")", "")
    except:
      return ''

  def crawl_product_thumbnails(self):
    result = []
    thumbnails = self.driver.find_elements(By.XPATH, self.XPATH['thumbnail'])
    if len(thumbnails) > 0:
      for thumbnail in thumbnails:
        image = thumbnail.get_attribute('src')
        image = image.replace("$n_240w$&wid=40", "$n_320w$&wid=317")
        result.append(image)
    return result
