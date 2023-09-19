from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests


def crawl_and_save_images(menu, color, sub_menu, total_images, output_folder):
    # 웹 드라이버 인스턴스 생성 (Chrome 웹 드라이버가 설치되어 있다고 가정)
    driver_path= '/crawling/chromedriver.exe'
    OP = webdriver.ChromeOptions()
    # user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    #
    # OP.add_argument(f"user-agent = {user_agent}")
    OP.add_argument("--headless")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=OP
    )
    # 웹 페이지로 이동
    base_url = "https://www.musinsa.com/app/"
    driver.get(base_url)

    try:
        # 페이지를 아래로 스크롤합니다.
        for i in range(2):  # 예시로 3번 스크롤하도록 설정하였습니다.
            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(1)  # 스크롤 후 로딩을 기다리기 위한 대기 시간

        # 아래 XPath는 예시이며, 웹 페이지의 실제 구조에 따라 수정해야 할 수 있습니다.
        xpath = f"//div[@class='sc-8hpehb-3 HnLvd']/strong[text()='{menu}']"
        wait = WebDriverWait(driver, 1)
        element_to_click = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

        element_to_click.click()

        sub_xpath = f"//a[contains(text(), '{sub_menu}')]"
        wait = WebDriverWait(driver, 1)
        sub_element = wait.until(EC.element_to_be_clickable((By.XPATH, sub_xpath)))
        sub_element.click()

        # 페이지가 로딩될 때까지 대기합니다.
        # 페이지 로딩 여부를 예시로 확인하는 코드입니다. 실제 웹 페이지에 맞게 수정하세요.
        time.sleep(1)

        # 필터를 적용하기 위한 XPath 추가 (예: "블랙" 색상 필터)
        filter_xpath = f"//a[@data-filter-value='{color}'and @data-filter-key='color']"
        wait = WebDriverWait(driver, 1)
        filter_element = wait.until(
            EC.element_to_be_clickable((By.XPATH, filter_xpath))
        )
        filter_element.click()

        new_page_url = driver.current_url



        first = output_folder.replace(sub_menu, "")
        second = sub_menu.replace("/", "")
        output_folder = first + "/" + second
        os.makedirs(output_folder, exist_ok=True)

        image_count = 0
        page_number = 1

        while image_count < total_images:
            driver.get(new_page_url.format(page_number=page_number))

            # 스크롤을 최하단까지 내립니다. (이미지 로딩을 위해)
            # last_height = driver.execute_script("return document.body.scrollHeight")
            # while True:
            #     driver.execute_script("window.scrollBy(0, 5000)")
            #     time.sleep(0.1)
            #     new_height = driver.execute_script("return document.body.scrollHeight")
            #     if new_height == last_height:
            #         break
            #     last_height = new_height

            soup = BeautifulSoup(driver.page_source, "html.parser")
            links = soup.find_all("a", href=True)
            links = [link["href"] for link in links]
            goods_links = [
                link for link in links if "www.musinsa.com/app/goods" in link
            ]
            unique_goods_links = list(set(goods_links))
            http_link = []
            for http in unique_goods_links:
                http = "https:" + http
                http_link.append(http)

            valid_link = []

            for link in http_link:
                response = requests.head(link)
                if response.status_code == 403:
                    valid_link.append(link)

            for url in valid_link:
                try:
                    driver.get(url)
                    time.sleep(0.1)
                    img_elements = driver.find_elements(By.XPATH, "//img[@id='bigimg']")
                    for idx, img_element in enumerate(img_elements):
                        img_src = img_element.get_attribute("src")
                        image_files = [
                            f for f in os.listdir(output_folder) if f.endswith(".jpg")
                        ]
                    max_number = 0
                    for image_file in image_files:
                        try:
                            # 이미지 파일 이름에서 번호 부분을 추출합니다.
                            image_number = int(image_file.split("_")[1].split(".")[0])
                            if image_number > max_number:
                                max_number = image_number
                        except ValueError:
                            pass  # 파일 이름에서 숫자를 추출할 수 없는 경우 무시합니다.

                    # 새 이미지에 할당할 번호 계산
                    if max_number == 0:
                        new_image_number = 1  # 이미지가 없을 때는 1부터 시작
                    else:
                        new_image_number = max_number + 1

                    # 다운로드한 이미지에 새 번호를 매겨 저장
                    urllib.request.urlretrieve(
                        img_src,
                        os.path.join(output_folder, f"image_{new_image_number}.jpg"),
                    )

                    # 이미지 카운트 증가
                    image_count += 1

                    if image_count >= total_images:
                        break
                        filter_element.click()

                    driver.back()
                    time.sleep(1)

                except Exception as e:
                    # 오류가 발생한 경우 해당 링크에 대한 오류 메시지만 출력
                    print(f"{url}로 이동 중 오류 발생: {e}")
                    continue

            # # 이미지 요소를 찾아서 하나씩 다운로드합니다.
            # img_elements = driver.find_elements(
            #     By.XPATH, "//img[@class='lazyload lazy']"
            # )
            # for idx, img_element in enumerate(img_elements):
            #     try:
            #         # 이미지 URL과 대체 텍스트 가져오기
            #         img_src = img_element.get_attribute("data-original")

            #         image_files = [
            #             f for f in os.listdir(output_folder) if f.endswith(".jpg")
            #         ]  # 이미지 다운로드
            #         max_number = 0
            #         for image_file in image_files:
            #             try:
            #                 # 이미지 파일 이름에서 번호 부분을 추출합니다.
            #                 image_number = int(image_file.split("_")[1].split(".")[0])
            #                 if image_number > max_number:
            #                     max_number = image_number
            #             except ValueError:
            #                 pass  # 파일 이름에서 숫자를 추출할 수 없는 경우 무시합니다.

            #         # 새 이미지에 할당할 번호 계산
            #         if max_number == 0:
            #             new_image_number = 1  # 이미지가 없을 때는 1부터 시작
            #         else:
            #             new_image_number = max_number + 1

            #         # 다운로드한 이미지에 새 번호를 매겨 저장
            #         urllib.request.urlretrieve(
            #             img_src,
            #             os.path.join(output_folder, f"image_{new_image_number}.jpg"),
            #         )

            #         # 이미지 카운트 증가
            #         image_count += 1

            #         if image_count >= total_images:
            #             break
            #             filter_element.click()
            #     except Exception as e:
            #         print(f"Error: {str(e)}")
            #         continue

            # 다음 페이지로 이동
            page_number += 1
            if not driver.current_url.startswith(new_page_url):
                print("No more pages.")
                break

            if image_count < total_images and page_number > 2:
                print("Not enough images found.")
                break
    except Exception as e:
        print(f"Error: {str(e)}")

    driver.quit()
