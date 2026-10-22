# -*- coding: utf-8 -*-
"""
Apply Tier-1 Tech Firm (Apple/Stripe/Linear) Mobile Delight Dynamic Motion System to Moore Labs index.html:
1. CSS: Mobile ambient shimmer glow, tactile touch scale feedback, radar pulse rings, photo sweep shimmer.
2. GSAP: Responsive Mobile In-View Spring Entrance Engine (vertical clean spring, 0 horizontal jitter, once: true).
3. Mobile Capability Cards: Refined micro-tilt damping, eliminating severe shaking.
4. Radar dot and photo shimmer sweep attached to Section 7 conference cards.
5. Marquee: Hardware accelerated with -webkit-backface-visibility and touch scroll protection.
6. Zero-Cobo strictly maintained.
"""

import re

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update CSS style block with mobile delight animation keyframes and rules
css_mobile_block = """
    /* --- 大厂级移动端优雅动效引擎 (Apple/Linear/Stripe Mobile Motion System) --- */
    @keyframes mobileAmbientGlow {
      0%, 100% {
        opacity: 0.32;
        transform: translate3d(0, 0, 0);
      }
      50% {
        opacity: 0.72;
        transform: translate3d(1.5%, 1%, 0);
      }
    }

    @keyframes mobileBorderPulse {
      0%, 100% {
        border-color: rgba(255, 255, 255, 0.12);
        box-shadow: 0 0 14px rgba(56, 189, 248, 0.04);
      }
      50% {
        border-color: rgba(125, 211, 252, 0.32);
        box-shadow: 0 0 26px rgba(56, 189, 248, 0.14);
      }
    }

    @keyframes radarPing {
      0% { transform: scale(1); opacity: 0.85; }
      80%, 100% { transform: scale(2.8); opacity: 0; }
    }

    @keyframes photoShimmer {
      0% { transform: translateX(-150%) skewX(-15deg); }
      100% { transform: translateX(250%) skewX(-15deg); }
    }

    .radar-ring {
      position: absolute;
      inset: -2px;
      border-radius: 9999px;
      background-color: rgba(52, 211, 153, 0.55);
      animation: radarPing 2.2s cubic-bezier(0, 0, 0.2, 1) infinite;
      pointer-events: none;
    }

    .photo-shimmer-sweep {
      position: relative;
      overflow: hidden;
    }

    .photo-shimmer-sweep::after {
      content: '';
      position: absolute;
      top: 0;
      bottom: 0;
      left: 0;
      width: 60%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.22), transparent);
      transform: translateX(-150%) skewX(-15deg);
      pointer-events: none;
    }

    .in-view .photo-shimmer-sweep::after {
      animation: photoShimmer 1.5s ease-out forwards;
    }

    /* 移动端触摸屏专属微触觉与常态微流动光晕 */
    @media (max-width: 1023px) {
      .shine-card::before {
        opacity: 0.52 !important;
        animation: mobileAmbientGlow 7s ease-in-out infinite alternate !important;
      }
      .scenario-card,
      .cap-mobile-card {
        animation: mobileBorderPulse 6.5s ease-in-out infinite alternate;
      }
      .scenario-card {
        transition: transform 0.2s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.2s ease, border-color 0.2s ease !important;
      }
    }

    @media (hover: none) and (pointer: coarse) {
      /* 手机真实触控反馈 */
      .card-interactive:active,
      .scenario-card:active,
      .cap-mobile-card:active,
      .timeline-card:active {
        transform: scale(0.982) translateZ(0) !important;
        border-color: rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 0 24px rgba(56, 189, 248, 0.22), 0 12px 32px rgba(3, 8, 20, 0.3) !important;
        filter: brightness(1.08) !important;
        transition: transform 0.12s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.12s ease, filter 0.12s ease !important;
      }
    }

    /* 跑马灯移动端极速硬件加速 */
    .animate-marquee,
    .animate-marquee-reverse {
      will-change: transform;
      -webkit-backface-visibility: hidden;
      backface-visibility: hidden;
      transform: translate3d(0, 0, 0);
    }
  </style>"""

