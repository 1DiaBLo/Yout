# youtube_view_bot.py (Playwright version)

import asyncio
import random
from playwright.async_api import async_playwright

VIDEO_URL = "https://youtu.be/R2MYQ-OmyoU?si=IleiqfKq1fY0cswF"
NUM_VIEWS = 5  # عدد المشاهدات المتزامنة


async def watch_video(playwright):
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    try:
        await page.goto(VIDEO_URL)
        print("🎬 Watching video...")
        time_to_watch = random.randint(40, 70)
        await asyncio.sleep(time_to_watch)
        print(f"✅ Watched for {time_to_watch} seconds")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        await browser.close()


async def main():
    async with async_playwright() as playwright:
        tasks = []
        for _ in range(NUM_VIEWS):
            task = asyncio.create_task(watch_video(playwright))
            tasks.append(task)
            await asyncio.sleep(random.uniform(1.0, 3.0))

        await asyncio.gather(*tasks)
        print("🔥 All views finished!")


if __name__ == "__main__":
    asyncio.run(main())
    
