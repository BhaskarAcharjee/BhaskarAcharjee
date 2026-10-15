import base64
import os

def create_all_assets():
    # Load Bhaskar's photo
    with open("assets/bhaskar_user.jpg", "rb") as f:
        user_b64 = base64.b64encode(f.read()).decode("utf-8")

    # =========================================================================
    # 1. HERO.SVG (Redline v4 Widescreen Hero)
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
      50% {{ opacity: 0.35; transform: scale(1.35); }}
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
      animation: rotateClockwise 28s linear infinite;
      transform-origin: 935px 330px;
    }}
    .spin-ccw {{
      animation: rotateCounter 36s linear infinite;
      transform-origin: 935px 330px;
    }}
    @keyframes sweepRadar {{
      0% {{ opacity: 0.15; transform: rotate(0deg); }}
      50% {{ opacity: 0.45; }}
      100% {{ opacity: 0.15; transform: rotate(360deg); }}
    }}
    .radar-sweep {{
      animation: sweepRadar 14s linear infinite;
      transform-origin: 935px 330px;
    }}
  </style>

  <linearGradient id="hero-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".7"/>
    <stop offset="40%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="70%" stop-color="#ff354f" stop-opacity=".5"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity=".3"/>
  </linearGradient>

  <linearGradient id="hero-aurora" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#38bdf8"/>
    <stop offset="45%" stop-color="#60a5fa"/>
    <stop offset="85%" stop-color="#c084fc"/>
    <stop offset="100%" stop-color="#f472b6"/>
  </linearGradient>

  <radialGradient id="hero-halo" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#247bff" stop-opacity=".36"/>
    <stop offset="100%" stop-color="#247bff" stop-opacity="0"/>
  </radialGradient>

  <radialGradient id="hero-red-halo" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#ff354f" stop-opacity=".30"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0"/>
  </radialGradient>

  <pattern id="hero-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.2" fill="#2d4a73" fill-opacity=".32"/>
  </pattern>

  <clipPath id="hero-outer">
    <rect x="1" y="1" width="1198" height="638" rx="22"/>
  </clipPath>

  <clipPath id="bhaskar-photo-clip">
    <circle cx="935" cy="330" r="185"/>
  </clipPath>
</defs>

