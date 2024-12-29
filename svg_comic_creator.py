import os
from krita import Krita
from PyQt5.Qt import *

WIDTH = 1600
HEIGHT = 2560

HEIGHT_LIST = [2,3,2,3]

def fit_svg_in_panel(svg_content, x, y, panel_width, panel_height):
    """
    Adjusts the given SVG content to fit within a specified panel.
    """
    transformed_svg = f"""
    <g transform="translate({x}, {y}) scale({panel_width / 400}, {panel_height / 400})">
        {svg_content}
    </g>
    """
    return transformed_svg
   
CORPUS = [
    "Euthyphro. Why have you left the Lyceum, Socrates? and what are you doing in the Porch of the King Archon? Surely you cannot be concerned in a suit before the King, like myself?",
    "Socrates. Not in a suit, Euthyphro; impeachment is the word which the Athenians use.",
    "Euth. What! I suppose that some one has been prosecuting you, for I cannot believe that you are the prosecutor of another.",
    "Soc. Certainly not.",
    "Euth. Then some one else has been prosecuting you?",
    "Soc. Yes."
]



def draw_panels(width, height, n, padding=20, m=0, rh=1000): #rh means height of the panels
    svgstring = ""
    width= width
    xypositions = []
    panel_width = (width - padding*(n+1))/n
    pwidths = []
    panel_height = rh
    for i in range(n):
        rect = f"<rect x='{i*(panel_width+padding)+padding}' y='{m+padding}' width ='{panel_width}px' height='{rh}px' fill ='none' stroke='black' stroke-width='2'  />\n"
        print(rect)
        xypositions.append(( i*(panel_width+padding)+padding, m+padding, panel_width, panel_height))
        svgstring += rect
        #pwidths = pwidths + [panel_width]
    return svgstring, xypositions#, pwidths

def draw_text(x,y, string="test"):
    svgstring = """<foreignObject x="{x}" y="{y}" width="750" height="580">
    <body xmlns="http://www.w3.org/1999/xhtml">
      <div style="font-size:24px; font-family:Arial; color:blue; text-align:left;">
        Euthyphro: Then someone else has been prosecuting you?
      </div>
    </body>
  </foreignObject>"""
    
    f"""<text x='{x}' y ='{y}' font-size='36px' font-family='komika hand' fill='blue'>{string}</text> """
    return svgstring


positions = []


svgContent = f"""\
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="{WIDTH}"
   height="{HEIGHT}"
   viewBox="0 0 {WIDTH} {HEIGHT}">
"""
xypos = []
panel_widths = []
for j in range(len(HEIGHT_LIST)):
    svgstring, xypositions= draw_panels(WIDTH, HEIGHT, HEIGHT_LIST[j],20, j*630,600)
    xypos = xypos + xypositions
    #panel_widths = panel_widths + panel_width
    svgContent+=svgstring
print(xypos)
#print(panel_width)

