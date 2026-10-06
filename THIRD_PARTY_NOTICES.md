# ที่มาและสิทธิ์

## ชุดหนังจีนเดิม

โครงสร้าง Prompt / workflow / production template รูปแบบหน้า README และตัวตรวจเอกสารใน `scripts/check_repo.py` ต่อจาก [boombignose/chinese-short-film-flow](https://github.com/boombignose/chinese-short-film-flow) ตัวตรวจดัดแปลงสำหรับเรื่องใหม่และ regression checks ของชุดนี้

MIT License — Copyright (c) 2026 boombignose. ประกาศสิทธิ์และข้อความอนุญาตของต้นทางคงไว้ใน [LICENSE](LICENSE) งานเพิ่มเติมของชุดนี้เผยแพร่ภายใต้ MIT เช่นกัน

## เนื้อหาที่สร้างใหม่

เรื่อง **One Floor Below**, character bible, storyboard และ Prompt จัดทำขึ้นสำหรับชุดนี้ ตัวละครสมมติ ไม่ใช้ชื่อหรือภาพอ้างอิงนักแสดงจริง

- [ภาพปก](assets/hero.png) สร้างด้วย built-in imagegen ใช้แบนเนอร์ของชุดหนังจีนเป็น reference ด้านการจัดวาง — [Prompt](assets/hero-prompt.md) เป็นภาพแนวคิด ไม่ใช่เฟรมจากวิดีโอหรือ reference ที่ใช้เจนคลิป
- [คลิปทดลองพูดไทย](assets/demo.mp4) สร้างใน Google Flow ด้วย Veo 3.1 - Lite จากข้อความของเรื่องใหม่ ไม่แนบภาพหรือเสียงจากหนังฝรั่ง ลบซับเพี้ยนที่โมเดลเติมด้วย FFmpeg โดยคงเสียงเดิม — [Prompt และการตั้งค่า](examples/quick-demo.md) · [รายละเอียดการแก้และผลตรวจ](docs/TEST-REPORT.md)
- [GIF](assets/demo.gif) ทำจากคลิปทดลองเดียวกันด้วย FFmpeg ย่อเป็น 240×426 และ 8 fps ไม่มีเสียง

ไม่มีฟุตเทจนักแสดง เพลง หรือเสียงอ้างอิงจากหนังฝรั่งแนบมา คลิปทดลองยังต้องตรวจเสียงและ lip sync โดยมนุษย์ก่อนรับเป็นงาน final — [ผลตรวจ](docs/TEST-REPORT.md)

## เครื่องมือและเอกสารอ้างอิง

- [Google Flow: create videos](https://support.google.com/flow/answer/16353334?hl=en)
- [Google Flow: models and supported features](https://support.google.com/flow/answer/16352836?hl=en)
- [Google Flow: credits](https://support.google.com/flow/answer/16526234?hl=en)

อ้างอิงวิธีใช้จากเอกสารทางการโดยสรุปใหม่ ตรวจเมื่อ 6 ตุลาคม 2026 ฟีเจอร์และราคาของบริการอาจเปลี่ยนหรือแตกต่างตามบัญชี/ภูมิภาค การแจกไฟล์ MIT ไม่ได้เปลี่ยนเงื่อนไขของ ChatGPT, Claude, Flow หรือสิทธิ์ของสื่อที่ผู้ใช้เพิ่มภายหลัง
