"""
File: webcrawler.py
Name: Roger141
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')
        try:
            element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
            WebDriverWait(driver, 5).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        tags = soup.find_all('table', {'class': 't-stripe'})
        # print(type(tags))
        # print(tags.text)
        total_men, total_women = 0, 0
        count = 0
        for tag in tags:
            # print(type(tag))
            # print(tag.text)
            tokens = tag.text.split()
            # print(tokens)
            # s = '15\nJaydan 126,064 Chloe 85,300\n16\nMattew...'
            for token in tokens:
                if ',' in token:
                    count += 1
                    clean_token = token.replace(',', '')
                    num_ppl = int(clean_token)
                    # num_ppl = token
                    # print(num_ppl)

                    if count % 2 == 1:  #(Odd)
                        total_men += num_ppl
                    else:  #(Even)
                        total_women += num_ppl
        print(f'Total men: {total_men}')
        print(f'Total women: {total_women}')
        driver.quit()


if __name__ == '__main__':
    main()
