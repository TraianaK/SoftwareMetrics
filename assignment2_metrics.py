import csv
import json
from selenium import webdriver
import requests


URL = "https://en.wikipedia.org/wiki/Software_metric"
EXECUTABLE_PATH = '/home/traiana/Desktop/HW_2/QA/testing/chromedriver'
COUNT = 10


def get_metrics():
    "extracting performance data"
    # tdd
    name_duration = {}
    # init once before the cycle
    driver = webdriver.Chrome(executable_path=EXECUTABLE_PATH)
    with open('output.txt', 'w') as json_file:
        for i in range(COUNT):
            driver.get(URL)
            performance_data = driver.execute_script("return window.performance.getEntries()")
            for curr in performance_data:
                json_file.write(json.dumps(curr, indent=2))
                url = curr["name"]
                current_list = name_duration.get(URL, [])
                current_list.append(i)
                name_duration[URL] = current_list
    driver.close()
    # must be a part of get_metrics()
    with open('some_results.csv', 'w') as f:
        f.write(f'name, url, duration, ms\n')
        for key in list(name_duration.keys()):
            # metric = name_duration[key]
            metric = requests.get(URL)
            print(metric.elapsed.total_seconds())
            average = sum(name_duration[key]) / len(name_duration[key])
            # print("Average time:", average)
            f.write(f'{key}, {average} \n')

    return key


if __name__ == "__main__":
    get_metrics()
