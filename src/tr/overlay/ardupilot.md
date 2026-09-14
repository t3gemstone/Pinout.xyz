<!--
---
name: ArduPilot
page_url: ardupilot
description: ArduPilot tarafından kullanılan T3 Gemstone O1 başlık işlevleri
url: https://docs.t3gemstone.org/tr/projects/ardupilot
pin:
  '27':
    name: Ayrılmış I2C SDA
  '28':
    name: Ayrılmış I2C SCL
-->
# ArduPilot GPIO Bağlantıları

Bu bölümde, gerekli Device Tree overlay'leri etkinleştirildiğinde T3 Gemstone'un resmi ArduPilot yapılandırması tarafından 40 pinli başlığa atanan işlevler gösterilmektedir.

## Seyrüsefer ve kontrol

* **GPS ve harici pusula:** 7 (UART-MAIN6 RX), 11 (UART-MAIN6 TX), 3 (I2C-MCU0 SDA) ve 5 (I2C-MCU0 SCL) numaralı pinler kullanılır.
* **RC girişi:** 10 numaralı pin (UART-MAIN1 RX) SBUS sinyalini destekler.
* **RC çıkışları:** 29, 8, 31, 33, 32, 36 ve 12 numaralı pinler sırasıyla RCOut 1–7 çıkışlarını sağlar.
* **Telemetri:** 18 (UART-WKUP0 TX) ve 26 (UART-WKUP0 RX) numaralı pinler kullanılır.

## Atanmış diğer pinler

19, 21, 23 ve 24 numaralı pinler SPI-MCU0 arayüzünü oluşturur. 27 ve 28 numaralı pinler I2C-WKUP0 için ayrılmıştır; 37 numaralı pin ise harici buzzer bağlantısı için atanmıştır.

> **SBUS uyarısı:** SBUS, terslenmiş seri sinyal kullanır. Alıcı ile 10 numaralı pin arasına harici bir sinyal tersleyici bağlayın. Standart SBUS çıkışını doğrudan 10 numaralı pine bağlamayın.

> **Güç ve lojik uyarısı:** RCOut pinleri yalnızca 3,3 V lojik seviyesinde PWM sinyali sağlar ve servolar için güç çıkışı sağlamaz. Servo ve diğer harici yükleri, kart ile ortak toprak bağlantısına sahip ve yeterli akım kapasitesine sahip harici bir güç kaynağından besleyin. Gerektiğinde uygun bir sürücü devresi veya lojik seviye dönüştürücü kullanın. GPS ve telemetri cihazlarını bağlamadan önce sinyal seviyelerinin 3,3 V lojik seviyesine uygun olduğunu doğrulayın.

Çevre birimlerini bağlamadan önce resmi T3 Gemstone dokümantasyonunda belirtilen gerekli Device Tree overlay'lerini etkinleştirin. İlgili kılavuzda Linux aygıt yolları, servis yapılandırması ve QGroundControl bağlantısına ilişkin kurulum adımları da açıklanmaktadır.