extra_stuff = ["""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <!-- Background: A dark, grimy alleyway at night -->
  <rect width="400" height="400" fill="black" />
  <rect x="50" y="0" width="300" height="400" fill="#2c2c2c" /> <!-- Grimy walls -->
  <circle cx="200" cy="50" r="30" fill="#ccc" opacity="0.3" /> <!-- Dim streetlight glow -->
  <line x1="200" y1="80" x2="200" y2="200" stroke="#aaa" stroke-width="2" opacity="0.3" /> <!-- Light pole -->
  <rect x="100" y="300" width="50" height="30" fill="#333" /> <!-- Trash bin -->
  <path d="M120,300 L125,320 L115,320 Z" fill="#555" /> <!-- Trash heap -->

  <!-- Mugger character -->
  <g transform="translate(50, 50)">
    <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
    <rect x="75" y="110" width="50" height="110" fill="black" />
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    <path d="M88,95 Q100,97 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
    <path d="M75,180 Q65,185 70,195 Q80,190 75,180 Z" fill="#d4c3b5" />
    <path d="M125,180 Q135,185 130,195 Q120,190 125,180 Z" fill="#d4c3b5" />
    <rect x="85" y="220" width="10" height="50" fill="black" />
    <rect x="105" y="220" width="10" height="50" fill="black" />
    <rect x="80" y="270" width="20" height="10" fill="darkgray" />
    <rect x="100" y="270" width="20" height="10" fill="darkgray" />
  </g>

  <!-- Pascal character -->
  <g transform="translate(250, 100)">
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    <path d="M90,70 Q100,80 110,70" fill="none" stroke="#000" stroke-width="2" />
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
    <rect x="80" y="170" width="20" height="30" fill="#000" />
    <rect x="100" y="170" width="20" height="30" fill="#000" />
  </g>

  <!-- Dialogue -->
  <text x="10" y="20" font-family="Arial" font-size="12" fill="white">
    <tspan x="10" dy="1.2em">Mugger: Hey, give me your wallet.</tspan>
    <tspan x="10" dy="1.5em">Pascal: Why on Earth would I want to do that?</tspan>
  </text>
</svg>""",

""" <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="400" height="400" fill="#2f2f2f" />
  <rect x="50" y="50" width="300" height="300" fill="#444" stroke="#222" stroke-width="5" />

  <!-- Mugger -->
  <g transform="translate(120,100)">
    <circle cx="30" cy="30" r="30" fill="#d4c3b5" stroke="#000" stroke-width="2" />
    <path d="M15,35 Q30,50 45,35" fill="none" stroke="#000" stroke-width="2" />
    <rect x="0" y="60" width="60" height="80" fill="#000" />
    <rect x="15" y="140" width="10" height="30" fill="#333" />
    <rect x="35" y="140" width="10" height="30" fill="#333" />
    <path d="M15,60 Q30,20 45,60" fill="#000" />
    <path d="M15,60 Q0,70 15,90" fill="#d4c3b5" />
    <path d="M45,60 Q60,70 45,90" fill="#d4c3b5" />
  </g>

  <!-- Pascal -->
  <g transform="translate(220,160)">
    <circle cx="30" cy="30" r="30" fill="#f1c27d" />
    <path d="M15,35 Q30,45 45,35" fill="none" stroke="#000" stroke-width="2" />
    <rect x="0" y="60" width="60" height="80" fill="#87CEEB" />
    <rect x="5" y="140" width="10" height="30" fill="#000" />
    <rect x="45" y="140" width="10" height="30" fill="#000" />
    <line x1="30" y1="100" x2="30" y2="140" stroke="#000" stroke-width="2" />
    <path d="M30,90 Q20,70 10,90" fill="#87CEEB" />
    <path d="M30,90 Q40,70 50,90" fill="#87CEEB" />
  </g>

  <!-- Dialogue -->
  <text x="20" y="20" fill="#fff" font-family="Arial" font-size="16">
    <tspan x="20" y="20">Mugger: Otherwise I’ll shoot you.</tspan>
    <tspan x="20" y="50">Pascal: But you don’t have a gun.</tspan>
  </text>
</svg>"""   , 

"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <!-- Background -->
  <rect width="400" height="400" fill="#2b2b2b" />
  <rect x="50" y="50" width="300" height="300" fill="#383838" rx="15" />

  <!-- Mugger -->
  <g transform="translate(80, 120) scale(0.8)">
    <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
    <rect x="75" y="110" width="50" height="110" fill="black" />
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    <path d="M88,95 Q100,97 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
    <path d="M75,180 Q65,185 70,195 Q80,190 75,180 Z" fill="#d4c3b5" />
    <path d="M125,180 Q135,185 130,195 Q120,190 125,180 Z" fill="#d4c3b5" />
    <rect x="85" y="220" width="10" height="50" fill="black" />
    <rect x="105" y="220" width="10" height="50" fill="black" />
    <rect x="80" y="270" width="20" height="10" fill="darkgray" />
    <rect x="100" y="270" width="20" height="10" fill="darkgray" />
  </g>

  <!-- Pascal -->
  <g transform="translate(220, 100) scale(1.1)">
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    <path d="M90,70 Q100,80 110,70" fill="none" stroke="#000" stroke-width="2" />
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
    <rect x="80" y="170" width="20" height="30" fill="#000" />
    <rect x="100" y="170" width="20" height="30" fill="#000" />
  </g>

  <!-- Dialogue -->
  <text x="20" y="360" font-family="Arial, sans-serif" font-size="14" fill="white">
    <tspan x="20" dy="0">Mugger: Oops! I knew I had forgotten something.</tspan>
    <tspan x="20" dy="20">Pascal: No wallet for you then. Have a nice evening.</tspan>
  </text>
</svg>""",
 
 """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- Background -->
  <rect width="400" height="400" fill="#f5f5f5"/>
  
  <!-- Panel border -->
  <rect width="398" height="398" x="1" y="1" fill="none" stroke="black" stroke-width="2"/>

  <!-- Pascal (transformed and positioned) -->
  <g transform="translate(220, 50) scale(1.2) rotate(10)">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
      <!-- Head -->
      <circle cx="100" cy="60" r="30" fill="#f1c27d" />
      <!-- Blindfold -->
      <rect x="70" y="50" width="60" height="10" fill="#000" />
      <!-- Mouth -->
      <path d="M90,70 Q100,80 110,70" fill="none" stroke="#000" stroke-width="2" />
      <!-- Body -->
      <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
      <!-- Arms -->
      <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
      <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
      <!-- Wallet -->
      <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
      <!-- Legs -->
      <rect x="80" y="170" width="20" height="30" fill="#000" />
      <rect x="100" y="170" width="20" height="30" fill="#000" />
    </svg>
  </g>

  <!-- Mugger (transformed and positioned) -->
  <g transform="translate(50, 50) scale(1.2)">
    <svg width="200" height="300" viewBox="0 0 200 300">
      <!-- Background glow (muted) -->
      <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
      <!-- Figure body -->
      <rect x="75" y="110" width="50" height="110" fill="black" />
      <!-- Figure head -->
      <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
      <!-- Blindfold -->
      <rect x="75" y="70" width="50" height="12" fill="black" />
      <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
      <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
      <!-- Mouth -->
      <path d="M88,95 Q100,97 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
      <!-- Hooded cloak -->
      <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
      <!-- Hands (reaching out) -->
      <path d="M125,180 Q155,170 160,190 Q150,195 125,180 Z" fill="#d4c3b5" />
      <!-- Legs -->
      <rect x="85" y="220" width="10" height="50" fill="black" />
      <rect x="105" y="220" width="10" height="50" fill="black" />
      <!-- Boots -->
      <rect x="80" y="270" width="20" height="10" fill="darkgray" />
      <rect x="100" y="270" width="20" height="10" fill="darkgray" />
    </svg>
  </g>

  <!-- Speech bubbles and text -->
  <g transform="translate(0, 0)">
    <!-- Mugger's speech bubble -->
    <path d="M150,80 Q130,80 120,100 L110,120 L130,100 Q150,90 170,90 L230,90 Q250,90 250,70 L250,50 Q250,30 230,30 L170,30 Q150,30 150,50 Z" 
          fill="white" stroke="black" stroke-width="1"/>
    <text x="190" y="65" text-anchor="middle" font-family="Comic Sans MS, cursive">
      <tspan x="190">Wait!</tspan>
    </text>

    <!-- Pascal's speech bubble -->
    <path d="M280,140 Q260,140 250,160 L240,180 L260,160 Q280,150 300,150 L360,150 Q380,150 380,130 L380,110 Q380,90 360,90 L300,90 Q280,90 280,110 Z"
          fill="white" stroke="black" stroke-width="1"/>
    <text x="320" y="125" text-anchor="middle" font-family="Comic Sans MS, cursive">
      <tspan x="320">Sigh.</tspan>
    </text>
  </g>
</svg> """,
""" <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- Background -->
  <rect width="400" height="400" fill="#f5f5f5"/>
  
  <!-- Panel border -->
  <rect width="398" height="398" x="1" y="1" fill="none" stroke="black" stroke-width="2"/>

  <!-- Alley background details -->
  <path d="M0,0 L400,0 L400,400 L0,400 Z" fill="#e0e0e0"/>
  <path d="M50,0 L30,400" stroke="#d0d0d0" stroke-width="5"/>
  <path d="M150,0 L130,400" stroke="#d0d0d0" stroke-width="5"/>
  <path d="M250,0 L270,400" stroke="#d0d0d0" stroke-width="5"/>
  <path d="M350,0 L370,400" stroke="#d0d0d0" stroke-width="5"/>

  <!-- Pascal (transformed and positioned) -->
  <g transform="translate(220, 100) scale(1.2)">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
      <!-- Head (with raised eyebrow effect) -->
      <circle cx="100" cy="60" r="30" fill="#f1c27d" />
      <!-- Blindfold -->
      <rect x="70" y="50" width="60" height="10" fill="#000" />
      <!-- Skeptical mouth -->
      <path d="M90,75 Q100,70 110,75" fill="none" stroke="#000" stroke-width="2" />
      <!-- Body -->
      <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
      <!-- Arms (crossed position) -->
      <rect x="60" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" transform="rotate(-20 80 110)" />
      <rect x="100" y="110" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" transform="rotate(20 120 120)" />
      <!-- Wallet -->
      <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
      <!-- Legs -->
      <rect x="80" y="170" width="20" height="30" fill="#000" />
      <rect x="100" y="170" width="20" height="30" fill="#000" />
    </svg>
  </g>

  <!-- Mugger (transformed and positioned with grand gesture) -->
  <g transform="translate(50, 100) scale(1.2)">
    <svg width="200" height="300" viewBox="0 0 200 300">
      <!-- Background glow (muted) -->
      <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
      <!-- Figure body -->
      <rect x="75" y="110" width="50" height="110" fill="black" />
      <!-- Figure head -->
      <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
      <!-- Blindfold -->
      <rect x="75" y="70" width="50" height="12" fill="black" />
      <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
      <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
      <!-- Enthusiastic mouth -->
      <path d="M88,95 Q100,90 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
      <!-- Hooded cloak -->
      <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
      <!-- Hands (gesture) -->
      <path d="M65,160 Q45,150 35,170 Q55,175 65,160 Z" fill="#d4c3b5" />
      <path d="M135,160 Q155,150 165,170 Q145,175 135,160 Z" fill="#d4c3b5" />
      <!-- Legs -->
      <rect x="85" y="220" width="10" height="50" fill="black" />
      <rect x="105" y="220" width="10" height="50" fill="black" />
      <!-- Boots -->
      <rect x="80" y="270" width="20" height="10" fill="darkgray" />
      <rect x="100" y="270" width="20" height="10" fill="darkgray" />
    </svg>
  </g>

  <!-- Speech bubbles and text -->
  <!-- First speech bubble -->
  <path d="M100,50 Q80,50 70,70 L60,90 L80,70 Q100,60 120,60 L260,60 Q280,60 280,40 L280,20 Q280,0 260,0 L120,0 Q100,0 100,20 Z" 
        fill="white" stroke="black" stroke-width="1"/>
  <text x="190" y="35" text-anchor="middle" font-family="Comic Sans MS, cursive">
    <tspan x="190">I've got a business proposition</tspan>
    <tspan x="190" dy="20">for you...</tspan>
  </text>

  <!-- Second speech bubble -->
  <path d="M100,130 Q80,130 70,150 L60,170 L80,150 Q100,140 120,140 L260,140 Q280,140 280,120 L280,100 Q280,80 260,80 L120,80 Q100,80 100,100 Z"
        fill="white" stroke="black" stroke-width="1"/>
  <text x="190" y="115" text-anchor="middle" font-family="Comic Sans MS, cursive">
    <tspan x="190">How about you give me</tspan>
    <tspan x="190" dy="20">your wallet now?</tspan>
  </text>
</svg>""", 
"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- Background with night effect -->
  <rect width="400" height="400" fill="#2b2b35"/>
  
  <!-- Moonlight effect -->
  <radialGradient id="moonlight" cx="75%" cy="25%" r="80%">
    <stop offset="0%" style="stop-color:#a5c1d4;stop-opacity:0.2"/>
    <stop offset="100%" style="stop-color:#2b2b35;stop-opacity:0"/>
  </radialGradient>
  <rect width="400" height="400" fill="url(#moonlight)"/>
  
  <!-- Panel border -->
  <rect width="398" height="398" x="1" y="1" fill="none" stroke="black" stroke-width="2"/>

  <!-- Alley details -->
  <path d="M50,0 L30,400" stroke="#3a3a45" stroke-width="5"/>
  <path d="M150,0 L130,400" stroke="#3a3a45" stroke-width="5"/>
  <path d="M250,0 L270,400" stroke="#3a3a45" stroke-width="5"/>
  <path d="M350,0 L370,400" stroke="#3a3a45" stroke-width="5"/>

  <!-- Pascal (transformed and positioned, more skeptical) -->
  <g transform="translate(220, 100) scale(1.2)">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="200" height="200">
      <!-- Head -->
      <circle cx="100" cy="60" r="30" fill="#f1c27d" />
      <!-- Blindfold -->
      <rect x="70" y="50" width="60" height="10" fill="#000" />
      <!-- Skeptical mouth (more pronounced) -->
      <path d="M90,75 Q100,78 110,75" fill="none" stroke="#000" stroke-width="2.5" />
      <!-- Body -->
      <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
      <!-- Arms (firmly crossed) -->
      <rect x="55" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" transform="rotate(-25 75 110)" />
      <rect x="105" y="110" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" transform="rotate(25 125 120)" />
      <!-- Wallet -->
      <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
      <!-- Legs -->
      <rect x="80" y="170" width="20" height="30" fill="#000" />
      <rect x="100" y="170" width="20" height="30" fill="#000" />
    </svg>
  </g>

  <!-- Mugger (transformed and positioned, enthusiastic) -->
  <g transform="translate(50, 100) scale(1.2)">
    <svg width="200" height="300" viewBox="0 0 200 300">
      <!-- Background glow (muted) -->
      <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
      <!-- Figure body -->
      <rect x="75" y="110" width="50" height="110" fill="black" />
      <!-- Figure head -->
      <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
      <!-- Blindfold -->
      <rect x="75" y="70" width="50" height="12" fill="black" />
      <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
      <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
      <!-- Excited mouth -->
      <path d="M88,95 Q100,88 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
      <!-- Hooded cloak -->
      <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
      <!-- Hands (enthusiastic gesture) -->
      <path d="M55,150 Q35,140 25,160 Q45,165 55,150 Z" fill="#d4c3b5" />
      <path d="M145,150 Q165,140 175,160 Q155,165 145,150 Z" fill="#d4c3b5" />
      <!-- Legs -->
      <rect x="85" y="220" width="10" height="50" fill="black" />
      <rect x="105" y="220" width="10" height="50" fill="black" />
      <!-- Boots -->
      <rect x="80" y="270" width="20" height="10" fill="darkgray" />
      <rect x="100" y="270" width="20" height="10" fill="darkgray" />
    </svg>
  </g>

  <!-- Speech bubbles and text -->
  <!-- Mugger's speech bubble -->
  <path d="M100,50 Q80,50 70,70 L60,90 L80,70 Q100,60 120,60 L280,60 Q300,60 300,40 L300,20 Q300,0 280,0 L120,0 Q100,0 100,20 Z" 
        fill="white" stroke="black" stroke-width="1"/>
  <text x="190" y="25" text-anchor="middle" font-family="Comic Sans MS, cursive">
    <tspan x="190">I promise to give you double</tspan>
    <tspan x="190" dy="20">the value tomorrow.</tspan>
  </text>

  <!-- Pascal's speech bubble -->
  <path d="M280,130 Q260,130 250,150 L240,170 L260,150 Q280,140 300,140 L360,140 Q380,140 380,120 L380,100 Q380,80 360,80 L300,80 Q280,80 280,100 Z"
        fill="white" stroke="black" stroke-width="1"/>
  <text x="330" y="115" text-anchor="middle" font-family="Comic Sans MS, cursive">
    <tspan x="330">No way.</tspan>
  </text>
</svg> """, 

""" <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- Background -->
  <rect width="400" height="400" fill="#ffffff"/>
  
  <!-- Panel border -->
  <rect width="398" height="398" x="1" y="1" fill="none" stroke="black" stroke-width="2"/>

  <!-- Mugger (scaled and positioned) -->
  <g transform="translate(100,50) scale(1.2)">
    <!-- Background glow (muted) -->
    <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
    
    <!-- Figure body -->
    <rect x="75" y="110" width="50" height="110" fill="black" />
    
    <!-- Figure head -->
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    
    <!-- Blindfold -->
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    
    <!-- Mouth (pleading expression) -->
    <path d="M88,95 Q100,100 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    
    <!-- Hand raised with three fingers -->
    <g transform="translate(-20,-20)">
      <path d="M125,180 Q135,175 130,165 L127,160 L124,160 L121,160" fill="#d4c3b5" stroke="black" stroke-width="1" />
      <line x1="127" y1="160" x2="127" y2="150" stroke="#d4c3b5" stroke-width="3" />
      <line x1="124" y1="160" x2="124" y2="150" stroke="#d4c3b5" stroke-width="3" />
      <line x1="121" y1="160" x2="121" y2="150" stroke="#d4c3b5" stroke-width="3" />
    </g>
  </g>

  <!-- Pascal (scaled and positioned) -->
  <g transform="translate(200,100) scale(1.1)">
    <!-- Head -->
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    
    <!-- Blindfold -->
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    
    <!-- Mouth (dismissive expression) -->
    <path d="M90,70 Q100,73 110,70" fill="none" stroke="#000" stroke-width="2" />
    
    <!-- Body -->
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    
    <!-- Arms -->
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    
    <!-- Wallet -->
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
  </g>

  <!-- Speech bubbles and text -->
  <g transform="translate(0,0)">
    <!-- Mugger's speech bubble -->
    <path d="M120,100 Q170,90 220,100 Q270,110 220,120 Q170,130 120,120 Z" fill="white" stroke="black" stroke-width="1" />
    <text x="170" y="105" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12">
      <tspan x="170" dy="0">Give me your wallet, and I'll bring</tspan>
      <tspan x="170" dy="14">you 10 times its value tomorrow!</tspan>
    </text>

    <!-- Pascal's speech bubble -->
    <path d="M280,150 Q300,160 320,150 Q340,140 320,170 Q300,180 280,170 Z" fill="white" stroke="black" stroke-width="1" />
    <text x="300" y="165" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12">
      <tspan x="300">Sorry.</tspan>
    </text>
  </g>
</svg>""", 

"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- Dark alley background -->
  <rect width="400" height="400" fill="#1a1a1a"/>
  
  <!-- Perspective lines for alley -->
  <path d="M0,0 L150,100 M400,0 L250,100" stroke="#333333" stroke-width="2" opacity="0.5"/>
  <path d="M0,400 L150,300 M400,400 L250,300" stroke="#333333" stroke-width="2" opacity="0.5"/>
  
  <!-- Panel border -->
  <rect width="398" height="398" x="1" y="1" fill="none" stroke="black" stroke-width="2"/>

  <!-- Mugger (scaled and positioned) -->
  <g transform="translate(80,50) scale(1.2)">
    <!-- Background glow (muted) -->
    <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />
    
    <!-- Figure body -->
    <rect x="75" y="110" width="50" height="110" fill="black" />
    
    <!-- Figure head -->
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    
    <!-- Blindfold -->
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    
    <!-- Mouth (calculating expression) -->
    <path d="M88,95 Q100,93 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    
    <!-- Hands calculating in air -->
    <g transform="translate(-20,-20)">
      <path d="M125,160 Q135,155 130,145" fill="none" stroke="#d4c3b5" stroke-width="3"/>
      <path d="M120,155 Q130,150 125,140" fill="none" stroke="#d4c3b5" stroke-width="3"/>
      <circle cx="132" cy="143" r="3" fill="#d4c3b5"/>
      <circle cx="127" cy="138" r="3" fill="#d4c3b5"/>
    </g>
  </g>

  <!-- Pascal (scaled and positioned) -->
  <g transform="translate(200,100) scale(1.1)">
    <!-- Head -->
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    
    <!-- Blindfold -->
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    
    <!-- Mouth (intrigued expression) -->
    <path d="M90,70 Q100,75 110,70" fill="none" stroke="#000" stroke-width="2" />
    
    <!-- Body -->
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    
    <!-- Arms -->
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    
    <!-- Wallet -->
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
  </g>

  <!-- Speech bubbles and text -->
  <g transform="translate(0,0)">
    <!-- Mugger's speech bubble -->
    <path d="M120,100 Q170,90 220,100 Q270,110 220,120 Q170,130 120,120 Z" fill="white" stroke="black" stroke-width="1" />
    <text x="170" y="105" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12">
      <tspan x="170" dy="0">What probability do you give</tspan>
      <tspan x="170" dy="14">that I'll keep my promise?</tspan>
    </text>

    <!-- Pascal's speech bubble -->
    <path d="M280,150 Q300,160 320,150 Q340,140 320,170 Q300,180 280,170 Z" fill="white" stroke="black" stroke-width="1" />
    <text x="300" y="165" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12">
      <tspan x="300">One in a thousand.</tspan>
    </text>
  </g>
</svg>""", 


"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  <!-- Dark alley background -->
  <rect width="400" height="400" fill="#1a1a1a"/>
  
  <!-- Surreal glowing symbols -->
  <g opacity="0.3">
    <text x="50" y="100" font-family="serif" font-size="24" fill="#4da6ff" filter="url(#glow)">∞</text>
    <text x="300" y="150" font-family="serif" font-size="20" fill="#4da6ff" filter="url(#glow)">π</text>
    <text x="200" y="80" font-family="serif" font-size="28" fill="#4da6ff" filter="url(#glow)">∑</text>
    <text x="150" y="200" font-family="serif" font-size="22" fill="#4da6ff" filter="url(#glow)">×</text>
  </g>

  <!-- Glow filter -->
  <defs>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Panel border -->
  <rect width="398" height="398" x="1" y="1" fill="none" stroke="black" stroke-width="2"/>

  <!-- Mugger (scaled and positioned) -->
  <g transform="translate(80,50) scale(1.2)">
    <!-- Background glow (enhanced for surreal effect) -->
    <circle cx="100" cy="150" r="100" fill="none" stroke="rgba(77, 166, 255, 0.2)" stroke-width="20" />
    
    <!-- Figure body -->
    <rect x="75" y="110" width="50" height="110" fill="black" />
    
    <!-- Figure head -->
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    
    <!-- Blindfold -->
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    
    <!-- Mouth (mysterious expression) -->
    <path d="M88,95 Q100,90 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    
    <!-- Hands gesturing mysteriously -->
    <g transform="translate(-20,-20)">
      <path d="M125,160 Q145,150 135,140 Q125,130 135,120" fill="none" stroke="#d4c3b5" stroke-width="3"/>
      <circle cx="135" cy="120" r="4" fill="#4da6ff" opacity="0.6"/>
    </g>
  </g>

  <!-- Pascal (scaled and positioned) -->
  <g transform="translate(200,100) scale(1.1)">
    <!-- Head -->
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    
    <!-- Blindfold -->
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    
    <!-- Mouth (skeptical expression) -->
    <path d="M90,70 Q100,68 110,70" fill="none" stroke="#000" stroke-width="2" />
    
    <!-- Body -->
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    
    <!-- Arms -->
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    
    <!-- Wallet -->
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
  </g>

  <!-- Speech bubbles and text -->
  <g transform="translate(0,0)">
    <!-- Mugger's speech bubble with tail -->
    <path d="M180,60 
             C220,50 260,50 280,60 
             C300,70 300,90 280,100
             C260,110 220,110 180,100
             C160,90 160,70 180,60
             M190,100 L170,120" 
          fill="white" stroke="black" stroke-width="1" />
    <text x="230" y="75" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12">
      <tspan x="230" dy="0">I'll give you 2,000 times</tspan>
      <tspan x="230" dy="14">the value!</tspan>
    </text>

    <!-- Pascal's speech bubble with tail -->
    <path d="M200,150
             C240,140 280,140 300,150
             C320,160 320,180 300,190
             C280,200 240,200 200,190
             C180,180 180,160 200,150
             M210,190 L190,210"
          fill="white" stroke="black" stroke-width="1" />
    <text x="250" y="165" text-anchor="middle" font-family="Comic Sans MS, cursive" font-size="12">
      <tspan x="250" dy="0">I doubt you even have</tspan>
      <tspan x="250" dy="14">that much money.</tspan>
    </text>
  </g>
</svg> """, 

""" <svg width="400" height="400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">

  <!-- Background glow (muted) -->
  <circle cx="200" cy="200" r="100" fill="none" stroke="rgba(50, 50, 50, 0.3)" stroke-width="20" />

  <!-- Mugger -->
  <g transform="translate(150, 80)">
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    <rect x="75" y="110" width="50" height="110" fill="black" />
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    <path d="M88,95 Q100,97 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
    <path d="M75,180 Q65,185 70,195 Q80,190 75,180 Z" fill="#d4c3b5" />
    <path d="M125,180 Q135,185 130,195 Q120,190 125,180 Z" fill="#d4c3b5" />
    <rect x="85" y="220" width="10" height="50" fill="black" />
    <rect x="105" y="220" width="10" height="50" fill="black" />
    <rect x="80" y="270" width="20" height="10" fill="darkgray" />
    <rect x="100" y="270" width="20" height="10" fill="darkgray" />
  </g>

  <!-- Pascal -->
  <g transform="translate(70, 200)">
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    <path d="M90,70 Q100,80 110,70" fill="none" stroke="#000" stroke-width="2" />
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
    <rect x="80" y="170" width="20" height="30" fill="#000" />
    <rect x="100" y="170" width="20" height="30" fill="#000" />
  </g>

  <!-- Dialogue Text -->
  <text x="20" y="330" font-family="Arial" font-size="14" fill="black">
    <tspan x="20" dy="1.2em">Mugger: I am an Operator of the Seventh Dimension!</tspan>
    <tspan x="20" dy="1.2em">Pascal: Gee... OK, one in a quadrillion.</tspan>
  </text>

</svg>
""", 

"""<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">

  <!-- Background glow (eerie) -->
  <circle cx="200" cy="200" r="100" fill="none" stroke="rgba(100, 100, 255, 0.5)" stroke-width="20" />

  <!-- Mugger (pointing at Pascal) -->
  <g transform="translate(120, 80)">
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    <rect x="75" y="110" width="50" height="110" fill="black" />
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    <path d="M88,95 Q100,97 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
    <path d="M75,180 Q65,185 70,195 Q80,190 75,180 Z" fill="#d4c3b5" />
    <path d="M125,180 Q135,185 130,195 Q120,190 125,180 Z" fill="#d4c3b5" />
    <rect x="85" y="220" width="10" height="50" fill="black" />
    <rect x="105" y="220" width="10" height="50" fill="black" />
    <rect x="80" y="270" width="20" height="10" fill="darkgray" />
    <rect x="100" y="270" width="20" height="10" fill="darkgray" />

    <!-- Mugger's hand pointing -->
    <path d="M120,140 L145,120 Q155,130 140,140 Q135,130 120,140" fill="#d4c3b5" />
  </g>

  <!-- Pascal (rubbing chin thoughtfully) -->
  <g transform="translate(200, 200)">
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    <path d="M90,70 Q100,80 110,70" fill="none" stroke="#000" stroke-width="2" />
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
    <rect x="80" y="170" width="20" height="30" fill="#000" />
    <rect x="100" y="170" width="20" height="30" fill="#000" />

    <!-- Pascal rubbing chin -->
    <circle cx="135" cy="80" r="5" fill="#f1c27d" />
    <path d="M130,90 Q135,100 140,90" fill="none" stroke="#000" stroke-width="2" />
  </g>

  <!-- Dialogue Text -->
  <text x="20" y="280" font-family="Arial" font-size="12" fill="black">
    <tspan x="20" dy="1.2em">Mugger: Hand me your wallet,</tspan>
    <tspan x="20" dy="1.2em">and I’ll give you 1,000 quadrillion</tspan>
    <tspan x="20" dy="1.2em">happy days.</tspan>
    <tspan x="20" dy="1.2em">Pascal: I admit I see no flaw</tspan>
    <tspan x="20" dy="1.2em">in your mathematics.</tspan>
  </text>

</svg>
""",
           
"""<svg width="400" height="400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">
  
  <!-- Background glow (dim streetlight) -->
  <circle cx="200" cy="200" r="100" fill="none" stroke="rgba(150, 150, 150, 0.5)" stroke-width="20" />
  
  <!-- Mugger (grinning triumphantly, holding out hand dramatically) -->
  <g transform="translate(120, 80)">
    <circle cx="100" cy="80" r="28" fill="#d4c3b5" stroke="black" stroke-width="1.5" />
    <rect x="75" y="110" width="50" height="110" fill="black" />
    <rect x="75" y="70" width="50" height="12" fill="black" />
    <path d="M75,76 L65,72 Q60,76 65,80 Z" fill="black" />
    <path d="M125,76 L135,72 Q140,76 135,80 Z" fill="black" />
    <path d="M88,95 Q100,97 112,95" fill="none" stroke="#4a4a4a" stroke-width="2" />
    <path d="M75,110 Q100,70 125,110 L125,200 Q100,230 75,200 Z" fill="black" />
    <path d="M75,180 Q65,185 70,195 Q80,190 75,180 Z" fill="#d4c3b5" />
    <path d="M125,180 Q135,185 130,195 Q120,190 125,180 Z" fill="#d4c3b5" />
    <rect x="85" y="220" width="10" height="50" fill="black" />
    <rect x="105" y="220" width="10" height="50" fill="black" />
    <rect x="80" y="270" width="20" height="10" fill="darkgray" />
    <rect x="100" y="270" width="20" height="10" fill="darkgray" />

    <!-- Mugger's hand dramatically extended -->
    <path d="M120,140 L160,130 Q170,140 155,150 Q150,140 120,140" fill="#d4c3b5" />
  </g>

  <!-- Pascal (hesitantly handing over wallet) -->
  <g transform="translate(200, 200)">
    <circle cx="100" cy="60" r="30" fill="#f1c27d" />
    <rect x="70" y="50" width="60" height="10" fill="#000" />
    <path d="M90,70 Q100,80 110,70" fill="none" stroke="#000" stroke-width="2" />
    <rect x="70" y="90" width="60" height="80" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="30" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="130" y="100" width="40" height="15" fill="#87CEEB" stroke="#000" stroke-width="1" />
    <rect x="140" y="115" width="30" height="20" fill="#654321" stroke="#000" stroke-width="1" />
    <rect x="80" y="170" width="20" height="30" fill="#000" />
    <rect x="100" y="170" width="20" height="30" fill="#000" />

    <!-- Pascal's hand handing over wallet -->
    <path d="M170,125 L160,120 Q155,130 165,135 Q170,130 170,125" fill="#d4c3b5" />
  </g>

  <!-- Dialogue Text -->
  <text x="20" y="280" font-family="Arial" font-size="12" fill="black">
    <tspan x="20" dy="1.2em">Mugger: Pleasure doing business!</tspan>
    <tspan x="20" dy="1.2em">Mugger: The magic will be performed</tspan>
    <tspan x="20" dy="1.2em">tomorrow, as agreed.</tspan>
  </text>

</svg>"""
 ]

for i in range(10):
    z = fit_svg_in_panel(extra_stuff[i],xypos[i][0],xypos[i][1],xypos[i][2],xypos[i][3])
    svgContent += z

textstring = ""
for i in range(len(xypos)):
    curr = draw_text(xypos[i][0]+50, xypos[i][1]+50, "Placeholder")
    textstring+=curr

svgContent+=textstring
svgContent +="</svg>"

def importSvg(svgContent, layer):
#    if not layer is None:    
#        doc.setActiveNode(vLayer)
#        #doc.waitForDone()  # ==> waitForDone() doesn't work, need to apply a sleep :-(
#        sleep(450)
        
    mimeContent=QMimeData()
    mimeContent.setData('image/svg+xml', svgContent.encode())
    QGuiApplication.clipboard().setMimeData(mimeContent)

importSvg(svgContent, 0)
