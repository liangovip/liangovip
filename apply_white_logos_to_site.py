# -*- coding: utf-8 -*-
"""
Apply 36 unified white transparent logos to index.html.
No blue backgrounds, no card outlines, optical alignment, smooth hover bright/scale.
"""

import json

with open("/workspace/agent/moore-labs/assets/backers/white_manifest.json", "r", encoding="utf-8") as f:
    manifest = json.load(f)

with open("/workspace/agent/moore-labs/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update backers array in index.html
backers_js = "    const backers = [\n"
for item in manifest:
    name_escaped = item['name'].replace("'", "\\'")
    backers_js += f"      {{ name: '{name_escaped}', logo: '{item['white_logo']}' }},\n"
backers_js += "    ];"

# Find old backers definition
import re
old_backers_match = re.search(r"    const backers = \[\n[\s\S]*?    \];", content)
assert old_backers_match is not None, "Could not find old backers array"
content = content[:old_backers_match.start()] + backers_js + content[old_backers_match.end():]

# 2. Update the Backers section JSX
old_section = """            <section id="backers" className="relative border-y border-white/10 bg-[#0f1624] py-12">
              <div className="mx-auto max-w-7xl overflow-hidden px-6 lg:px-10">
                <div className="mb-6 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                  <div className="text-sm uppercase tracking-[0.28em] text-white/60">Backers & Global Media Partners</div>
                  <div className="text-xs tracking-wider text-white/40">36+ Tier-1 Crypto Media & Strategic Allies</div>
                </div>
                <div className="relative overflow-hidden space-y-4">
                  {/* Row 1: 向左平滑流动 (18家媒体与生态机构) */}
                  <div className="flex min-w-max animate-marquee gap-4">
                    {marqueeRow1.map((item, idx) => (
                      <div
                        key={`r1-${item.name}-${idx}`}
                        className="flex items-center justify-center rounded-2xl border border-white/10 bg-white/5 p-1 backdrop-blur-md transition hover:border-amber-400/50 hover:scale-105"
                      >
                        <img src={item.logo} alt={item.name} className="h-10 w-auto rounded-xl object-contain drop-shadow" />
                      </div>
                    ))}
                  </div>

                  {/* Row 2: 反向向右平滑流动 (18家媒体与战略盟友) */}
                  <div className="flex min-w-max animate-marquee-reverse gap-4">
                    {marqueeRow2.map((item, idx) => (
                      <div
                        key={`r2-${item.name}-${idx}`}
                        className="flex items-center justify-center rounded-2xl border border-white/10 bg-white/5 p-1 backdrop-blur-md transition hover:border-amber-400/50 hover:scale-105"
                      >
                        <img src={item.logo} alt={item.name} className="h-10 w-auto rounded-xl object-contain drop-shadow" />
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </section>"""

new_section = """            <section id="backers" className="relative border-y border-white/10 bg-[#0f1624] py-14">
              <div className="mx-auto max-w-7xl overflow-hidden px-6 lg:px-10">
                <div className="mb-8 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                  <div className="text-sm uppercase tracking-[0.28em] text-white/60">Backers & Global Media Partners</div>
                  <div className="text-xs tracking-wider text-white/40">36+ Strategic Media & Tier-1 Crypto Allies (Color-Unified & Transparent)</div>
                </div>
                <div className="relative overflow-hidden space-y-6">
                  {/* Row 1: 向左平滑流动 (前18家媒体，透明纯白，悬浮高亮放大) */}
                  <div className="flex min-w-max animate-marquee gap-8 items-center">
                    {marqueeRow1.map((item, idx) => (
                      <div
                        key={`r1-${item.name}-${idx}`}
                        className="flex h-12 min-w-[120px] items-center justify-center px-3 opacity-65 transition-all duration-300 hover:opacity-100 hover:scale-110 cursor-pointer"
                        title={item.name}
                      >
                        <img
                          src={item.logo}
                          alt={item.name}
                          className="h-7 max-h-8 w-auto max-w-[150px] object-contain drop-shadow"
                          loading="lazy"
                        />
                      </div>
                    ))}
                  </div>

                  {/* Row 2: 反向向右平滑流动 (后18家媒体，透明纯白，悬浮高亮放大) */}
                  <div className="flex min-w-max animate-marquee-reverse gap-8 items-center">
                    {marqueeRow2.map((item, idx) => (
                      <div
                        key={`r2-${item.name}-${idx}`}
                        className="flex h-12 min-w-[120px] items-center justify-center px-3 opacity-65 transition-all duration-300 hover:opacity-100 hover:scale-110 cursor-pointer"
                        title={item.name}
                      >
                        <img
                          src={item.logo}
                          alt={item.name}
                          className="h-7 max-h-8 w-auto max-w-[150px] object-contain drop-shadow"
                          loading="lazy"
                        />
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </section>"""

assert old_section in content, "old_section not found"
content = content.replace(old_section, new_section)

with open("/workspace/agent/moore-labs/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: 36 unified white transparent logos applied to index.html!")
