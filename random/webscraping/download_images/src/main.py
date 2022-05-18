from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time


PATH = "/home/skypper/Projects/eLearning/python/random/webscraping/download_images/src/chromedriver_linux64/chromedriver"
wd = webdriver.Chrome(PATH)


def get_img_from_G(wd, delay, max_images):
  def scroll_down(wd):
    wd.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll down
    time.sleep(delay)

  url = "https://www.google.com/search?q=cats&sxsrf=AOaemvIyeWwTl1wAYpCEpOPe_3jBw9g7Fw:1635934366622&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiK1LC2-vvzAhXyoFwKHROJDgcQ_AUoAXoECAEQAw&biw=1517&bih=832&dpr=1#imgrc=0V922RrJgQc9SM"
  wd.get(url)

  image_urls = set() # we need a set so it does not go infinitely but respecting the max_images
  skips = 0

  while len(image_urls) + skips < max_images:
    scroll_down(wd)
    thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd") # whwn runing this command again it will give the same thumbnails + the additional urls

    for img in thumbnails[len(image_urls) + skips:max_images]: # avoid looping through already looped thumbnails
      try: # we might get an error while clicking on the image
        img.click()
        time.sleep(delay)
      except: # if error go to next image
        continue

      images = wd.find_elements(By.CLASS_NAME, "n3VNCb") # it could potentially return multiple images
      for image in images:
        if image.get_attribute('src') in image_urls:
          max_images += 1
          skips += 1
          break
        
        if image.get_attribute('src') and 'http' in image.get_attribute('src'):
          image_urls.add(image.get_attribute('src'))
          print(f"Found {len(image_urls)}")
  
  return image_urls


def download_image(download_path, url, file_name):
  try:
    image_content = requests.get(url).content # get the content of the image
    image_file = io.BytesIO(image_content) # store the content of the image as bytes (binary data type) in the memory
    image = Image.open(image_file)
    image_path = download_path + file_name

    with open(image_path, "wb") as f:
      image.save(f, "JPEG")
    
    print("Success")
  except Exception as e:
    print('FAILED -', e)


urls = get_img_from_G(wd, 3, 5)
# print(f"I've found these urls:{urls}")
for count, url in enumerate(urls, start=1):
  print(f"{count} - Found: {url}")

for index, url in enumerate(urls):
  #               path                       extensions
  download_image("imgs/", url, str(index) + ".jpg")

wd.quit() # we need tot quit or it will remain opne occupying RAM
