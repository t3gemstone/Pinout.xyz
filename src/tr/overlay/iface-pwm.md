<!--
---
name: PWM
page_url: pwm
description: T3 Gemstone O1 donanımsal PWM destekli başlık pinleri
-->
# PWM - Darbe Genişlik Modülasyonu

Dört pin, donanım tabanlı PWM sinyali üretebilir. Bu sayede PWM sinyalinin zamanlaması işlemci yükünden bağımsız olarak kararlı şekilde korunur. Bu pinler iki çift halinde gruplandırılmıştır:

| Pinler | Kanallar |
| :-- | :-- |
| 29 ve 32 | PWM-0A ve PWM-0B |
| 31 ve 33 | PWM-1A ve PWM-1B |

Aynı çift içerisindeki iki pin ortak bir PWM frekansı kullanır; ancak her pinin görev döngüsü bağımsız olarak ayarlanabilir. Böylece iki farklı PWM frekansı üzerinde toplam dört bağımsız görev döngüsü yapılandırılabilir.

Bunları `/sys/class/pwm` üzerinden kontrol edebilirsiniz.

> **PWM pinleri güç çıkışı sağlamaz:** Bu pinler yalnızca 3,3 V lojik seviyesinde PWM sinyali sağlar. Servo, motor veya LED şeridi gibi yükler doğrudan PWM pinlerinden beslenmemelidir. Bu tür yükler için uygun bir harici güç kaynağı kullanılmalı, yükün toprak bağlantısı başlıktaki bir toprak pinine bağlanmalı ve gerekli durumlarda uygun bir sürücü devresi veya transistör kullanılmalıdır.
