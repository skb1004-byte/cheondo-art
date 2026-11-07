# 장식 SVG (직접 제작): 운문(구름무늬), 먹선, 낙관(天道)
CLOUD = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 64" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">
<path d="M8 44c0-10 8-18 18-18 4-10 14-16 25-14 6-8 18-10 27-4 10-4 22 2 25 12 9 0 16 7 16 16"/>
<path d="M26 26c6 0 10 5 10 10s-4 8-8 8-6-3-6-6 2-5 5-5"/>
<path d="M78 20c7 0 12 6 12 12s-5 10-10 10-7-4-7-7 3-6 6-6"/>
<path d="M119 34c-6 0-9 4-9 8s3 6 6 6 5-2 5-5"/>
<path d="M4 52h56M70 52h86" stroke-width="1"/></svg>'''

INKLINE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 24" preserveAspectRatio="none"><defs><filter id="ink" x="-5%" y="-50%" width="110%" height="200%"><feTurbulence type="fractalNoise" baseFrequency="0.035 0.6" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter></defs>
<path filter="url(#ink)" d="M4 13 C120 7 220 15 330 11 S520 9 596 12 L596 14 C500 16 400 15 300 16 S80 17 4 15Z" fill="currentColor"/></svg>'''

SEAL = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" role="img" aria-label="天道 낙관"><defs><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.25"/><feComposite in="SourceGraphic" operator="in"/></filter></defs>
<g filter="url(#rough)" fill="currentColor"><path d="M6 8 L114 5 L116 113 L5 116 Z M16 18 L16 104 L104 104 L104 16 Z" fill-rule="evenodd"/>
<text x="60" y="56" text-anchor="middle" font-family="'Noto Serif TC Variable','Noto Serif KR Variable',serif" font-weight="800" font-size="40">天</text>
<text x="60" y="98" text-anchor="middle" font-family="'Noto Serif TC Variable','Noto Serif KR Variable',serif" font-weight="800" font-size="40">道</text></g></svg>'''

PAPER = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.012 0.09' numOctaves='3' seed='11'/%3E%3CfeColorMatrix values='0 0 0 0 0.45  0 0 0 0 0.38  0 0 0 0 0.25  0 0 0 0.05 0'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23p)'/%3E%3C/svg%3E")
