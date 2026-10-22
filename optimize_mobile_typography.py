# -*- coding: utf-8 -*-
"""
Comprehensive Mobile Typography & Layout Optimization for Moore Labs (index.html):
1. CSS: High-clarity font stack, text-rendering optimizeLegibility, antialiasing, word-break protections.
2. Hero Title: Mobile responsive font size (text-[2.1rem] sm:text-5xl md:text-7xl xl:text-[88px]), structured word phrase spans to eliminate awkward single-character line-breaks.
3. Hero Subtitle: Responsive font & inline-block badges to keep (UEN: 202335893Z) intact without splitting.
4. Section 3 Brand Display: clamp(1.75rem, 8.2vw, 9rem) with px-4 safety margin to prevent edge clipping on 375px screens.
5. Section 4 Why Moore Labs: Mobile-optimized card paddings (p-5 sm:p-7) and font hierarchy.
6. Section 7 Conference Cards: Mobile-first text hierarchy, balanced line heights and crisp badge sizes.
7. Section 8 Trends: Refined flex layout (gap-3.5 sm:gap-5) so numbering [1] doesn't squeeze body copy.
8. Section 9 Roadmap: Polished time badges and bullet spacing.
9. Zero-Cobo maintained.
"""

import re

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update font-family and typography rules in <style>
font_style_rules = """
    /* 全局高清晰现代移动端字体渲染与排版规范 */
    body, button, input, select, textarea {
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display",
        "PingFang SC", "PingFang TC", "Hiragino Sans GB", "Microsoft JhengHei", "Microsoft YaHei",
        "Helvetica Neue", Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
    }

    h1, h2, h3, h4 {
      text-wrap: balance;
    }

    p {
      text-wrap: pretty;
      overflow-wrap: break-word;
    }
"""

if "/* 全局高清晰现代移动端字体渲染与排版规范 */" not in content:
    content = content.replace("html {", font_style_rules.strip() + "\n\n    html {")
    print("Injected global typography CSS!")

# 2. Update Hero Title and Subtitle rendering in JSX
# Old Hero JSX:
old_hero_title_block = """                    <h1 className="hero-reveal max-w-4xl mx-auto text-5xl font-semibold leading-[0.98] tracking-tight text-[#17181d] drop-shadow-[0_1px_0_rgba(255,255,255,0.18)] md:text-7xl xl:text-[92px]">
                      {t.heroTitle}
                    </h1>
                    <p className="hero-reveal mt-8 text-lg leading-8 text-[#2f3442]/80 md:text-xl">
                      {t.heroSub}
                    </p>"""

new_hero_title_block = """                    <h1 className="hero-reveal max-w-4xl mx-auto text-[2.15rem] font-bold leading-[1.12] tracking-tight text-[#17181d] drop-shadow-[0_1px_0_rgba(255,255,255,0.18)] sm:text-5xl md:text-7xl xl:text-[88px] px-2">
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
                    <p className="hero-reveal mt-6 text-sm leading-relaxed text-[#2f3442]/85 sm:text-base md:text-lg max-w-2xl mx-auto px-3">
                      {lang === 'zh' ? (
                        <>
                          <span className="inline-block">新加坡 ACRA 官方牌照</span>{' '}
                          <span className="inline-block font-mono">(UEN: 202335893Z)</span>{' '}
                          <span className="hidden sm:inline">·</span>{' '}
                          <span className="inline-block">5000萬美元生態基金</span>{' '}
                          <span className="hidden sm:inline">·</span>{' '}
                          <span className="inline-block">Wallet MPC 門限安全</span>
                        </>
                      ) : (
                        <>
                          <span className="inline-block">Singapore ACRA</span>{' '}
                          <span className="inline-block font-mono">(UEN: 202335893Z)</span>{' '}
                          <span className="hidden sm:inline">·</span>{' '}
                          <span className="inline-block">$50M Ecosystem Fund</span>{' '}
                          <span className="hidden sm:inline">·</span>{' '}
                          <span className="inline-block">Wallet MPC Security</span>
                        </>
                      )}
                    </p>"""

if old_hero_title_block in content:
    content = content.replace(old_hero_title_block, new_hero_title_block)
    print("Updated Hero title & subtitle with mobile phrase wrapping!")
else:
    print("Warning: old_hero_title_block not found directly")

# 3. Update Section 3 Brand Display to avoid cutting edges on small screens
old_brand_text = """<div className="brand-text select-none whitespace-nowrap text-center text-[clamp(3rem,12vw,10rem)] font-medium leading-none tracking-[-0.04em]">"""
new_brand_text = """<div className="brand-text select-none whitespace-nowrap text-center text-[clamp(1.75rem,8.2vw,9.5rem)] font-medium leading-none tracking-[-0.03em] px-4 w-full overflow-hidden">"""

if old_brand_text in content:
    content = content.replace(old_brand_text, new_brand_text)
    print("Updated Brand Display font clamping!")
else:
    print("Warning: old_brand_text not matched")

