import asyncio
from PIL import Image
import numpy as np
from playwright.async_api import async_playwright

async def verify_viewport(p, name, width, height, is_mobile):
    browser = await p.chromium.launch(
        headless=True,
        args=["--no-sandbox", "--disable-setuid-sandbox", "--allow-file-access-from-files"]
    )
    context = await browser.new_context(
        viewport={"width": width, "height": height},
        is_mobile=is_mobile,
        has_touch=is_mobile,
        device_scale_factor=2
    )
    page = await context.new_page()
    errors = []
    page.on("pageerror", lambda err: errors.append(str(err)))

    # 1. Test external direct navigation with #here-it-is hash
    url = "file:///workspace/agent/moore-labs/index.html#here-it-is"
    await page.goto(url, wait_until="load")
    await page.wait_for_selector("#here-it-is .scenario-card", timeout=10000)
    # Wait for smooth scrollIntoView + GSAP ScrollTrigger settle
    await asyncio.sleep(0.8)

    scroll_y = await page.evaluate("window.scrollY")
    header_box = await page.locator("header").bounding_box()
    section_el = page.locator("#here-it-is")
    section_classes = await section_el.get_attribute("class")
    section_box = await section_el.bounding_box()
    title_box = await page.locator("#here-it-is h2").bounding_box()
    card1_box = await page.locator("#here-it-is .scenario-card").nth(0).bounding_box()

    # Check photo-shimmer-sweep removal
    shimmer_count = await page.locator(".photo-shimmer-sweep").count()
    has_shimmer_css = await page.evaluate(
        "Array.from(document.styleSheets).some(s => { try { return Array.from(s.cssRules).some(r => r.cssText.includes('photo-shimmer-sweep')); } catch(e) { return false; } })"
    )

    # Check horizontal overflow on mobile/desktop
    overflow_x = await page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")

    screenshot_path = f"/workspace/agent/moore-labs/temp/verify_{name}_here_it_is.png"
    await page.screenshot(path=screenshot_path, full_page=False)

    print(f"=== [{name.upper()} ({width}x{height})] ===")
    print(f"scrollY after #here-it-is mount: {scroll_y:.1f}px")
    print(f"Header bottom: {header_box['y'] + header_box['height']:.1f}px")
    print(f"Section #here-it-is top: {section_box['y']:.1f}px, classes has scroll-mt-24: {'scroll-mt-24' in section_classes}")
    print(f"Section Title (h2) top: {title_box['y']:.1f}px, bottom: {title_box['y'] + title_box['height']:.1f}px")
    print(f"Card 01 top: {card1_box['y']:.1f}px, bottom: {card1_box['y'] + card1_box['height']:.1f}px")
    print(f"photo-shimmer-sweep DOM count: {shimmer_count}, CSS present: {has_shimmer_css}")
    print(f"Horizontal overflow: {overflow_x}, Page errors: {len(errors)}")

    # Assertions
    assert len(errors) == 0, f"Unexpected page errors: {errors}"
    assert scroll_y > 1500, f"SPA #here-it-is failed to scroll! scrollY={scroll_y}"
    assert "scroll-mt-24" in section_classes, "Missing scroll-mt-24 on #here-it-is"
    header_bottom = header_box["y"] + header_box["height"]
    assert title_box["y"] > header_bottom + 15, f"Section title is occluded by header! title_top={title_box['y']}, header_bottom={header_bottom}"
    assert title_box["y"] + title_box["height"] < height * 0.65, f"Section title not in upper-middle viewport! bottom={title_box['y'] + title_box['height']}"
    assert card1_box["y"] < height * 0.75, f"Card 01 not visible in viewport! card1_top={card1_box['y']}"
    assert shimmer_count == 0 and not has_shimmer_css, "photo-shimmer-sweep was not completely removed"
    assert not overflow_x, "Horizontal overflow detected"

    # 2. Test clicking in-page visible CTA button <a href="#here-it-is"> from top of page
    await page.evaluate("window.scrollTo(0, 0)")
    await asyncio.sleep(0.15)
    await page.locator('a[href="#here-it-is"]:visible').first.click()
    await asyncio.sleep(0.65)
    click_scroll_y = await page.evaluate("window.scrollY")
    print(f"In-page click a[href='#here-it-is']:visible scrollY: {click_scroll_y:.1f}px")
    assert click_scroll_y > 1500, f"In-page anchor click failed to scroll! scrollY={click_scroll_y}"

    await browser.close()

def verify_images_clean():
    for fname in ["conf_01_stadium_10k.jpg", "conf_03_thailand_summit_6800.jpg"]:
        p = f"/workspace/agent/moore-labs/assets/events/{fname}"
        arr = np.asarray(Image.open(p).convert("L"), dtype=np.float32)
        # Top-left corner (100x80) used to be a bright white block (mean > 215)
        tl_mean = float(arr[:80, :200].mean())
        print(f"Image {fname} top-left (200x80) mean luminance: {tl_mean:.1f} (expected < 80 for dark stadium ceiling)")
        assert tl_mean < 80.0, f"{fname} still has bright white mask in top-left! mean={tl_mean}"

async def main():
    verify_images_clean()
    async with async_playwright() as p:
        await verify_viewport(p, "desktop", 1440, 900, False)
        await verify_viewport(p, "mobile", 375, 812, True)
    print("ALL PLAYWRIGHT & IMAGE ASSERTIONS PASSED 100%!")

if __name__ == "__main__":
    asyncio.run(main())