# Replace the closing </style>
if "</style>" in content:
    content = content.replace("  </style>", css_mobile_block)
    print("Injected mobile delight CSS styles!")
else:
    print("Error: </style> not found")

# 2. Update Section 7 cards JSX: add radar-ring and photo-shimmer-sweep
old_img_container = """                          <div className="absolute bottom-3 left-3 flex items-center gap-2 text-xs text-white/95">
                            <span className="inline-block h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.9)] animate-pulse" />
                            <span className="font-mono tracking-wide font-medium">{item.location}</span>
                          </div>"""

new_img_container = """                          <div className="absolute bottom-3 left-3 flex items-center gap-2 text-xs text-white/95">
                            <div className="relative flex h-2.5 w-2.5 items-center justify-center">
                              <span className="radar-ring" />
                              <span className="relative inline-block h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.9)]" />
                            </div>
                            <span className="font-mono tracking-wide font-medium">{item.location}</span>
                          </div>"""

if old_img_container in content:
    content = content.replace(old_img_container, new_img_container)
    print("Injected radar ring into Section 7 cards!")
else:
    print("Warning: old_img_container not found directly")

# Add photo-shimmer-sweep class to image container
content = content.replace(
    'relative mb-5 w-full h-48 md:h-52 overflow-hidden rounded-2xl border border-white/10 bg-slate-900/60 shadow-inner group/img',
    'relative mb-5 w-full h-48 md:h-52 overflow-hidden rounded-2xl border border-white/10 bg-slate-900/60 shadow-inner group/img photo-shimmer-sweep'
)

# 3. Update GSAP scroll animations for stagger-drop, scenario-group, and timeline-card
# Check and replace in useEffect:
old_stagger = """          gsap.utils.toArray('.stagger-drop').forEach((group) => {
            const items = Array.from(group.querySelectorAll('.fade-up'));
            items.forEach((item, index) => {
              const direction = index % 2 === 0 ? -1 : 1;
              const fromX = direction * (16 + index * 7);
              const fromY = 86 + index * 20;
              const fromRotate = direction * (2.8 + index * 0.6);
              const endRotate = direction * (0.85 + index * 0.08);
              const endX = direction * (1.8 + index * 0.35);

              gsap.fromTo(
                item,
                {
                  y: fromY, x: fromX, rotateZ: fromRotate, rotateX: 2,
                  scale: 0.988, opacity: 0.16, transformOrigin: '50% 88%', force3D: true,
                },
                {
                  y: 0, x: endX, rotateZ: endRotate, rotateX: 0, scale: 1, opacity: 1, ease: 'none',
                  scrollTrigger: {
                    trigger: item,
                    start: () => `top ${98 - index * 6}%`,
                    end: () => `top ${70 - index * 4}%`,
                    scrub: true,
                  },
                }
              );
            });
          });"""

new_stagger = """          gsap.utils.toArray('.stagger-drop').forEach((group) => {
            const items = Array.from(group.querySelectorAll('.fade-up'));
            items.forEach((item, index) => {
              if (isDesktop) {
                const direction = index % 2 === 0 ? -1 : 1;
                const fromX = direction * (16 + index * 7);
                const fromY = 86 + index * 20;
                const fromRotate = direction * (2.8 + index * 0.6);
                const endRotate = direction * (0.85 + index * 0.08);
                const endX = direction * (1.8 + index * 0.35);

                gsap.fromTo(
                  item,
                  {
                    y: fromY, x: fromX, rotateZ: fromRotate, rotateX: 2,
                    scale: 0.988, opacity: 0.16, transformOrigin: '50% 88%', force3D: true,
                  },
                  {
                    y: 0, x: endX, rotateZ: endRotate, rotateX: 0, scale: 1, opacity: 1, ease: 'none',
                    scrollTrigger: {
                      trigger: item,
                      start: () => `top ${98 - index * 6}%`,
                      end: () => `top ${70 - index * 4}%`,
                      scrub: true,
                    },
                  }
                );
              } else {
                // 手機端：純正縱向微彈性上浮，杜絕橫向晃動
                gsap.fromTo(
                  item,
                  { y: 32, opacity: 0.08, scale: 0.97, force3D: true },
                  {
                    y: 0, opacity: 1, scale: 1, duration: 0.75, ease: 'power3.out',
                    scrollTrigger: {
                      trigger: item,
                      start: 'top 88%',
                      toggleActions: 'play none none none',
                      once: true,
                    },
                  }
                );
              }
            });
          });"""

