# -*- coding: utf-8 -*-
from PIL import Image
import os

source_dir = "/workspace/agent/moore-labs/assets/conferences"
out_dir = "/workspace/agent/moore-labs/assets/events"
os.makedirs(out_dir, exist_ok=True)

targets = [
    {
        "src": "泰国新泰华旅运集团202_p32_1_1280x720.jpg",
        "out": "conf_01_stadium_10k.jpg",
        "crop_box": None
    },
    {
        "src": "GLOBALCONSUM_p16_2_1280x960.jpg",
        "out": "conf_02_rwa_cyberport.jpg",
        "crop_box": (0, 120, 1280, 840)
    },
    {
        "src": "泰国新泰华旅运集团202_p34_1_1280x720.jpg",
        "out": "conf_03_thailand_summit_6800.jpg",
        "crop_box": None
    },
    {
        "src": "泰国新泰华旅运集团202_p27_1_1280x720.jpg",
        "out": "conf_04_bangkok_brand_2300.jpg",
        "crop_box": None
    },
    {
        "src": "GLOBALCONSUM_p7_5_2700x1519.jpg",
        "out": "conf_05_hk_signing.jpg",
        "crop_box": None
    },
    {
        "src": "GLOBALCONSUM_p25_2_1920x1280.jpg",
        "out": "conf_06_moore_web3_summit.jpg",
        "crop_box": (0, 100, 1920, 1180)
    }
]

for item in targets:
    src_p = os.path.join(source_dir, item["src"])
    out_p = os.path.join(out_dir, item["out"])
    if not os.path.exists(src_p):
        print(f"Error: missing {src_p}")
        continue
    im = Image.open(src_p).convert("RGB")
    if item["crop_box"]:
        im = im.crop(item["crop_box"])
    # resize to 800x450 (16:9) with Lanczos for ultra-crisp web rendering & fast loading
    im_resized = im.resize((800, 450), Image.Resampling.LANCZOS)
    im_resized.save(out_p, "JPEG", quality=88, optimize=True)
    size_kb = os.path.getsize(out_p) / 1024
    print(f"Saved {item['out']}: {size_kb:.1f} KB")

print("All event card images processed successfully!")
