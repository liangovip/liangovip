# -*- coding: utf-8 -*-
"""
High-Precision White Transparent Logo Extractor for all 36 Partners.
Completely removes background gradients, card borders, and internal shadow boxes.
Produces pure white (#FFFFFF) foreground with smooth alpha transparency.
"""

from PIL import Image
import numpy as np
import os, json

manifest_path = "/workspace/agent/moore-labs/assets/backers/backers_manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

img_full = Image.open("/workspace/.user_uploaded/image_1792662687875_0adfdd.png")

col_coords = [
    (45, 294),
    (331, 580),
    (616, 865),
    (902, 1151),
    (1187, 1437),
    (1473, 1722)
]

row_coords = [
    (42, 140),
    (168, 266),
    (294, 392),
    (420, 518),
    (546, 644),
    (672, 770)
]

out_dir = "/workspace/agent/moore-labs/assets/backers"
results = []

for item in manifest:
    idx = item["id"]
    r = item["row"]
    c = item["col"]
    slug = item["slug"]
    name = item["name"]
    x1, x2 = col_coords[c]
    y1, y2 = row_coords[r]
    
    card = img_full.crop((x1, y1, x2, y2)).convert("RGBA")
    w, h = card.size
    
    # 12px horizontal and 10px vertical inset to eliminate outer border
    inset_x = 12
    inset_y = 10
    card_inner = card.crop((inset_x, inset_y, w - inset_x, h - inset_y))
    arr = np.array(card_inner, dtype=np.float32)
    
    # Sample background color from edge strips
    top_edge = arr[:6, :, :3].reshape(-1, 3)
    bot_edge = arr[-6:, :, :3].reshape(-1, 3)
    left_edge = arr[:, :6, :3].reshape(-1, 3)
    right_edge = arr[:, -6:, :3].reshape(-1, 3)
    edges = np.concatenate([top_edge, bot_edge, left_edge, right_edge], axis=0)
    bg_color = np.median(edges, axis=0)
    bg_lum = 0.299 * bg_color[0] + 0.587 * bg_color[1] + 0.114 * bg_color[2]
    
    # Pixel distance and lum diff
    diff_color = np.sqrt(np.sum((arr[:, :, :3] - bg_color) ** 2, axis=2))
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    diff_lum = np.maximum(0, lum - bg_lum)
    
    metric = np.maximum(diff_color, diff_lum * 1.5)
    
    # For shadow-box cards, determine threshold dynamically
    # Non-background pixels are typically above 82th percentile
    p80 = np.percentile(metric, 80)
    max_m = metric.max()
    
    # Base threshold
    thresh = 28.0
    if slug in ["us_post_now", "universal_guide", "budao_labs", "us_times_today", "public_shade"]:
        thresh = max(45.0, p80 * 0.75)
    elif slug == "press9":
        # Press9 has a white box on left with a green tick, extract text and outline cleanly
        thresh = 35.0
        
    alpha = np.clip((metric - thresh) / 20.0, 0.0, 1.0) * 255.0
    
    # Pure white output
    out_arr = np.zeros_like(arr, dtype=np.uint8)
    out_arr[:, :, 0] = 255
    out_arr[:, :, 1] = 255
    out_arr[:, :, 2] = 255
    out_arr[:, :, 3] = alpha.astype(np.uint8)
    
    res = Image.fromarray(out_arr, "RGBA")
    bbox = res.getbbox()
    if bbox:
        cropped = res.crop(bbox)
        # Add 12px transparent padding around logo
        final_im = Image.new("RGBA", (cropped.width + 24, cropped.height + 24), (0, 0, 0, 0))
        final_im.paste(cropped, (12, 12), cropped)
    else:
        final_im = res
        
    out_filename = f"backer_white_{idx:02d}_{slug}.png"
    out_path = os.path.join(out_dir, out_filename)
    final_im.save(out_path)
    results.append({
        "id": idx,
        "name": name,
        "slug": slug,
        "white_logo": f"./assets/backers/{out_filename}",
        "width": final_im.width,
        "height": final_im.height
    })

with open(os.path.join(out_dir, "white_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Generate composite sheet on site dark background #0f1624
comp_w = 1200
comp_h = 750
comp_bg = Image.new("RGBA", (comp_w, comp_h), (15, 22, 36, 255))

for idx, item in enumerate(results):
    r = idx // 6
    c = idx % 6
    cell_w = comp_w // 6
    cell_h = comp_h // 6
    
    logo = Image.open(os.path.join(out_dir, f"backer_white_{idx:02d}_{item['slug']}.png"))
    aspect = logo.width / max(1, logo.height)
    th = 32
    tw = min(150, int(th * aspect))
    logo_thumb = logo.resize((tw, th), Image.Resampling.LANCZOS)
    
    paste_x = c * cell_w + (cell_w - tw) // 2
    paste_y = r * cell_h + (cell_h - th) // 2
    comp_bg.paste(logo_thumb, (paste_x, paste_y), logo_thumb)

comp_bg.save(os.path.join(out_dir, "composite_white_matrix_preview.png"))
print(f"Successfully refined all {len(results)} white transparent logos!")
