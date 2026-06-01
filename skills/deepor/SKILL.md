Deepor (ดีพอ) — Thai-to-English translation layer for Claude Code. Use this skill whenever the user writes any instruction, task, or question in Thai or mixed Thai-English. Deepor automatically detects Thai input, shows an interactive setup menu on first use, translates the prompt into precise technical English using Claude's built-in language capability (no external API needed), then executes — so Claude always receives a well-formed English instruction regardless of how the user typed it. Also triggers on: "แปลก่อน", "translate first", "/translate", "/deepor". Session toggle keywords — ON: translate:on / แปล:เปิด / deepor:on / ดีพอ:เปิด; OFF: translate:off / แปล:ปิด / deepor:off / ดีพอ:ปิด; Status: translate:status / แปล:สถานะ / deepor:status / ดีพอ:สถานะ. Respects session ON/OFF toggle and saved default preferences from CLAUDE.md.Version1.0.0AuthorbankziiesLicenseMITTagstranslation,thai,localization,multilingual,claude-code,productivityDeepor (ดีพอ) — Thai Translation Layer for Claude Code
Deepor คือ skill ที่ทำหน้าที่เป็น translation layer ระหว่างผู้ใช้ที่พิมพ์ภาษาไทย กับ Claude
ที่ทำงานได้ดีที่สุดเมื่อรับ prompt ภาษาอังกฤษ ชื่อ "ดีพอ" มาจากแนวคิดว่า — แค่พิมพ์ภาษาไทยก็
ดีพอ แล้ว ที่เหลือ Deepor จัดการให้เอง

Translation Engine
การแปลทั้งหมดทำโดย Claude โดยตรง โดยใช้ความสามารถด้านภาษาที่มีในตัว
ห้ามเรียก external API ใดๆ (DeepL, Google Translate, LibreTranslate ฯลฯ)
และห้ามใช้ bash/curl/python script เพื่อแปลภาษาโดยเด็ดขาด
ข้อดีของแนวทางนี้:

ไม่ต้องตั้งค่า API key — install แล้วใช้งานได้ทันที
ไม่มีค่าใช้จ่ายเพิ่มเติม — ใช้ความสามารถของ Claude ที่มีอยู่แล้ว
คุณภาพสูง — Claude เข้าใจ context, คำศัพท์เทคนิค, และภาษาไทยผสมอังกฤษได้ดีมาก
แชร์ได้ทันที — ทุกคนที่ install skill นี้ใช้งานได้เลยโดยไม่ต้องตั้งค่าอะไรเพิ่ม


ความสามารถหลัก
1. Auto-detect & Translate
ตรวจจับภาษาไทยในทุก message อัตโนมัติ แล้วแปลเป็น English ที่ถูกต้องตามบริบท technical
ก่อนดำเนินการ — ผู้ใช้ไม่ต้องสลับภาษาเอง
2. Interactive Setup Menu
ทุก session ใหม่ Deepor จะถามตัวเลือกก่อนเริ่มทำงาน ให้ผู้ใช้เลือก translation mode
และภาษาที่ต้องการให้ตอบกลับ ไม่ต้องจำคำสั่ง
3. Translation Modes
ปรับความละเอียดของการแปลให้เหมาะกับงานแต่ละประเภท
4. Response Language Control
ควบคุมภาษาที่ Claude ใช้ตอบกลับ แยกอิสระจาก translation — สั่งงานไทยแต่รับคำอธิบายเป็น
English ได้ หรือสั่งงาน English แต่รับคำอธิบายเป็นไทยก็ได้
5. Session Toggle
เปิด/ปิด Deepor ได้ทันทีโดยไม่ต้องถอดติดตั้ง และ override ได้แบบ per-message
6. Saved Defaults
บันทึก preference ไว้ใน CLAUDE.md ของ project เพื่อข้าม setup menu ใน session ถัดไป

Step 1 — First-run setup (ทุก session ใหม่)
ครั้งแรกที่ตรวจพบ Thai input ในแต่ละ session (หรือผู้ใช้พิมพ์ /deepor setup),
แสดง setup menu ด้านล่างก่อนทำงานทุกครั้ง รอผู้ใช้ตอบ แล้วค่อย proceed
ถ้ามี saved defaults ใน CLAUDE.md ให้ข้าม menu แล้วแสดงแค่บรรทัดยืนยันสั้น ๆ
Setup menu format
╔══════════════════════════════════════════════╗
║   🌐  DEEPOR — ดีพอ  ·  Thai for Claude Code  ║
╚══════════════════════════════════════════════╝

