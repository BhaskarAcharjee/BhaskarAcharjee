import base64
import os

def generate_ug_style_svgs():
    with open("assets/bhaskar_user.jpg", "rb") as f:
        user_b64 = base64.b64encode(f.read()).decode("utf-8")

    # =========================================================================
    # 1. HERO.SVG
    # =========================================================================
    hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 640" width="100%" height="100%">
<defs>
  <style>
    @font-face {{
      font-family: 'Inter';
      font-style: normal;
      font-weight: 400 900;
      src: local('Inter'), local('Segoe UI'), local('Roboto'), sans-serif;
    }}
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 900; }}
    
    @keyframes pulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.35; transform: scale(1.3); }}
    }}
    .pulse {{
      animation: pulseDot 2s infinite ease-in-out;
      transform-origin: 228px 118px;
    }}
    @keyframes rotateClockwise {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    @keyframes rotateCounter {{
      0% {{ transform: rotate(360deg); }}
      100% {{ transform: rotate(0deg); }}
    }}
    .spin-cw {{
      animation: rotateClockwise 26s linear infinite;
      transform-origin: 935px 330px;
    }}
    .spin-ccw {{
      animation: rotateCounter 34s linear infinite;
      transform-origin: 935px 330px;
    }}
  </style>

  <linearGradient id="hero-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".6"/>
    <stop offset="40%" stop-color="#1f3760" stop-opacity=".2"/>
    <stop offset="70%" stop-color="#ff354f" stop-opacity=".4"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity=".2"/>
  </linearGradient>

  <linearGradient id="hero-aurora" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#38bdf8"/>
    <stop offset="45%" stop-color="#60a5fa"/>
    <stop offset="85%" stop-color="#c084fc"/>
    <stop offset="100%" stop-color="#f472b6"/>
  </linearGradient>

  <radialGradient id="hero-halo" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#247bff" stop-opacity=".32"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
  </radialGradient>

  <radialGradient id="hero-red-halo" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff354f" stop-opacity=".28"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
  </radialGradient>

  <pattern id="hero-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#2d4a73" fill-opacity=".3"/>
  </pattern>

  <clipPath id="hero-outer">
    <rect x="1" y="1" width="1198" height="638" rx="22"/>
  </clipPath>

  <clipPath id="bhaskar-photo-clip">
    <circle cx="935" cy="330" r="185"/>
  </clipPath>
</defs>

<g clip-path="url(#hero-outer)">
  <!-- Background -->
  <rect x="1" y="1" width="1198" height="638" rx="22" fill="#070b16" stroke="url(#hero-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="636" rx="21" fill="url(#hero-dots)"/>

  <!-- Ambient Halos -->
  <ellipse cx="935" cy="330" rx="380" ry="360" fill="url(#hero-halo)"/>
  <ellipse cx="1180" cy="110" rx="260" ry="320" fill="url(#hero-red-halo)"/>

  <!-- Big Watermark Numbers in Background -->
  <text x="710" y="525" font-size="260" fill="#0c1e38" class="heading" letter-spacing="-6" opacity="0.6">TCS</text>

  <!-- Slanted Structural Grid Rays -->
  <path d="M630 95 L310 640" fill="none" stroke="#193057" stroke-width="1.5" opacity=".25"/>
  <path d="M714 95 L394 640" fill="none" stroke="#193057" stroke-width="1.5" opacity=".25"/>
  <path d="M798 95 L478 640" fill="none" stroke="#193057" stroke-width="1.5" opacity=".25"/>
  <path d="M882 95 L562 640" fill="none" stroke="#193057" stroke-width="1.5" opacity=".25"/>

  <!-- Animated Sci-Fi Concentric Rings -->
  <g class="spin-cw">
    <circle cx="935" cy="330" r="215" fill="none" stroke="#247bff" opacity=".2"/>
    <circle cx="935" cy="330" r="215" fill="none" stroke="#247bff" stroke-width="2" stroke-dasharray="70 40 20 80"/>
  </g>
  <g class="spin-ccw">
    <circle cx="935" cy="330" r="232" fill="none" stroke="#ff354f" opacity=".2"/>
    <circle cx="935" cy="330" r="232" fill="none" stroke="#ff354f" stroke-width="2" stroke-dasharray="60 30 10 90"/>
  </g>

  <!-- Top Metadata Bar -->
  <path d="M42 76 L1158 76" fill="none" stroke="#223149" stroke-width="1.5"/>
  <text x="44" y="44" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">BA / SOFTWARE ENGINEER</text>
  <text x="446" y="44" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">KOLKATA, IN</text>
  
  <!-- Red Slanted Hazard Chevrons (Top Right) -->
  <path d="M1092 29l9 0 -7 18h-9Z" fill="#ff354f"/>
  <path d="M1104 29l9 0 -7 18h-9Z" fill="#ff354f"/>
  <path d="M1116 29l9 0 -7 18h-9Z" fill="#ff354f"/>

  <!-- Status Capsule Badge -->
  <rect x="44" y="104" width="168" height="28" rx="6" fill="#122c49"/>
  <text x="56" y="122.5" font-size="10" fill="#f2f5ff" class="mono" letter-spacing="1">OPEN TO COLLABS</text>
  <circle cx="228" cy="118" r="4.5" fill="#3d93ff" class="pulse"/>

  <!-- Subtitle -->
  <text x="45" y="176" font-size="18" fill="#b6c5dd" class="mono">Hi there, I'm</text>

  <!-- Huge Name Typography -->
  <g class="heading">
    <text x="39" y="286" font-size="124" fill="#f2f5ff" letter-spacing="1">BHASKAR</text>
    <text x="40" y="396" font-size="124" fill="url(#hero-aurora)" letter-spacing="1">ACHARJEE</text>
  </g>

  <!-- Hazard Chevrons & Slogan -->
  <path d="M383 314l9 0 -7 18h-9Z" fill="#ff354f"/>
  <path d="M395 314l9 0 -7 18h-9Z" fill="#ff354f"/>
  <path d="M407 314l9 0 -7 18h-9Z" fill="#ff354f"/>
  <text x="382" y="365" font-size="28" fill="#f2f5ff" class="heading">INNOVATE.</text>
  <text x="382" y="395" font-size="28" fill="#f2f5ff" class="heading">SCALE.</text>

  <!-- Dynamic Role Cycling -->
  <g class="sans">
    <text x="46" y="446" font-size="26" font-weight="700" fill="#f2f5ff">
      Java Backend Developer @ TCS
    </text>
    <text x="46" y="482" font-size="14.5" fill="#adbed8" class="mono">
      Building scalable enterprise microservices &amp; 5+ published Google Play apps.
    </text>
  </g>

  <!-- Bhaskar's Real Photo Embedded on Right -->
  <g>
    <!-- Background circle glow frame -->
    <circle cx="935" cy="330" r="188" fill="none" stroke="#247bff" stroke-width="3"/>
    <circle cx="935" cy="330" r="198" fill="none" stroke="#ff354f" stroke-width="1.5" stroke-dasharray="12 10" opacity="0.6"/>
    <image href="data:image/jpeg;base64,{user_b64}" x="750" y="145" width="370" height="370" clip-path="url(#bhaskar-photo-clip)"/>
  </g>

  <!-- Floating Identity Card Badge (Over Photo) -->
  <rect x="850" y="522" width="300" height="58" rx="10" fill="#0b1323" stroke="#2d527b" stroke-width="1.5"/>
  <path d="M865 538l9 0 -7 18h-9Z" fill="#247bff"/>
  <path d="M877 538l9 0 -7 18h-9Z" fill="#247bff"/>
  <path d="M889 538l9 0 -7 18h-9Z" fill="#247bff"/>
  <text x="910" y="548" font-size="17" fill="#ffffff" class="heading">ENGINEER / CREATOR</text>
  <text x="910" y="567" font-size="10.5" fill="#85a4ce" class="mono">@BhaskarAcharjee</text>

  <!-- Bottom Divider Line -->
  <path d="M44 554 L644 554" fill="none" stroke="#24334d" stroke-width="1.5"/>

  <!-- Bottom Metadata Row with Icons -->
  <!-- Kolkata -->
  <g transform="translate(44 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 22s8-8 8-14a8 8 0 0 0-16 0c0 6 8 14 8 14Z M15 8a3 3 0 1 1-6 0a3 3 0 1 1 6 0"/>
  </g>
  <text x="70" y="593" font-size="11.5" fill="#9db2d1" class="mono">Kolkata, IN</text>

  <!-- TCS -->
  <g transform="translate(200 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M8 6V3h8v3 M3 7h18v15H3Z M3 12q9 6 18 0 M11 14h2"/>
  </g>
  <text x="226" y="593" font-size="11.5" fill="#9db2d1" class="mono">TCS Backend</text>

  <!-- 34 Repos -->
  <g transform="translate(356 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 3h16v18H4Z M8 3v18 M12 7h4"/>
  </g>
  <text x="382" y="593" font-size="11.5" fill="#9db2d1" class="mono">34 repos</text>

  <!-- 5+ Play Apps -->
  <g transform="translate(490 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="m12 2 3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1Z"/>
  </g>
  <text x="516" y="593" font-size="11.5" fill="#9db2d1" class="mono">5+ play apps</text>

  <!-- Right Section Number -->
  <text x="890" y="612" font-size="10.5" fill="#6688b5" class="mono">01 / ENGINEERED TO EVOLVE</text>
</g>
</svg>
'''
    with open("assets/hero.svg", "w", encoding="utf-8") as f:
        f.write(hero_svg)
    print("Built assets/hero.svg")

    # =========================================================================
    # 2. ABOUT-LIFE.SVG
    # =========================================================================
    about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 640" width="100%" height="100%">
<defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }}
  </style>

  <linearGradient id="about-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".5"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".2"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".4"/>
  </linearGradient>

  <pattern id="about-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="about-outer">
    <rect x="1" y="1" width="1198" height="638" rx="22"/>
  </clipPath>
</defs>

<g clip-path="url(#about-outer)">
  <rect x="1" y="1" width="1198" height="638" rx="22" fill="#070b16" stroke="url(#about-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="636" rx="21" fill="url(#about-dots)"/>

  <!-- Top Header -->
  <path d="M42 66 L1158 66" fill="none" stroke="#223149" stroke-width="1.5"/>
  <text x="44" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">02 / THE BLUEPRINT</text>
  <text x="960" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">FOUNDATIONS &amp; CRAFT</text>

  <!-- Left Column: Core Focus Cards -->
  <g transform="translate(44, 90)">
    <text x="0" y="24" font-size="28" fill="#f2f5ff" class="heading">Engineering Architecture</text>
    <text x="0" y="52" font-size="13.5" fill="#8e9db9" class="mono">Where backend resilience meets mobile craft.</text>

    <!-- Card 1: Enterprise Backend -->
    <g transform="translate(0, 80)">
      <rect width="530" height="120" rx="12" fill="#0b1424" stroke="#223b5e" stroke-width="1.4"/>
      <path d="M16 0 L80 0" stroke="#247bff" stroke-width="3"/>
      <text x="24" y="36" font-size="18" fill="#f2f5ff" class="heading">Enterprise Java @ TCS</text>
      <text x="24" y="64" font-size="13" fill="#9db2d1" class="sans">Architecting high-throughput microservices, robust RESTful APIs,</text>
      <text x="24" y="86" font-size="13" fill="#9db2d1" class="sans">and fault-tolerant data pipelines for mission-critical enterprise systems.</text>
      <rect x="420" y="20" width="86" height="24" rx="4" fill="#122c49"/>
      <text x="432" y="36" font-size="10" fill="#73b0ff" class="mono">BACKEND</text>
    </g>

    <!-- Card 2: Mobile Ecosystem -->
    <g transform="translate(0, 220)">
      <rect width="530" height="120" rx="12" fill="#0b1424" stroke="#223b5e" stroke-width="1.4"/>
      <path d="M16 0 L80 0" stroke="#ff354f" stroke-width="3"/>
      <text x="24" y="36" font-size="18" fill="#f2f5ff" class="heading">5+ Published Play Store Apps</text>
      <text x="24" y="64" font-size="13" fill="#9db2d1" class="sans">End-to-end native Android engineering with Kotlin, Jetpack</text>
      <text x="24" y="86" font-size="13" fill="#9db2d1" class="sans">Compose, offline SQLite caching, and fluid user experiences.</text>
      <rect x="420" y="20" width="86" height="24" rx="4" fill="#301524"/>
      <text x="432" y="36" font-size="10" fill="#ff7088" class="mono">ANDROID</text>
    </g>

    <!-- Card 3: Creative 3D & Analytics -->
    <g transform="translate(0, 360)">
      <rect width="530" height="120" rx="12" fill="#0b1424" stroke="#223b5e" stroke-width="1.4"/>
      <path d="M16 0 L80 0" stroke="#38bdf8" stroke-width="3"/>
      <text x="24" y="36" font-size="18" fill="#f2f5ff" class="heading">3D Web Labs &amp; Data Insights</text>
      <text x="24" y="64" font-size="13" fill="#9db2d1" class="sans">Building 3D simulations (3D-Room, TShirtify AI), audio visualizers,</text>
      <text x="24" y="86" font-size="13" fill="#9db2d1" class="sans">and automated Python data analytics pipelines for deep business insights.</text>
      <rect x="420" y="20" width="86" height="24" rx="4" fill="#0e2a3a"/>
      <text x="435" y="36" font-size="10" fill="#38bdf8" class="mono">3D + AI</text>
    </g>
  </g>

  <!-- Right Column: Beyond the Desk Card -->
  <g transform="translate(620, 110)">
    <rect width="536" height="470" rx="14" fill="#0c1628" stroke="#233d61" stroke-width="1.5"/>
    <text x="32" y="44" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">BEYOND CODE // PHILOSOPHY</text>
    <text x="32" y="86" font-size="32" fill="#f2f5ff" class="heading">Discipline. Logic. Impact.</text>

    <!-- Point 01 -->
    <g transform="translate(32, 130)">
      <text x="0" y="28" font-size="32" fill="#247bff" class="heading">01</text>
      <text x="50" y="16" font-size="11" fill="#8e9db9" class="mono">B.TECH ELECTRONICS (JGEC)</text>
      <text x="50" y="36" font-size="15" fill="#f2f5ff" class="sans">Hardware-informed understanding of low-level systems &amp; optimization.</text>
      <path d="M0 56 L470 56" stroke="#1c2d47" stroke-width="1"/>
    </g>

    <!-- Point 02 -->
    <g transform="translate(32, 215)">
      <text x="0" y="28" font-size="32" fill="#ff354f" class="heading">02</text>
      <text x="50" y="16" font-size="11" fill="#8e9db9" class="mono">ALGORITHMIC PROBLEM SOLVING</text>
      <text x="50" y="36" font-size="15" fill="#f2f5ff" class="sans">Consistently solving on LeetCode &amp; CodeChef for analytical rigor.</text>
      <path d="M0 56 L470 56" stroke="#1c2d47" stroke-width="1"/>
    </g>

    <!-- Point 03 -->
    <g transform="translate(32, 300)">
      <text x="0" y="28" font-size="32" fill="#38bdf8" class="heading">03</text>
      <text x="50" y="16" font-size="11" fill="#8e9db9" class="mono">INDEPENDENT CREATOR</text>
      <text x="50" y="36" font-size="15" fill="#f2f5ff" class="sans">Published apps, web portals (corvas.in) and developer YouTube videos.</text>
      <path d="M0 56 L470 56" stroke="#1c2d47" stroke-width="1"/>
    </g>

    <!-- Bottom Accent Pill -->
    <rect x="32" y="390" width="470" height="50" rx="8" fill="#11223b"/>
    <circle cx="56" cy="415" r="4.5" fill="#38bdf8"/>
    <text x="74" y="419" font-size="12" fill="#b9d6ff" class="mono">CURIOUS BY DEFAULT · BUILDING WITH INTENT</text>
  </g>
</g>
</svg>
'''
    with open("assets/about-life.svg", "w", encoding="utf-8") as f:
        f.write(about_svg)
    print("Built assets/about-life.svg")

    # =========================================================================
    # 3. STACK.SVG
    # =========================================================================
    stack_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 640" width="100%" height="100%">
<defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }}
  </style>

  <linearGradient id="stack-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".5"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".2"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".4"/>
  </linearGradient>

  <pattern id="stack-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="stack-outer">
    <rect x="1" y="1" width="1198" height="638" rx="22"/>
  </clipPath>
