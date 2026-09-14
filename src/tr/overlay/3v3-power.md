<!--
---
name: 3,3 V Güç
page_url: 3v3_power
description: T3 Gemstone O1 3,3 V başlık besleme pinleri
url: https://docs.t3gemstone.org/tr/boards/o1/peripherals/introduction
-->
# 3,3 V Güç

Physical Pin 1 ve Physical Pin 17, 3,3 V verir. Bu aynı zamanda tüm sinyal pinlerinin çalıştığı gerilimdir, dolayısıyla sensörler, küçük ekranlar ve benzeri az güç çeken eklentiler için doğru besleme budur.

Kart bu 3,3 V'u kendi regülatörüyle üretir ve M.2 yuvası ile kamera, ekran ve USB konnektörleriyle paylaşır. Yani buradan çekebileceğiniz akım, karta başka nelerin takılı olduğuna bağlıdır.

> **Buradan güç vermeyin:** Bu pinler çıkıştır, giriş değildir. Kendi 3,3 V'unuzu buraya uygulamak kartın regülatörüne karşı çalışır ve ona zarar verebilir.
