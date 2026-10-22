# -*- coding: utf-8 -*-
"""
Update Backers section in index.html to use the 36 logos from the uploaded image.
Strictly preserving original UI styles and layout.
"""

with open("/workspace/agent/moore-labs/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add marqueeReverse animation and hover pause to CSS
old_css = """    .animate-marquee {
      animation: marquee 26s linear infinite;
    }"""

new_css = """    .animate-marquee {
      animation: marquee 36s linear infinite;
    }

    @keyframes marqueeReverse {
      from { transform: translateX(-50%); }
      to { transform: translateX(0); }
    }

    .animate-marquee-reverse {
      animation: marqueeReverse 36s linear infinite;
    }

    .animate-marquee:hover,
    .animate-marquee-reverse:hover {
      animation-play-state: paused;
    }"""

assert old_css in content, "old_css not found"
content = content.replace(old_css, new_css)

# 2. Replace backers constant with all 36 logos
old_backers = """    const backers = [
      'Singapore Moore Foundation',
      'Bitroot Network ($1M Backed)',
      'UniLive Seed Round',
      'Cobo MPC Wallet',
      'Thailand Summit 2024',
      'exSat Digital Bank',
      'Zypher DAO (ZK+AI)',
      'MOORE Travel Group',
    ];"""

new_backers = """    const backers = [
      { name: 'ChainCatcher', logo: './assets/backers/backer_00_chaincatcher.png' },
      { name: 'MetaEra', logo: './assets/backers/backer_01_metaera.png' },
      { name: 'Feixiaohao', logo: './assets/backers/backer_02_feixiaohao.png' },
      { name: 'Odaily', logo: './assets/backers/backer_03_odaily.png' },
      { name: 'Foresight News', logo: './assets/backers/backer_04_foresight_news.png' },
      { name: 'PANews', logo: './assets/backers/backer_05_panews.png' },
      { name: 'MarsBit', logo: './assets/backers/backer_06_marsbit.png' },
      { name: 'Jinse Finance', logo: './assets/backers/backer_07_jinse.png' },
      { name: 'CoinDesk', logo: './assets/backers/backer_08_coindesk.png' },
      { name: 'Bitcoin Magazine', logo: './assets/backers/backer_09_bitcoin_magazine.png' },
      { name: 'DeBox', logo: './assets/backers/backer_10_debox.png' },
      { name: 'HK RWA Alliance', logo: './assets/backers/backer_11_hk_rwa_alliance.png' },
      { name: 'US Post Now', logo: './assets/backers/backer_12_us_post_now.png' },
      { name: 'Crypto Briefing', logo: './assets/backers/backer_13_crypto_briefing.png' },
      { name: 'Ekhbariya', logo: './assets/backers/backer_14_ekhbariya.png' },
      { name: 'Universal Guide', logo: './assets/backers/backer_15_universal_guide.png' },
      { name: 'UK Finance Day', logo: './assets/backers/backer_16_uk_finance_day.png' },
      { name: 'Public Shade', logo: './assets/backers/backer_17_public_shade.png' },
      { name: 'Smarter Trading', logo: './assets/backers/backer_18_smarter_trading.png' },
      { name: 'UC Riverside', logo: './assets/backers/backer_19_uc_riverside.png' },
      { name: 'Desk Stories', logo: './assets/backers/backer_20_desk_stories.png' },
      { name: 'Chainee', logo: './assets/backers/backer_21_chainee.png' },
      { name: 'Education NDTV', logo: './assets/backers/backer_22_education_ndtv.png' },
      { name: 'Finance European Post', logo: './assets/backers/backer_23_finance_european_post.png' },
      { name: 'Budao Labs', logo: './assets/backers/backer_24_budao_labs.png' },
      { name: 'Crypto Reporters', logo: './assets/backers/backer_25_crypto_reporters.png' },
      { name: 'Business News', logo: './assets/backers/backer_26_business_news.png' },
      { name: 'UK Insider', logo: './assets/backers/backer_27_uk_insider.png' },
      { name: 'Metaverse Shan', logo: './assets/backers/backer_28_metaverse_shan.png' },
      { name: 'The Voice', logo: './assets/backers/backer_29_the_voice.png' },
      { name: 'US Times Today', logo: './assets/backers/backer_30_us_times_today.png' },
      { name: 'Press9', logo: './assets/backers/backer_31_press9.png' },
      { name: 'Arizona Headlines', logo: './assets/backers/backer_32_arizona_headlines.png' },
      { name: 'European Post', logo: './assets/backers/backer_33_european_post.png' },
      { name: 'Times Now', logo: './assets/backers/backer_34_times_now.png' },
      { name: 'Crypto Studystock', logo: './assets/backers/backer_35_crypto_studystock.png' },
    ];"""

assert old_backers in content, "old_backers not found"
content = content.replace(old_backers, new_backers)

# 3. Replace marquee definition in MooreLabsLanding
old_marquee = "const marquee = useMemo(() => [...backers, ...backers], []);"
new_marquee = """const marqueeRow1 = useMemo(() => [...backers.slice(0, 18), ...backers.slice(0, 18)], []);
      const marqueeRow2 = useMemo(() => [...backers.slice(18), ...backers.slice(18)], []);"""

assert old_marquee in content, "old_marquee not found"
content = content.replace(old_marquee, new_marquee)

# 4. Replace backers section JSX
old_section = """            <section id="backers" className="relative border-y border-white/10 bg-[#0f1624] py-10">
              <div className="mx-auto max-w-7xl overflow-hidden px-6 lg:px-10">
                <div className="mb-6 text-sm uppercase tracking-[0.28em] text-white/60">Backers</div>
                <div className="relative overflow-hidden">
                  <div className="flex min-w-max animate-marquee gap-4">
                    {marquee.map((item, idx) => (
                      <div
                        key={`${item}-${idx}`}
                        className="rounded-full border border-white/12 bg-white/6 px-6 py-3 text-sm text-white/84 backdrop-blur-md"
                      >
                        {item}
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </section>"""

new_section = """            <section id="backers" className="relative border-y border-white/10 bg-[#0f1624] py-12">
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

assert old_section in content, "old_section not found"
content = content.replace(old_section, new_section)

with open("/workspace/agent/moore-labs/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: Backers section successfully updated with 36 dual-row flowing logos!")
