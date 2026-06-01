🌐 Deepor — Thai Translation Layer for Claude Code

ดีพอ (dee-por) — "Just typing Thai is enough."
Deepor is a Claude Code skill that automatically detects Thai input, translates it into precise technical English, and executes — so you never have to switch languages mid-workflow.

Compatible with Claude Code, OpenAI Codex CLI, and any AI coding tool that supports the SKILL.md format.

✨ Why Deepor?
Thai developers and technical teams often think and communicate in Thai, but AI coding assistants perform best with English prompts. Deepor bridges that gap — no API keys, no setup, no cost — by using Claude's built-in language capability to translate Thai instructions before execution.
Without DeeporWith DeeporSwitch to English mentallyType naturally in ThaiRisk losing technical nuanceFull context preservedExtra cognitive loadJust code

🚀 Install
Claude Code (personal — all projects)
bashcp -r skills/deepor ~/.claude/skills/
Claude Code (project-level)
bashcp -r skills/deepor .claude/skills/
OpenAI Codex CLI
bashcp -r skills/deepor ~/.codex/skills/
Or clone and copy in one step:
bashgit clone https://github.com/bankziies/deepor-skill.git
cp -r deepor-skill/skills/deepor ~/.claude/skills/

🎯 How It Works
1. Auto-detect & Translate
Deepor watches every message. When Thai text is detected, it translates to precise technical English before Claude acts — preserving variable names, file paths, error messages, and all technical terms unchanged.
2. Interactive Setup Menu (first use per session)
On first Thai input each session, Deepor shows a quick setup menu:
╔══════════════════════════════════════════════╗
║   🌐  DEEPOR — ดีพอ  ·  Thai for Claude Code  ║
╚══════════════════════════════════════════════╝

📝 Translation Mode
   [1] Concise   Best for coding / CLI tasks        ← recommended
   [2] Full      Preserves all nuance (complex logic)
   [3] Short     1–2 sentences for simple commands

🗣️ Response Language
   [A] Auto      Matches your input language        ← recommended
   [B] Thai      Always reply in Thai
   [C] English   Always reply in English

⚡ Quick options
   [D] Use recommended defaults (Concise + Auto)
   
   Type: e.g.  1A  /  2B  /  D
3. Save Defaults (skip menu on future sessions)
set default 1B    → saves: mode=concise, reply=thai
set default D     → saves: recommended defaults
default:clear     → resets to show menu every session
Add to your CLAUDE.md to persist across sessions:
markdown# Deepor defaults
translate-mode: concise
translate-reply: thai

⚡ Session Controls
ActionKeywordsEnabletranslate:on · แปล:เปิด · deepor:on · ดีพอ:เปิดDisabletranslate:off · แปล:ปิด · deepor:off · ดีพอ:ปิดStatustranslate:status · แปล:สถานะ · deepor:statusForce translate onceprefix แปลก่อน or translate this:Skip translate onceprefix ไม่ต้องแปล or skip translate:Re-show setup menu/deepor setup

💡 Example Usage
User:   เขียนฟังก์ชัน Python หาค่าเฉลี่ย

Deepor: ✅ Deepor ready: Mode concise · Reply thai — translating...

        🌐 Deepor [mode: concise]
        ──────────────────────────────────────
        Write a Python function that calculates the average of a list.
        Return None if the list is empty.
        ──────────────────────────────────────
        กำลังดำเนินการ...

        นี่คือฟังก์ชันคำนวณค่าเฉลี่ยครับ:

        def average(numbers: list) -> float | None:
            if not numbers:
                return None
            return sum(numbers) / len(numbers)
User:   แก้ bug ใน login function แล้ว commit

Deepor: 🌐 Deepor [mode: concise]
        ──────────────────────────────────────
        Fix the bug in the login function, then commit the changes.
        ──────────────────────────────────────
        [reads code → fixes bug → git commit]

🔧 Translation Principles

Translates meaning, not words — Thai often omits subject; Deepor makes it explicit
Technical terms always preserved: useState, pandas, file paths, error messages, class names
Vague phrases like "ทำให้มันดีขึ้น" are inferred from context → "Refactor for readability"
No assumptions added beyond what the original intent implies


📁 Repository Structure
deepor-skill/
├── skills/
│   └── deepor/
│       └── SKILL.md        ← Core skill file
├── README.md
└── LICENSE                 ← MIT

🤝 Contributing
Contributions welcome — especially:

Improvements to translation quality for specific technical domains
Additional language support (e.g., Japanese, Korean using the same pattern)
Edge case handling for mixed Thai-English technical prompts

Please open an issue or PR on GitHub.

📄 License
MIT — free to use, modify, and distribute.

🏷️ Tags
claude-code · skills · translation · thai · localization · multilingual · productivity · SKILL.md