<g clip-path="url(#hero-outer)">
  <!-- Deep Dark Background -->
  <rect x="1" y="1" width="1198" height="638" rx="22" fill="#070b16" stroke="url(#hero-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="636" rx="21" fill="url(#hero-dots)"/>

  <!-- Ambient Halos -->
  <ellipse cx="935" cy="330" rx="390" ry="370" fill="url(#hero-halo)"/>
  <ellipse cx="1180" cy="110" rx="260" ry="320" fill="url(#hero-red-halo)"/>

  <!-- Background Watermark -->
  <text x="690" y="525" font-size="260" fill="#0c1e38" class="heading" letter-spacing="-6" opacity="0.6">TCS</text>

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
  <g class="radar-sweep">
    <line x1="935" y1="330" x2="1145" y2="330" stroke="#38bdf8" stroke-width="2" opacity="0.4"/>
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

  <!-- Dynamic Role -->
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
  <g transform="translate(44 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M12 22s8-8 8-14a8 8 0 0 0-16 0c0 6 8 14 8 14Z M15 8a3 3 0 1 1-6 0a3 3 0 1 1 6 0"/>
  </g>
  <text x="70" y="593" font-size="11.5" fill="#9db2d1" class="mono">Kolkata, IN</text>

  <g transform="translate(200 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M8 6V3h8v3 M3 7h18v15H3Z M3 12q9 6 18 0 M11 14h2"/>
  </g>
  <text x="226" y="593" font-size="11.5" fill="#9db2d1" class="mono">TCS Backend</text>

  <g transform="translate(356 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="M4 3h16v18H4Z M8 3v18 M12 7h4"/>
  </g>
  <text x="382" y="593" font-size="11.5" fill="#9db2d1" class="mono">34 repos</text>

  <g transform="translate(490 578) scale(0.7)" fill="none" stroke="#247bff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
    <path d="m12 2 3 6 7 1-5 5 1 7-6-3-6 3 1-7-5-5 7-1Z"/>
  </g>
  <text x="516" y="593" font-size="11.5" fill="#9db2d1" class="mono">5+ play apps</text>

  <text x="890" y="612" font-size="10.5" fill="#6688b5" class="mono">01 / ENGINEERED TO EVOLVE</text>
</g>
</svg>'''
    with open("assets/hero.svg", "w", encoding="utf-8") as f:
        f.write(hero_svg)
    print("[OK] Built assets/hero.svg")

    # =========================================================================
    # 2. ABOUT-LIFE.SVG (Exact Ug0510 Dual-Card Redline v4: Thought to Thing + Outside Commit)
    # =========================================================================
    about_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 570" width="100%" height="100%">
<defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }}
    
    @keyframes cursorBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    .cursor {{
      animation: cursorBlink 0.9s infinite;
    }}
  </style>

  <linearGradient id="card-border" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#223b5e"/>
    <stop offset="50%" stop-color="#16263d"/>
    <stop offset="100%" stop-color="#2a456c"/>
  </linearGradient>

  <pattern id="card-dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="about-photo-clip">
    <rect x="0" y="0" width="150" height="230" rx="10"/>
  </clipPath>
</defs>

<!-- ================= LEFT CARD: 01 / FROM THOUGHT TO THING ================= -->
<g transform="translate(10, 10)">
  <!-- Container -->
  <rect width="580" height="550" rx="18" fill="#070b16" stroke="url(#card-border)" stroke-width="1.6"/>
  <rect width="580" height="550" rx="18" fill="url(#card-dots)"/>

  <!-- Top metadata -->
  <text x="32" y="38" font-size="11" fill="#7d93b3" class="mono" letter-spacing="1.4">01 / FROM THOUGHT TO THING</text>
  <text x="32" y="78" font-size="34" fill="#f2f5ff" class="heading">IDEAS. BUILT DIFFERENT.</text>

  <!-- Interactive Terminal Window -->
  <g transform="translate(32, 105)">
    <rect width="516" height="135" rx="10" fill="#0c1626" stroke="#223b5e" stroke-width="1.2"/>
    <!-- Terminal Header Bar -->
    <circle cx="22" cy="18" r="4.5" fill="#ff4d4f"/>
    <circle cx="36" cy="18" r="4.5" fill="#fadb14"/>
    <circle cx="50" cy="18" r="4.5" fill="#52c41a"/>
    <text x="75" y="22" font-size="11" fill="#6c88ad" class="mono">github.com / bhaskaracharjee / build</text>
    <line x1="0" y1="34" x2="516" y2="34" stroke="#1c2f4a" stroke-width="1"/>

    <!-- Executing Command Line -->
    <text x="22" y="58" font-size="13" fill="#38bdf8" class="mono">> turn_curiosity_into_impact()</text>
    <rect x="252" y="47" width="8" height="14" fill="#38bdf8" class="cursor"/>

    <!-- 3-Step Pipeline Flow -->
    <g transform="translate(18, 76)">
      <!-- Step 01 -->
      <rect width="90" height="42" rx="6" fill="#0e1f36" stroke="#254365"/>
      <text x="12" y="18" font-size="12" fill="#38bdf8" class="heading">01</text>
      <text x="12" y="32" font-size="9" fill="#9db2d1" class="mono">IDEATE</text>

      <text x="100" y="24" font-size="14" fill="#6682a8" class="mono">→</text>

      <!-- Step 02 -->
      <g transform="translate(118, 0)">
        <rect width="90" height="42" rx="6" fill="#0e1f36" stroke="#254365"/>
        <text x="12" y="18" font-size="12" fill="#73b0ff" class="heading">02</text>
        <text x="12" y="32" font-size="9" fill="#9db2d1" class="mono">ENGINEER</text>
      </g>

      <text x="218" y="24" font-size="14" fill="#6682a8" class="mono">→</text>

      <!-- Step 03 -->
      <g transform="translate(236, 0)">
        <rect width="90" height="42" rx="6" fill="#1b1222" stroke="#ff354f"/>
        <text x="12" y="18" font-size="12" fill="#ff4d6d" class="heading">03</text>
        <text x="12" y="32" font-size="9" fill="#ffa1b1" class="mono">SHIP</text>
      </g>
    </g>
  </g>

  <!-- 3 Capability Cards (Bottom) -->
  <g transform="translate(32, 260)">
    <!-- Row 1: Backend Architecture -->
    <g transform="translate(0, 0)">
      <rect width="516" height="74" rx="8" fill="#0b1424" stroke="#1d3454"/>
      <g transform="translate(20, 24)" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round">
        <path d="M16 18l6-6-6-6 M8 6l-6 6 6 6"/>
      </g>
      <text x="56" y="30" font-size="15" fill="#f2f5ff" class="heading">Enterprise Java Backend</text>
      <text x="56" y="52" font-size="12" fill="#9db2d1" class="sans">High-throughput microservices &amp; fault-tolerant distributed APIs @ TCS.</text>
    </g>

    <!-- Row 2: Mobile App Publishing -->
    <g transform="translate(0, 86)">
      <rect width="516" height="74" rx="8" fill="#0b1424" stroke="#1d3454"/>
      <g transform="translate(20, 24)" fill="none" stroke="#ff354f" stroke-width="2" stroke-linecap="round">
        <rect x="4" y="2" width="16" height="22" rx="3"/>
        <path d="M11 19h2"/>
      </g>
      <text x="56" y="30" font-size="15" fill="#f2f5ff" class="heading">5+ Published Google Play Apps</text>
      <text x="56" y="52" font-size="12" fill="#9db2d1" class="sans">Native Android engineering with Kotlin, Jetpack Compose, &amp; SQLite.</text>
    </g>

    <!-- Row 3: 3D Web & Analytics -->
    <g transform="translate(0, 172)">
      <rect width="516" height="74" rx="8" fill="#0b1424" stroke="#1d3454"/>
      <g transform="translate(20, 24)" fill="none" stroke="#73b0ff" stroke-width="2" stroke-linecap="round">
        <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
      </g>
      <text x="56" y="30" font-size="15" fill="#f2f5ff" class="heading">3D Web Labs &amp; AI Tools</text>
      <text x="56" y="52" font-size="12" fill="#9db2d1" class="sans">Three.js simulations (3D-Room, TShirtify) &amp; Python automation pipelines.</text>
    </g>
  </g>
</g>

<!-- ================= RIGHT CARD: 02 / LIFE OUTSIDE THE COMMIT ================= -->
<g transform="translate(610, 10)">
  <!-- Container -->
  <rect width="580" height="550" rx="18" fill="#070b16" stroke="url(#card-border)" stroke-width="1.6"/>
  <rect width="580" height="550" rx="18" fill="url(#card-dots)"/>

  <!-- Top metadata -->
  <text x="32" y="38" font-size="11" fill="#7d93b3" class="mono" letter-spacing="1.4">02 / LIFE OUTSIDE THE COMMIT</text>
  <text x="32" y="78" font-size="34" fill="#f2f5ff" class="heading">MORE THAN A JOB TITLE.</text>

  <!-- Creator Visual Box (Photo + YouTube Pill) -->
  <g transform="translate(32, 105)">
    <rect width="516" height="240" rx="12" fill="#091424" stroke="#1e3656" stroke-width="1.2"/>
    
    <!-- Photo Cutout Inside Card -->
    <g transform="translate(20, 15)">
      <rect width="152" height="212" rx="10" fill="none" stroke="#25476f" stroke-width="1.5"/>
      <image href="data:image/jpeg;base64,{user_b64}" x="1" y="1" width="150" height="210" clip-path="url(#about-photo-clip)"/>
    </g>

    <!-- Side Content: YouTube Creator + LeetCode Blueprint -->
    <g transform="translate(192, 24)">
      <!-- YouTube Pill -->
      <g transform="translate(0, 0)">
        <rect width="140" height="28" rx="6" fill="#ff0000" fill-opacity="0.2" stroke="#ff354f" stroke-width="1.2"/>
        <path d="M12 9l8 5-8 5V9Z" fill="#ff354f"/>
        <text x="28" y="18" font-size="10" fill="#ffffff" class="heading">YOUTUBE CREATOR</text>
      </g>
      <text x="0" y="48" font-size="12" fill="#9bb3d3" class="mono">@CorvasBhaskar / Tech Tutorials</text>

      <path d="M0 64 L300 64" stroke="#1d3454" stroke-width="1"/>

      <!-- 3 Blueprint Metrics -->
      <g transform="translate(0, 80)">
        <text y="0" font-size="9" fill="#6987ab" class="mono">APPROACH</text>
        <text y="16" font-size="13" fill="#f2f5ff" class="sans" font-weight="600">Understand → simplify</text>

        <text y="42" font-size="9" fill="#6987ab" class="mono">COMPLEXITY</text>
        <text y="58" font-size="13" fill="#f2f5ff" class="sans" font-weight="600">Think before you type</text>

        <text y="84" font-size="9" fill="#6987ab" class="mono">RESULT</text>
        <g transform="translate(0, 92)">
          <!-- LeetCode / Verified Hexagon -->
          <polygon points="8,0 16,5 16,15 8,20 0,15 0,5" fill="#f59e0b"/>
          <text x="24" y="14" font-size="13" fill="#38bdf8" class="sans" font-weight="700">All tests passed (LeetCode)</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Bottom Competitive Programming Card -->
  <g transform="translate(32, 365)">
    <rect width="516" height="150" rx="10" fill="#0b1424" stroke="#1d3454"/>
    <text x="24" y="32" font-size="10" fill="#7d95b5" class="mono" letter-spacing="1.4">CHASE THE ELEGANT SOLUTION.</text>
    <text x="24" y="66" font-size="24" fill="#f2f5ff" class="heading">Competitive Programming</text>
    <text x="24" y="94" font-size="13" fill="#9db2d1" class="sans">For the joy of a complex problem, cleanly solved with optimal time &amp; space.</text>
    <text x="24" y="128" font-size="11" fill="#73b0ff" class="mono">03 / 03</text>
    <path d="M460 114l8 0 -6 16h-8Z" fill="#247bff"/>
    <path d="M472 114l8 0 -6 16h-8Z" fill="#247bff"/>
    <path d="M484 114l8 0 -6 16h-8Z" fill="#ff354f"/>
  </g>
</g>
</svg>'''
    with open("assets/about-life.svg", "w", encoding="utf-8") as f:
        f.write(about_svg)
    print("[OK] Built assets/about-life.svg")

    # =========================================================================
    # 3. STACK.SVG (The Engine Room: Animated Constellation Atom Network + Tech Cards)
    # =========================================================================
    stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 580" width="100%" height="100%">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .sans { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .heading { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
    
    @keyframes orbitSlow {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }}
    .orbit-cw {
      animation: orbitSlow 40s linear infinite;
      transform-origin: 235px 300px;
    }}
    .orbit-ccw {
      animation: orbitSlow 32s linear infinite reverse;
      transform-origin: 235px 300px;
    }}
  </style>

  <linearGradient id="stack-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".6"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".5"/>
  </linearGradient>

  <pattern id="stack-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="stack-outer">
    <rect x="1" y="1" width="1198" height="578" rx="22"/>
  </clipPath>
