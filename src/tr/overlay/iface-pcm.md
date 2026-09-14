<!--
---
name: PCM
page_url: pcm
description: T3 Gemstone O1 PCM/I2S uyumlu başlık sinyalleri
url: https://docs.t3gemstone.org/tr/boards/o1/peripherals/introduction
pin:
  '38':
    name: DATA0
  '40':
    name: DATA1
-->
# PCM - Darbe Kod Modülasyonu

Dört pin, dijital ses arayüzü için kullanılır ve Raspberry Pi'nin I²S arayüzünde kullandığı fiziksel pin konumlarıyla aynıdır. Bu nedenle Raspberry Pi uyumlu bir ses HAT'i fiziksel olarak başlığa takılabilir.

| Pin | İşlev |
| --: | :-- |
| 12 | Bit Saati (CLK) |
| 35 | Çerçeve Eşzamanlaması (FS) |
| 38 | Ses verisi |
| 40 | Ses verisi |

T3 Gemstone O1 üzerinde her iki ses veri pini de yazılım üzerinden giriş veya çıkış olarak yapılandırılabilir. Veri pinlerinin yönü, fiziksel bağlantıdan bağımsız olarak kullanılan ses yapılandırmasına göre belirlenir.