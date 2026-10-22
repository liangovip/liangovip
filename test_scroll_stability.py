import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox", "--allow-file-access-from-files"])
        context = await browser.new_context(
            viewport={"width": 375, "height": 812},
            is_mobile=True,
            has_touch=True,
            device_scale_factor=2
        )
        page = await context.new_page()
        page.on("console", lambda msg: print(f"CONSOLE [{msg.type}]: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))
        
        await page.goto("file:///workspace/agent/moore-labs/index.html", wait_until="load")
        
        # Wait for React Babel to mount
        await page.wait_for_selector(".scenario-card", timeout=10000)
        
        cards = page.locator("#here-it-is .scenario-card")
        total = await cards.count()
        print(f"Total Section 7 cards mounted: {total}")
        
        # 1. Scroll DOWN through all cards
        print("--- Scrolling DOWN ---")
        for i in range(total):
            card = cards.nth(i)
            await card.scroll_into_view_if_needed()
            await asyncio.sleep(0.4)
            img = card.locator("img")
            vis = await img.is_visible()
            box = await img.bounding_box()
            classes = await card.get_attribute("class")
            in_view = "in-view" in classes
            y_pos = round(box['y'], 1) if box else None
            print(f"Card {i+1} DOWN: visible={vis}, in-view={in_view}, y={y_pos}")
            
        # 2. Scroll UP back to Card 1
        print("--- Scrolling UP (Backwards) ---")
        for i in range(total - 1, -1, -1):
            card = cards.nth(i)
            await card.scroll_into_view_if_needed()
            await asyncio.sleep(0.4)
            img = card.locator("img")
            vis = await img.is_visible()
            box = await img.bounding_box()
            classes = await card.get_attribute("class")
            in_view = "in-view" in classes
            y_pos = round(box['y'], 1) if box else None
            print(f"Card {i+1} UP: visible={vis}, in-view={in_view}, y={y_pos}")
            
        await browser.close()

asyncio.run(main())