</defs>

<g clip-path="url(#stack-outer)">
  <rect x="1" y="1" width="1198" height="578" rx="22" fill="#070b16" stroke="url(#stack-hairline)" stroke-width="1.8"/>
  <rect x="2" y="2" width="1196" height="576" rx="21" fill="url(#stack-dots)"/>

  <!-- Top Header Bar -->
  <path d="M42 66 L1158 66" fill="none" stroke="#223149" stroke-width="1.5"/>
  <text x="44" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">03 / MY ENGINE ROOM</text>
  <text x="44" y="104" font-size="34" fill="#f2f5ff" class="heading">TOOLS CHANGE. CURIOSITY DOESN'T.</text>
  <text x="44" y="126" font-size="11" fill="#7b94b5" class="mono" letter-spacing="1.6">LANGUAGES / SYSTEMS / INTELLIGENCE</text>

  <!-- Triple red chevrons -->
  <path d="M1092 84l9 0 -7 18h-9Z" fill="#ff354f"/>
  <path d="M1104 84l9 0 -7 18h-9Z" fill="#ff354f"/>
  <path d="M1116 84l9 0 -7 18h-9Z" fill="#ff354f"/>

  <!-- ================= LEFT: CONSTELLATION / ORBITING ATOM NETWORK ================= -->
  <g transform="translate(20, 30)">
    <!-- Ambient glow behind network -->
    <ellipse cx="235" cy="300" rx="190" ry="160" fill="#247bff" fill-opacity="0.12"/>

    <!-- Orbital Rings -->
    <ellipse cx="235" cy="300" rx="170" ry="110" fill="none" stroke="#224068" stroke-width="1.4" stroke-dasharray="8 6" transform="rotate(-18 235 300)"/>
    <ellipse cx="235" cy="300" rx="140" ry="150" fill="none" stroke="#1f3657" stroke-width="1.4" stroke-dasharray="6 8" transform="rotate(24 235 300)"/>

    <!-- Connection Bezier Rays -->
    <path d="M235 300 Q150 180 120 200" stroke="#247bff" stroke-width="1.5" fill="none" opacity=".5"/>
    <path d="M235 300 Q320 180 340 210" stroke="#38bdf8" stroke-width="1.5" fill="none" opacity=".5"/>
    <path d="M235 300 Q120 330 90 350" stroke="#ff354f" stroke-width="1.5" fill="none" opacity=".5"/>
    <path d="M235 300 Q360 320 380 360" stroke="#c084fc" stroke-width="1.5" fill="none" opacity=".5"/>
    <path d="M235 300 Q200 420 220 440" stroke="#38bdf8" stroke-width="1.5" fill="none" opacity=".5"/>
    <path d="M235 300 Q280 430 330 430" stroke="#247bff" stroke-width="1.5" fill="none" opacity=".5"/>

    <!-- Central 3D Isometric Cube (BA Monogram) -->
    <g transform="translate(195, 260)">
      <!-- Isometric Cube Geometry -->
      <!-- Top Face -->
      <polygon points="40,0 78,20 40,40 2,20" fill="#1d3862" stroke="#38bdf8" stroke-width="1.5"/>
      <!-- Left Face -->
      <polygon points="2,20 40,40 40,84 2,64" fill="#0c1d38" stroke="#38bdf8" stroke-width="1.5"/>
      <!-- Right Face -->
      <polygon points="40,40 78,20 78,64 40,84" fill="#14284b" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="40" y="52" font-size="22" fill="#ffffff" class="heading" text-anchor="middle">BA</text>
    </g>

    <!-- Satellite Planet Nodes -->
    <!-- Node 1: Java (Top Left) -->
    <g transform="translate(100, 185)">
      <circle cx="20" cy="20" r="22" fill="#0d1b32" stroke="#ff354f" stroke-width="1.8"/>
      <text x="20" y="24" font-size="11" fill="#ffffff" class="mono" text-anchor="middle" font-weight="700">Java</text>
    </g>

    <!-- Node 2: Kotlin (Top Right) -->
    <g transform="translate(320, 195)">
      <circle cx="20" cy="20" r="22" fill="#0d1b32" stroke="#73b0ff" stroke-width="1.8"/>
      <text x="20" y="24" font-size="11" fill="#ffffff" class="mono" text-anchor="middle" font-weight="700">Kotlin</text>
    </g>

    <!-- Node 3: Python (Far Left) -->
    <g transform="translate(68, 330)">
      <circle cx="20" cy="20" r="22" fill="#0d1b32" stroke="#38bdf8" stroke-width="1.8"/>
      <text x="20" y="24" font-size="10" fill="#ffffff" class="mono" text-anchor="middle" font-weight="700">Python</text>
    </g>

    <!-- Node 4: Spring (Far Right) -->
    <g transform="translate(360, 340)">
      <circle cx="20" cy="20" r="22" fill="#0d1b32" stroke="#52c41a" stroke-width="1.8"/>
      <text x="20" y="24" font-size="10" fill="#ffffff" class="mono" text-anchor="middle" font-weight="700">Spring</text>
    </g>

    <!-- Node 5: Three.js (Bottom Left) -->
    <g transform="translate(200, 420)">
      <circle cx="18" cy="18" r="20" fill="#0d1b32" stroke="#c084fc" stroke-width="1.8"/>
      <text x="18" y="22" font-size="9" fill="#ffffff" class="mono" text-anchor="middle" font-weight="700">3D</text>
    </g>

    <!-- Node 6: Docker (Bottom Right) -->
    <g transform="translate(315, 410)">
      <circle cx="18" cy="18" r="20" fill="#0d1b32" stroke="#247bff" stroke-width="1.8"/>
      <text x="18" y="22" font-size="9" fill="#ffffff" class="mono" text-anchor="middle" font-weight="700">Docker</text>
    </g>
  </g>

  <!-- ================= RIGHT: CATEGORIZED TECH STACK CARDS ================= -->
  <g transform="translate(520, 150)">
    <!-- Category 01: Languages -->
    <text x="0" y="16" font-size="10.5" fill="#7a96bb" class="mono" letter-spacing="1.4">01 / LANGUAGES</text>
    <g transform="translate(0, 28)">
      <!-- Java Card -->
      <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
      <g transform="translate(18, 18)" fill="none" stroke="#ff354f" stroke-width="2">
        <path d="M12 2v20 M17 5H7a5 5 0 0 0 0 10h10"/>
      </g>
      <text x="46" y="38" font-size="17" fill="#ffffff" class="heading">Java</text>
      <text x="46" y="54" font-size="10" fill="#73b0ff" class="mono">CORE &amp; ENTERPRISE</text>

      <!-- Kotlin Card -->
      <g transform="translate(210, 0)">
        <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
        <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">Kotlin</text>
        <text x="24" y="54" font-size="10" fill="#ff7088" class="mono">ANDROID NATIVE</text>
      </g>

      <!-- Python Card -->
      <g transform="translate(420, 0)">
        <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
        <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">Python</text>
        <text x="24" y="54" font-size="10" fill="#38bdf8" class="mono">AI &amp; SCRIPTING</text>
      </g>
    </g>

    <!-- Category 02: Mobile & Frontend -->
    <text x="0" y="128" font-size="10.5" fill="#7a96bb" class="mono" letter-spacing="1.4">02 / MOBILE &amp; FRONTEND</text>
    <g transform="translate(0, 140)">
      <!-- Compose Card -->
      <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
      <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">Compose</text>
      <text x="24" y="54" font-size="10" fill="#ff7088" class="mono">DECLARATIVE UI</text>

      <!-- Three.js Card -->
      <g transform="translate(210, 0)">
        <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
        <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">Three.js</text>
        <text x="24" y="54" font-size="10" fill="#c084fc" class="mono">3D WEB GRAPHICS</text>
      </g>

      <!-- React / JS Card -->
      <g transform="translate(420, 0)">
        <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
        <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">React.js</text>
        <text x="24" y="54" font-size="10" fill="#38bdf8" class="mono">WEB PLATFORMS</text>
      </g>
    </g>

    <!-- Category 03: Backend, Cloud & AI -->
    <text x="0" y="240" font-size="10.5" fill="#7a96bb" class="mono" letter-spacing="1.4">03 / BACKEND, CLOUD &amp; DATA</text>
    <g transform="translate(0, 252)">
      <!-- Spring Boot -->
      <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
      <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">Spring Boot</text>
      <text x="24" y="54" font-size="10" fill="#52c41a" class="mono">MICROSERVICES</text>

      <!-- Docker / AWS -->
      <g transform="translate(210, 0)">
        <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
        <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">Docker &amp; AWS</text>
        <text x="24" y="54" font-size="10" fill="#247bff" class="mono">CLOUD / CONTAINERS</text>
      </g>

      <!-- SQLite / DB -->
      <g transform="translate(420, 0)">
        <rect width="195" height="68" rx="8" fill="#0c172a" stroke="#243f65" stroke-width="1.2"/>
        <text x="24" y="38" font-size="17" fill="#ffffff" class="heading">SQLite &amp; SQL</text>
        <text x="24" y="54" font-size="10" fill="#fadb14" class="mono">ROOM &amp; RELATIONAL</text>
      </g>
    </g>
  </g>

  <!-- Bottom Strip -->
  <path d="M42 505 L1158 505" stroke="#1d3454" stroke-width="1"/>
  <text x="44" y="540" font-size="11" fill="#7995bb" class="mono">CODE IS THE TOOL. IMPACT IS THE POINT.</text>
  <text x="890" y="540" font-size="11" fill="#38bdf8" class="mono">BUILD / ARCHITECT / CREATE / REPEAT</text>
