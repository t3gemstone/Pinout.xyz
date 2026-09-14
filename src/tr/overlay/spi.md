<!--
---
page_url: spi
description: T3 Gemstone O1 SPI-MCU0 başlık pinleri
url: https://docs.t3gemstone.org/tr/boards/o1/peripherals/introduction
-->
# SPI

SPI arayüzü beş pin kullanır. Physical Pin 19 veri gönderimi (MOSI), Physical Pin 21 veri alımı (MISO), Physical Pin 23 ise saat (SCLK) hattıdır. Physical Pin 24 ve Physical Pin 26, bağlı cihazlardan hangisinin etkin olduğunu belirleyen chip-select (CS) hatlarıdır. İlgili Device Tree overlay'i etkinleştirildiğinde bu arayüzler Linux üzerinde `/dev/spidev0.0` ve `/dev/spidev0.2` aygıt dosyaları olarak görünür.

Her cihaza ayrı bir chip-select hattı atanması ve chip-select hattı etkin olmayan cihazların SPI veri hattını sürmemesi koşuluyla, aynı MOSI, MISO ve SCLK hatları birden fazla cihaz tarafından paylaşılabilir.

## Kartın kendi sensörleri de bu hattı kullanır

Kart üzerindeki barometre ve IMU sensörleri, SPI veri ve saat hatlarını harici cihazlarla paylaşır. Sensörlerin kendilerine ait chip-select (CS) hatları bulunur ve bu hatlar 40 pinli başlığa çıkarılmamıştır. Bu nedenle, uygun şekilde yapılandırılmış harici cihazların SPI iletişimi sensörlerin chip-select hatlarıyla çakışmaz.

> **Dikkat** Yalnızca 3,3 V lojik seviyesini destekleyen cihazlar kullanın. Harici cihazın chip-select (CS) hattı etkin değilken SPI veri hatlarını sürmediğinden emin olun. CS hattı etkin olmayan bir cihazın veri hattını sürmesi, kart üzerindeki sensörlerin SPI iletişimini etkileyerek hatalı sensör okumalarına neden olabilir. Aynı şekilde, kart üzerindeki sensörlerin veri hattını sürmesi de harici cihazın iletişimini etkileyebilir.

> **Physical Pin 26'nın ikinci işlevi:** Physical Pin 26, ek bir seri portun alım (RX) hattı olarak da kullanılabilir. Bu işlev etkinleştirildiğinde SPI arayüzünde yalnızca Physical Pin 24 chip-select (CS) hattı olarak kullanılabilir.