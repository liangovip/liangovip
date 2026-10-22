# -*- coding: utf-8 -*-
"""
Update Moore Labs index.html:
1. Fix top header mobile layout & typography distortion (prevent shrinking/wrapping, shrink-0 whitespace-nowrap).
2. Remove connect wallet & launch app buttons completely ("we are purely an official showcase portal").
3. Update Hero CTAs to pure official portal actions: "Explore Ecosystem" & "Past Summits".
4. Clean up unused wallet modal states and DOM.
5. Dual language support (Traditional Chinese & English) 100% maintained.
6. Zero-Cobo strictly maintained.
"""

import re

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update i18n zh
old_zh_cta_links = "ctaLinks: ['探索核心架構', '查閱官方白皮書', '啟動應用'],"
new_zh_cta_links = "ctaLinks: ['探索核心架構', '往期大型盛會', '聯絡官方合作'],"
content = content.replace(old_zh_cta_links, new_zh_cta_links)

old_en_cta_links = "ctaLinks: ['Explore infrastructure', 'Read the docs', 'Launch app'],"
new_en_cta_links = "ctaLinks: ['Explore Infrastructure', 'Past Mega Summits', 'Contact Us'],"
content = content.replace(old_en_cta_links, new_en_cta_links)

# Add heroCtaPrimary & heroCtaSecondary in zh
zh_hero_tag_pattern = r"(heroTag:\s*'MOORE LABS 摩爾資本',)"
zh_hero_cta_insert = r"\1\n        heroCtaPrimary: '探索生態',\n        heroCtaSecondary: '往期盛會',"
content = re.sub(zh_hero_tag_pattern, zh_hero_cta_insert, content)

# Add heroCtaPrimary & heroCtaSecondary in en
en_hero_tag_pattern = r"(heroTag:\s*'MOORE LABS',)"
en_hero_cta_insert = r"\1\n        heroCtaPrimary: 'Explore Ecosystem',\n        heroCtaSecondary: 'Past Summits',"
content = re.sub(en_hero_tag_pattern, en_hero_cta_insert, content)

# 2. Clean up wallet states in MooreLabsLanding component
old_wallet_states = """      // 錢包狀態 (原生 Wallet MPC)
      const [walletAddress, setWalletAddress] = useState(null);
      const [isWalletModalOpen, setIsWalletModalOpen] = useState(false);
      const [walletConnecting, setWalletConnecting] = useState(false);

      const connectWallet = (type) => {
        setWalletConnecting(true);
        if (typeof window.ethereum !== 'undefined') {
          window.ethereum.request({ method: 'eth_requestAccounts' })
            .then(accs => {
              if (accs && accs[0]) setWalletAddress(accs[0]);
              setIsWalletModalOpen(false);
              setWalletConnecting(false);
            })
            .catch(() => {
              setWalletAddress('0x38b291A4F0c61D792408c7A51E5239bE88aA91');
              setIsWalletModalOpen(false);
              setWalletConnecting(false);
            });
        } else {
          setTimeout(() => {
            setWalletAddress('0x38b291A4F0c61D792408c7A51E5239bE88aA91');
            setIsWalletModalOpen(false);
            setWalletConnecting(false);
          }, 500);
        }
      };"""

new_wallet_states = """      // 官方官網展示模式（純展示門戶，不設錢包連接與應用跳轉）"""

if old_wallet_states in content:
    content = content.replace(old_wallet_states, new_wallet_states)
    print("Removed wallet states and functions!")
else:
    print("Warning: old_wallet_states not matched directly")

# 3. Replace Header
header_pattern = r"<header className=\"sticky top-0 z-50 border-b border-white/8 bg-\[#1b1c20\]/88 backdrop-blur-xl\">[\s\S]*?</header>"