📝 Translation Mode — โหมดการแปล
   [1] Concise   กระชับ เหมาะกับ coding / CLI tasks       ← แนะนำ
   [2] Full      ครบทุก nuance เหมาะกับ logic ซับซ้อน
   [3] Short     1–2 ประโยค เหมาะกับคำสั่งง่าย ๆ

🗣️ Response Language — ภาษาที่ต้องการให้ตอบกลับ
   [A] Auto      ตามภาษา input อัตโนมัติ                   ← แนะนำ
   [B] ไทย       ตอบกลับเป็นภาษาไทยเสมอ
   [C] English   Always respond in English

⚡ Quick options
   [D] ใช้ค่าแนะนำทั้งหมด (Concise + Auto) → เริ่มเลย
   [E] ใช้ default ที่บันทึกไว้ [แสดงค่าถ้ามี หรือ "ยังไม่ได้บันทึก"]

   พิมพ์ตัวเลือก เช่น  1A  /  2B  /  3C  /  D
──────────────────────────────────────────────
Parsing the reply:

1 / 2 / 3 → translation mode (concise / full / short)
A / B / C → response language (auto / thai / english)
รวมกันได้อิสระ: 1B = concise + thai, 2C = full + english, 3A = short + auto
D → apply recommended defaults (concise + auto) แล้ว proceed ทันที
E → apply saved defaults ถ้ามี; ถ้าไม่มีให้แจ้งและแสดง menu ใหม่

หลังผู้ใช้เลือก ยืนยันด้วย 1 บรรทัด:
✅ Deepor พร้อมแล้ว: Mode [concise/full/short] · Reply [auto/thai/english] — กำลังแปล...
แล้วดำเนินการแปลและ execute prompt ต้นฉบับต่อ

Step 2 — Translation
Translation mode behaviour
Modeเหมาะกับพฤติกรรมconcise (default)Coding, CLI, file operationsแปลกระชับ ตัดคำฟุ่มเฟือย คงไว้ทุก constraintfullLogic ซับซ้อน, business rules, multi-stepแปลครบทุก nuance อาจยาวกว่า originalshortคำสั่งง่าย, quick lookups1–2 ประโยค ตัด context ที่ไม่จำเป็นออก
Translation principles

แปล ความหมาย ไม่ใช่คำ — ภาษาไทยมักละ subject ให้เติมให้ชัดเจนใน English
คง technical terms ไว้ทุกครั้ง: useState, pandas, requirements.txt, file paths, error messages
คำคลุมเครือ เช่น "ทำให้มันดีขึ้น" ให้ infer จาก context แล้วทำให้ concrete (เช่น "Refactor the function to improve readability")
ไม่เพิ่ม assumption หรือ requirement ที่ไม่มีใน original

Output format
🌐 Deepor [mode: concise]
──────────────────────────────────────
<English translation here>
──────────────────────────────────────
กำลังดำเนินการ... แจ้งได้เลยถ้าต้องการปรับการแปล

Step 3 — Response language
ควบคุมภาษาที่ Claude ใช้ใน output — คำอธิบาย, comment, error message
Code, variable name, file path, technical term ไม่แปลเสมอ ไม่ว่าจะตั้งค่าอะไรก็ตาม
Settingพฤติกรรมauto (default)Thai input → Thai reply · English input → English reply · Mixed → Thaithaiตอบไทยเสมอ แม้รับ prompt ภาษาอังกฤษenglishตอบ English เสมอ แม้รับ prompt ภาษาไทย

Saving defaults (ตั้งค่าถาวร)
บันทึก preference เพื่อข้าม setup menu ในทุก session ถัดไป:
set default 1B    → บันทึก: mode=concise, reply=thai
set default 2C    → บันทึก: mode=full,    reply=english
set default D     → บันทึก: recommended defaults
default:clear     → ลบ default, กลับมาแสดง menu ทุก session
default:show      → แสดงค่าที่บันทึกไว้
เมื่อบันทึก Deepor จะแนะนำให้เพิ่มบรรทัดนี้ใน CLAUDE.md ของ project:
markdown# Deepor defaults
translate-mode: concise
translate-reply: thai
Claude อ่านไฟล์นี้ทุก session — Deepor จะตรวจพบและข้าม menu อัตโนมัติ
ยืนยันการบันทึก:
💾 บันทึก Deepor defaults แล้ว: Mode [x] · Reply [y]
   เพิ่มบรรทัดด้านล่างใน CLAUDE.md เพื่อให้ใช้งานได้ทุก session:

   translate-mode: concise
   translate-reply: thai

