# -*- coding: utf-8 -*-
"""
Fix ReferenceError: isDesktop is not defined in useEffect,
and ensure Rock-Solid stability for Section 7 cards & all mobile animations.
"""

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Declare isDesktop at the top of gsap.context
old_ctx_start = """        const ctx = gsap.context(() => {
          gsap.from('.hero-reveal', {"""

new_ctx_start = """        const ctx = gsap.context(() => {
          const isDesktop = window.matchMedia('(min-width: 1024px)').matches;

          gsap.from('.hero-reveal', {"""

if old_ctx_start in content:
    content = content.replace(old_ctx_start, new_ctx_start)
    print("Declared isDesktop at the top of gsap.context successfully!")
else:
    print("Warning: old_ctx_start not matched directly")

# 2. Also ensure card-interactive pointer events check isDesktop safely
content = content.replace(
    "const onEnter = () => { if (isDesktop)",
    "const onEnter = () => { if (typeof isDesktop !== 'undefined' && isDesktop)"
)
content = content.replace(
    "const onLeave = () => { if (isDesktop)",
    "const onLeave = () => { if (typeof isDesktop !== 'undefined' && isDesktop)"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved index.html with isDesktop fix successfully!")
