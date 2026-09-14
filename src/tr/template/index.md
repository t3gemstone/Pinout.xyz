# T3 Gemstone O1 Pin Dizilimi

T3 Gemstone pin dizilimi, T3 Gemstone O1 geliştirme kartının fiziksel pinlerini, uyumluluk GPIO numaralarını ve varsayılan arayüzlerini belgeler. Header, yaygın olarak kullanılan Raspberry Pi 40 pin fiziksel dizilimini kullanır; ancak işlemci, pin çoklama seçenekleri ve yazılım altyapısı Texas Instruments AM67A platformuna özgüdür.

## Header arayüzleri

Header; I²C, SPI, akış kontrollü bir seri port, dört dijital ses sinyali ve 3,3 V GPIO bağlantıları sunar. Buna ek olarak Physical Pin 29, Physical Pin 31, Physical Pin 32 ve Physical Pin 33 üzerinde donanımsal PWM desteği bulunur. Bazı işlevler yalnızca ilgili Device Tree overlay'i `/boot/uEnv.txt` dosyasında etkinleştirildiğinde kullanılabilir. Herhangi bir cihaz bağlamadan önce açılış yapılandırmasını kontrol edin.

## Uyumlu HAT ve eklentiler

Bir eklentinin fiziksel olarak header'a takılabilmesi, elektriksel veya yazılımsal olarak uyumlu olduğu anlamına gelmez. [Uyumlu kartlar kataloğunda](/tr/boards) yalnızca T3 Gemstone O1 pin dizilimi, gerilim gereksinimleri, pin yönleri, Device Tree yapılandırması ve Linux sürücü desteği incelenmiş kartlar yer alır.

Bir eklenti, katalogda **Doğrulandı** veya **Koşullu uyumlu** durumu belirtilmedikçe T3 Gemstone O1 ile uyumlu kabul edilmemelidir.

Uyumluluk durumları:

* **Doğrulandı:** Donanım ve yazılım uyumluluğu test edilerek doğrulanmıştır.
* **Koşullu uyumlu:** Belirtilen sınırlamalar veya gerekli yapılandırmalar sağlandığında çalışabilir.
* **Uyumsuz:** T3 Gemstone O1 ile kullanılmamalıdır veya gerekli bir özellik desteklenmemektedir.

## Resmi kaynaklar

* [T3 Gemstone O1 dokümantasyonu](https://docs.t3gemstone.org/tr/boards/o1/introduction)
* [GPIO kılavuzu](https://docs.t3gemstone.org/tr/boards/o1/peripherals/gpio)
* [PWM kılavuzu](https://docs.t3gemstone.org/tr/boards/o1/peripherals/pwm)
* [Açık donanım tasarım dosyaları](https://github.com/t3gemstone/hardware)
