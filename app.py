#!/usr/bin/env python3

from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

app = Flask(__name__)

options = Options()

# this parameter tells Chrome that
# it should be run without UI (Headless)
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')

# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(options=options)

@app.route('/foobar/<path:path>')
def get_path(path):
    return jsonify({'path': path})

@app.route('/weather/<path:path>', methods=['GET'])
def get_weather(path):
    try:
        driver.get(f'https://www.wunderground.com/weather/{path}')

        temperature = driver.find_element( by=By.XPATH, value='//*[@id="inner-content"]/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[2]/lib-display-unit/span/span[1]').text
        # # click on 2015 for movie list of films
        # driver.find_element(By.ID, '2015').click()
        # film_titles = WebDriverWait(driver, 5).until(
        #     EC.presence_of_all_elements_located((By.CLASS_NAME, 'film-title')))

        # for film_title in film_titles:
        #     print(film_title.text)
        return jsonify({'temperature': temperature})
    except Exception as e:
        return jsonify({'message': 'an error occurred'})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5959)

