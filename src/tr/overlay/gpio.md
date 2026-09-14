<!--
---
name: GPIO
page_url: gpio
description: T3 Gemstone O1 genel amaçlı 3,3 V GPIO pinleri
-->
# GPIO - Genel Amaçlı Giriş/Çıkış

T3 Gemstone O1 üzerindeki 40 pinli başlık, 3,3 V lojik seviyesinde çalışan dijital GPIO pinleri sunar. Her pin; dijital giriş olarak okunabilir, dijital çıkış olarak sürülebilir veya UART, SPI, I²C, PCM ve PWM gibi alternatif işlevler için yapılandırılabilir.

GPIO pinlerini Linux üzerinden kontrol etmek için `libgpiod` araçlarını kullanabilirsiniz. GPIO pinlerini listelemek için `gpioinfo`, pin durumunu okumak için `gpioget` ve pin durumunu ayarlamak için `gpioset` komutlarını kullanabilirsiniz. GPIO pinlerini fiziksel pin numarasıyla değil, sistem tarafından tanımlanan GPIO adıyla belirtmelisiniz.

> **3,3 V lojik seviyesini kullanın:** GPIO pinleri doğrudan işlemciye bağlıdır ve aralarında herhangi bir koruma devresi bulunmaz. GPIO pinlerine 5 V uygulanması işlemciye ve karta zarar verebilir. GPIO pinleri yalnızca sinyal amaçlı kullanılmalıdır. LED, buzzer, röle veya motor gibi yükleri doğrudan GPIO pinine bağlamayın; bu tür yükler için uygun bir sürücü devresi, transistör veya röle modülü kullanın.

Bazı alternatif işlevler, ilgili Device Tree overlay'i `/boot/uEnv.txt` dosyasında etkinleştirildiğinde kullanılabilir. Overlay etkinleştirilmediği sürece ilgili pin GPIO olarak çalışır.