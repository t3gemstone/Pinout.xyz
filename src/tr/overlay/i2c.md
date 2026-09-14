<!--
---
page_url: i2c
description: T3 Gemstone O1 I2C-MCU0 ve paylaşımlı I2C-WKUP0 başlık pinleri
-->
# I2C

Physical Pin 3 (veri) ve Physical Pin 5 (saat), harici cihazların kullanımı için ayrılmış I²C veri yolunu oluşturur. Bu veri yoluna kart üzerinde başka bir cihaz bağlı değildir; dolayısıyla harici cihazlar için ayrılmıştır. I²C iletişimi için gerekli pull-up dirençleri kart üzerinde bulunmaktadır ve ek direnç kullanılmasına gerek yoktur.

I²C veri yolu numarası, kullanılan yazılım imajına göre değişiklik gösterebilir. Veri yolu `/dev/i2c-1` veya `/dev/i2c-2` olarak görünebilir. Mevcut I²C veri yollarını listelemek için aşağıdaki komutu kullanın:

```bash
ls /dev/i2c-*
```

Bir veri yolundaki bağlı cihazları ve I²C adreslerini görüntülemek için ilgili veri yolu üzerinde `i2cdetect` komutunu kullanın.

> **Bağlantı öncesi:** Yalnızca 3,3 V lojik seviyesini destekleyen cihazlar kullanın. I²C hattındaki her cihazın benzersiz bir adresi olmalıdır; aynı adresin birden fazla cihaz tarafından kullanılması iletişim çakışmasına neden olabilir. Harici pull-up direnci eklemeden önce kart üzerinde mevcut pull-up dirençlerinin bulunduğunu göz önünde bulundurun.

## 27 ve 28 numaralı pinler paylaşımlı bir I²C hattıdır

Physical Pin 27 ve Physical Pin 28 pinleri, kart üzerindeki ikinci I²C veri yoluna aittir. Bu veri yolunda gerekli pull-up dirençleri kart üzerinde bulunmaktadır. Güç yönetim entegresi (PMIC), gerçek zamanlı saat (RTC) ve EEPROM bu veri yoluna dahili olarak bağlıdır.

Bu pinlere harici I²C cihazları bağlayabilirsiniz. Ancak veri yolu mevcut cihazlarla paylaşıldığından, yeni bir cihaz bağlamadan önce i2cdetect komutunu kullanarak veri yolundaki mevcut I²C adreslerini kontrol edin ve çakışma oluşturmayacak benzersiz bir adres kullanın.

> **Dikkat:** Bu I²C hattı, pin 3 ve 5'te bulunan I²C hattına kıyasla daha dikkatli kullanılmalıdır. Güç yönetim entegresinin (PMIC) bu hatta bağlı olması nedeniyle oluşabilecek bir kısa devre, yanlış gerilim uygulanması veya veri yolunun kilitlenmesi, yalnızca bağlı çevre biriminin değil, kartın tamamının çalışmasını etkileyebilir. Veri yolunda hâlihazırda bulunan cihazların yapılandırmasını değiştirmeyin. Genel amaçlı sensör ve çevre birimi bağlantıları için Physical Pin 3 ve Physical Pin 5'te bulunan I²C veri yolunun kullanılması önerilir. Bu veri yolu harici cihazların kullanımına ayrılmıştır.