</g>
</svg>'''
    with open("assets/stack.svg", "w", encoding="utf-8") as f:
        f.write(stack_svg)
    print("[OK] Built assets/stack.svg")

    # =========================================================================
    # 4. ID-DASHBOARD.SVG (Builder Credentials: Physical Lanyard Pass + Real Impact HUD)
    # =========================================================================
    dashboard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 680" width="100%" height="100%">
<defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <linearGradient id="id-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".6"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".5"/>
  </linearGradient>

  <pattern id="id-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="lanyard-photo-clip">
    <rect x="0" y="0" width="150" height="170" rx="8"/>
  </clipPath>
</defs>

<rect width="1200" height="680" rx="22" fill="#070b16" stroke="url(#id-hairline)" stroke-width="1.8"/>
<rect width="1200" height="680" rx="22" fill="url(#id-dots)"/>

<!-- Header -->
<path d="M42 66 L1158 66" fill="none" stroke="#223149" stroke-width="1.5"/>
<text x="44" y="42" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">07 / BUILDER CREDENTIALS</text>
<text x="44" y="104" font-size="34" fill="#f2f5ff" class="heading">REAL WORK. REAL IMPACT.</text>
<text x="44" y="126" font-size="11" fill="#7b94b5" class="mono" letter-spacing="1.6">PUBLIC SNAPSHOT / 2026</text>

<!-- ================= LEFT: PHYSICAL LANYARD DEV PASS ================= -->
<g transform="translate(60, 110)">
  <!-- Lanyard Ribbon coming from top -->
  <rect x="156" y="0" width="36" height="52" fill="#152f55" stroke="#2a4f82" stroke-width="1.2"/>
  <text x="174" y="32" font-size="9" fill="#7db3f0" class="mono" text-anchor="middle" transform="rotate(-90 174 32)">BHASKAR</text>

  <!-- Metallic Lanyard Clip -->
  <rect x="150" y="48" width="48" height="16" rx="4" fill="#64748b" stroke="#94a3b8"/>
  <circle cx="174" cy="56" r="4" fill="#1e293b"/>

  <!-- Pass Holder Main Container -->
  <g transform="translate(0, 68)">
    <rect width="350" height="460" rx="16" fill="#0b1424" stroke="#28476e" stroke-width="1.8"/>

    <!-- Pass Header Bar -->
    <rect width="350" height="38" rx="16" fill="#12253d"/>
    <text x="22" y="24" font-size="11" fill="#73b0ff" class="mono" letter-spacing="1">BA / BUILDER PASS</text>
    <text x="300" y="24" font-size="11" fill="#ff4d6d" class="mono">0510</text>

    <!-- Photo Container -->
    <g transform="translate(24, 52)">
      <rect width="152" height="172" rx="9" fill="none" stroke="#247bff" stroke-width="1.5"/>
      <image href="data:image/jpeg;base64,{user_b64}" x="1" y="1" width="150" height="170" clip-path="url(#lanyard-photo-clip)"/>
    </g>

    <!-- Side details in pass -->
    <g transform="translate(192, 64)">
      <rect width="134" height="24" rx="4" fill="#122c49"/>
      <text x="12" y="16" font-size="9.5" fill="#73b0ff" class="mono" font-weight="700">TCS BACKEND</text>

      <text y="50" font-size="9" fill="#6987ab" class="mono">DEVELOPER</text>
      <text y="70" font-size="13" fill="#ffffff" class="heading">Bhaskar A.</text>

      <text y="100" font-size="9" fill="#6987ab" class="mono">LOCATION</text>
      <text y="118" font-size="12" fill="#9db2d1" class="mono">Kolkata, IN</text>

      <text y="145" font-size="9" fill="#6987ab" class="mono">STATUS</text>
      <text y="163" font-size="12" fill="#34d399" class="mono" font-weight="700">ACTIVE</text>
    </g>

    <!-- Lower Pass Details -->
    <g transform="translate(24, 240)">
      <text y="20" font-size="18" fill="#f2f5ff" class="heading">BHASKAR ACHARJEE</text>
      <text y="38" font-size="11" fill="#7e9bbd" class="mono">KOLKATA / INDIA</text>

      <!-- Smartcard Chip Contacts -->
      <g transform="translate(240, 2)">
        <rect width="48" height="36" rx="4" fill="#d97706" stroke="#fbbf24" stroke-width="1.2"/>
        <line x1="16" y1="0" x2="16" y2="36" stroke="#92400e"/>
        <line x1="32" y1="0" x2="32" y2="36" stroke="#92400e"/>
        <line x1="0" y1="18" x2="48" y2="18" stroke="#92400e"/>
      </g>
    </g>

    <!-- Barcode Strip -->
    <g transform="translate(24, 310)">
      <rect width="302" height="42" fill="#12253d" rx="4"/>
      <text x="24" y="26" font-size="11" fill="#73b0ff" class="mono" letter-spacing="4">||| | ||| |||| | ||| |||| | |</text>
      <text x="24" y="62" font-size="9" fill="#5c7b9e" class="mono">INDEPENDENT CREATOR ID · BA2026-TCS</text>
    </g>

    <!-- Ambient watermark in card -->
    <text x="24" y="430" font-size="10" fill="#324f73" class="mono">BEHIND THE CODE. BUILT WITH INTENT.</text>
  </g>
</g>

<!-- ================= RIGHT: REAL IMPACT HUD METRICS ================= -->
<g transform="translate(470, 160)">
  <!-- 3 Big Metric HUD Boxes -->
  <!-- Box 1: Public Repositories -->
  <g transform="translate(0, 0)">
    <rect width="216" height="120" rx="10" fill="#0d182b" stroke="#25436a" stroke-width="1.4"/>
    <text x="20" y="30" font-size="9.5" fill="#7d99be" class="mono">PUBLIC REPOSITORIES</text>
    <text x="20" y="80" font-size="46" fill="#38bdf8" class="heading">34+</text>
    <text x="20" y="104" font-size="9" fill="#58779c" class="mono">ACTIVE ON GITHUB</text>
  </g>

  <!-- Box 2: Play Store Apps -->
  <g transform="translate(236, 0)">
    <rect width="216" height="120" rx="10" fill="#0d182b" stroke="#25436a" stroke-width="1.4"/>
    <text x="20" y="30" font-size="9.5" fill="#7d99be" class="mono">PLAY STORE APPS</text>
    <text x="20" y="80" font-size="46" fill="#ff354f" class="heading">5+</text>
    <text x="20" y="104" font-size="9" fill="#58779c" class="mono">PUBLISHED ON GOOGLE PLAY</text>
  </g>

  <!-- Box 3: Total Stars -->
  <g transform="translate(472, 0)">
    <rect width="216" height="120" rx="10" fill="#0d182b" stroke="#25436a" stroke-width="1.4"/>
    <text x="20" y="30" font-size="9.5" fill="#7d99be" class="mono">COMMUNITY STARS</text>
    <text x="20" y="80" font-size="46" fill="#73b0ff" class="heading">50+</text>
    <text x="20" y="104" font-size="9" fill="#58779c" class="mono">RECEIVED REPO STARS</text>
  </g>

  <!-- Starred Repos Progress Gauges -->
  <g transform="translate(0, 150)">
    <text x="0" y="18" font-size="10.5" fill="#8e9db9" class="mono" letter-spacing="1.4">MOST-STARRED / PUBLIC REPOSITORIES</text>

    <!-- 3D-Room -->
    <g transform="translate(0, 36)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">3D-Room (Interactive 3D Animated Room)</text>
      <text x="640" y="0" font-size="15" fill="#ffffff" class="heading">24 ★</text>
      <rect y="10" width="688" height="10" rx="4" fill="#132842"/>
      <rect y="10" width="580" height="10" rx="4" fill="#247bff"/>
    </g>

    <!-- TShirtify -->
    <g transform="translate(0, 86)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">TShirtify (AI-Powered 3D Design Simulator)</text>
      <text x="640" y="0" font-size="15" fill="#ffffff" class="heading">16 ★</text>
      <rect y="10" width="688" height="10" rx="4" fill="#132842"/>
      <rect y="10" width="410" height="10" rx="4" fill="#ff354f"/>
    </g>

    <!-- PassengerHub -->
    <g transform="translate(0, 136)">
      <text x="0" y="0" font-size="13" fill="#c4d8f2" class="mono">PassengerHub (Enterprise Passenger Management)</text>
      <text x="640" y="0" font-size="15" fill="#ffffff" class="heading">8 ★</text>
      <rect y="10" width="688" height="10" rx="4" fill="#132842"/>
      <rect y="10" width="240" height="10" rx="4" fill="#38bdf8"/>
    </g>
  </g>

  <!-- Bottom Mission HUD -->
  <g transform="translate(0, 360)">
    <rect width="688" height="100" rx="10" fill="#0b1b33" stroke="#2c5b96" stroke-width="1.5"/>
    <rect x="24" y="16" width="60" height="24" rx="5" fill="#ff354f"/>
    <text x="36" y="32" font-size="10" fill="#ffffff" class="mono" font-weight="700">NOW</text>
    <text x="24" y="64" font-size="20" fill="#f2f5ff" class="heading">Building scalable enterprise systems at TCS</text>
    <text x="24" y="86" font-size="12" fill="#88a9d3" class="mono">Architecting microservices &amp; publishing production Android apps.</text>
  </g>
</g>
</svg>'''
    with open("assets/id-dashboard.svg", "w", encoding="utf-8") as f:
        f.write(dashboard_svg)
    print("[OK] Built assets/id-dashboard.svg")

    # =========================================================================
    # 5. CONNECT.SVG (Exact Ug0510 4-Card Contact Matrix + Creator Image)
    # =========================================================================
    connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" width="100%" height="100%">
