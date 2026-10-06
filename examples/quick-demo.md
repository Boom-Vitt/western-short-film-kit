# ลองหนึ่งช็อตก่อน — One Floor Below

ทดลองช็อต S01 แบบข้อความเป็นวิดีโอ เพื่อดูภาพและฟังบทพูดก่อนทำ [ตอนเต็ม 6 ช็อต](one-floor-below-48s.md) ไม่ใช้ภาพอ้างอิงในการทดลองนี้ จึงยังไม่พิสูจน์ว่าหน้าตาคงที่ข้ามช็อต

| ตั้งค่า | ค่าในการทดลอง |
|---|---|
| เครื่องมือ | Google Flow |
| โหมด | Video / Frames โดยไม่ใส่ start/end frame (Text-to-Video) |
| โมเดล | Veo 3.1 - Lite |
| อัตราส่วน / ระยะเวลา / outputs | 9:16 / 8 วินาที / x1 |
| ความละเอียด | 720p |
| เครดิตที่ UI แสดงก่อนสร้าง | 10 เครดิตสำหรับผลลัพธ์เดียว ตรวจราคาใหม่ก่อนใช้ |
| บทพูด | Ella: “I know that tune.” |

## 1. คัดลอก Prompt

```text
Create one continuous 8-second vertical 9:16 cinematic shot for an original fictional suspense story. The character is entirely fictional and invented for this story, not based on any real person, actor or public figure.
One adult woman aged 32 with fair freckled skin, hazel eyes and a dark brown bob. She wears a navy wool coat over a cream sweater, black trousers, dark brown ankle boots and a thin silver necklace.
She is standing inside a brushed-steel elevator car in an old apartment building at night, facing the closed doors with empty hands relaxed. Cold overhead light and subtle warm ambient spill. Static medium close-up.
At the start a faint brief three-note whistle comes from beyond the doors, without words. The woman freezes and slowly looks up. The elevator doors remain closed. No scarf is present.
Only this fictional woman speaks, in English with a neutral American accent and a restrained medium-low adult female voice, saying exactly: "I know that tune." Leave a brief pause after the line.
Quiet elevator hum, no music, no narrator, no other speech. No subtitles, no captions, no text, no logos, no extra people.
```

## 2. ตรวจผล

- แนวตั้ง 9:16 เปิดเล่นได้ครบ มีภาพและเสียง
- ผู้ใหญ่หนึ่งคน ผมบ๊อบน้ำตาล โค้ทกรมท่า เสื้อครีม สร้อยเงิน ตรงบรีฟ
- ประตูลิฟต์ปิดตลอด ไม่มีผ้าพันคอหรือคนอื่นในภาพ
- Ella พูด “I know that tune.” คนเดียว ไม่มีบทเพิ่มหรือผู้บรรยาย
- เสียงผิวปากสั้นช่วงต้น ไม่กลบคำพูด ไม่มีซับหรือโลโก้ที่โมเดลเติมเอง

ดูและฟัง take จริงก่อนรับงาน หากผิดใช้ [REPAIR](../prompts/REPAIR.md) และแก้เฉพาะเป้าหมายที่ระบุ

## 3. ดูตัวอย่างและไปต่อ

[เปิด MP4 พร้อมเสียง](../assets/demo.mp4) · [GIF พรีวิวเงียบ](../assets/demo.gif) · [ผลตรวจและข้อจำกัด](../docs/TEST-REPORT.md)

เดโมเป็นช็อตทดลอง S01 จากข้อความ ไม่ได้ใช้ภาพปกเป็น reference ของตัวละคร ชุดบท 48 วินาทีเป็นแผนสำหรับทำต่อ เมื่อจะทำครบเรื่องให้สร้างและเลือก approved references แล้วทำตาม [WORKFLOW](../WORKFLOW.md)
