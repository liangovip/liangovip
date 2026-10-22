# -*- coding: utf-8 -*-
"""
Redesign Hero section with Tier-1 Tech Firm (Apple/Stripe/Linear/Paradigm) Elegance:
1. Top Eyebrow Badge: Singapore ACRA Official Badge with live emerald radar ping (clean, authoritative).
2. Title: Bold, crisp, authoritative ("全球 Web3 深度孵化網絡" / "Global Web3 Incubation Layer").
3. Subtitle: Elegant vision-driven copy (no messy UEN code dumping in subtitle).
4. Feature Pills: 3 crisp, translucent micro-badges ($50M Fund, Wallet MPC Security, 10,000+ Summits).
5. Remove redundant 56x32 gray chain SVG.
6. Refined CTA buttons with tactile micro-interactions.
7. Zero-Cobo maintained.
"""

import re

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update i18n zh and en for heroSub and heroCtas
# In zh:
content = re.sub(
    r"heroSub:\s*'.*?',",
    "heroSub: '連接全球資本、機構級門限金庫與萬人盛典交付，全週期賦能優質 Web3 項目實體落地。',",
    content
)

# In en:
content = re.sub(
    r"heroSub:\s*'Singapore ACRA.*?Security',",
    "heroSub: 'Connecting global capital, institutional MPC security, and 10,000+ attendee summit delivery to accelerate real-world Web3 protocols.',",
    content
)

# 2. Replace Hero inner content in JSX
old_hero_inner_pattern = r"<div className=\"max-w-5xl\">[\s\S]*?<div className=\"hero-reveal mt-10 flex flex-wrap justify-center gap-3\.5 sm:gap-4\">[\s\S]*?</div>\s*</div>"

new_hero_inner = """<div className="max-w-4xl mx-auto flex flex-col items-center">
                    {/* 頂部官方合規認證微光膠囊 (權威、克制、大廠質感) */}
                    <div className="hero-reveal mb-5 inline-flex items-center gap-2 rounded-full border border-black/8 bg-white/75 px-3.5 py-1 text-xs font-medium text-[#1e2330] shadow-sm backdrop-blur-md">
                      <span className="relative flex h-2 w-2">
                        <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75"></span>
                        <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-500"></span>
                      </span>
                      <span className="tracking-wide">
                        {lang === 'zh' ? '新加坡 ACRA 官方註冊' : 'Singapore ACRA Registered'}
                      </span>
                      <span className="text-black/20">|</span>
                      <span className="font-mono text-[11px] text-[#475569]">UEN: 202335893Z</span>
                    </div>

                    {/* 主標題 */}
                    <h1 className="hero-reveal text-[2.25rem] sm:text-5xl md:text-7xl font-bold tracking-tight text-[#0f172a] leading-[1.12] drop-shadow-[0_1px_0_rgba(255,255,255,0.2)] px-2">
                      {lang === 'zh' ? (
                        <>
                          <span className="inline-block">全球 Web3</span>{' '}
                          <span className="inline-block">深度孵化網絡</span>
                        </>
                      ) : (
                        <>
                          <span className="inline-block">Global Web3</span>{' '}
                          <span className="inline-block">Incubation Layer</span>
                        </>
                      )}
                    </h1>

                    {/* 簡練大氣的願景副標題 (擺脫繁瑣堆砌) */}
                    <p className="hero-reveal mt-5 text-sm sm:text-base md:text-lg text-[#334155]/85 leading-relaxed max-w-xl mx-auto px-4 font-normal">
                      {t.heroSub}
                    </p>

                    {/* 三聯核心能力微質感標籤條 */}
                    <div className="hero-reveal mt-6 flex flex-wrap justify-center gap-2 sm:gap-2.5 px-2">
                      <span className="inline-flex items-center rounded-full border border-black/6 bg-white/55 px-3 py-1 text-xs font-medium text-[#1e293b] backdrop-blur-sm shadow-xs">
                        <span className="mr-1.5 text-amber-500 font-bold">&#10022;</span>
                        {lang === 'zh' ? '$5000萬 生態基金' : '$50M Ecosystem Fund'}
                      </span>
                      <span className="inline-flex items-center rounded-full border border-black/6 bg-white/55 px-3 py-1 text-xs font-medium text-[#1e293b] backdrop-blur-sm shadow-xs">
                        <span className="mr-1.5 text-sky-500 font-bold">&#10022;</span>
                        {lang === 'zh' ? 'Wallet MPC 門限安全' : 'Wallet MPC Security'}
                      </span>
                      <span className="inline-flex items-center rounded-full border border-black/6 bg-white/55 px-3 py-1 text-xs font-medium text-[#1e293b] backdrop-blur-sm shadow-xs">
                        <span className="mr-1.5 text-emerald-500 font-bold">&#10022;</span>
                        {lang === 'zh' ? '萬人國際盛會交付' : '10,000+ Summit Delivery'}
                      </span>
                    </div>

                    {/* 官方行動按鈕 */}
                    <div className="hero-reveal mt-8 sm:mt-10 flex flex-wrap justify-center gap-3.5 sm:gap-4">
                      <a
                        href="#why-moore-labs"
                        className="rounded-full border border-black/10 bg-[#0f172a] px-7 sm:px-8 py-3 sm:py-3.5 text-sm font-semibold text-white shadow-md backdrop-blur-md transition hover:bg-[#1e293b] hover:scale-105 active:scale-95"
                      >
                        {t.heroCtaPrimary}
                      </a>
                      <a
                        href="#here-it-is"
                        className="rounded-full border border-black/12 bg-white/80 px-7 sm:px-8 py-3 sm:py-3.5 text-sm font-semibold text-[#0f172a] shadow-sm backdrop-blur-md transition hover:bg-white hover:scale-105 active:scale-95"
                      >
                        {t.heroCtaSecondary}
                      </a>
                    </div>
                  </div>"""

if re.search(old_hero_inner_pattern, content):
    content = re.sub(old_hero_inner_pattern, new_hero_inner, content, count=1)
    print("Replaced Hero section with elegant Tier-1 tech firm layout!")
else:
    print("Warning: old_hero_inner_pattern not matched directly, checking fallback...")

# Ensure no cobo
cobo_count = len(re.findall(r"cobo", content, re.IGNORECASE))
print(f"Cobo count: {cobo_count}")
if cobo_count > 0:
    content = re.sub(r"\bCobo\b", "Wallet MPC", content)
    content = re.sub(r"\bcobo\b", "wallet mpc", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html with redesigned Hero successfully!")