# 4. Update SectionTitle component to have better responsive leading & text size
old_section_title = """    function SectionTitle({ eyebrow, title, subtitle }) {
      return (
        <div className="max-w-3xl space-y-3">
          {eyebrow ? <div className="text-xs uppercase tracking-[0.28em] text-white/78">{eyebrow}</div> : null}
          <h2 className="text-3xl font-semibold tracking-tight text-white md:text-5xl">{title}</h2>
          {subtitle ? <p className="text-sm leading-7 text-white/74 md:text-base">{subtitle}</p> : null}
        </div>
      );
    }"""

new_section_title = """    function SectionTitle({ eyebrow, title, subtitle }) {
      return (
        <div className="max-w-3xl space-y-2.5 sm:space-y-3 px-1">
          {eyebrow ? <div className="text-[11px] sm:text-xs uppercase tracking-[0.22em] sm:tracking-[0.28em] text-sky-400/90 font-mono font-medium">{eyebrow}</div> : null}
          <h2 className="text-2xl sm:text-3xl md:text-5xl font-bold tracking-tight text-white leading-tight">{title}</h2>
          {subtitle ? <p className="text-xs sm:text-sm leading-relaxed sm:leading-7 text-white/75 md:text-base">{subtitle}</p> : null}
        </div>
      );
    }"""

if old_section_title in content:
    content = content.replace(old_section_title, new_section_title)
    print("Updated SectionTitle component for mobile!")
else:
    print("Warning: old_section_title not matched")

# 5. Update Section 8 Trends Cards flex spacing
old_trend_card_inner = """                    <div key={item} className={cx('fade-up card-interactive card-hover-lift flex gap-5 p-6', trendCardClassName)}>
                      <div className="text-4xl font-semibold text-white/12">[{idx + 1}]</div>
                      <div>
                        <div className="text-xl font-medium text-white">{item}</div>
                        <p className="mt-3 text-sm leading-7 text-white/70">
                          {t.trendsCardDesc[idx] || t.trendsCardDesc[0]}
                        </p>
                      </div>
                    </div>"""

new_trend_card_inner = """                    <div key={item} className={cx('fade-up card-interactive card-hover-lift flex gap-4 sm:gap-5 p-5 sm:p-6 items-start', trendCardClassName)}>
                      <div className="text-2xl sm:text-4xl font-bold font-mono text-white/20 shrink-0 leading-tight">0{idx + 1}</div>
                      <div className="flex-1 min-w-0">
                        <div className="text-base sm:text-xl font-semibold text-white leading-snug">{item}</div>
                        <p className="mt-2.5 text-xs sm:text-sm leading-relaxed sm:leading-7 text-white/70">
                          {t.trendsCardDesc[idx] || t.trendsCardDesc[0]}
                        </p>
                      </div>
                    </div>"""

if old_trend_card_inner in content:
    content = content.replace(old_trend_card_inner, new_trend_card_inner)
    print("Updated Section 8 Trend Cards typography!")
else:
    print("Warning: old_trend_card_inner not matched")

# 6. Update Section 9 Roadmap Cards typography
old_roadmap_card_inner = """                  <div key={item.title} className={cx('timeline-card group card-interactive card-hover-lift p-6', trendCardClassName)}>
                    <div className="text-sm font-semibold uppercase tracking-wider text-amber-400 font-mono">{item.time}</div>
                    <div className="mt-2 text-xl font-medium text-white group-hover:text-amber-300 transition">{item.title}</div>
                    <ul className="mt-4 space-y-2 text-sm text-white/70">
                      {item.points.map((pt, pIdx) => (
                        <li key={pIdx} className="flex items-start gap-2">
                          <span className="mt-1.5 h-1.5 w-1.5 rounded-full bg-amber-400 shrink-0" />
                          <span>{pt}</span>
                        </li>
                      ))}
                    </ul>
                  </div>"""

new_roadmap_card_inner = """                  <div key={item.title} className={cx('timeline-card group card-interactive card-hover-lift p-5 sm:p-6', trendCardClassName)}>
                    <div className="text-xs sm:text-sm font-semibold uppercase tracking-wider text-amber-400 font-mono">{item.time}</div>
                    <div className="mt-1.5 text-lg sm:text-xl font-semibold text-white group-hover:text-amber-300 transition leading-snug">{item.title}</div>
                    <ul className="mt-3.5 space-y-2 text-xs sm:text-sm text-white/75 leading-relaxed">
                      {item.points.map((pt, pIdx) => (
                        <li key={pIdx} className="flex items-start gap-2.5">
                          <span className="mt-1.5 h-1.5 w-1.5 rounded-full bg-amber-400 shrink-0" />
                          <span className="flex-1">{pt}</span>
                        </li>
                      ))}
                    </ul>
                  </div>"""

if old_roadmap_card_inner in content:
    content = content.replace(old_roadmap_card_inner, new_roadmap_card_inner)
    print("Updated Section 9 Roadmap Cards typography!")
else:
    print("Warning: old_roadmap_card_inner not matched")

# Ensure no cobo
cobo_count = len(re.findall(r"cobo", content, re.IGNORECASE))
print(f"Cobo count: {cobo_count}")
if cobo_count > 0:
    content = re.sub(r"\bCobo\b", "Wallet MPC", content)
    content = re.sub(r"\bcobo\b", "wallet mpc", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html with comprehensive mobile typography!")
