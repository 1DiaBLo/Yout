# youtube_view_bot.py

import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Process

VIDEO_URL = "https://youtu.be/R2MYQ-OmyoU?si=IleiqfKq1fY0cswF"
NUM_VIEWS = 5  # عدد المشاهدات المتزامنة


def watch_video():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--mute-audio")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(VIDEO_URL)
        print("🎬 Watching video...")
        time_to_watch = random.randint(40, 70)
        time.sleep(time_to_watch)
        print(f"✅ Watched for {time_to_watch} seconds")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    processes = []
    for _ in range(NUM_VIEWS):
        p = Process(target=watch_video)
        p.start()
        processes.append(p)
        time.sleep(random.uniform(1.0, 3.0))  # تفادي الكشف بالتزامن الكامل

    for p in processes:
        p.join()

    print("🔥 All views finished!")
  