if old_stagger in content:
    content = content.replace(old_stagger, new_stagger)
    print("Updated stagger-drop GSAP with mobile adaptation!")
else:
    print("Warning: old_stagger not found directly")

old_scenarios_gsap = """          gsap.utils.toArray('.scenario-group').forEach((group) => {
            const items = Array.from(group.querySelectorAll('.scenario-card'));
            items.forEach((item, index) => {
              const direction = index % 2 === 0 ? 1 : -1;
              const fromX = direction * (18 + index * 8);
              const fromY = 96 + index * 22;
              const fromRotate = direction * (3 + index * 0.7);
              const endRotate = direction * (0.95 + index * 0.1);
              const endX = direction * (2.1 + index * 0.45);

              gsap.fromTo(
                item,
                {
                  y: fromY, x: fromX, rotateZ: fromRotate, rotateX: 2,
                  scale: 0.988, opacity: 0.14, transformOrigin: '50% 88%', force3D: true,
                },
                {
                  y: 0, x: endX, rotateZ: endRotate, rotateX: 0, scale: 1, opacity: 1, ease: 'none',
                  scrollTrigger: {
                    trigger: item,
                    start: () => `top ${99 - index * 6}%`,
                    end: () => `top ${72 - index * 4}%`,
                    scrub: true,
                  },
                }
              );
            });
          });"""

new_scenarios_gsap = """          gsap.utils.toArray('.scenario-group').forEach((group) => {
            const items = Array.from(group.querySelectorAll('.scenario-card'));
            items.forEach((item, index) => {
              if (isDesktop) {
                const direction = index % 2 === 0 ? 1 : -1;
                const fromX = direction * (18 + index * 8);
                const fromY = 96 + index * 22;
                const fromRotate = direction * (3 + index * 0.7);
                const endRotate = direction * (0.95 + index * 0.1);
                const endX = direction * (2.1 + index * 0.45);

                gsap.fromTo(
                  item,
                  {
                    y: fromY, x: fromX, rotateZ: fromRotate, rotateX: 2,
                    scale: 0.988, opacity: 0.14, transformOrigin: '50% 88%', force3D: true,
                  },
                  {
                    y: 0, x: endX, rotateZ: endRotate, rotateX: 0, scale: 1, opacity: 1, ease: 'none',
                    scrollTrigger: {
                      trigger: item,
                      start: () => `top ${99 - index * 6}%`,
                      end: () => `top ${72 - index * 4}%`,
                      scrub: true,
                    },
                  }
                );
              } else {
                // 手機端：大廠級視口進入觸發 + 圖片流光掠影
                gsap.fromTo(
                  item,
                  { y: 36, opacity: 0.08, scale: 0.96, force3D: true },
                  {
                    y: 0, opacity: 1, scale: 1, duration: 0.8, ease: 'power3.out',
                    scrollTrigger: {
                      trigger: item,
                      start: 'top 88%',
                      toggleActions: 'play none none none',
                      once: true,
                      onEnter: () => {
                        item.classList.add('in-view');
                      },
                    },
                  }
                );
              }
            });
          });"""

if old_scenarios_gsap in content:
    content = content.replace(old_scenarios_gsap, new_scenarios_gsap)
    print("Updated scenario-group GSAP with mobile adaptation!")