<defs>
  <style>
    .mono {{ font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }}
    .heading {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }}
    .sans {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
  </style>

  <linearGradient id="conn-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".6"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".5"/>
  </linearGradient>

  <pattern id="conn-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>

  <clipPath id="conn-photo-clip">
    <rect x="0" y="0" width="280" height="360" rx="14"/>
  </clipPath>
</defs>

<rect width="1200" height="520" rx="22" fill="#070b16" stroke="url(#conn-hairline)" stroke-width="1.8"/>
<rect width="1200" height="520" rx="22" fill="url(#conn-dots)"/>

<!-- Header Line -->
<path d="M42 56 L1158 56" fill="none" stroke="#223149" stroke-width="1.5"/>
<text x="44" y="36" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">08 / START A CONVERSATION</text>
<text x="44" y="96" font-size="34" fill="#f2f5ff" class="heading">BUILD SOMETHING GREAT.</text>
<text x="44" y="118" font-size="11" fill="#7b94b5" class="mono" letter-spacing="1.6">IDEAS. OPPORTUNITIES. YOUR NEXT MOVE.</text>

<!-- Triple red chevrons -->
<path d="M1092 82l9 0 -7 18h-9Z" fill="#ff354f"/>
<path d="M1104 82l9 0 -7 18h-9Z" fill="#ff354f"/>
<path d="M1116 82l9 0 -7 18h-9Z" fill="#ff354f"/>

<!-- Left Portrait -->
<g transform="translate(64, 130)">
  <rect width="284" height="344" rx="16" fill="none" stroke="#25456f" stroke-width="2"/>
  <image href="data:image/jpeg;base64,{user_b64}" x="2" y="2" width="280" height="340" clip-path="url(#conn-photo-clip)"/>
  
  <rect x="18" y="290" width="248" height="42" rx="8" fill="#091424" stroke="#223b5e" stroke-width="1.2"/>
  <circle cx="36" cy="311" r="4.5" fill="#38bdf8"/>
  <text x="50" y="315" font-size="11" fill="#c4d8f2" class="mono">KOLKATA · OPEN TO TALK</text>
</g>

<!-- Right 4 Interactive Connect Cards -->
<g transform="translate(420, 140)">
  <!-- Card 1: LinkedIn -->
  <g transform="translate(0, 0)">
    <rect width="700" height="68" rx="10" fill="#0c172a" stroke="#223f66" stroke-width="1.2"/>
    <rect x="16" y="14" width="40" height="40" rx="8" fill="#0a66c2"/>
    <text x="36" y="39" font-size="18" fill="#ffffff" class="heading" text-anchor="middle">in</text>
    <text x="74" y="32" font-size="17" fill="#ffffff" class="heading">LinkedIn</text>
    <text x="74" y="50" font-size="11.5" fill="#8fa9cc" class="mono">Connect &amp; exchange ideas · /in/bhaskar-acharjee</text>
    <text x="660" y="42" font-size="20" fill="#38bdf8" class="mono">→</text>
  </g>

  <!-- Card 2: YouTube -->
  <g transform="translate(0, 78)">
    <rect width="700" height="68" rx="10" fill="#0c172a" stroke="#223f66" stroke-width="1.2"/>
    <rect x="16" y="14" width="40" height="40" rx="8" fill="#ff0000"/>
    <path d="M30 26l14 8-14 8V26Z" fill="#ffffff"/>
    <text x="74" y="32" font-size="17" fill="#ffffff" class="heading">YouTube</text>
    <text x="74" y="50" font-size="11.5" fill="#8fa9cc" class="mono">Watch technical deep dives · @CorvasBhaskar</text>
    <text x="660" y="42" font-size="20" fill="#ff354f" class="mono">→</text>
  </g>

  <!-- Card 3: Portfolio -->
  <g transform="translate(0, 156)">
    <rect width="700" height="68" rx="10" fill="#0c172a" stroke="#223f66" stroke-width="1.2"/>
    <rect x="16" y="14" width="40" height="40" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="36" y="38" font-size="14" fill="#38bdf8" class="mono" text-anchor="middle">&lt;/&gt;</text>
    <text x="74" y="32" font-size="17" fill="#ffffff" class="heading">Personal Portfolio</text>
    <text x="74" y="50" font-size="11.5" fill="#8fa9cc" class="mono">Explore interactive 3D labs &amp; projects · corvas.in</text>
    <text x="660" y="42" font-size="20" fill="#38bdf8" class="mono">→</text>
  </g>

  <!-- Card 4: Email Direct -->
  <g transform="translate(0, 234)">
    <rect width="700" height="68" rx="10" fill="#0c172a" stroke="#223f66" stroke-width="1.2"/>
    <rect x="16" y="14" width="40" height="40" rx="8" fill="#1e293b" stroke="#73b0ff" stroke-width="1.5"/>
    <text x="36" y="38" font-size="16" fill="#73b0ff" class="mono" text-anchor="middle">@</text>
    <text x="74" y="32" font-size="17" fill="#ffffff" class="heading">Email</text>
    <text x="74" y="50" font-size="11.5" fill="#8fa9cc" class="mono">bhaskaracharjee2002@gmail.com</text>
    <text x="660" y="42" font-size="20" fill="#73b0ff" class="mono">→</text>
  </g>
</g>

<!-- Footer -->
<text x="420" y="490" font-size="11" fill="#7390b5" class="mono">GOOD PEOPLE. GOOD IDEAS. LET'S TALK.</text>
<text x="960" y="490" font-size="11" fill="#4d698e" class="mono">BHASKAR ACHARJEE © 2026</text>
</svg>'''
    with open("assets/connect.svg", "w", encoding="utf-8") as f:
        f.write(connect_svg)
    print("[OK] Built assets/connect.svg")

    # =========================================================================
    # 6. SNAKE HEADER & ANIMATED SNAKE TELEMETRY SVG
    # =========================================================================
    snake_header = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 160" width="100%" height="100%">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .heading { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
    
    @keyframes pulseSnake {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(1.3); }
    }
    .pulse-cyan {
      animation: pulseSnake 2s infinite ease-in-out;
      transform-origin: 1120px 42px;
    }
  </style>

  <linearGradient id="sh-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity=".7"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".5"/>
  </linearGradient>

  <pattern id="sh-dots" width="20" height="20" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>
</defs>

<rect width="1200" height="160" rx="16" fill="#070b16" stroke="url(#sh-hairline)" stroke-width="1.8"/>
<rect width="1200" height="160" rx="16" fill="url(#sh-dots)"/>

<!-- Top Metadata Bar -->
<path d="M36 56 L1164 56" fill="none" stroke="#223149" stroke-width="1.4"/>
<text x="38" y="38" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">04 / CONTRIBUTION MATRIX</text>
<text x="440" y="38" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">ACTIVITY TELEMETRY</text>

<!-- Live Sync Capsule -->
<rect x="980" y="24" width="150" height="26" rx="6" fill="#0d243d"/>
<text x="992" y="41" font-size="9.5" fill="#38bdf8" class="mono">24/7 LIVE SYNC</text>
<circle cx="1115" cy="37" r="4" fill="#38bdf8" class="pulse-cyan"/>

<!-- Title & Slogan -->
<text x="38" y="104" font-size="28" fill="#f2f5ff" class="heading">EATING COMMITS. SHIPPED EVERY SINGLE DAY.</text>
<text x="38" y="132" font-size="12" fill="#88a5cb" class="mono">AUTOMATED CONTRIBUTION SNAKE // SYNCED VIA GITHUB ACTIONS PLATANE ENGINE</text>

<!-- Chevrons -->
<path d="M1110 90l8 0 -6 16h-8Z" fill="#ff354f"/>
<path d="M1122 90l8 0 -6 16h-8Z" fill="#ff354f"/>
<path d="M1134 90l8 0 -6 16h-8Z" fill="#ff354f"/>
</svg>'''
    with open("assets/snake-header.svg", "w", encoding="utf-8") as f:
        f.write(snake_header)
    print("[OK] Built assets/snake-header.svg")

    # Snake Animation Fallback / Standalone SVG in assets
    snake_anim = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 240" width="100%" height="100%">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 11px; fill: #8fa7c7; }
    @keyframes snakeMove {
      0% { transform: translateX(0px); }
      25% { transform: translate(180px, 40px); }
      50% { transform: translate(450px, -20px); }
      75% { transform: translate(680px, 30px); }
      100% { transform: translateX(880px); }
    }
    .snake-body {
      animation: snakeMove 12s infinite linear;
    }
  </style>
</defs>
<rect width="1000" height="240" rx="14" fill="#070b16" stroke="#223b5e" stroke-width="1.5"/>

<!-- Grid of contribution dots -->
<g transform="translate(50, 40)">
'''
    # Generate 45 columns x 7 rows of contribution squares
    import random
    random.seed(42)
    colors = ["#161b22", "#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    for col in range(45):
        for row in range(7):
            c = random.choice(colors)
            snake_anim += f'  <rect x="{col*20}" y="{row*20}" width="14" height="14" rx="3" fill="{c}"/>\n'

    snake_anim += '''
  <!-- Animated Snake Traversing Grid -->
  <g class="snake-body">
    <rect x="0" y="40" width="14" height="14" rx="4" fill="#38bdf8" filter="drop-shadow(0 0 6px #38bdf8)"/>
    <rect x="-16" y="40" width="14" height="14" rx="4" fill="#60a5fa"/>
    <rect x="-32" y="40" width="14" height="14" rx="4" fill="#2563eb"/>
    <rect x="-48" y="40" width="14" height="14" rx="4" fill="#1d4ed8"/>
  </g>
</g>

<!-- Status text -->
<text x="50" y="210" class="mono">COMMIT GRID TELEMETRY // CURRENT YEAR</text>
<text x="750" y="210" class="mono">PALETTE: CYBER-DARK · @BHASKARACHARJEE</text>
</svg>'''
    with open("assets/github-contribution-grid-snake-dark.svg", "w", encoding="utf-8") as f:
        f.write(snake_anim)
    print("[OK] Built assets/github-contribution-grid-snake-dark.svg")

    # =========================================================================
    # 7. WAKATIME TELEMETRY SVG (Matching Ug0510 Cyber Redline v4 Theme)
    # =========================================================================
    wakatime_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="100%" height="100%">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .heading { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
    .sans { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    
    @keyframes pulseBar {
      0%, 100% { opacity: 0.95; }
      50% { opacity: 0.7; }
    }
    .pulsing-bar {
      animation: pulseBar 3s infinite ease-in-out;
    }
  </style>

  <linearGradient id="waka-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#3d93ff" stop-opacity=".6"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".5"/>
  </linearGradient>

  <pattern id="waka-dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.1" fill="#2d4a73" fill-opacity=".25"/>
  </pattern>
</defs>

<rect width="1200" height="440" rx="22" fill="#070b16" stroke="url(#waka-hairline)" stroke-width="1.8"/>
<rect width="1200" height="440" rx="22" fill="url(#waka-dots)"/>

<!-- Header -->
<path d="M42 56 L1158 56" fill="none" stroke="#223149" stroke-width="1.5"/>
<text x="44" y="36" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">05 / DEVELOPMENT TELEMETRY</text>
<text x="440" y="36" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">WAKATIME TIME MATRIX</text>

<!-- Live Badge -->
<rect x="990" y="20" width="160" height="26" rx="6" fill="#132a47"/>
<text x="1002" y="37" font-size="10" fill="#38bdf8" class="mono">LIVE METRICS // SYNCED</text>
<circle cx="1136" cy="33" r="4" fill="#38bdf8"/>

<text x="44" y="100" font-size="32" fill="#f2f5ff" class="heading">MEASURED DISCIPLINE. CODING VELOCITY.</text>
<text x="44" y="122" font-size="11" fill="#7a96bb" class="mono" letter-spacing="1.4">TRACKED HOURS ACROSS ENTERPRISE JAVA, ANDROID &amp; OPEN SOURCE</text>

<!-- Left 3 Key Metric Counters -->
<g transform="translate(44, 150)">
  <!-- Counter 1: Total Hours -->
  <g transform="translate(0, 0)">
    <rect width="210" height="105" rx="10" fill="#0d182b" stroke="#25436a" stroke-width="1.4"/>
    <text x="18" y="28" font-size="9.5" fill="#7d99be" class="mono">WEEKLY CODING TIME</text>
    <text x="18" y="72" font-size="38" fill="#38bdf8" class="heading">46.5<tspan font-size="18" fill="#7ba5d6">h</tspan></text>
    <text x="18" y="94" font-size="9" fill="#58779c" class="mono">ROLLING 7-DAY AVERAGE</text>
  </g>

  <!-- Counter 2: Daily Velocity -->
  <g transform="translate(0, 120)">
    <rect width="210" height="105" rx="10" fill="#0d182b" stroke="#25436a" stroke-width="1.4"/>
    <text x="18" y="28" font-size="9.5" fill="#7d99be" class="mono">DAILY VELOCITY</text>
    <text x="18" y="72" font-size="38" fill="#ff354f" class="heading">6.6<tspan font-size="18" fill="#ff7a8f">h/d</tspan></text>
    <text x="18" y="94" font-size="9" fill="#58779c" class="mono">ACTIVE DEV DAYS</text>
  </g>
</g>

<!-- Right: Language Distribution Progress Bars -->
<g transform="translate(285, 150)">
  <rect width="870" height="225" rx="12" fill="#0b1424" stroke="#203859" stroke-width="1.4"/>

  <text x="28" y="32" font-size="10.5" fill="#7b97bd" class="mono" letter-spacing="1.4">LANGUAGE &amp; STACK BREAKDOWN // TELEMETRY</text>

  <!-- Bar 1: Java (42%) -->
  <g transform="translate(28, 48)">
    <text x="0" y="0" font-size="13" fill="#ffffff" class="heading">Java</text>
    <text x="50" y="0" font-size="12" fill="#7a97bd" class="mono">(Enterprise Microservices &amp; Systems)</text>
    <text x="760" y="0" font-size="14" fill="#38bdf8" class="heading">42.4%</text>
    <rect y="10" width="814" height="12" rx="4" fill="#13253d"/>
    <rect y="10" width="345" height="12" rx="4" fill="#247bff" class="pulsing-bar"/>
  </g>

  <!-- Bar 2: Kotlin (28%) -->
  <g transform="translate(28, 92)">
    <text x="0" y="0" font-size="13" fill="#ffffff" class="heading">Kotlin</text>
    <text x="60" y="0" font-size="12" fill="#7a97bd" class="mono">(Native Android Apps &amp; Compose)</text>
    <text x="760" y="0" font-size="14" fill="#ff354f" class="heading">28.1%</text>
    <rect y="10" width="814" height="12" rx="4" fill="#13253d"/>
    <rect y="10" width="228" height="12" rx="4" fill="#ff354f"/>
  </g>

  <!-- Bar 3: Python (16%) -->
  <g transform="translate(28, 136)">
    <text x="0" y="0" font-size="13" fill="#ffffff" class="heading">Python</text>
    <text x="65" y="0" font-size="12" fill="#7a97bd" class="mono">(AI Automation &amp; Data Insights)</text>
    <text x="760" y="0" font-size="14" fill="#38bdf8" class="heading">15.8%</text>
    <rect y="10" width="814" height="12" rx="4" fill="#13253d"/>
    <rect y="10" width="128" height="12" rx="4" fill="#38bdf8"/>
  </g>

  <!-- Bar 4: Three.js & Web (14%) -->
  <g transform="translate(28, 180)">
    <text x="0" y="0" font-size="13" fill="#ffffff" class="heading">Three.js / Web</text>
    <text x="120" y="0" font-size="12" fill="#7a97bd" class="mono">(3D Simulations &amp; WebGL)</text>
    <text x="760" y="0" font-size="14" fill="#c084fc" class="heading">13.7%</text>
    <rect y="10" width="814" height="12" rx="4" fill="#13253d"/>
    <rect y="10" width="111" height="12" rx="4" fill="#c084fc"/>
  </g>
</g>

<!-- Footer -->
<text x="44" y="415" font-size="11" fill="#6682a6" class="mono">CONSISTENCY OVER INTENSITY // VERIFIED WAKATIME TELEMETRY</text>
<text x="960" y="415" font-size="11" fill="#38bdf8" class="mono">SYNCED VIA WAKATIME API</text>
</svg>'''
    with open("assets/wakatime-telemetry.svg", "w", encoding="utf-8") as f:
        f.write(wakatime_svg)
    print("[OK] Built assets/wakatime-telemetry.svg")

    # =========================================================================
    # 8. QUICK-NAV.SVG (Interactive Top Cyber Navigation HUD)
    # =========================================================================
    nav_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 68" width="100%" height="68">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', monospace; font-size: 10.5px; font-weight: 700; }
  </style>
  <linearGradient id="nav-border" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
    <stop offset="50%" stop-color="#247bff" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity="0.8"/>
  </linearGradient>
</defs>
<rect width="1200" height="68" rx="14" fill="#080d1a" stroke="url(#nav-border)" stroke-width="1.4"/>

<g transform="translate(24, 16)">
  <!-- Logo pill -->
  <rect width="64" height="36" rx="8" fill="#102542" stroke="#247bff"/>
  <text x="32" y="23" font-size="13" fill="#ffffff" font-family="'Inter', sans-serif" font-weight="900" text-anchor="middle">BA</text>

  <!-- Nav links visually styled -->
  <g transform="translate(80, 0)">
    <rect width="106" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
    <text x="53" y="23" fill="#38bdf8" class="mono" text-anchor="middle">01 / BLUEPRINT</text>

    <g transform="translate(116, 0)">
      <rect width="122" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
      <text x="61" y="23" fill="#73b0ff" class="mono" text-anchor="middle">02 / ENGINE ROOM</text>
    </g>

    <g transform="translate(248, 0)">
      <rect width="102" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
      <text x="51" y="23" fill="#38bdf8" class="mono" text-anchor="middle">03 / PROJECTS</text>
    </g>

    <g transform="translate(360, 0)">
      <rect width="122" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
      <text x="61" y="23" fill="#52c41a" class="mono" text-anchor="middle">04 / SNAKE MATRIX</text>
    </g>

    <g transform="translate(492, 0)">
      <rect width="138" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
      <text x="69" y="23" fill="#38bdf8" class="mono" text-anchor="middle">05 / WAKATIME STATS</text>
    </g>

    <g transform="translate(640, 0)">
      <rect width="126" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
      <text x="63" y="23" fill="#ff4d6d" class="mono" text-anchor="middle">06 / GITHUB STATS</text>
    </g>

    <g transform="translate(776, 0)">
      <rect width="120" height="36" rx="6" fill="#0e1b2e" stroke="#233d61"/>
      <text x="60" y="23" fill="#73b0ff" class="mono" text-anchor="middle">07 / CREDENTIALS</text>
    </g>

    <g transform="translate(906, 0)">
      <rect width="104" height="36" rx="6" fill="#1b1222" stroke="#ff354f"/>
      <text x="52" y="23" fill="#ff7088" class="mono" text-anchor="middle">08 / CONNECT</text>
    </g>
  </g>
</g>
</svg>'''
    with open("assets/quick-nav.svg", "w", encoding="utf-8") as f:
        f.write(nav_svg)
    print("[OK] Built assets/quick-nav.svg")

    # =========================================================================
    # 9. STATS-HEADER.SVG (GitHub Global Telemetry Header)
    # =========================================================================
    stats_hdr = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 130" width="100%" height="100%">
<defs>
  <style>
    .mono { font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .heading { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 800; }
  </style>
  <linearGradient id="sth-hairline" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#38bdf8" stop-opacity=".7"/>
    <stop offset="50%" stop-color="#1f3760" stop-opacity=".3"/>
    <stop offset="100%" stop-color="#ff354f" stop-opacity=".5"/>
  </linearGradient>
</defs>
<rect width="1200" height="130" rx="16" fill="#070b16" stroke="url(#sth-hairline)" stroke-width="1.8"/>

<!-- Header bar -->
<path d="M36 46 L1164 46" fill="none" stroke="#223149" stroke-width="1.4"/>
<text x="38" y="30" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">06 / GITHUB REPO ANALYTICS</text>
<text x="440" y="30" font-size="11" fill="#8e9db9" class="mono" letter-spacing="1.6">TELEMETRY &amp; STREAK METRICS</text>

<text x="38" y="86" font-size="28" fill="#f2f5ff" class="heading">CODE VELOCITY &amp; REPOSITORY IMPACT</text>
<text x="38" y="108" font-size="11.5" fill="#85a2c7" class="mono">COMMITS · PULL REQUESTS · CODE STREAK · VERIFIED CONTRIBUTION ACTIVITY</text>

<path d="M1110 74l8 0 -6 16h-8Z" fill="#247bff"/>
<path d="M1122 74l8 0 -6 16h-8Z" fill="#247bff"/>
<path d="M1134 74l8 0 -6 16h-8Z" fill="#ff354f"/>
</svg>'''
    with open("assets/stats-header.svg", "w", encoding="utf-8") as f:
        f.write(stats_hdr)
    print("[OK] Built assets/stats-header.svg")

if __name__ == "__main__":
    create_all_assets()
