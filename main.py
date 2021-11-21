from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ProductListing import ProductListing
from ProductDetail import ProductDetail
import json

def crawl_links_from_listing_page(driver, url):
  productListing = ProductListing(driver)
  productListing.open_browser_with_link(url)
  productListing.click_load_more()
  links = productListing.crawl_links_from_product_list()
  return links

def crawl_data_from_detail_page(driver, links, limit_size = 0):
  productDetail = ProductDetail(driver)
  result = []
  count = 0
  for link in links:
    if limit_size > 0 and count == limit_size:
      break
    productDetail.open_browser_with_link(link)
    productDetail.open_browser_with_link(link)
    title = productDetail.crawl_product_title()
    current_price = productDetail.crawl_product_current_price()
    previous_price = productDetail.crawl_product_previous_price()
    color = productDetail.crawl_product_color()
    thumbnails = productDetail.crawl_product_thumbnails()
    rating = productDetail.crawl_product_rating()
    total_reviews = productDetail.crawl_product_total_reviews()
    result.append({
      "url": link,
      "title": title,
      "current_price": current_price,
      "previous_price": previous_price,
      "color": color,
      "rating": rating,
      "total_reviews": total_reviews,
      "thumbnails": thumbnails
    })
    count = count + 1
  return result

def main():
  # Initialize Chrome WebDriver
  driver = webdriver.Chrome(ChromeDriverManager().install())
  init_link = 'https://www.asos.com/women/shoes/boots/cat/?cid=6455&nlid=ww|shoes|shop+by+product|boots'

  links = crawl_links_from_listing_page(driver, init_link)

  # Demo with limit size
  limit_size = 10
  products = crawl_data_from_detail_page(driver, links, limit_size)

  result = {
    "count": len(products),
    "products": products,
  }

  driver.quit()

  with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

main()