</defs>

<g clip-path="url(#stack-outer)">
  <rect x="1" y="1" width="1198" height="638" rx="22" fill="#070b16" stroke="url(#stack-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="636" rx="21" fill="url(#stack-dots)"/>

  <!-- Top Header -->
  <path d="M42 66 L1158 66" fill="none" stroke="#223149" stroke-width="1.5"/>
  <text x="44" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">03 / THE ARSENAL</text>
  <text x="940" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">TECHNOLOGY &amp; TOOLING</text>

  <!-- Left Column: Core Languages & Mobile -->
  <text x="44" y="115" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">LANGUAGES &amp; MOBILE</text>

  <!-- Tech Cards Grid -->
  <!-- Row 1 -->
  <!-- Java -->
  <g transform="translate(44, 135)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#ff354f" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">CORE</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">Java</text>
  </g>

  <!-- Kotlin -->
  <g transform="translate(226, 135)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#ff354f" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">MOBILE</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">Kotlin</text>
  </g>

  <!-- Python -->
  <g transform="translate(408, 135)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">AI / DATA</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">Python</text>
  </g>

  <!-- Row 2 -->
  <!-- Android Compose -->
  <g transform="translate(44, 235)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#ff354f" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">UI / UX</text>
    <text x="18" y="64" font-size="22" fill="#ffffff" class="heading">Compose</text>
  </g>

  <!-- C++ -->
  <g transform="translate(226, 235)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">SYSTEMS</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">C / C++</text>
  </g>

  <!-- SQL / SQLite -->
  <g transform="translate(408, 235)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">STORAGE</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">SQLite</text>
  </g>

  <!-- Row 3 -->
  <!-- TypeScript -->
  <g transform="translate(44, 335)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">WEB</text>
    <text x="18" y="64" font-size="23" fill="#ffffff" class="heading">TypeScript</text>
  </g>

  <!-- JavaScript -->
  <g transform="translate(226, 335)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">SCRIPT</text>
    <text x="18" y="64" font-size="23" fill="#ffffff" class="heading">JavaScript</text>
  </g>

  <!-- Bash -->
  <g transform="translate(408, 335)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">CLI</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">Bash</text>
  </g>

  <!-- Right Column: Backend, Cloud & Creative -->
  <text x="625" y="115" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">BACKEND, CLOUD &amp; CREATIVE</text>

  <!-- Spring Boot -->
  <g transform="translate(625, 135)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">ENTERPRISE</text>
    <text x="18" y="64" font-size="22" fill="#ffffff" class="heading">Spring Boot</text>
  </g>

  <!-- Microservices -->
  <g transform="translate(807, 135)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#ff354f" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">DISTRIBUTED</text>
    <text x="18" y="64" font-size="20" fill="#ffffff" class="heading">Microservices</text>
  </g>

  <!-- Docker -->
  <g transform="translate(989, 135)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">CONTAINERS</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">Docker</text>
  </g>

  <!-- AWS / Cloud -->
  <g transform="translate(625, 235)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#ff354f" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">CLOUD</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">AWS / GCP</text>
  </g>

  <!-- Node.js / Express -->
  <g transform="translate(807, 235)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">SERVERS</text>
    <text x="18" y="64" font-size="22" fill="#ffffff" class="heading">Node / Express</text>
  </g>

  <!-- MySQL / MongoDB -->
  <g transform="translate(989, 235)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">DATABASES</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">MySQL</text>
  </g>

  <!-- Three.js (3D Web) -->
  <g transform="translate(625, 335)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#38bdf8" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">3D GRAPHICS</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">Three.js</text>
  </g>

  <!-- React.js -->
  <g transform="translate(807, 335)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#247bff" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">FRONTEND</text>
    <text x="18" y="64" font-size="24" fill="#ffffff" class="heading">React.js</text>
  </g>

  <!-- Pandas & Power BI -->
  <g transform="translate(989, 335)">
    <rect width="168" height="84" rx="9" fill="#0d182c" stroke="#284465"/>
    <path d="M12 84 L72 84" stroke="#ff354f" stroke-width="2"/>
    <text x="18" y="34" font-size="12" fill="#7db5ff" class="mono">ANALYTICS</text>
    <text x="18" y="64" font-size="22" fill="#ffffff" class="heading">Pandas / BI</text>
  </g>

  <!-- Bottom Strip -->
  <rect x="44" y="470" width="1112" height="110" rx="12" fill="#0c1628" stroke="#1f3760" stroke-width="1.5"/>
  <text x="74" y="515" font-size="12" fill="#8e9db9" class="mono" letter-spacing="1.6">ENGINEERING CULTURE // MANIFESTO</text>
  <text x="74" y="550" font-size="22" fill="#f2f5ff" class="heading">"Write robust systems. Deliver frictionless mobile apps. Never stop learning."</text>
  <text x="890" y="550" font-size="11" fill="#73b0ff" class="mono">BUILD / OPTIMIZE / SCALE</text>
</g>
</svg>
'''
    with open("assets/stack.svg", "w", encoding="utf-8") as f:
        f.write(stack_svg)
    print("Built assets/stack.svg")

    # =========================================================================
    # 4. ID-DASHBOARD.SVG
    # =========================================================================
    dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 780" width="100%" height="100%">
<defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', monospace; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <linearGradient id="id-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".5"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".2"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".4"/>
  </linearGradient>

  <pattern id="id-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="id-outer">
    <rect x="1" y="1" width="1198" height="778" rx="22"/>
  </clipPath>

  <clipPath id="id-photo-clip">
    <rect x="0" y="0" width="160" height="180" rx="10"/>
  </clipPath>
</defs>

<g clip-path="url(#id-outer)">
  <rect x="1" y="1" width="1198" height="778" rx="22" fill="#070b16" stroke="url(#id-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="776" rx="21" fill="url(#id-dots)"/>

  <!-- Top Header -->
  <path d="M42 66 L1158 66" fill="none" stroke="#223149" stroke-width="1.5"/>
  <text x="44" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">04 / BUILDER ID &amp; PUBLIC DASHBOARD</text>
  <text x="960" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">VERIFIED METRICS</text>

  <!-- Left: Industrial Cyber Identity Badge -->
  <g transform="translate(64, 110)">
    <!-- ID Card Container -->
    <rect width="380" height="580" rx="16" fill="#0a1324" stroke="#254365" stroke-width="2"/>

    <!-- ID Header -->
    <rect x="0" y="0" width="380" height="52" rx="16" fill="#12253d"/>
    <text x="24" y="32" font-size="12" fill="#73b0ff" class="mono" letter-spacing="1">DEV IDENTIFICATION PASS</text>
    <circle cx="346" cy="26" r="6" fill="#ff354f"/>

    <!-- Bhaskar's Photo inside ID Card -->
    <g transform="translate(30, 80)">
      <rect width="162" height="182" rx="11" fill="none" stroke="#247bff" stroke-width="2"/>
      <image href="data:image/jpeg;base64,{user_b64}" x="1" y="1" width="160" height="180" clip-path="url(#id-photo-clip)"/>
    </g>

    <!-- Side metadata in badge -->
    <g transform="translate(210, 95)" class="mono">
      <text y="0" font-size="9" fill="#5b789d">NAME</text>
      <text y="20" font-size="14" fill="#ffffff" font-weight="700">Bhaskar A.</text>
      
      <text y="50" font-size="9" fill="#5b789d">ORGANIZATION</text>
      <text y="70" font-size="13" fill="#38bdf8" font-weight="600">TCS</text>

      <text y="100" font-size="9" fill="#5b789d">ROLE</text>
      <text y="120" font-size="13" fill="#ffffff">Backend Dev</text>

      <text y="150" font-size="9" fill="#5b789d">STATUS</text>
      <text y="170" font-size="12" fill="#34d399">ACTIVE</text>
    </g>

    <!-- Lower Details in ID -->
    <g transform="translate(30, 290)">
      <text y="20" font-size="11" fill="#7998bf" class="mono">EDUCATION</text>
      <text y="42" font-size="15" fill="#f2f5ff" class="heading">B.Tech ECE (JGEC Alum)</text>

      <text y="78" font-size="11" fill="#7998bf" class="mono">MOBILE PUBLISHING</text>
      <text y="100" font-size="15" fill="#f2f5ff" class="heading">5+ Production Android Apps</text>

      <text y="136" font-size="11" fill="#7998bf" class="mono">LOCATION</text>
      <text y="158" font-size="15" fill="#f2f5ff" class="heading">Kolkata, West Bengal, India</text>
    </g>

    <!-- Barcode Strip at bottom -->
    <g transform="translate(30, 490)">
      <rect width="320" height="35" fill="#12253d" rx="4"/>
      <text x="24" y="22" font-size="10" fill="#73b0ff" class="mono" letter-spacing="4">||| | | |||| || | ||| |||| |</text>
      <text x="20" y="55" font-size="9" fill="#56779f" class="mono">ID: BA-TCS-2026-WB-JGEC</text>
    </g>
  </g>

  <!-- Right: Public Metrics HUD -->
  <!-- 3 Metric Counter Boxes -->
  <!-- Box 1: Public Repos -->
  <g transform="translate(480, 110)">
    <rect width="210" height="130" rx="10" fill="#101c31" stroke="#28476d" stroke-width="1.5"/>
    <text x="20" y="32" font-size="10" fill="#8aa7cf" class="mono">PUBLIC REPOSITORIES</text>
    <text x="20" y="88" font-size="52" fill="#38bdf8" class="heading">34+</text>
    <text x="20" y="114" font-size="9.5" fill="#688ab5" class="mono">ACTIVE GITHUB</text>
  </g>

  <!-- Box 2: Play Store Apps -->
  <g transform="translate(710, 110)">
    <rect width="210" height="130" rx="10" fill="#101c31" stroke="#28476d" stroke-width="1.5"/>
    <text x="20" y="32" font-size="10" fill="#8aa7cf" class="mono">PLAY STORE APPS</text>
    <text x="20" y="88" font-size="52" fill="#ff354f" class="heading">5+</text>
    <text x="20" y="114" font-size="9.5" fill="#688ab5" class="mono">LIVE ON GOOGLE PLAY</text>
  </g>

  <!-- Box 3: Total Stars -->
  <g transform="translate(940, 110)">
    <rect width="210" height="130" rx="10" fill="#101c31" stroke="#28476d" stroke-width="1.5"/>
    <text x="20" y="32" font-size="10" fill="#8aa7cf" class="mono">RECEIVED STARS</text>
    <text x="20" y="88" font-size="52" fill="#73b0ff" class="heading">50+</text>
    <text x="20" y="114" font-size="9.5" fill="#688ab5" class="mono">COMMUNITY STARS</text>
  </g>

  <!-- Starred Repos Progress Gauges -->
  <g transform="translate(480, 280)">
    <text x="0" y="20" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">FEATURED / POPULAR REPOSITORIES</text>

    <!-- Repo 1: 3D-Room -->
    <g transform="translate(0, 45)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">3D-Room (Interactive 3D Room)</text>
      <text x="640" y="0" font-size="18" fill="#ffffff" class="heading">24 ★</text>
      <rect y="10" width="670" height="12" rx="4" fill="#132842"/>
      <rect y="10" width="580" height="12" rx="4" fill="#247bff"/>
    </g>

    <!-- Repo 2: TShirtify -->
    <g transform="translate(0, 105)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">TShirtify (AI 3D T-Shirt Simulator)</text>
      <text x="640" y="0" font-size="18" fill="#ffffff" class="heading">16 ★</text>
      <rect y="10" width="670" height="12" rx="4" fill="#132842"/>
      <rect y="10" width="420" height="12" rx="4" fill="#ff354f"/>
    </g>

    <!-- Repo 3: TravelGenius -->
    <g transform="translate(0, 165)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">TravelGenius (Smart Travel Planner)</text>
      <text x="640" y="0" font-size="18" fill="#ffffff" class="heading">6 ★</text>
      <rect y="10" width="670" height="12" rx="4" fill="#132842"/>
      <rect y="10" width="220" height="12" rx="4" fill="#247bff"/>
    </g>

    <!-- Repo 4: MelodyMorph -->
    <g transform="translate(0, 225)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">MelodyMorph (Real-Time Audio Visualizer)</text>
      <text x="640" y="0" font-size="18" fill="#ffffff" class="heading">4 ★</text>
      <rect y="10" width="670" height="12" rx="4" fill="#132842"/>
      <rect y="10" width="160" height="12" rx="4" fill="#38bdf8"/>
    </g>
  </g>

  <!-- Bottom Mission HUD -->
  <g transform="translate(480, 580)">
    <rect width="670" height="110" rx="10" fill="#0b1b33" stroke="#2c5b96" stroke-width="1.5"/>
    <rect x="24" y="18" width="64" height="26" rx="5" fill="#ff354f"/>
    <text x="36" y="35" font-size="10.5" fill="#ffffff" class="mono" font-weight="700">NOW</text>
    <text x="24" y="68" font-size="24" fill="#f2f5ff" class="heading">Engineering backend systems @ TCS</text>
    <text x="24" y="92" font-size="12" fill="#88a9d3" class="mono">Building scalable microservices &amp; publishing Android apps.</text>
  </g>
</g>
</svg>
'''
    with open("assets/id-dashboard.svg", "w", encoding="utf-8") as f:
        f.write(dashboard_svg)
    print("Built assets/id-dashboard.svg")

    # =========================================================================
    # 5. CONNECT.SVG
    # =========================================================================
    connect_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', monospace; }
    .heading { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
  </style>

  <linearGradient id="conn-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".5"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".2"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".4"/>
  </linearGradient>

  <pattern id="conn-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="conn-outer">
    <rect x="1" y="1" width="1198" height="318" rx="22"/>
  </clipPath>
</defs>

<g clip-path="url(#conn-outer)">
  <rect x="1" y="1" width="1198" height="318" rx="22" fill="#070b16" stroke="url(#conn-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="316" rx="21" fill="url(#conn-dots)"/>

  <!-- Header line -->
  <path d="M42 54 L1158 54" fill="none" stroke="#223149" stroke-width="1.5"/>
  <text x="44" y="34" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">05 / INITIATE CONTACT</text>
  <text x="960" y="34" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">OPEN FOR OPPORTUNITIES</text>

  <!-- Big Call to Action -->
  <text x="44" y="128" font-size="48" fill="#f2f5ff" class="heading">Let's build what's next.</text>
  <text x="44" y="168" font-size="16" fill="#a9c0df" class="sans">
    Open to high-impact distributed backend engineering, mobile app architecture, and open-source collaborations.
  </text>

  <!-- Status Capsule -->
  <rect x="44" y="210" width="240" height="38" rx="8" fill="#102542" stroke="#247bff" stroke-width="1.4"/>
  <circle cx="68" cy="229" r="4.5" fill="#38bdf8"/>
  <text x="84" y="234" font-size="11" fill="#b9d6ff" class="mono">KOLKATA, IN · OPEN TO WORK</text>

  <!-- Right Side Accent -->
  <path d="M1092 120l9 0 -7 18h-9Z" fill="#247bff"/>
  <path d="M1104 120l9 0 -7 18h-9Z" fill="#247bff"/>
  <path d="M1116 120l9 0 -7 18h-9Z" fill="#ff354f"/>
  <text x="920" y="234" font-size="11" fill="#6688b5" class="mono">BHASKAR ACHARJEE © 2026</text>
</g>
</svg>
'''
    with open("assets/connect.svg", "w", encoding="utf-8") as f:
        f.write(connect_svg)
    print("Built assets/connect.svg")

if __name__ == "__main__":
    generate_ug_style_svgs()
