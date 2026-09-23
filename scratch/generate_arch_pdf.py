import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Set up figure and axis
fig, ax = plt.subplots(figsize=(8.5, 6), dpi=300)
ax.set_xlim(0, 100)
ax.set_ylim(0, 80)
ax.axis('off')

# Font and Style settings
font_family = 'sans-serif'
border_color = '#1A365D'
bg_box = '#EBF8FF'
accent_box = '#EDF2F7'
sub_box = '#FFFFFF'
text_color = '#2D3748'
line_color = '#2B6CB0'

# Title Box: Sentinel Desktop Outer Boundary
outer_rect = patches.FancyBboxPatch(
    (2, 2), 96, 76,
    boxstyle="round,pad=0.5,rounding_size=1.5",
    ec=border_color, fc='#F7FAFC', lw=2, linestyle='-'
)
ax.add_patch(outer_rect)

# Top Title Label
ax.text(50, 75, "Sentinel Desktop System Architecture (Host Local Loopback: 127.0.0.1)",
        ha='center', va='center', fontsize=12, fontweight='bold', color=border_color, family=font_family)

# Helper function to draw module boxes
def draw_box(x, y, w, h, title, subtitles, fill=bg_box, ec=line_color):
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.3,rounding_size=1.0",
        ec=ec, fc=fill, lw=1.5
    )
    ax.add_patch(rect)
    ax.text(x + w/2, y + h - 3.5, title, ha='center', va='center',
            fontsize=10, fontweight='bold', color=border_color, family=font_family)
    
    sub_y = y + h - 8.5
    for sub in subtitles:
        sub_rect = patches.FancyBboxPatch(
            (x + 2, sub_y - 2.5), w - 4, 4.5,
            boxstyle="round,pad=0.2,rounding_size=0.5",
            ec='#CBD5E0', fc=sub_box, lw=1.0
        )
        ax.add_patch(sub_rect)
        ax.text(x + w/2, sub_y, sub, ha='center', va='center',
                fontsize=8.5, color=text_color, family=font_family)
        sub_y -= 5.5

# Module 1: Local LLM Integration (Top Left)
draw_box(6, 48, 40, 20, "Local LLM Integration", ["Ollama Host Loopback (127.0.0.1:11434)", "Quarantined Prompts & Citation Grounding"])

# Module 2: Context Management (Top Right)
draw_box(54, 48, 40, 20, "Context Management Engine", ["In-Memory Evidence Store (evidenceStore)", "Log Archiving (.kilo/archives/) & JSON Snapshots"])

# Module 3: Browser Instrumentation (Middle Left)
draw_box(6, 22, 40, 20, "Browser Instrumentation", ["Electron WebContentsView attached to CDP 1.3", "Header Streams, Console & Exception Observation"])

# Module 4: Security Analysis (Middle Right)
draw_box(54, 22, 40, 20, "Security Analysis Engine", ["Passive Rules Engine (CSP_MISSING_CHECK)", "Scanner Ingestion (SARIF v2.1.0 & OWASP ZAP)"])

# Module 5: Replay Comparison & Evidence Collection (Bottom Center)
draw_box(20, 4, 60, 14, "Replay Comparison & Evidence Collection Module", ["Differential Header Differencing & SHA-256 Hashed Evidence Log"], fill='#E2E8F0', ec='#4A5568')

# Draw Connection Arrows
def draw_arrow(x1, y1, x2, y2, label=""):
    ax.annotate(
        label, xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="<->,head_width=0.3,head_length=0.5", color=line_color, lw=1.5),
        ha='center', va='center', fontsize=8, color='#4A5568', family=font_family
    )

def draw_single_arrow(x1, y1, x2, y2, label=""):
    ax.annotate(
        label, xy=(x2, y2), xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->,head_width=0.3,head_length=0.5", color=line_color, lw=1.5),
        ha='center', va='center', fontsize=8, color='#4A5568', family=font_family
    )

# Arrows between top modules
draw_arrow(46, 58, 54, 58, "Prompts / State")
# Arrows top left to bottom left
draw_single_arrow(26, 48, 26, 42, "Structured JSON")
# Arrows top right to bottom right
draw_single_arrow(74, 48, 74, 42, "State Updates")
# Arrows middle left to bottom center
draw_single_arrow(26, 22, 35, 18, "Raw Observation")
# Arrows middle right to bottom center
draw_single_arrow(74, 22, 65, 18, "Hypotheses / Findings")

# Final Output Arrow exiting system
ax.annotate(
    "Reproducible Evidence Report", xy=(50, 0.5), xytext=(50, 4),
    arrowprops=dict(arrowstyle="->,head_width=0.4,head_length=0.6", color='#2B6CB0', lw=2),
    ha='center', va='center', fontsize=9, fontweight='bold', color='#1A365D', family=font_family
)

plt.tight_layout()

# Save as PDF
os.makedirs('research/ieee/figures', exist_ok=True)
pdf_path = 'research/ieee/figures/system_architecture.pdf'
plt.savefig(pdf_path, format='pdf', bbox_inches='tight')
plt.close()

print(f"Successfully generated vector architecture figure: {pdf_path}")
