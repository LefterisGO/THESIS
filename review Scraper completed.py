Every stage run independent
#START CODING 1st page only

# import undetected_chromedriver as uc
# import time
# from bs4 import BeautifulSoup

# def scrape_page(url):
#     options = uc.ChromeOptions()
#     options.headless = True  # Set headless to True for headless mode

#     driver = uc.Chrome(options=options)

#     driver.get(url)

#     html_content = driver.page_source
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Save the HTML content of the page
#     filename = "scraped_1_page.html"
#     with open(filename, "w", encoding="utf-8") as file:
#         file.write(html_content)

#     # You can perform other actions here, such as scraping data from the page

#     driver.quit()

# # Specific URL to scrape
# specific_url = "https://webcache.googleusercontent.com/search?q=cache:https://www.skroutz.gr/c/40/kinhta-thlefwna.html&sca_esv=a142d6466750453f&strip=1&vwsrc=0"

# # Call the scrape_page function with the specific URL
# scrape_page(specific_url)


#2 scraping all other menu pages


# import undetected_chromedriver as uc
# import time
# from bs4 import BeautifulSoup

# def scrape_pages(base_url, total_pages):
#     options = uc.ChromeOptions()
#     options.headless = True  # Set headless to True for headless mode

#     driver = uc.Chrome(options=options)

#     for page in range(2, total_pages + 1):
#         url = base_url.format(page)
#         driver.get(url)

#         html_content = driver.page_source
#         soup = BeautifulSoup(html_content, 'html.parser')

#         # Save the HTML content of the page
#         filename = f"page_{page}_scraped.html"
#         with open(filename, "w", encoding="utf-8") as file:
#             file.write(html_content)

#         # You can perform other actions here, such as scraping data from each page
        
#         # Delay between requests
#         time.sleep(60)

#     driver.quit()

# # Set the total number of pages to scrape
# total_pages_to_scrape = 52  # Adjust this according to the actual number of pages

# # Base URL with a placeholder for the page number
# base_url = "https://webcache.googleusercontent.com/search?q=cache:https://www.skroutz.gr/c/40/kinhta-thlefwna.html?page={}&sca_esv=941af24518045317&strip=1&vwsrc=0"

# # Call the scrape_pages function with the modified base URL and the total number of pages to scrape
# scrape_pages(base_url, total_pages_to_scrape)


#3 merge previous files here(all phone pages cleaning after on name file after /s character):

# import json
# from bs4 import BeautifulSoup

# # Initialize a set to store all unique hrefs
# all_unique_hrefs = set()

# # Loop through pages from 2 to 52
# for page_number in range(1, 53):
#     # Load the HTML content from the saved file for each page
#     file_path = f"C:\\Users\\lefte\\OneDrive\\Desktop\\thesis total\\code\\page_{page_number}_scraped.html"
#     with open(file_path, "r", encoding="utf-8") as file:
#         html_content = file.read()

#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find all <a> tags with class="js-sku-link"
#     links = soup.find_all('a', class_='js-sku-link')

#     # Extract href attribute values from the <a> tags and add them to the set
#     for link in links:
#         href = link.get('href')
#         all_unique_hrefs.add(href)

# # Define the output JSON file path
# output_json_file = "pages_1_to_52.json"

# # Save all extracted unique hrefs to a JSON file
# with open(output_json_file, "w") as json_file:
#     json.dump(list(all_unique_hrefs), json_file, indent=4)

# print("Unique Hrefs from pages 1 to 52 saved to", output_json_file)


#  4  save the href list and keep only the ones with 0 ending.


# import undetected_chromedriver as uc
# from bs4 import BeautifulSoup
# import json

# options = uc.ChromeOptions()
# options.headless = True  # Set headless to True for headless mode

# driver = uc.Chrome(options=options)
# url = "https://webcache.googleusercontent.com/search?q=cache:https://www.skroutz.gr{?}"
# driver.get(url)

# html_content = driver.page_source
# soup = BeautifulSoup(html_content, 'html.parser')

# # Find all <a> tags
# a_tags = soup.find_all('a')

# # List to store href attributes
# hrefs = []

# # Iterate through each <a> tag and extract href attribute
# for a_tag in a_tags:
#     href = a_tag.get('href')
#     if href:
#         hrefs.append(href)

# # Save href attributes to a JSON file
# filename = "all_hrefs_1.json"
# with open(filename, "w", encoding="utf-8") as file:
#     json.dump(hrefs, file, indent=4)

# # Quit the Chrome instance
# driver.quit()

#5 create list

# import undetected_chromedriver as uc
# from bs4 import BeautifulSoup
# import json
# import time

# options = uc.ChromeOptions()
# options.headless = True  # Set headless to True for headless mode

# driver = uc.Chrome(options=options)

# # Load the JSON file containing URLs
# with open("pages_1_to_52.json", "r", encoding="utf-8") as pages_file:
#     pages = json.load(pages_file)

# for page in pages:
#     # Replace {?} with the URL
#     url = "https://webcache.googleusercontent.com/search?q=cache:https://www.skroutz.gr" + page
#     driver.get(url)

#     html_content = driver.page_source
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find all <a> tags
#     a_tags = soup.find_all('a')

#     # List to store href attributes
#     hrefs = []

#     # Iterate through each <a> tag and extract href attribute
#     for a_tag in a_tags:
#         href = a_tag.get('href')
#         if href:
#             hrefs.append(href)
    
#     # Save href attributes to a JSON file
#     filename = f"all_hrefs_{page.replace('/', '_')}.json"
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(hrefs, file, indent=4)
#     time.sleep(60)
# # Quit the Chrome instance
# driver.quit()


# create the dataset
    

# import json
# import undetected_chromedriver as uc
# import time

# # Load JSON file
# with open('pages_1_to_52.json', 'r') as file:
#     urls = json.load(file)

# # Iterate through URLs
# for url in urls:
#     options = uc.ChromeOptions()
#     options.headless = True  # Set headless to True for headless mode

#     driver = uc.Chrome(options=options)

#     # Construct the modified URL
#     modified_url = "https://www.skroutz.gr/s/40947299/Samsung-Galaxy-A54-5G-Dual-SIM-8GB-256GB-Awesome-Violet.html#reviews"

#     driver.get(modified_url)

#     # Get the entire HTML content of the page
#     html_content = driver.page_source

#     driver.quit()

#     # Generate a unique filename based on the URL
#     filename = modified_url.split('/')[-1] + ".json"

#     # Save scraped content into a JSON file
#     with open(filename, 'w', encoding='utf-8') as outfile:
#         outfile.write(html_content)

#     time.sleep(50)  # Sleep for 50 seconds



