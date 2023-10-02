from playwright.sync_api import sync_playwright
import time
import random
import json
import urllib.parse

def generate_pinterest_search_url(query):
    base_url = "https://in.pinterest.com/search/pins/?q="
    encoded_query = urllib.parse.quote(query)
    search_url = f"{base_url}{encoded_query}"
    return search_url

def scroll_me(query):
    # Number of Pinterest search result pages to scrape
    num_pages = 1

    search_url = generate_pinterest_search_url(query)

    def check_json(response):
        if "https://in.pinterest.com/resource/BaseSearchResource/get/" in response.url:
            data = {"url": response.url, "body": response.json()}
            data_list.append(data)  # Append data to the list

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        try:
            data_list = []  # List to store the data
            page = browser.new_page()
            page.set_viewport_size({"width": 1280, "height": 1080})
            page.on("response", lambda response: check_json(response))
            page.goto(search_url)
            time.sleep(4)
            page.wait_for_load_state("networkidle")
            for x in range(1, 2):
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(4)

            # Write the collected data to a JSON file for each URL
            with open(f"pinterest_data_{random.randint(1, 1000)}.json", "w") as json_file:
                json.dump(data_list, json_file, indent=4)
        finally:
            browser.close()

def main():
    query = input("Enter a query: ")
    scroll_me(query)

if __name__ == "__main__":
    main() 
