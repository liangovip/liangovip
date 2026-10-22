# -*- coding: utf-8 -*-
"""
Full Bilingual (Traditional Chinese & English) Upgrade & Complete Cobo Removal.
100% preservation of all original CSS, GSAP animations, layout geometry and light halos.
"""

import re

with open("/workspace/agent/moore-labs/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Define complete bilingual dictionary
i18n_block = """
    const i18n = {
      zh: {
        siteTitle: 'MOORE LABS - 全球 Web3 深度孵化與流動性網絡',
        navLinks: [
          { name: '為何選擇', href: '#why-moore-labs' },
          { name: '最新動態', href: '#what-s-new' },
          { name: '業務生態', href: '#here-it-is' },
          { name: '合作陣容', href: '#backers' },
        ],
        connectWallet: '連接 Wallet MPC',
        connectedWallet: 'MPC 已連接',
        disconnect: '點擊斷開',
        launchApp: '進入應用',
        heroTag: 'MOORE LABS 摩爾資本',
        heroTitle: '全球 Web3 深度孵化網絡',
        heroSub: '新加坡 ACRA 官方牌照 (UEN: 202335893Z) · 5000萬美元生態基金 · Wallet MPC 門限安全',
        backersTitle: '戰略投資與全球媒體矩陣',
        backersSub: '36+ 家頂級加密媒體與行業盟友（全透明純白矩陣）',
        whyTitle: '為何選擇 MOORE LABS？',
        whyDesc: '由新加坡 Moore 基金會發起（ACRA UEN: 202335893Z），設立 5000 萬美元生態孵化基金，提供 Wallet MPC 機構級資產協管、全球 7 大實體遊民站與萬人國際峰會落地交付。',
        pillars: [
          {
            title: '5000萬美元生態孵化基金',
            desc: '由新加坡 Moore 基金會（UEN: 202335893Z）發起，重點佈局 Web3 種子輪、天使輪及 A 輪，每年深度賦能超過 50 個優質項目。',
          },
          {
            title: 'Wallet MPC 機構級資產協管',
            desc: '整合 Wallet MPC 門限密鑰分片與多簽金庫架構，提供企業級私鑰安全防護、多重簽名金庫治理及深厚鏈上流動性支持。',
          },
          {
            title: '全球 7 大實體數位遊民基地',
            desc: '在曼谷、新加坡、香港、東京、首爾、吉隆坡及胡志明市設立常設實體據點，打造全球一體化的 Web3 實體協同網絡。',
          },
          {
            title: 'MOORE 旅運與萬人峰會交付',
            desc: '頂級大型峰會統籌執行能力，曾承辦芭達雅萬人體育館盛典，提供泰國皇家警察護送、直升機接送及全泰 100+ 商戶代幣 POS 刷卡消費落地。',
          },
          {
            title: 'PWA Web3 全自動化增長引擎',
            desc: '提供從社群精準打粉、全網公關新聞通稿分發，到 Telegram/WhatsApp 7x24小時智能機器人、音視頻製作與鏈上數據分析全套服務。',
          },
        ],
        hiTitle: '你好，我們是 MOORE LABS',
        capabilities: [
          'Wallet MPC 門限安全',
          '社群精準打粉獲客',
          '5000萬美元生態基金',
          '全球 7 大實體基地',
          'TG / WA 智能機器人',
        ],
        capabilitiesCardDesc: [
          '以 Wallet MPC 門限密鑰分片技術守護項目核心資產，結合 5000 萬美元資本注入與全球實體落地資源。',
          '依託自研 PWA 增長引擎實現精準用戶畫像獲客、全球加密媒體通稿矩陣與 7x24小時 TG/WA 智能社區助手。',
          '具備新加坡 ACRA 合法官方註冊牌照（UEN: 202335893Z），遵循跨國合規準則，提供全週期孵化資金扶持。',
          '打通泰國全境 100+ 商戶多鏈代幣 POS 刷卡消費場景，具備萬人國際體育館大會與政商高端禮遇統籌實力。',
          '提供企業級全鏈路基礎設施，嚴密對齊跨國金融監管、合規託管與大規模業務連續性。',
        ],
        scenariosEyebrow: 'CORE SOLUTIONS',
        scenariosTitle: '全景生態業務交付',
        scenariosDesc: '覆蓋項目孵化、多簽資產金庫、社群工業化運營與跨國實體消費落地全鏈路。',
        scenarios: [
          'Web3 創投與天使孵化（5000萬美元基金）',
          'Wallet MPC 機構級資產協管與多簽金庫',
          'PWA Web3 全自動化增長引擎（打粉/新聞/機器人）',
          'MOORE 旅運與萬人體育館國際盛會',
          '新加坡官方 ACRA 牌照（UEN: 202335893Z）',
        ],
        scenariosCardDesc: [
          '設立 5000 萬美元生態孵化基金，重點投資 Web3 天使輪及 A 輪，每年深度孵化超 50 個優質創新項目，提供資金、技術、品牌與市場全方位賦能。',
          '深度整合 Wallet MPC 門限簽名安全與多簽金庫架構，實現項目方資金物理隔離、鏈上高頻結算與多鏈大額資產合規協管。',
          '提供從社群精準打粉、全網新聞通稿分发，到 Telegram/WhatsApp 7x24小時智能客服機器人與 16秒短視頻/5分鐘深度解說的工業化自動化執行。',
          'MOORE 旅運擁有獨棟 4000 平方公尺大樓，成功承辦芭達雅 10,000 人體育館超級盛典，並推動全泰 100+ 商戶（7-11/Central World）支持 Token POS 刷卡消費。',
          '新加坡會計與企業管理局（ACRA UEN: 202335893Z）合法登記，已在曼谷、香港、新加坡、東京、首爾、吉隆坡、胡志明設立常設實體協作據點。',
        ],
        trendsEyebrow: 'MARKET TRENDS',
        trendsTitle: '未來趨勢洞察',
        trendsDesc: '緊扣全球 Web3 合規化、機構級安全與真實世界賦能發展脈搏。',
        trends: [
          'Wallet MPC 機構級私鑰門限保護',
          '自研 PWA 自動化運營矩陣',
          '全泰 100+ 實體商戶代幣 POS 落地',
          '跨國官方合規牌照與實體網絡',
        ],
        trendsCardDesc: [
          'Wallet MPC 門限簽名與機構級多簽金庫守護鏈上核心資產。',
          '自研 PWA 自動化內核驅動社群打粉與全網新聞通稿矩陣。',
          '全泰 100+ 實體商戶代幣 POS 刷卡直接消費落地生態。',
          '新加坡政府 ACRA 官方核發牌照與跨國合規經營（UEN: 202335893Z）。',
        ],
        roadmapEyebrow: 'ROADMAP',
        roadmapTitle: '發展路線圖',
        roadmapDesc: '從新加坡基金會啟航，構築橫跨全球的實體與鏈上流動性帝國。',
        roadmap: [
          { time: '2023 Q3', title: '基金會創立 (新加坡)', points: ['獲得新加坡 ACRA 合規牌照 (UEN: 202335893Z)', '跨越5國常設辦公室設立', '核心創投與孵化團隊組建'] },
          { time: '2024 Q1-Q2', title: '資本啟動與基建佈局', points: ['初始基金募集 (超 1000 萬 USDT)', 'Mison AI 智能合約安全防護', 'Wallet MPC 機構級金庫協管接入'] },
          { time: '2024 Q4', title: '泰國萬人峰會與實體消費落地', points: ['泰國萬人峰會與 RWA 大會聯合承辦', '全泰 100+ 商戶 Token POS 刷卡結算', '全球 7 大實體數位遊民基地全面啟用'] },
          { time: '2025 Q1-Q2', title: '5000萬美元生態全面擴張', points: ['年度深度孵化 50+ 優質項目', 'PWA Web3 全自動化增長引擎上線', '數字資產財富管理合規門戶啟動'] },
          { time: '2025-2026', title: '持續拓展…', points: ['推動生態基金擴容至 1億 - 10億 美元 AUM', '打造全球化真實世界資產（RWA）合規樞紐'] },
        ],
        ctaTag: 'MOORE LABS',
        ctaTitle: '為下一代 Web3 全球創新而生',
        ctaDesc: '由新加坡 Moore 基金會全面賦能，整合 5000 萬美元創投資金、Wallet MPC 門限安全金庫與全球實體落地樞紐。',
        ctaLinks: ['探索核心架構', '查閱官方白皮書', '啟動應用'],
        footerText: '新加坡 MOORE FOUNDATION LTD. 官方平台（ACRA UEN: 202335893Z）。整合 5000 萬美元生態基金、Wallet MPC 門限安全金庫與 MOORE 旅運集團。',
        modalTitle: '連接 Web3 錢包',
        modalConnecting: '正在連接 Wallet MPC...',
        modalMpcTitle: 'Wallet MPC (門限安全錢包)',
        modalMpcBadge: '首選推薦',
        modalMpcSub: '機構級門限密鑰分片技術',
        modalMetaMask: 'MetaMask 錢包',
        modalOkx: 'OKX 歐易錢包',
        modalFoot: '受去中心化門限多簽（MPC）演算法保護',
      },
      en: {
        siteTitle: 'MOORE LABS - Global Web3 Incubation & Liquidity Layer',
        navLinks: [
          { name: 'Why MOORE LABS', href: '#why-moore-labs' },
          { name: "What's New", href: '#what-s-new' },
          { name: 'Here It Is', href: '#here-it-is' },
          { name: 'Backers', href: '#backers' },
        ],
        connectWallet: 'Connect Wallet MPC',
        connectedWallet: 'MPC Connected',
        disconnect: 'Click to Disconnect',
        launchApp: 'Launch App',
        heroTag: 'MOORE LABS',
        heroTitle: 'Global Web3 Incubation Layer',
        heroSub: 'Singapore ACRA (UEN: 202335893Z) · $50M Ecosystem Fund · Wallet MPC Security',
        backersTitle: 'Backers & Global Media Partners',
        backersSub: '36+ Strategic Media & Tier-1 Crypto Allies (Color-Unified & Transparent)',
        whyTitle: 'Why MOORE LABS?',
        whyDesc: 'Initiated by Singapore Moore Foundation (ACRA UEN: 202335893Z), deploying a $50M ecosystem incubation fund, Wallet MPC institutional custody, 7 global physical nomad hubs, and 10,000+ attendee summit execution.',
        pillars: [
          {
            title: '$50M Ecosystem Incubation Fund',
            desc: 'Initiated by Singapore Moore Foundation (UEN: 202335893Z), deploying capital into Web3 seed, Angel, and Series A rounds with 50+ quality projects incubated annually.',
          },
          {
            title: 'Wallet MPC Institutional Custody',
            desc: 'Integrated with Wallet MPC threshold security, delivering enterprise-grade asset protection, multi-sig treasury governance and deep on-chain liquidity.',
          },
          {
            title: 'Global 7-City Digital Nomad Stations',
            desc: 'Permanent physical hubs across Bangkok, Singapore, Hong Kong, Tokyo, Seoul, Kuala Lumpur and HCMC, forming a worldwide Web3 collaboration and landing network.',
          },
          {
            title: 'MOORE Travel & High-End Events',
            desc: 'Premier event execution with 10,000+ attendee stadium summits, royal police escort, VIP helicopter arrival and 100+ Thailand merchants accepting token POS payments.',
          },
          {
            title: 'PWA Web3 Growth & Automation',
            desc: 'End-to-end operational engine providing targeted user acquisition (traffic inflow), news syndication, TG/WA AI bots, multimedia studio and on-chain analytics.',
          },
        ],
        hiTitle: 'Hi~ This is MOORE LABS',
        capabilities: [
          'Wallet MPC',
          'Targeted Traffic',
          '$50M Eco Fund',
          'Global 7 Nomad Hubs',
          'TG / WA AI Bots',
        ],
        capabilitiesCardDesc: [
          'Empowering Web3 teams with Wallet MPC institutional threshold security, $50M capital injection, and global physical landing.',
          'Leverage PWA automation for targeted user acquisition (traffic funnel), global news distribution, and 7x24h TG/WA AI bots.',
          'Backed by Singapore ACRA registration (UEN: 202335893Z) and rigorous compliance standards across 5 countries.',
          'Connecting physical merchants across Thailand with multi-chain token POS payments and 10,000+ attendee summits.',
          'Enterprise-grade infrastructure aligned for scale, compliance and operational reliability.',
        ],
        scenariosEyebrow: 'CORE SOLUTIONS',
        scenariosTitle: 'Here It Is',
        scenariosDesc: 'Comprehensive Web3 venture, custody, and real-world execution solutions.',
        scenarios: [
          'Web3 Venture & Angel Incubation ($50M Fund)',
          'Wallet MPC Institutional Custody & Asset Vault',
          'PWA Web3 Growth & Automation Engine (Traffic/News/Bots)',
          'MOORE Travel & 10,000-Attendee Summits',
          'Singapore ACRA Official License (UEN: 202335893Z)',
        ],
        scenariosCardDesc: [
          'Deploying a $50M incubation fund focused on Web3 Seed and Series A stages, incubating 50+ tier-1 projects annually with comprehensive capital, technical, and market acceleration.',
          'Deep integration with Wallet MPC threshold signature technology and multi-sig vault architecture, providing project fund isolation, high-frequency settlement, and compliant multi-chain asset custody.',
          'End-to-end industrial execution covering community traffic acquisition, global PR news syndication, 7x24h Telegram/WhatsApp AI bots, 16s viral reels, and 5-min executive explainers.',
          'Operating a 4,000 sqm standalone building, successful host of the 10,000-attendee Pattaya stadium summit, and enabling 100+ merchants in Thailand (7-11/Central World) with token POS payments.',
          'Officially registered with Singapore ACRA (UEN: 202335893Z), with physical hubs active in Bangkok, Hong Kong, Singapore, Tokyo, Seoul, Kuala Lumpur, and Ho Chi Minh City.',
        ],
        trendsEyebrow: 'MARKET TRENDS',
        trendsTitle: 'Key Trends Shaping The Next Cycle',
        trendsDesc: 'Key industry paradigms powering our growth.',
        trends: [
          'Institutional MPC Security',
          'PWA Automated Operations',
          'Real-World Token Utilities',
          'Global Compliance & Licensing',
        ],
        trendsCardDesc: [
          'Wallet MPC threshold signature & enterprise multi-sig vaults protecting on-chain assets.',
          'Proprietary PWA automation engine driving community growth and global media syndication.',
          '100+ physical merchants in Thailand enabling seamless multi-chain token POS payments.',
          'Official Singapore government ACRA registration & cross-border compliance (UEN: 202335893Z).',
        ],
        roadmapEyebrow: 'ROADMAP',
        roadmapTitle: 'Roadmap',
        roadmapDesc: 'From genesis in Singapore to a worldwide institutional and real-world asset ecosystem.',
        roadmap: [
          { time: '2023 Q3', title: 'Foundation Genesis (Singapore)', points: ['Singapore ACRA License (UEN: 202335893Z)', '5-Country Office Setup', 'Venture Team Formation'] },
          { time: '2024 Q1-Q2', title: 'Capital & Infrastructure', points: ['Initial Fund Raising (USDT 10M+)', 'Mison AI Smart Contract Shield', 'Wallet MPC Institutional Custody Integration'] },
          { time: '2024 Q4', title: 'Thailand Summit & Real-World Utility', points: ['Thailand Summit & RWA Conference Co-Host', '100+ POS Merchants Token Settlement', 'Global 7 Digital Nomad Hubs Active'] },
          { time: '2025 Q1-Q2', title: '$50M Ecosystem Expansion', points: ['Annual 50+ Projects Incubation', 'PWA Web3 Growth Engine Launch', 'Digital Asset Wealth Management Portal'] },
          { time: '2025-2026', title: 'To be continued…', points: ['Scale Fund to $100M - $1B AUM', 'Global Compliant Real-World Asset Layer'] },
        ],
        ctaTag: 'MOORE LABS',
        ctaTitle: 'Built for the next generation of Web3 innovation.',
        ctaDesc: 'A comprehensive venture & liquidity ecosystem backed by Singapore Moore Foundation, deploying $50M capital, Wallet MPC custody, and global physical landing.',
        ctaLinks: ['Explore infrastructure', 'Read the docs', 'Launch app'],
        footerText: 'Official Web3 platform by MOORE FOUNDATION LTD. (Singapore ACRA UEN: 202335893Z). Integrating $50M Ecosystem Fund, Wallet MPC Custody, and MOORE Travel Group.',
        modalTitle: 'Connect Web3 Wallet',
        modalConnecting: 'Connecting to Wallet MPC...',
        modalMpcTitle: 'Wallet MPC (Threshold Signature)',
        modalMpcBadge: 'Recommended',
        modalMpcSub: 'Institutional Multi-Sig Threshold Security',
        modalMetaMask: 'MetaMask',
        modalOkx: 'OKX Wallet',
        modalFoot: 'Protected by Decentralized Threshold Signature (MPC)',
      }
    };
"""

# Insert i18n_block right before MooreLabsLanding
landing_def_match = re.search(r"    function MooreLabsLanding\(\) \{", content)
assert landing_def_match is not None, "MooreLabsLanding not found"
content = content[:landing_def_match.start()] + i18n_block + "\n" + content[landing_def_match.start():]

# Add state to MooreLabsLanding
old_landing_start = """    function MooreLabsLanding() {
      const rootRef = useRef(null);
      const heroRef = useRef(null);
      const marqueeRow1 = useMemo(() => [...backers.slice(0, 18), ...backers.slice(0, 18)], []);
      const marqueeRow2 = useMemo(() => [...backers.slice(18), ...backers.slice(18)], []);

      // 仅用于弹窗与地址展示，完全不改变任何基础UI布局
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
              setWalletAddress('0x3C0b0891A4F0c61D792408c7A51E5239bE88aA91');
              setIsWalletModalOpen(false);
              setWalletConnecting(false);
            });
        } else {
          setTimeout(() => {
            setWalletAddress('0x3C0b0891A4F0c61D792408c7A51E5239bE88aA91');
            setIsWalletModalOpen(false);
            setWalletConnecting(false);
          }, 500);
        }
      };"""

new_landing_start = """    function MooreLabsLanding() {
      const rootRef = useRef(null);
      const heroRef = useRef(null);
      const marqueeRow1 = useMemo(() => [...backers.slice(0, 18), ...backers.slice(0, 18)], []);
      const marqueeRow2 = useMemo(() => [...backers.slice(18), ...backers.slice(18)], []);

      // 雙語言狀態 (預設繁體中文，支援一鍵切換英文)
      const [lang, setLang] = useState(() => {
        try {
          return localStorage.getItem('moore_lang') || 'zh';
        } catch (e) {
          return 'zh';
        }
      });
      const t = i18n[lang] || i18n.zh;

      useEffect(() => {
        document.title = t.siteTitle;
      }, [lang]);

      const toggleLang = (target) => {
        setLang(target);
        try {
          localStorage.setItem('moore_lang', target);
        } catch (e) {}
      };

      // 錢包狀態 (原生 Wallet MPC)
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

assert old_landing_start in content, "old_landing_start not found"
content = content.replace(old_landing_start, new_landing_start)

# Update Navbar
old_nav_block = """              <nav className="hidden items-center gap-8 md:flex">
                {["Why MOORE LABS", "What's New", "Here It Is", "Backers"].map((item) => (
                  <a
                    key={item}
                    href={`#${item.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`}
                    className="text-sm text-white/76 transition hover:text-white"
                  >
                    {item}
                  </a>
                ))}
              </nav>

              <div className="flex items-center gap-3">
                {walletAddress ? (
                  <button
                    onClick={() => setWalletAddress(null)}
                    className="rounded-full border border-amber-500/40 bg-amber-500/10 px-4 py-2 text-sm font-medium text-amber-300 transition hover:bg-amber-500/20"
                    title="点击断开"
                  >
                    {walletAddress.substring(0, 6)}...{walletAddress.substring(walletAddress.length - 4)} (Cobo)
                  </button>
                ) : (
                  <button
                    onClick={() => setIsWalletModalOpen(true)}
                    className="rounded-full border border-white/15 px-4 py-2 text-sm text-white/80 transition hover:bg-white/8"
                  >
                    Connect Cobo Wallet
                  </button>
                )}
                <a className="rounded-full bg-white px-4 py-2 text-sm font-medium text-black transition hover:opacity-90" href="#why-moore-labs">
                  Launch App
                </a>
              </div>"""

new_nav_block = """              <nav className="hidden items-center gap-8 md:flex">
                {t.navLinks.map((item) => (
                  <a
                    key={item.name}
                    href={item.href}
                    className="text-sm text-white/76 transition hover:text-white"
                  >
                    {item.name}
                  </a>
                ))}
              </nav>

              <div className="flex items-center gap-3">
                {/* 雙語言切換膠囊 (繁體 / EN) */}
                <div className="flex items-center rounded-full border border-white/15 bg-white/5 p-0.5 text-xs backdrop-blur-md">
                  <button
                    onClick={() => toggleLang('zh')}
                    className={`rounded-full px-2.5 py-1 transition-all ${lang === 'zh' ? 'bg-amber-500/20 text-amber-300 font-semibold shadow' : 'text-white/60 hover:text-white'}`}
                  >
                    繁體
                  </button>
                  <button
                    onClick={() => toggleLang('en')}
                    className={`rounded-full px-2.5 py-1 transition-all ${lang === 'en' ? 'bg-amber-500/20 text-amber-300 font-semibold shadow' : 'text-white/60 hover:text-white'}`}
                  >
                    EN
                  </button>
                </div>

                {walletAddress ? (
                  <button
                    onClick={() => setWalletAddress(null)}
                    className="rounded-full border border-amber-500/40 bg-amber-500/10 px-4 py-2 text-sm font-medium text-amber-300 transition hover:bg-amber-500/20"
                    title={t.disconnect}
                  >
                    {walletAddress.substring(0, 6)}...{walletAddress.substring(walletAddress.length - 4)} (MPC)
                  </button>
                ) : (
                  <button
                    onClick={() => setIsWalletModalOpen(true)}
                    className="rounded-full border border-white/15 px-4 py-2 text-sm text-white/80 transition hover:bg-white/8"
                  >
                    {t.connectWallet}
                  </button>
                )}
                <a className="rounded-full bg-white px-4 py-2 text-sm font-medium text-black transition hover:opacity-90" href="#why-moore-labs">
                  {t.launchApp}
                </a>
              </div>"""

assert old_nav_block in content, "old_nav_block not found"
content = content.replace(old_nav_block, new_nav_block)

# Update Hero Section
old_hero_block = """                    <h1 className="hero-reveal max-w-4xl mx-auto text-5xl font-semibold leading-[0.98] tracking-tight text-[#17181d] drop-shadow-[0_1px_0_rgba(255,255,255,0.18)] md:text-7xl xl:text-[92px]">
                      Global Web3 Incubation Layer
                    </h1>
                    <p className="hero-reveal mt-8 text-lg leading-8 text-[#2f3442]/80 md:text-xl">
                      Singapore ACRA (UEN: 202335893Z) · $50M Ecosystem Fund · Cobo MPC Security
                    </p>

                    <div className="hero-reveal mt-10 flex justify-center">
                      <svg width="56" height="32" viewBox="0 0 56 32" fill="none" xmlns="http://www.w3.org/2000/svg" className="text-[#2f3442]/70">
                        <path d="M20 4C11.16 4 4 11.16 4 20s7.16 16 16 16c5.3 0 9.96-2.58 12.88-6.54" stroke="currentColor" strokeWidth="3.2" strokeLinecap="round" fill="none"/>
                        <path d="M36 28c8.84 0 16-7.16 16-16S44.84-4 36-4c-5.3 0-9.96 2.58-12.88 6.54" stroke="currentColor" strokeWidth="3.2" strokeLinecap="round" fill="none"/>
                      </svg>
                    </div>

                    <div className="hero-reveal mt-10 flex flex-wrap justify-center gap-4">
                      <a
                        href="#why-moore-labs"
                        className="rounded-full border border-black/8 bg-white/40 px-8 py-3.5 text-sm font-medium text-[#1d2028] backdrop-blur-md transition hover:bg-white/55"
                      >
                        Launch App
                      </a>
                      <button
                        onClick={() => setIsWalletModalOpen(true)}
                        className="rounded-full border border-[#d6c29b]/55 bg-[#e7d5ae]/82 px-8 py-3.5 text-sm font-medium text-[#22211c] transition hover:bg-[#eadab7]"
                      >
                        {walletAddress ? 'Cobo Connected' : 'Connect Cobo Wallet'}
                      </button>
                    </div>"""

new_hero_block = """                    <h1 className="hero-reveal max-w-4xl mx-auto text-5xl font-semibold leading-[0.98] tracking-tight text-[#17181d] drop-shadow-[0_1px_0_rgba(255,255,255,0.18)] md:text-7xl xl:text-[92px]">
                      {t.heroTitle}
                    </h1>
                    <p className="hero-reveal mt-8 text-lg leading-8 text-[#2f3442]/80 md:text-xl">
                      {t.heroSub}
                    </p>

                    <div className="hero-reveal mt-10 flex justify-center">
                      <svg width="56" height="32" viewBox="0 0 56 32" fill="none" xmlns="http://www.w3.org/2000/svg" className="text-[#2f3442]/70">
                        <path d="M20 4C11.16 4 4 11.16 4 20s7.16 16 16 16c5.3 0 9.96-2.58 12.88-6.54" stroke="currentColor" strokeWidth="3.2" strokeLinecap="round" fill="none"/>
                        <path d="M36 28c8.84 0 16-7.16 16-16S44.84-4 36-4c-5.3 0-9.96 2.58-12.88 6.54" stroke="currentColor" strokeWidth="3.2" strokeLinecap="round" fill="none"/>
                      </svg>
                    </div>

                    <div className="hero-reveal mt-10 flex flex-wrap justify-center gap-4">
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

assert old_hero_block in content, "old_hero_block not found"
content = content.replace(old_hero_block, new_hero_block)

# Update Backers section title
old_backers_header = """                <div className="mb-8 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                  <div className="text-sm uppercase tracking-[0.28em] text-white/60">Backers & Global Media Partners</div>
                  <div className="text-xs tracking-wider text-white/40">36+ Strategic Media & Tier-1 Crypto Allies (Color-Unified & Transparent)</div>
                </div>"""

new_backers_header = """                <div className="mb-8 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-2">
                  <div className="text-sm uppercase tracking-[0.28em] text-white/60">{t.backersTitle}</div>
                  <div className="text-xs tracking-wider text-white/40">{t.backersSub}</div>
                </div>"""

assert old_backers_header in content, "old_backers_header not found"
content = content.replace(old_backers_header, new_backers_header)

# Update Why MOORE LABS section header & pillars loop
old_why_block = """            <section id="why-moore-labs" className="relative bg-[#0a1220] py-24 lg:py-32">
              <div className="mx-auto max-w-7xl px-6 lg:px-10">
                <h2 className="text-center text-3xl font-semibold tracking-tight text-white md:text-5xl">Why MOORE LABS?</h2>
                <p className="mx-auto mt-6 max-w-3xl text-center text-sm leading-7 text-white/70 md:text-base">
                  由新加坡 Moore 基金会发起（ACRA UEN: 202335893Z），设立 5000 万美金生态孵化基金，提供 Cobo MPC 机构级资产协管、全球 7 大实体游民站与万人国际峰会落地交付。
                </p>

                <div className="pillar-container mt-14 overflow-hidden rounded-2xl">
                  {pillars.map((item, idx) => {"""

new_why_block = """            <section id="why-moore-labs" className="relative bg-[#0a1220] py-24 lg:py-32">
              <div className="mx-auto max-w-7xl px-6 lg:px-10">
                <h2 className="text-center text-3xl font-semibold tracking-tight text-white md:text-5xl">{t.whyTitle}</h2>
                <p className="mx-auto mt-6 max-w-3xl text-center text-sm leading-7 text-white/70 md:text-base">
                  {t.whyDesc}
                </p>

                <div className="pillar-container mt-14 overflow-hidden rounded-2xl">
                  {t.pillars.map((item, idx) => {"""

assert old_why_block in content, "old_why_block not found"
content = content.replace(old_why_block, new_why_block)

# Update "Hi~ This is MOORE LABS" in Section 6
content = content.replace("Hi~ This is MOORE LABS", "{t.hiTitle}")

# Update Section 6 cards: title and descriptions for mobile and desktop
content = content.replace(
    "{capabilities.slice(0, 5).map((item, idx) => (",
    "{t.capabilities.slice(0, 5).map((item, idx) => ("
)
content = content.replace(
    "{capabilities.slice(0, 5).map((item, idx) => {",
    "{t.capabilities.slice(0, 5).map((item, idx) => {"
)

# Mobile cards descriptions
old_mob_desc = """                            <p className="text-[0.85rem] leading-6 text-white/88">
                              {idx === 0 && 'Empowering Web3 teams with Cobo MPC institutional security, $50M capital injection, and global physical landing.'}
                              {idx === 1 && 'Leverage PWA automation for targeted user acquisition (打粉), global news distribution, and 7x24h TG/WA AI bots.'}
                              {idx === 2 && 'A transparent trust layer designed for reliable value transfer and ecosystem growth.'}
                              {idx === 3 && 'Connecting physical merchants across Thailand with multi-chain token POS payments and 10,000+ attendee summits.'}
                              {idx === 4 && 'Enterprise-grade infrastructure aligned for scale, compliance and operational reliability.'}
                            </p>"""

new_mob_desc = """                            <p className="text-[0.85rem] leading-6 text-white/88">
                              {t.capabilitiesCardDesc[idx] || t.capabilitiesCardDesc[0]}
                            </p>"""

assert old_mob_desc in content, "old_mob_desc not found"
content = content.replace(old_mob_desc, new_mob_desc)

# Desktop cards descriptions
old_desk_desc = """                                  <p className="max-w-[20rem] text-[1rem] leading-7 text-white/88">
                                    {idx === 0 && 'Empowering Web3 teams with Cobo MPC institutional security, $50M capital injection, and global physical landing.'}
                                    {idx === 1 && 'Leverage PWA automation for targeted user acquisition (打粉), global news distribution, and 7x24h TG/WA AI bots.'}
                                    {idx === 2 && 'A transparent trust layer designed for reliable value transfer and ecosystem growth.'}
                                    {idx === 3 && 'Connecting physical merchants across Thailand with multi-chain token POS payments and 10,000+ attendee summits.'}
                                    {idx === 4 && 'Enterprise-grade infrastructure aligned for scale, compliance and operational reliability.'}
                                  </p>"""

new_desk_desc = """                                  <p className="max-w-[20rem] text-[1rem] leading-7 text-white/88">
                                    {t.capabilitiesCardDesc[idx] || t.capabilitiesCardDesc[0]}
                                  </p>"""

assert old_desk_desc in content, "old_desk_desc not found"
content = content.replace(old_desk_desc, new_desk_desc)

# Update Section 7 "Here It Is"
old_sec7 = """            <section id="here-it-is" className="mx-auto max-w-7xl px-6 py-24 lg:px-10 lg:py-32">
              <SectionTitle
                eyebrow="Core Application Scenarios"
                title="Scenario cards that enter as you scroll"
                subtitle="This mirrors the source page's use of repeated scenario modules. The animation intentionally stays understated: fade, rise, light hover, strong spacing."
              />

              <div className="scenario-group mt-14 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
                {scenarios.map((item, idx) => (
                  <div key={item} className={cx('scenario-card group card-interactive card-hover-lift p-7', scenarioCardClassName)}>
                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_left,rgba(255,255,255,0.1),transparent_35%),radial-gradient(circle_at_bottom_right,rgba(138,170,255,0.12),transparent_35%)] opacity-0 transition duration-500 group-hover:opacity-100" />
                    <div className="relative">
                      <div className="mb-6 text-5xl font-semibold text-white/12">0{idx + 1}</div>
                      <h3 className="text-2xl font-medium text-white">{item}</h3>
                      <p className="mt-3 text-sm leading-7 text-white/70">
                        {idx === 0 && '设立 5000 万美金生态孵化基金，重点投资 Web3 天使轮及 A 轮，每年深度孵化超 50 个优质创新项目，提供资金、技术、品牌与市场全方位赋能。'}
                        {idx === 1 && '深度整合 Cobo Wallet 机构级 MPC 阈值安全与多签金库架构，实现项目资金隔离、链上高频结算与多链大额资产合规协管。'}
                        {idx === 2 && '提供从社群精准打粉、全网新闻通稿分发，到 Telegram/WhatsApp 7x24小时智能客服机器人与 16秒短视频/5分钟深度解说的工业化自动化执行。'}
                        {idx === 3 && 'MOORE 旅运拥有独栋 4000 平米大楼，成功承办芭提雅 10,000 人体育馆超级盛典，并推动全泰 100+ 商户（7-11/Central World）支持 Token POS 刷卡消费。'}
                        {idx === 4 && '新加坡会计与企业管理局（ACRA UEN: 202335893Z）合法登记，已在曼谷、香港、新加坡、东京、首尔、吉隆坡、胡志明设立常设实体协作据点。'}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </section>"""

new_sec7 = """            <section id="here-it-is" className="mx-auto max-w-7xl px-6 py-24 lg:px-10 lg:py-32">
              <SectionTitle
                eyebrow={t.scenariosEyebrow}
                title={t.scenariosTitle}
                subtitle={t.scenariosDesc}
              />

              <div className="scenario-group mt-14 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
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
              </div>
            </section>"""

assert old_sec7 in content, "old_sec7 not found"
content = content.replace(old_sec7, new_sec7)

# Update Section 8 "Trends"
old_sec8 = """            <section className="border-y border-white/10 bg-white/[0.02]">
              <div className="mx-auto max-w-7xl bg-black px-6 py-24 lg:px-10 lg:py-32">
                <SectionTitle
                  eyebrow="Looking Ahead"
                  title="Key trends shaping the next cycle"
                  subtitle="The original page includes a trend list with ordinal markers. This version rebuilds that editorial motif with cleaner visual hierarchy and more modern spacing."
                />

                <div className="stagger-drop mt-14 grid gap-4 lg:grid-cols-2">
                  {trends.map((item, idx) => (
                    <div key={item} className={cx('fade-up card-interactive card-hover-lift flex gap-5 p-6', trendCardClassName)}>
                      <div className="text-4xl font-semibold text-white/12">[{idx + 1}]</div>
                      <div>
                        <div className="text-xl font-medium text-white">{item}</div>
                        <p className="mt-3 text-sm leading-7 text-white/70">
                          {idx === 0 && 'Cobo MPC 阈值签名与机构级多签金库守护链上核心资产。'}
                          {idx === 1 && '自研 PWA 自动化内核驱动社群打粉与全网新闻通稿。'}
                          {idx === 2 && '全泰 100+ 实体商户代币 POS 刷卡直接消费落地。'}
                          {idx === 3 && '新加坡政府 ACRA 官方核发牌照（UEN: 202335893Z）。'}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </section>"""

new_sec8 = """            <section className="border-y border-white/10 bg-white/[0.02]">
              <div className="mx-auto max-w-7xl bg-black px-6 py-24 lg:px-10 lg:py-32">
                <SectionTitle
                  eyebrow={t.trendsEyebrow}
                  title={t.trendsTitle}
                  subtitle={t.trendsDesc}
                />

                <div className="stagger-drop mt-14 grid gap-4 lg:grid-cols-2">
                  {t.trends.map((item, idx) => (
                    <div key={item} className={cx('fade-up card-interactive card-hover-lift flex gap-5 p-6', trendCardClassName)}>
                      <div className="text-4xl font-semibold text-white/12">[{idx + 1}]</div>
                      <div>
                        <div className="text-xl font-medium text-white">{item}</div>
                        <p className="mt-3 text-sm leading-7 text-white/70">
                          {t.trendsCardDesc[idx] || t.trendsCardDesc[0]}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </section>"""

assert old_sec8 in content, "old_sec8 not found"
content = content.replace(old_sec8, new_sec8)

# Update Section 9 "Roadmap"
old_sec9 = """            <section className="mx-auto max-w-7xl px-6 py-24 lg:px-10 lg:py-32">
              <SectionTitle
                eyebrow="Last But Not Least"
                title="Roadmap"
                subtitle="A timeline with cinematic spacing and alternating reveal direction creates a similar narrative finish to the reference site."
              />"""

new_sec9 = """            <section id="roadmap" className="mx-auto max-w-7xl px-6 py-24 lg:px-10 lg:py-32">
              <SectionTitle
                eyebrow={t.roadmapEyebrow}
                title={t.roadmapTitle}
                subtitle={t.roadmapDesc}
              />"""

assert old_sec9 in content, "old_sec9 not found"
content = content.replace(old_sec9, new_sec9)

content = content.replace(
    "{roadmap.map((item, idx) => (",
    "{t.roadmap.map((item, idx) => ("
)

# Update Section 10 "CTA"
old_sec10 = """                  <div className="text-xs uppercase tracking-[0.32em] text-white/56">MOORE LABS</div>
                  <h2 className="mt-5 max-w-4xl text-4xl font-semibold leading-[0.95] tracking-tight text-white md:text-6xl xl:text-[88px]">
                    Built for the next generation of Web3 innovation.
                  </h2>
                  <p className="mt-6 max-w-2xl text-base leading-8 text-white/66 md:text-lg">
                    A modular infrastructure layer for identity, payments, tokenized real-world assets and programmable financial access.
                  </p>
                </div>

                <div className="rounded-[32px] border border-white/10 bg-[linear-gradient(180deg,rgba(19,26,40,0.52),rgba(10,14,24,0.68))] p-6 shadow-[0_22px_60px_rgba(0,0,0,0.24)] backdrop-blur-xl">
                  <div className="text-sm uppercase tracking-[0.28em] text-white/46">Start here</div>
                  <div className="mt-6 space-y-3">
                    {['Explore infrastructure', 'Read the docs', 'Launch app'].map((item) => (
                      <a
                        key={item}
                        href="#"
                        className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/[0.04] px-5 py-4 text-white/84 transition hover:bg-white/[0.06]"
                      >
                        <span>{item}</span>
                        <ArrowUpRight className="h-4 w-4" />
                      </a>
                    ))}
                  </div>"""

new_sec10 = """                  <div className="text-xs uppercase tracking-[0.32em] text-white/56">{t.ctaTag}</div>
                  <h2 className="mt-5 max-w-4xl text-4xl font-semibold leading-[0.95] tracking-tight text-white md:text-6xl xl:text-[88px]">
                    {t.ctaTitle}
                  </h2>
                  <p className="mt-6 max-w-2xl text-base leading-8 text-white/66 md:text-lg">
                    {t.ctaDesc}
                  </p>
                </div>

                <div className="rounded-[32px] border border-white/10 bg-[linear-gradient(180deg,rgba(19,26,40,0.52),rgba(10,14,24,0.68))] p-6 shadow-[0_22px_60px_rgba(0,0,0,0.24)] backdrop-blur-xl">
                  <div className="text-sm uppercase tracking-[0.28em] text-white/46">Start here</div>
                  <div className="mt-6 space-y-3">
                    {t.ctaLinks.map((item) => (
                      <a
                        key={item}
                        href="#why-moore-labs"
                        className="flex items-center justify-between rounded-2xl border border-white/10 bg-white/[0.04] px-5 py-4 text-white/84 transition hover:bg-white/[0.06]"
                      >
                        <span>{item}</span>
                        <ArrowUpRight className="h-4 w-4" />
                      </a>
                    ))}
                  </div>"""

assert old_sec10 in content, "old_sec10 not found"
content = content.replace(old_sec10, new_sec10)

# Update Footer
old_footer = """                <p className="mt-3 max-w-xl text-sm leading-7 text-white/62">
                  Official Web3 platform by MOORE FOUNDATION LTD. (Singapore ACRA UEN: 202335893Z). Integrating $50M Ecosystem Fund, Cobo MPC Custody, and MOORE Travel Group.
                </p>"""

new_footer = """                <p className="mt-3 max-w-xl text-sm leading-7 text-white/62">
                  {t.footerText}
                </p>"""

assert old_footer in content, "old_footer not found"
content = content.replace(old_footer, new_footer)

# Update Modal
old_modal = """          {/* 轻量 COBO 钱包连接弹窗 (原生纯净样式) */}
          {isWalletModalOpen && (
            <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4 backdrop-blur-md">
              <div className="w-full max-w-sm rounded-3xl border border-white/15 bg-[#0f172a] p-6 text-white shadow-2xl">
                <div className="flex items-center justify-between border-b border-white/10 pb-3 mb-4">
                  <h3 className="text-base font-bold text-white">Connect Web3 Wallet</h3>
                  <button onClick={() => setIsWalletModalOpen(false)} className="text-white/50 hover:text-white">✕</button>
                </div>
                {walletConnecting ? (
                  <div className="py-6 text-center text-sm text-white/70">Connecting to Cobo Wallet...</div>
                ) : (
                  <div className="space-y-3">
                    <button
                      onClick={() => connectWallet('cobo')}
                      className="w-full flex items-center justify-between rounded-2xl border border-amber-500/50 bg-amber-500/10 p-3.5 text-left hover:bg-amber-500/20 transition group"
                    >
                      <div>
                        <div className="text-sm font-bold text-white group-hover:text-amber-300">Cobo Wallet (MPC)</div>
                        <div className="text-xs text-amber-300/70">首选推荐 · 机构级阈值安全</div>
                      </div>
                      <span className="rounded bg-amber-500 px-2 py-0.5 text-[10px] font-bold text-black">Recommended</span>
                    </button>
                    <button
                      onClick={() => connectWallet('metamask')}
                      className="w-full flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 p-3 text-left hover:bg-white/10 transition"
                    >
                      <div className="text-sm text-white/90">MetaMask</div>
                      <span className="text-xs text-white/40">Browser</span>
                    </button>
                    <button
                      onClick={() => connectWallet('okx')}
                      className="w-full flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 p-3 text-left hover:bg-white/10 transition"
                    >
                      <div className="text-sm text-white/90">OKX Wallet</div>
                      <span className="text-xs text-white/40">Extension</span>
                    </button>
                    <div className="pt-2 text-center text-[11px] text-white/40">
                      Protected by Cobo Threshold Signature MPC
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}"""

new_modal = """          {/* 輕量 Wallet MPC 門限安全錢包連接彈窗 (原生純淨高質感) */}
          {isWalletModalOpen && (
            <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4 backdrop-blur-md">
              <div className="w-full max-w-sm rounded-3xl border border-white/15 bg-[#0f172a] p-6 text-white shadow-2xl">
                <div className="flex items-center justify-between border-b border-white/10 pb-3 mb-4">
                  <h3 className="text-base font-bold text-white">{t.modalTitle}</h3>
                  <button onClick={() => setIsWalletModalOpen(false)} className="text-white/50 hover:text-white">✕</button>
                </div>
                {walletConnecting ? (
                  <div className="py-6 text-center text-sm text-white/70">{t.modalConnecting}</div>
                ) : (
                  <div className="space-y-3">
                    <button
                      onClick={() => connectWallet('mpc')}
                      className="w-full flex items-center justify-between rounded-2xl border border-amber-500/50 bg-amber-500/10 p-3.5 text-left hover:bg-amber-500/20 transition group"
                    >
                      <div>
                        <div className="text-sm font-bold text-white group-hover:text-amber-300">{t.modalMpcTitle}</div>
                        <div className="text-xs text-amber-300/70">{t.modalMpcSub}</div>
                      </div>
                      <span className="rounded bg-amber-500 px-2 py-0.5 text-[10px] font-bold text-black">{t.modalMpcBadge}</span>
                    </button>
                    <button
                      onClick={() => connectWallet('metamask')}
                      className="w-full flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 p-3 text-left hover:bg-white/10 transition"
                    >
                      <div className="text-sm text-white/90">{t.modalMetaMask}</div>
                      <span className="text-xs text-white/40">Browser</span>
                    </button>
                    <button
                      onClick={() => connectWallet('okx')}
                      className="w-full flex items-center justify-between rounded-2xl border border-white/10 bg-white/5 p-3 text-left hover:bg-white/10 transition"
                    >
                      <div className="text-sm text-white/90">{t.modalOkx}</div>
                      <span className="text-xs text-white/40">Extension</span>
                    </button>
                    <div className="pt-2 text-center text-[11px] text-white/40">
                      {t.modalFoot}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}"""

assert old_modal in content, "old_modal not found"
content = content.replace(old_modal, new_modal)

# Check remaining cobo occurrences in the file
matches = re.findall(r".{0,30}cobo.{0,30}", content, re.IGNORECASE)
print(f"Remaining cobo occurrences in content: {len(matches)}")
for m in matches:
    print(" -> ", m.strip())

# Clean up any leftover top constants that contained cobo
content = content.replace("'Cobo MPC Wallet'", "'Wallet MPC'")
content = content.replace("'Cobo Wallet MPC'", "'Wallet MPC'")
content = content.replace("Cobo MPC Institutional Custody", "Wallet MPC Institutional Custody")
content = content.replace("Integrated with Cobo Wallet and MPC threshold security", "Integrated with Wallet MPC threshold security")
content = content.replace("Cobo Institutional MPC Asset Custody & Wallet", "Wallet MPC Institutional Custody & Asset Vault")
content = content.replace("Cobo MPC Institutional Custody Integration", "Wallet MPC Institutional Custody Integration")

# Double check cobo matches
matches2 = re.findall(r".{0,30}cobo.{0,30}", content, re.IGNORECASE)
print(f"Remaining cobo occurrences after constant cleanup: {len(matches2)}")
assert len(matches2) == 0, f"Error: Still found {len(matches2)} cobo occurrences!"

with open("/workspace/agent/moore-labs/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: index.html fully converted to Bilingual (Traditional Chinese & English) and 0 Cobo references remaining!")
