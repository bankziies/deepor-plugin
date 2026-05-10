# Deepor Plugin — ดีพอ 🌐

> **แค่พิมพ์ภาษาไทยก็ดีพอ** — Thai-to-English translation layer for Claude Code & Cowork

Deepor คือ plugin ที่ทำหน้าที่เป็น translation layer ระหว่างผู้ใช้ที่พิมพ์ภาษาไทย กับ Claude ที่ทำงานได้ดีที่สุดเมื่อรับ prompt ภาษาอังกฤษ ไม่ต้องสลับภาษา ไม่ต้องจำคำสั่ง — แค่พิมพ์ภาษาไทยก็พอ

---

## ✨ Features

- **Auto-detect & Translate** — ตรวจจับภาษาไทยอัตโนมัติ แปลเป็น English ที่ถูกต้องตาม technical context
- **Interactive Setup Menu** — เลือก translation mode และภาษาตอบกลับได้ง่าย ๆ ไม่ต้องจำ syntax
- **3 Translation Modes** — Concise / Full / Short ปรับให้เหมาะกับงานแต่ละประเภท
- **Response Language Control** — สั่งงานไทย แต่รับคำอธิบายเป็น English ได้ (หรือกลับกัน)
- **Session Toggle** — เปิด/ปิด Deepor ได้ทันที (`deepor:on` / `deepor:off`)
- **Saved Defaults** — บันทึก preference ใน `CLAUDE.md` เพื่อข้าม setup menu ทุก session

---

## 📦 Installation

### Via Claude Marketplace
ค้นหา **"deepor"** ใน Claude Plugin Marketplace แล้วกด Install

### Via GitHub (Manual)
1. Download `deepor.skill` จาก [Releases](https://github.com/Bankziies/deepor-plugin/releases)
2. เปิด Claude Code หรือ Cowork
3. Drag & drop ไฟล์ `.skill` เข้าไป หรือใช้คำสั่ง:
```bash
claude plugin install https://github.com/Bankziies/deepor-plugin
```

---

## 🚀 Quick Start

```
User:   เขียนฟังก์ชัน Python หาค่าเฉลี่ย

Deepor: ╔══════════════════════════════════════════════╗
        ║   🌐  DEEPOR — ดีพอ  ·  Thai for Claude Code  ║
        ╚══════════════════════════════════════════════╝
        [1] Concise  [2] Full  [3] Short
        [A] Auto     [B] ไทย   [C] English
        [D] ค่าแนะนำทั้งหมด

User:   D

Deepor: ✅ Deepor พร้อมแล้ว: Mode concise · Reply auto — กำลังแปล...

        🌐 Deepor [mode: concise]
        ──────────────────────────────────────
        Write a Python function that calculates the average of a list.
        Return None if the list is empty.
        ──────────────────────────────────────
```

---

## ⚙️ Session Controls

| Action | Keywords |
|--------|----------|
| เปิด Deepor | `translate:on` · `deepor:on` · `แปล:เปิด` · `ดีพอ:เปิด` |
| ปิด Deepor | `translate:off` · `deepor:off` · `แปล:ปิด` · `ดีพอ:ปิด` |
| ดูสถานะ | `translate:status` · `deepor:status` · `แปล:สถานะ` |
| เปลี่ยนภาษาตอบ | `reply:thai` · `reply:english` · `reply:auto` |
| บังคับแปลครั้งเดียว | `แปลก่อน <prompt>` |
| ข้ามการแปลครั้งเดียว | `ไม่ต้องแปล <prompt>` |

---

## 💾 Saving Defaults

บันทึก preference ถาวรโดยเพิ่มบรรทัดนี้ใน `CLAUDE.md` ของ project:

```markdown
# Deepor defaults
translate-mode: concise
translate-reply: auto
```

หรือพิมพ์ `set default 1A` ใน session แล้ว Deepor จะแนะนำให้บันทึกอัตโนมัติ

---

## 📁 Plugin Structure

```
deepor-plugin/
├── plugin.json          ← Plugin manifest
├── README.md            ← This file
└── skills/
    └── deepor/
        └── SKILL.md     ← Skill instructions
```

---

## 📄 License

MIT License — free to use, modify, and distribute

---

*Made with ❤️ for Thai developers using Claude Code & Cowork*
