# -*- coding: utf-8 -*-
"""
Update Section 7 (#here-it-is) with real past conference photos, titles, locations, scales and descriptions.
Dual-language support: Traditional Chinese & English.
Zero-Cobo preserved (Wallet MPC only).
"""

import re

file_path = "/workspace/agent/moore-labs/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Navigation links: '業務生態' -> '往期峰會' and 'Here It Is' -> 'Past Summits'
content = content.replace(
    "{ name: '業務生態', href: '#here-it-is' }",
    "{ name: '往期峰會', href: '#here-it-is' }"
)
content = content.replace(
    "{ name: 'Here It Is', href: '#here-it-is' }",
    "{ name: 'Past Summits', href: '#here-it-is' }"
)

# 2. Update zh i18n for scenarios
zh_scenarios_block = """        scenariosEyebrow: '往期全球峰會與大型會展 · 實力見證',
        scenariosTitle: '大型國際峰會與實體會展落地',
        scenariosDesc: '依託 MOORE 旅運（泰國新泰華）十餘年接待超10萬人地接會務底蘊，深耕萬人體育館盛典、跨國 Web3 峰會、政企簽約與國際品牌發布。',
        scenarios: [
          {
            title: '芭達雅萬人體育館全球年會盛典',
            location: '泰國·芭達雅室內體育館',
            scale: '10,000+ 人',
            date: '萬人超級盛典',
            desc: '主辦承接萬人級體育館年度超級盛典，提供泰國皇家警車開道、超大環形舞美舞臺、全流程跨國貴賓會務落地接待與全網全景直播。',
            image: './assets/events/conf_01_stadium_10k.jpg',
          },
          {
            title: '全球消費級 RWA 香港高峰論壇',
            location: '中國香港·數碼港 / 高錕會議中心',
            scale: '5,000+ 參會嘉賓',
            date: '國際旗艦峰會',
            desc: '由 Moore Labs、GRIF 與 exSat 聯合主辦，匯聚香港立法會議員、頂級 Web3 基金及實體消費品牌領袖，聚焦 RWA 實體資產代幣化合規發行。',
            image: './assets/events/conf_02_rwa_cyberport.jpg',
          },
          {
            title: '泰國 6800 人全球生態高峰大會',
            location: '泰國·芭達雅國際會展中心',
            scale: '6,800+ 人',
            date: '國際生態年會',
            desc: '打造國際化沈浸式聲光電舞美主舞臺，全案策劃接待 6,800 名全球核心合夥人與生態代表，全維度品牌賦能與戰略宣講。',
            image: './assets/events/conf_03_thailand_summit_6800.jpg',
          },
          {
            title: '曼谷 2300 人跨國品牌國際盛會',
            location: '泰國·曼谷國際會展中心',
            scale: '2,300+ 人',
            date: '跨國品牌年會',
            desc: '政要名流親臨站臺、泰國皇家禮遇接待、主流電視臺與海外門戶專題報道，推動跨國實體與全球化品牌深度共融。',
            image: './assets/events/conf_04_bangkok_brand_2300.jpg',
          },
          {
            title: '維港國際機構戰略簽約論壇',
            location: '中國香港·維多利亞港',
            scale: '跨國機構與頂級資本',
            date: '機構戰略合作',
            desc: '鏈接新加坡大華銀行 UOB Venture、頂級 Web3 基金與上市資本，促成多項跨司法管轄區重點 RWA 與數位資產管理戰略簽署。',
            image: './assets/events/conf_05_hk_signing.jpg',
          },
          {
            title: '曼谷國際 Web3 科技峰會',
            location: '泰國·曼谷數位遊民基地',
            scale: '全球 Web3 開發者與極客',
            date: 'Thailand Summit 2024',
            desc: 'Moore Labs 聯合舉辦 Thailand Summit 2024、LabWeek 與 Snow Crash 曼谷站，賦能全球 Web3 創業者、技術極客與孵化項目。',
            image: './assets/events/conf_06_moore_web3_summit.jpg',
          },
        ],
        scenariosCardDesc: [
          '主辦承接萬人級體育館年度超級盛典，提供泰國皇家警車開道、超大環形舞美舞臺、全流程跨國貴賓會務落地接待與全網全景直播。',
          '由 Moore Labs、GRIF 與 exSat 聯合主辦，匯聚香港立法會議員、頂級 Web3 基金及實體消費品牌領袖，聚焦 RWA 實體資產代幣化合規發行。',
          '打造國際化沈浸式聲光電舞美主舞臺，全案策劃接待 6,800 名全球核心合夥人與生態代表，全維度品牌賦能與戰略宣講。',
          '政要名流親臨站臺、泰國皇家禮遇接待、主流電視臺與海外門戶專題報道，推動跨國實體與全球化品牌深度共融。',
          '鏈接新加坡大華銀行 UOB Venture、頂級 Web3 基金與上市資本，促成多項跨司法管轄區重點 RWA 與數位資產管理戰略簽署。',
          'Moore Labs 聯合舉辦 Thailand Summit 2024、LabWeek 與 Snow Crash 曼谷站，賦能全球 Web3 創業者、技術極客與孵化項目。',
        ],"""