Session controls
Deepor toggle
ActionKeywords (รองรับทุกรูปแบบ ใช้อันไหนก็ได้)เปิดtranslate:on · แปล:เปิด · deepor:on · ดีพอ:เปิดปิดtranslate:off · แปล:ปิด · deepor:off · ดีพอ:ปิดสถานะtranslate:status · แปล:สถานะ · deepor:status · ดีพอ:สถานะ
ทุก keyword ในแต่ละแถวมีผลเท่ากัน — เลือกใช้ตามที่ถนัดได้เลย
เมื่อ toggle ให้ยืนยันทันที:

เปิด → ✅ Deepor เปิดแล้ว — Thai input จะถูกแปลก่อน execute
ปิด → ⏸️ Deepor ปิดแล้ว — Thai input จะถูกส่งตรงโดยไม่แปล

Status format:
📍 Deepor [ON/OFF] · Mode: [concise/full/short] · Reply: [auto/thai/english]
Response language (เปลี่ยน mid-session)

reply:thai · ตอบ:ไทย → 🗣️ ตอบกลับเป็นภาษาไทยเสมอ
reply:english · ตอบ:อังกฤษ → 🗣️ Responses will always be in English.
reply:auto · ตอบ:อัตโนมัติ → 🗣️ Response language set to auto.

Translation mode (เปลี่ยน mid-session)

mode: concise · mode: full · mode: short · โหมด full ฯลฯ

Per-message overrides (ครั้งเดียว ไม่เปลี่ยน session state)

บังคับแปลครั้งนี้ (แม้ปิดอยู่): prefix แปลก่อน หรือ translate this:
ข้ามการแปลครั้งนี้ (แม้เปิดอยู่): prefix ไม่ต้องแปล หรือ skip translate:

Re-show setup menu

/deepor setup → แสดง setup menu ใหม่ได้ทุกเมื่อ

แก้ไขการแปล

บอกได้เลยว่าผิดตรงไหน ภาษาไทยหรืออังกฤษก็ได้ — Deepor จะแก้และยืนยันก่อน execute ใหม่


ตัวอย่างการใช้งาน
First-run + บันทึก default
User:   เขียนฟังก์ชัน Python หาค่าเฉลี่ย

Deepor: ╔══════════════════════════════════════════════╗
        ║   🌐  DEEPOR — ดีพอ  ·  Thai for Claude Code  ║
        ╚══════════════════════════════════════════════╝
        [1] Concise  [2] Full  [3] Short
        [A] Auto     [B] ไทย   [C] English
        [D] ค่าแนะนำ  [E] Default ที่บันทึกไว้
        พิมพ์: เช่น 1B หรือ D

User:   1B

Deepor: ✅ Deepor พร้อมแล้ว: Mode concise · Reply thai — กำลังแปล...

        🌐 Deepor [mode: concise]
        ──────────────────────────────────────
        Write a Python function that calculates the average of a list of numbers.
        Return None if the list is empty.
        ──────────────────────────────────────

        [ตอบกลับเป็นภาษาไทย]
        นี่คือฟังก์ชันคำนวณค่าเฉลี่ยครับ:
        ...

User:   set default 1B

Deepor: 💾 บันทึก Deepor defaults แล้ว: Mode concise · Reply thai
        เพิ่มบรรทัดนี้ใน CLAUDE.md:

        translate-mode: concise
        translate-reply: thai
Session ถัดไป (มี default แล้ว)
User:   แก้ bug ใน login function

Deepor: ✅ Deepor พร้อมแล้ว (default): Mode concise · Reply thai

        🌐 Deepor [mode: concise]
        ──────────────────────────────────────
        Fix the bug in the login function.
        ──────────────────────────────────────
        ...
ปิดชั่วคราวและ override
User:   deepor:off
Deepor: ⏸️ Deepor OFF — Thai input จะถูกส่งตรงโดยไม่แปล

User:   แก้ bug ใน auth middleware   ← ไม่แปล, Claude รับภาษาไทยตรง ๆ

User:   แปลก่อน เพิ่ม rate limiting ใน API  ← บังคับแปลครั้งนี้ครั้งเดียว
Deepor: 🌐 Deepor [mode: concise]
        ──────────────────────────────────────
        Add rate limiting to the API.
        ──────────────────────────────────────
        (Deepor ยังคง OFF หลังจากนี้)