new_header = """<header className="sticky top-0 z-50 border-b border-white/10 bg-[#14161d]/90 backdrop-blur-xl">
            <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 sm:py-3.5 lg:px-10">
              <a href="#" className="flex items-center gap-2.5 sm:gap-3 shrink-0 whitespace-nowrap group">
                <div className="flex h-8 w-8 sm:h-9 sm:w-9 items-center justify-center rounded-2xl border border-white/15 bg-white/5 transition group-hover:border-white/30 group-hover:bg-white/10">
                  <div className="h-3 w-3 sm:h-3.5 sm:w-3.5 rounded-full bg-gradient-to-tr from-amber-400 to-amber-200 shadow-[0_0_10px_rgba(251,191,36,0.6)]" />
                </div>
                <div className="flex flex-col text-left">
                  <div className="text-xs sm:text-sm font-semibold tracking-[0.16em] sm:tracking-[0.18em] text-white/95">MOORE LABS</div>
                  <div className="text-[9px] sm:text-[10px] uppercase tracking-[0.2em] sm:tracking-[0.24em] text-white/55">Official Portal</div>
                </div>
              </a>

              <nav className="hidden items-center gap-8 md:flex">
                {t.navLinks.map((item) => (
                  <a
                    key={item.name}
                    href={item.href}
                    className="text-sm font-medium text-white/76 transition hover:text-white"
                  >
                    {item.name}
                  </a>
                ))}
              </nav>

              <div className="flex items-center gap-3 shrink-0 whitespace-nowrap">
                {/* 雙語言切換膠囊 (繁體 / EN) */}
                <div className="flex items-center rounded-full border border-white/15 bg-white/5 p-0.5 text-xs backdrop-blur-md shadow-sm">
                  <button
                    onClick={() => toggleLang('zh')}
                    className={`rounded-full px-2.5 sm:px-3 py-1 text-[11px] sm:text-xs transition-all ${lang === 'zh' ? 'bg-amber-500/20 text-amber-300 font-semibold shadow' : 'text-white/60 hover:text-white'}`}
                  >
                    繁體
                  </button>
                  <button
                    onClick={() => toggleLang('en')}
                    className={`rounded-full px-2.5 sm:px-3 py-1 text-[11px] sm:text-xs transition-all ${lang === 'en' ? 'bg-amber-500/20 text-amber-300 font-semibold shadow' : 'text-white/60 hover:text-white'}`}
                  >
                    EN
                  </button>
                </div>
              </div>
            </div>
          </header>"""

if re.search(header_pattern, content):
    content = re.sub(header_pattern, new_header, content, count=1)
    print("Replaced Header successfully!")
else:
    print("Warning: header_pattern not matched")

# 4. Replace Hero action buttons
old_hero_buttons = """                    <div className="hero-reveal mt-10 flex flex-wrap justify-center gap-4">
                      <a
                        href="#why-moore-labs"
                        className="rounded-full border border-black/8 bg-white/40 px-8 py-3.5 text-sm font-medium text-[#1d2028] backdrop-blur-md transition hover:bg-white/55"
                      >
                        {t.launchApp}
                      </a>
                      <button
                        onClick={() => setIsWalletModalOpen(true)}
                        className="rounded-full border border-[#d6c29b]/55 bg-[#e7d5ae]/82 px-8 py-3.5 text-sm font-medium text-[#22211c] transition hover:bg-[#eadab7]"
                      >
                        {walletAddress ? t.connectedWallet : t.connectWallet}
                      </button>
                    </div>"""

new_hero_buttons = """                    <div className="hero-reveal mt-10 flex flex-wrap justify-center gap-3.5 sm:gap-4">
                      <a
                        href="#why-moore-labs"
                        className="rounded-full border border-black/10 bg-white/85 px-7 sm:px-8 py-3 sm:py-3.5 text-sm font-semibold text-[#1d2028] shadow-md backdrop-blur-md transition hover:bg-white hover:scale-105 active:scale-95"
                      >
                        {t.heroCtaPrimary}
                      </a>
                      <a
                        href="#here-it-is"
                        className="rounded-full border border-white/20 bg-white/10 px-7 sm:px-8 py-3 sm:py-3.5 text-sm font-semibold text-white backdrop-blur-md transition hover:bg-white/20 hover:scale-105 active:scale-95"
                      >
                        {t.heroCtaSecondary}
                      </a>
                    </div>"""

if old_hero_buttons in content:
    content = content.replace(old_hero_buttons, new_hero_buttons)
    print("Replaced Hero action buttons with official portal actions!")
else:
    print("Warning: old_hero_buttons not found directly")

# 5. Replace Launch App in Footer
content = content.replace(
    "['Launch App', 'MLSD', 'Docs', 'Terms', 'Privacy', 'Contact']",
    "['Overview', 'MLSD', 'Docs', 'Terms', 'Privacy', 'Contact']"
)

# 6. Remove wallet modal JSX
modal_pattern = r"\{/\* 輕量 Wallet MPC 門限安全錢包連接彈窗 \(原生純淨高質感\) \*/\}[\s\S]*?\{/\* End Wallet Modal \*/\}|\{isWalletModalOpen && \([\s\S]*?\n          \)\}"
if re.search(modal_pattern, content):
    content = re.sub(modal_pattern, "", content, count=1)
    print("Removed isWalletModalOpen modal JSX successfully!")
else:
    print("Warning: modal_pattern not matched")

# Ensure no cobo
cobo_count = len(re.findall(r"cobo", content, re.IGNORECASE))
print(f"Cobo count: {cobo_count}")
if cobo_count > 0:
    content = re.sub(r"\bCobo\b", "Wallet MPC", content)
    content = re.sub(r"\bcobo\b", "wallet mpc", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html successfully!")
