const notMetni = document.getElementById('not-metni');
const fotografSec = document.getElementById('fotograf-sec');
const notKaydet = document.getElementById('not-kaydet');
const qrKoduAlani = document.getElementById('qr-kodu');

notKaydet.addEventListener('click', () => {
    const not = notMetni.value;
    const fotograf = fotografSec.files[0];

    // Fotoğrafı Base64'e dönüştür
    const okuyucu = new FileReader();
    okuyucu.onload = () => {
        const fotografBase64 = okuyucu.result;
        const veri = { not, fotograf: fotografBase64 };
        const veriJson = JSON.stringify(veri);

        // QR kod oluştur
        new QRCode(qrKoduAlani, veriJson);
    };
    if (fotograf) {
        okuyucu.readAsDataURL(fotograf);
    } else {
        const veri = { not, fotograf: null };
        const veriJson = JSON.stringify(veri);

        // QR kod oluştur
        new QRCode(qrKoduAlani, veriJson);
    }
});