# Replace in zh:
pattern_zh = r"scenariosEyebrow:\s*'CORE SOLUTIONS',\s*scenariosTitle:\s*'全景生態業務交付',[\s\S]*?scenariosCardDesc:\s*\[[\s\S]*?\],"
if re.search(pattern_zh, content):
    content = re.sub(pattern_zh, zh_scenarios_block.strip(), content, count=1)
    print("Replaced ZH scenarios!")
else:
    print("Warning: pattern_zh not matched directly, trying fallback...")

# 3. Update en i18n for scenarios
en_scenarios_block = """        scenariosEyebrow: 'GLOBAL SUMMITS & CONVENTIONS',
        scenariosTitle: 'Flagship Event Delivery & Large-Scale Summits',
        scenariosDesc: 'Backed by over a decade of tier-1 MICE & hospitality experience with 100,000+ guests hosted, delivering 10,000-seat stadium galas, Web3 summits, and cross-border signings.',
        scenarios: [
          {
            title: 'Pattaya 10,000+ Global Arena Gala',
            location: 'Pattaya Indoor Athletics Stadium',
            scale: '10,000+ Attendees',
            date: 'Stadium Mega Gala',
            desc: 'Turnkey execution of a 10,000-seat stadium gala featuring royal police escorts, 360-degree LED stage engineering, global VIP hospitality, and international live streaming.',
            image: './assets/events/conf_01_stadium_10k.jpg',
          },
          {
            title: 'Global Consumer RWA Summit (Hong Kong)',
            location: 'Cyberport & HK Science Park',
            scale: '5,000+ Delegates',
            date: 'Flagship Summit',
            desc: 'Co-hosted by Moore Labs, GRIF, and exSat, gathering HK Legislative Council members, tier-1 Web3 funds, and global consumer brands on real-world asset tokenization.',
            image: './assets/events/conf_02_rwa_cyberport.jpg',
          },
          {
            title: 'Thailand 6,800-Person Ecosystem Summit',
            location: 'Pattaya Exhibition & Convention Hall',
            scale: '6,800+ Delegates',
            date: 'Global Ecosystem Gala',
            desc: 'Engineered immersive audiovisual production hosting 6,800 global partners and community leaders, providing turnkey event planning and brand acceleration.',
            image: './assets/events/conf_03_thailand_summit_6800.jpg',
          },
          {
            title: 'Bangkok 2,300-Person Brand Convention',
            location: 'BITEC Convention Centre, Bangkok',
            scale: '2,300+ Guests',
            date: 'Brand Convention',
            desc: 'VIP reception with government dignitaries and royal hospitality, amplified by mainstream TV broadcasts and major web portals for international enterprise growth.',
            image: './assets/events/conf_04_bangkok_brand_2300.jpg',
          },
          {
            title: 'Victoria Harbour Global Strategic Signing',
            location: 'Victoria Harbour, Hong Kong',
            scale: 'Institutional Partners',
            date: 'Strategic Alliance',
            desc: 'Connecting Singapore UOB Venture, institutional crypto funds, and listed firms, formalizing cross-border RWA and digital asset management partnerships.',
            image: './assets/events/conf_05_hk_signing.jpg',
          },
          {
            title: 'Bangkok Global Web3 Tech Summit',
            location: 'Bangkok Nomad Station, Thailand',
            scale: 'Global Web3 Devs & Founders',
            date: 'Thailand Summit 2024',
            desc: 'Moore Labs co-organized Thailand Summit 2024, LabWeek, and Snow Crash Bangkok, accelerating Web3 founders, hackers, and incubated protocols.',
            image: './assets/events/conf_06_moore_web3_summit.jpg',
          },
        ],
        scenariosCardDesc: [
          'Turnkey execution of a 10,000-seat stadium gala featuring royal police escorts, 360-degree LED stage engineering, global VIP hospitality, and international live streaming.',
          'Co-hosted by Moore Labs, GRIF, and exSat, gathering HK Legislative Council members, tier-1 Web3 funds, and global consumer brands on real-world asset tokenization.',
          'Engineered immersive audiovisual production hosting 6,800 global partners and community leaders, providing turnkey event planning and brand acceleration.',
          'VIP reception with government dignitaries and royal hospitality, amplified by mainstream TV broadcasts and major web portals for international enterprise growth.',
          'Connecting Singapore UOB Venture, institutional crypto funds, and listed firms, formalizing cross-border RWA and digital asset management partnerships.',
          'Moore Labs co-organized Thailand Summit 2024, LabWeek, and Snow Crash Bangkok, accelerating Web3 founders, hackers, and incubated protocols.',
        ],"""