else:
    print("Warning: old_scenarios_gsap not found directly")

old_timeline = """          gsap.utils.toArray('.timeline-card').forEach((card, index) => {
            const direction = index % 2 === 0 ? -1 : 1;
            const endX = direction * 1.1;
            const endRotate = direction * 0.55;

            gsap.fromTo(
              card,
              {
                y: 78, x: direction * 14, rotateZ: direction * 1.8, rotateX: 1.5,
                scale: 0.992, opacity: 0.2, transformOrigin: '50% 88%', force3D: true,
              },
              {
                y: 0, x: endX, rotateZ: endRotate, rotateX: 0, scale: 1, opacity: 1, ease: 'none',
                scrollTrigger: {
                  trigger: card,
                  start: () => `top ${99 - index * 4}%`,
                  end: () => `top ${74 - index * 3}%`,
                  scrub: true,
                },
              }
            );
          });"""

new_timeline = """          gsap.utils.toArray('.timeline-card').forEach((card, index) => {
            if (isDesktop) {
              const direction = index % 2 === 0 ? -1 : 1;
              const endX = direction * 1.1;
              const endRotate = direction * 0.55;

              gsap.fromTo(
                card,
                {
                  y: 78, x: direction * 14, rotateZ: direction * 1.8, rotateX: 1.5,
                  scale: 0.992, opacity: 0.2, transformOrigin: '50% 88%', force3D: true,
                },
                {
                  y: 0, x: endX, rotateZ: endRotate, rotateX: 0, scale: 1, opacity: 1, ease: 'none',
                  scrollTrigger: {
                    trigger: card,
                    start: () => `top ${99 - index * 4}%`,
                    end: () => `top ${74 - index * 3}%`,
                    scrub: true,
                  },
                }
              );
            } else {
              // 手機端：優雅彈性就位
              gsap.fromTo(
                card,
                { y: 30, opacity: 0.1, scale: 0.97, force3D: true },
                {
                  y: 0, opacity: 1, scale: 1, duration: 0.75, ease: 'power3.out',
                  scrollTrigger: {
                    trigger: card,
                    start: 'top 88%',
                    toggleActions: 'play none none none',
                    once: true,
                  },
                }
              );
            }
          });"""

if old_timeline in content:
    content = content.replace(old_timeline, new_timeline)
    print("Updated timeline-card GSAP with mobile adaptation!")
else:
    print("Warning: old_timeline not found directly")

# 4. Refine mobile capability cards micro-damping
old_mobile_cap = """            const mobileCards = gsap.utils.toArray('.cap-mobile-card');

            mobileCards.forEach((card, i) => {
              const isLeft = i % 2 === 0;
              const entryRot = isLeft ? -10 : 10;
              const exitRot = isLeft ? 8 : -8;

              gsap.set(card, {
                y: 80, x: isLeft ? -40 : 40, rotateZ: entryRot, scale: 0.94, autoAlpha: 0, force3D: true,
              });

              gsap.to(card, {
                y: 0, x: 0, rotateZ: 0, scale: 1, autoAlpha: 1,
                duration: 1, ease: 'none',
                scrollTrigger: {
                  trigger: card,
                  start: 'top 105%',
                  end: 'top 55%',
                  scrub: 0.4,
                },
              });

              gsap.to(card, {
                rotateZ: exitRot,
                duration: 1, ease: 'none',
                scrollTrigger: {
                  trigger: card,
                  start: 'bottom 35%',
                  end: 'bottom 0%',
                  scrub: 0.4,
                },
              });
            });"""

