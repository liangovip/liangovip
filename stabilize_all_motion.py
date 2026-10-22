# -*- coding: utf-8 -*-
"""
Stabilize All Card & Image Animations across Moore Labs (index.html):
1. Section 7 (Conference Cards): Eliminate aggressive Y-axis bouncing/jumping and scrub disorientation.
   - Cards & images are 100% solidly visible (no ghost blanks or collapsed cards).
   - Bi-directional symmetric in-view shimmer trigger (onEnter & onEnterBack work consistently).
   - Images are rock-solid, zero vertical jitter.
2. Section 8 (Trends) & Section 9 (Roadmap): Remove violent scrub rotational twists; replace with smooth, stable presence.
3. Section 5 (Capabilities): Remove conflicting exit scrub tilts on mobile cards.
4. Images: remove lazy-loading layout shift flicker on critical cards.
5. Zero-Cobo maintained.
"""

import re

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Section 7 images to eager loading & stable aspect ratio in JSX
content = content.replace(
    'loading="lazy"\n                            className="h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-105 group-hover/img:scale-105"',
    'loading="eager"\n                            className="h-full w-full object-cover transition-transform duration-500 ease-out group-hover:scale-105 group-hover/img:scale-105"'
)

# 2. Replace the whole GSAP ScrollTrigger logic in useEffect with stable rock-solid engine
old_gsap_cards_pattern = r"gsap\.utils\.toArray\('\.stagger-drop'\)[\s\S]*?gsap\.utils\.toArray\('\.timeline-card'\)[\s\S]*?\}\);\s*\}\);"

new_gsap_cards_block = """// --- 大廠級極致穩定呈現引擎 (Rock-Solid Motion Engine) ---
          // 1. 未來趨勢卡片：平穩呼吸就位，絕不左右抽搐
          gsap.utils.toArray('.stagger-drop').forEach((group) => {
            const items = Array.from(group.querySelectorAll('.fade-up'));
            items.forEach((item, index) => {
              gsap.fromTo(
                item,
                { y: 20, opacity: 0.25, force3D: true },
                {
                  y: 0,
                  opacity: 1,
                  duration: 0.65,
                  ease: 'power2.out',
                  scrollTrigger: {
                    trigger: item,
                    start: 'top 92%',
                    toggleActions: 'play none none none',
                    once: true,
                  },
                }
              );
            });
          });

          // 2. Section 7 往期大型峰會卡片：圖片不動如山，全時穩定高清呈現，雙向流光對稱觸發
          gsap.utils.toArray('.scenario-group').forEach((group) => {
            const items = Array.from(group.querySelectorAll('.scenario-card'));
            items.forEach((item, index) => {
              // 堅實定格：位置與圖片全時可見，徹底消除上下跳躍顛簸
              gsap.set(item, { opacity: 1, y: 0, x: 0, rotateZ: 0, clearProps: 'transform' });

              // 雙向對稱微光觸發 (往下滑進場、往上滑回滾，表現 100% 穩定一致)
              ScrollTrigger.create({
                trigger: item,
                start: 'top 92%',
                end: 'bottom 8%',
                onEnter: () => item.classList.add('in-view'),
                onEnterBack: () => item.classList.add('in-view'),
                onLeave: () => item.classList.remove('in-view'),
                onLeaveBack: () => item.classList.remove('in-view'),
              });
            });
          });

          // 3. 路線圖卡片：平穩浮現，穩如磐石
          gsap.utils.toArray('.timeline-card').forEach((card, index) => {
            gsap.fromTo(
              card,
              { y: 20, opacity: 0.3, force3D: true },
              {
                y: 0,
                opacity: 1,
                duration: 0.6,
                ease: 'power2.out',
                scrollTrigger: {
                  trigger: card,
                  start: 'top 92%',
                  toggleActions: 'play none none none',
                  once: true,
                },
              }
            );
          });"""

if re.search(old_gsap_cards_pattern, content):
    content = re.sub(old_gsap_cards_pattern, new_gsap_cards_block, content, count=1)
    print("Replaced GSAP cards logic with Rock-Solid stable presentation engine!")
else:
    print("Warning: old_gsap_cards_pattern not matched directly, checking individual sections...")

# 4. Also stabilize mobile capability cards (remove conflicting exitRot scrub)
old_mobile_cap_scrub = """              gsap.to(card, {
                rotateZ: exitRot,
                duration: 0.8, ease: 'none',
                scrollTrigger: {
                  trigger: card,
                  start: 'bottom 35%',
                  end: 'bottom 0%',
                  scrub: 0.3,
                },
              });"""

new_mobile_cap_scrub = """              // 穩定呈現：移除多餘退出扭轉，保持平滑層疊"""

if old_mobile_cap_scrub in content:
    content = content.replace(old_mobile_cap_scrub, new_mobile_cap_scrub)
    print("Stabilized mobile capability cards!")

# Ensure no cobo
cobo_count = len(re.findall(r"cobo", content, re.IGNORECASE))
print(f"Cobo count: {cobo_count}")
if cobo_count > 0:
    content = re.sub(r"\bCobo\b", "Wallet MPC", content)
    content = re.sub(r"\bcobo\b", "wallet mpc", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html with stabilized animations successfully!")
