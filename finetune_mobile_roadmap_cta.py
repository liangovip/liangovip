# -*- coding: utf-8 -*-
"""
Fine-tune Roadmap and CTA typography for perfect mobile viewport.
"""

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix Roadmap mobile padding to avoid timeline overlapping card on small screens
old_roadmap_col = "className={idx % 2 === 0 ? 'md:pr-10' : 'md:col-start-2 md:pl-10'}"
new_roadmap_col = "className={idx % 2 === 0 ? 'pl-8 sm:pl-10 md:pl-0 md:pr-10' : 'pl-8 sm:pl-10 md:pl-10 md:col-start-2'}"

if old_roadmap_col in content:
    content = content.replace(old_roadmap_col, new_roadmap_col)
    print("Fixed Roadmap mobile padding away from timeline axis!")
else:
    print("Warning: old_roadmap_col not found directly")

# 2. Refine Roadmap card typography
old_roadmap_inner = """                          <div className="text-xs uppercase tracking-[0.28em] text-[#d2e2ff]/78">{item.time}</div>
                          <div className="mt-3 text-2xl font-medium text-white">{item.title}</div>
                          <ul className="mt-4 space-y-2 text-sm text-white/72">
                            {item.points.map((point) => (
                              <li key={point}>&#8226; {point}</li>
                            ))}
                          </ul>"""

new_roadmap_inner = """                          <div className="text-[11px] sm:text-xs uppercase tracking-[0.24em] sm:tracking-[0.28em] text-amber-400 font-mono font-semibold">{item.time}</div>
                          <div className="mt-2 sm:mt-3 text-lg sm:text-2xl font-semibold text-white leading-snug">{item.title}</div>
                          <ul className="mt-3 sm:mt-4 space-y-2 text-xs sm:text-sm text-white/75 leading-relaxed">
                            {item.points.map((point) => (
                              <li key={point} className="flex items-start gap-2">
                                <span className="text-amber-400/80 shrink-0">&#8226;</span>
                                <span className="flex-1">{point}</span>
                              </li>
                            ))}
                          </ul>"""

if old_roadmap_inner in content:
    content = content.replace(old_roadmap_inner, new_roadmap_inner)
    print("Updated Roadmap card inner typography!")
else:
    print("Warning: old_roadmap_inner not found directly")

# 3. Fix CTA title leading on mobile (avoid font overlapping)
old_cta_title = """<h2 className="mt-5 max-w-4xl text-4xl font-semibold leading-[0.95] tracking-tight text-white md:text-6xl xl:text-[88px]">"""
new_cta_title = """<h2 className="mt-5 max-w-4xl text-3xl sm:text-4xl md:text-6xl xl:text-[88px] font-bold leading-tight sm:leading-[0.98] tracking-tight text-white">"""

if old_cta_title in content:
    content = content.replace(old_cta_title, new_cta_title)
    print("Updated CTA title typography for mobile!")
else:
    print("Warning: old_cta_title not found directly")

# 4. Refine CTA action buttons
old_cta_actions = """                  <div className="mt-10 flex flex-wrap gap-4">
                    {t.ctaLinks.map((item) => (
                      <a
                        key={item}
                        href="#"
                        className="rounded-full border border-black/8 bg-white/40 px-7 py-3 text-sm font-medium text-[#1d2028] backdrop-blur-md transition hover:bg-white/55"
                      >
                        {item}
                      </a>
                    ))}
                  </div>"""

new_cta_actions = """                  <div className="mt-8 sm:mt-10 flex flex-wrap gap-3 sm:gap-4">
                    {t.ctaLinks.map((item, idx) => (
                      <a
                        key={item}
                        href={idx === 0 ? '#why-moore-labs' : idx === 1 ? '#here-it-is' : '#backers'}
                        className={`rounded-full px-6 sm:px-7 py-2.5 sm:py-3 text-xs sm:text-sm font-semibold transition active:scale-95 shadow-sm ${
                          idx === 0
                            ? 'bg-white text-black hover:bg-white/90'
                            : 'border border-white/20 bg-white/10 text-white hover:bg-white/20 backdrop-blur-md'
                        }`}
                      >
                        {item}
                      </a>
                    ))}
                  </div>"""

if old_cta_actions in content:
    content = content.replace(old_cta_actions, new_cta_actions)
    print("Updated CTA action buttons for mobile!")
else:
    print("Warning: old_cta_actions not found directly")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html successfully!")