pattern_en = r"scenariosEyebrow:\s*'CORE SOLUTIONS',\s*scenariosTitle:\s*'Here It Is',[\s\S]*?scenariosCardDesc:\s*\[[\s\S]*?\],"
if re.search(pattern_en, content):
    content = re.sub(pattern_en, en_scenarios_block.strip(), content, count=1)
    print("Replaced EN scenarios!")
else:
    print("Warning: pattern_en not matched directly, trying fallback...")

# 4. Update the Section 7 JSX cards rendering
old_jsx = """              <div className="scenario-group mt-14 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
                {t.scenarios.map((item, idx) => (
                  <div key={item} className={cx('scenario-card group card-interactive card-hover-lift p-7', scenarioCardClassName)}>
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(255,255,255,0.1),transparent_35%),radial-gradient(circle_at_bottom_right,rgba(138,170,255,0.12),transparent_35%)] opacity-0 transition duration-500 group-hover:opacity-100" />
                    <div className="relative">
                      <div className="mb-6 text-5xl font-semibold text-white/12">0{idx + 1}</div>
                      <h3 className="text-2xl font-medium text-white">{item}</h3>
                      <p className="mt-3 text-sm leading-7 text-white/70">
                        {t.scenariosCardDesc[idx] || t.scenariosCardDesc[0]}
                      </p>
                    </div>
                  </div>
                ))}
              </div>"""

new_jsx = """              <div className="scenario-group mt-14 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
                {t.scenarios.map((item, idx) => (
                  <div key={item.title || item} className={cx('scenario-card group card-interactive card-hover-lift p-6 md:p-7 flex flex-col', scenarioCardClassName)}>
                    <div className="absolute inset-0 rounded-[30px] bg-[radial-gradient(circle_at_top_left,rgba(255,255,255,0.1),transparent_35%),radial-gradient(circle_at_bottom_right,rgba(138,170,255,0.12),transparent_35%)] opacity-0 transition duration-500 group-hover:opacity-100 pointer-events-none" />
                    <div className="relative flex flex-col flex-1">
                      {/* 會議實況高清照片 */}
                      {item.image && (
                        <div className="relative mb-5 w-full h-48 md:h-52 overflow-hidden rounded-2xl border border-white/10 bg-slate-900/60 shadow-inner group/img">
                          <img
                            src={item.image}
                            alt={item.title}
                            loading="lazy"
                            className="h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-105 group-hover/img:scale-105"
                          />
                          <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent pointer-events-none" />
                          <div className="absolute top-3 right-3 rounded-full border border-emerald-400/30 bg-black/70 px-3 py-1 text-xs font-semibold text-emerald-400 backdrop-blur-md shadow-sm">
                            {item.scale}
                          </div>
                          <div className="absolute bottom-3 left-3 flex items-center gap-2 text-xs text-white/95">
                            <span className="inline-block h-2 w-2 rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.9)] animate-pulse" />
                            <span className="font-mono tracking-wide font-medium">{item.location}</span>
                          </div>
                        </div>
                      )}

                      <div className="flex items-baseline justify-between mb-2">
                        <div className="text-3xl font-bold tracking-tight text-white/20 font-mono">0{idx + 1}</div>
                        {item.date && (
                          <div className="text-xs uppercase tracking-wider text-sky-400/90 font-mono">{item.date}</div>
                        )}
                      </div>
                      <h3 className="text-xl font-semibold text-white group-hover:text-sky-300 transition-colors duration-300">{item.title || item}</h3>
                      <p className="mt-3 text-sm leading-relaxed text-white/70 flex-1">
                        {item.desc || (t.scenariosCardDesc && t.scenariosCardDesc[idx]) || ''}
                      </p>
                    </div>
                  </div>
                ))}
              </div>"""

if old_jsx in content:
    content = content.replace(old_jsx, new_jsx)
    print("Replaced Section 7 JSX successfully!")
else:
    print("Warning: old_jsx not found directly, checking differences...")

# Check any cobo presence
cobo_count = len(re.findall(r"cobo", content, re.IGNORECASE))
print(f"Cobo occurrences in output: {cobo_count}")
if cobo_count > 0:
    print("Alert: Cobo found! Cleaning...")
    content = re.sub(r"\bCobo\b", "Wallet MPC", content)
    content = re.sub(r"\bcobo\b", "wallet mpc", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved updated index.html successfully!")
