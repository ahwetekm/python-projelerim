# QR Project

Bu proje, kullanıcıların not oluşturabileceği ve bu notlara fotoğraf ekleyebileceği bir web uygulamasıdır. Uygulama, kullanıcıların oluşturduğu notları depolamak için Firebase veritabanını kullanmaktadır. Ayrıca, her not için bir QR kodu oluşturulmakta ve bu QR kodu diğer kullanıcılar tarafından taranarak notlara erişim sağlanmaktadır.

## Proje Yapısı

- **index.html**: Web sitesinin ana sayfası. Kullanıcıların not oluşturabileceği bir form içerir ve QR kodunu görüntülemek için gerekli alanları barındırır.
- **styles/style.css**: Web sitesinin stilini tanımlar. Renkler, yazı tipleri ve düzen gibi görsel unsurları içerir.
- **scripts/app.js**: Web sitesinin işlevselliğini sağlar. Kullanıcıların not oluşturmasını, fotoğraf eklemesini ve QR kodu oluşturmasını sağlayan JavaScript kodlarını içerir. Ayrıca, Firebase ile etkileşim kurarak notları depolar.
- **assets/images**: Kullanıcıların yüklediği fotoğrafları saklamak için kullanılır.
- **assets/qr-codes**: Oluşturulan QR kodlarını saklamak için kullanılır.
- **README.md**: Projenin açıklamasını ve kullanım talimatlarını içerir.
- **.gitignore**: Git tarafından izlenmemesi gereken dosya ve klasörleri belirtir.

## Kullanım Talimatları

1. Projeyi klonlayın veya indirin.
2. Firebase projesi oluşturun ve gerekli ayarları yapın.
3. `scripts/app.js` dosyasında Firebase yapılandırmasını güncelleyin.
4. `index.html` dosyasını bir tarayıcıda açarak uygulamayı kullanmaya başlayın.

## Katkıda Bulunma

Herhangi bir katkıda bulunmak isterseniz, lütfen bir pull request oluşturun veya sorunlarınızı bildirin.