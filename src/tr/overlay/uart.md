<!--
---
page_url: uart
description: T3 Gemstone O1 UART-MAIN1 başlık pinleri ve isteğe bağlı UART yönlendirmeleri
pin:
  '11':
    name: UART-MAIN1 RTS
  '36':
    name: UART-MAIN1 CTS
-->
# UART

Physical Pin 8 veri gönderimi (TX), Physical Pin 10 ise veri alımı (RX) için kullanılır. Linux üzerinde bu seri port /dev/ttyS3 aygıtı olarak görünür. Bağlantı sırasında harici cihazın RX hattını Physical Pin 8'e, TX hattını Physical Pin 10'a bağlayın ve cihaz ile kartın toprak bağlantılarını ortaklayın.

Physical Pin 11 ve Physical Pin 36, akış kontrolü gerektiren cihazlar için sırasıyla RTS ve CTS hatları olarak kullanılabilir. Basit seri haberleşme uygulamalarında bu hatlara genellikle ihtiyaç duyulmaz ve bağlantısız bırakılabilir.

> **Yalnızca 3,3 V lojik seviyesi kullanın:** Bu seri portu RS-232 arayüzüne veya 5 V lojik seviyeli bir seri dönüştürücüye doğrudan bağlamayın. Bu tür bağlantılar karta zarar verebilir. USB-seri bağlantısı için 3,3 V lojik seviyesini destekleyen bir USB-seri dönüştürücü veya uygun bir RS-232 seviye dönüştürücü kullanın.

Kart üzerindeki üç pinli konnektör, açılış konsolu için ayrılmış farklı bir seri porttur. Bu konnektör, Physical Pin 8, Physical Pin 10, Physical Pin 11 ve Physical Pin 36 üzerindeki seri port ile aynı arayüz değildir.