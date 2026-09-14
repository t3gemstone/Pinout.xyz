<!--
---
name: 5 V Güç
page_url: 5v_power
description: T3 Gemstone O1 5 V başlık besleme pinleri
url: https://docs.t3gemstone.org/tr/boards/o1/peripherals/introduction
-->
# 5 V Güç

Physical Pin 2 ve Physical Pin 4, 3,3 V'tan daha yüksek besleme gerilimine ihtiyaç duyan çevre birimleri için 5 V besleme sağlar. Ancak sinyal pinleri yalnızca 3,3 V lojik seviyesini destekler. Bir çevre biriminin 5 V ile beslenebilmesi, bu cihazın GPIO pinlerine 5 V lojik sinyal uygulayabileceği anlamına gelmez.

Bu pinlerdeki 5 V besleme, harici güç kaynağından doğrudan sağlanmaz; kart üzerindeki güç regülatörü tarafından üretilir. Güç yönetimi yapılandırmasına bağlı olarak bu besleme hattı devre dışı bırakılabilir.

> **Buradan güç vermeyin:** Physical Pin 2 ve Physical Pin 4 numaralı pinler 5 V çıkışıdır. Bu pinlere harici 5 V uygulanması, kart üzerindeki güç regülatörüyle çakışmaya ve güç girişindeki koruma devrelerinin devre dışı kalmasına neden olabilir. Bu nedenle kartı bu pinler üzerinden beslemeyin.