new_mobile_cap = """            const mobileCards = gsap.utils.toArray('.cap-mobile-card');

            mobileCards.forEach((card, i) => {
              const isLeft = i % 2 === 0;
              const entryRot = isLeft ? -3 : 3;
              const exitRot = isLeft ? 2 : -2;

              gsap.set(card, {
                y: 50, x: isLeft ? -10 : 10, rotateZ: entryRot, scale: 0.96, autoAlpha: 0, force3D: true,
              });

              gsap.to(card, {
                y: 0, x: 0, rotateZ: 0, scale: 1, autoAlpha: 1,
                duration: 0.8, ease: 'none',
                scrollTrigger: {
                  trigger: card,
                  start: 'top 98%',
                  end: 'top 60%',
                  scrub: 0.3,
                },
              });

              gsap.to(card, {
                rotateZ: exitRot,
                duration: 0.8, ease: 'none',
                scrollTrigger: {
                  trigger: card,
                  start: 'bottom 35%',
                  end: 'bottom 0%',
                  scrub: 0.3,
                },
              });
            });"""

if old_mobile_cap in content:
    content = content.replace(old_mobile_cap, new_mobile_cap)
    print("Refined cap-mobile-card micro-damping!")
else:
    print("Warning: old_mobile_cap not found directly")

# 5. Add touchstart / touchend event listeners to interactive cards
old_card_interactive = """          gsap.utils.toArray('.card-interactive:not(.cap-card)').forEach((card) => {
            const onEnter = () => { gsap.to(card, { y: -4, scale: 1.008, duration: 0.24, ease: 'power2.out', overwrite: 'auto' }); };
            const onLeave = () => { gsap.to(card, { y: 0, scale: 1, duration: 0.28, ease: 'power2.out', overwrite: 'auto' }); };
            const onDown = () => { gsap.to(card, { y: -2, scale: 0.994, duration: 0.12, ease: 'power2.out', overwrite: 'auto' }); };
            const onUp = () => { gsap.to(card, { y: -4, scale: 1.008, duration: 0.16, ease: 'power2.out', overwrite: 'auto' }); };

            card.addEventListener('pointerenter', onEnter);
            card.addEventListener('pointerleave', onLeave);
            card.addEventListener('pointerdown', onDown);
            card.addEventListener('pointerup', onUp);
            card.addEventListener('pointercancel', onLeave);

            interactiveCards.push({ element: card, onEnter, onLeave, onDown, onUp });
          });"""

new_card_interactive = """          gsap.utils.toArray('.card-interactive:not(.cap-card)').forEach((card) => {
            const onEnter = () => { if (isDesktop) gsap.to(card, { y: -4, scale: 1.008, duration: 0.24, ease: 'power2.out', overwrite: 'auto' }); };
            const onLeave = () => { if (isDesktop) gsap.to(card, { y: 0, scale: 1, duration: 0.28, ease: 'power2.out', overwrite: 'auto' }); };
            const onDown = () => { gsap.to(card, { scale: 0.985, duration: 0.12, ease: 'power2.out', overwrite: 'auto' }); };
            const onUp = () => { gsap.to(card, { scale: 1, duration: 0.22, ease: 'elastic.out(1, 0.4)', overwrite: 'auto' }); };

            card.addEventListener('pointerenter', onEnter);
            card.addEventListener('pointerleave', onLeave);
            card.addEventListener('pointerdown', onDown);
            card.addEventListener('pointerup', onUp);
            card.addEventListener('pointercancel', onLeave);

            // 手機觸摸屏原生觸覺彈性反饋
            card.addEventListener('touchstart', onDown, { passive: true });
            card.addEventListener('touchend', onUp, { passive: true });
            card.addEventListener('touchcancel', onUp, { passive: true });

            interactiveCards.push({ element: card, onEnter, onLeave, onDown, onUp });
          });"""

if old_card_interactive in content:
    content = content.replace(old_card_interactive, new_card_interactive)
    print("Injected mobile touch event listeners!")
else:
    print("Warning: old_card_interactive not found directly")

# Ensure no cobo introduced
cobo_count = len(re.findall(r"cobo", content, re.IGNORECASE))
print(f"Cobo count: {cobo_count}")
if cobo_count > 0:
    content = re.sub(r"\bCobo\b", "Wallet MPC", content)
    content = re.sub(r"\bcobo\b", "wallet mpc", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html with all mobile delight motion systems!")
