# -*- coding: utf-8 -*-
"""
Extract high-resolution conference and summit photos from uploaded PDF presentations.
"""

from pypdf import PdfReader
from PIL import Image
import os
import io

pdf_paths = [
    "/workspace/.user_uploaded/GLOBALCONSUMERRWASUMMIT-deck2_1792661267932_354296.pdf",
    "/workspace/.user_uploaded/泰国新泰华旅运集团2024_1792661271732_f39494.pdf",
    "/workspace/.user_uploaded/MooreFoundationLP_1792661273934_008316.pdf"
]

out_dir = "/workspace/agent/moore-labs/assets/conferences"
os.makedirs(out_dir, exist_ok=True)

img_count = 0

for p in pdf_paths:
    if not os.path.exists(p):
        print(f"File not found: {p}")
        continue
    reader = PdfReader(p)
    base_name = os.path.basename(p)[:12].replace(" ", "_")
    print(f"Processing {base_name} with {len(reader.pages)} pages...")
    for page_idx, page in enumerate(reader.pages):
        for img_idx, img_file in enumerate(page.images):
            try:
                # img_file is an ImageFile object
                data = img_file.data
                im = Image.open(io.BytesIO(data))
                w, h = im.size
                # Only keep conference/event photos (size >= 400x250)
                if w >= 400 and h >= 250:
                    out_filename = f"{base_name}_p{page_idx+1}_{img_idx+1}_{w}x{h}.jpg"
                    out_path = os.path.join(out_dir, out_filename)
                    im.convert("RGB").save(out_path, "JPEG", quality=90)
                    img_count += 1
                    if img_count <= 30:
                        print(f"Saved: {out_filename} ({w}x{h})")
            except Exception as e:
                pass

print(f"Done! Successfully extracted {img_count} event/conference images into {out_dir}")
