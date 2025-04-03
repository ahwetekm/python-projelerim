document.getElementById("noteForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const noteText = document.getElementById("noteText").value;
    const imageFile = document.getElementById("imageUpload").files[0];
    
    if (!noteText && !imageFile) {
        alert("Lütfen bir not yazın veya bir fotoğraf yükleyin!");
        return;
    }

    const data = { text: noteText };

    if (imageFile) {
        const reader = new FileReader();

        // Dosya okuma işlemi tamamlandığında QR kodu oluşturuluyor
        reader.onload = () => {
            data.image = reader.result; // Base64 olarak resim verisini ekliyoruz
            generateQRCode(data);       // QR kod oluşturma işlemi
        };

        reader.onerror = () => {
            console.error("Dosya yüklenirken bir hata oluştu.");
            alert("Resim yükleme işlemi başarısız oldu!");
        };

        // Dosya okuma işlemini başlatıyoruz
        reader.readAsDataURL(imageFile);
    } else {
        generateQRCode(data); // Resim yoksa yalnızca metni işliyoruz
    }
});

function generateQRCode(data) {
    const qrCodeContainer = document.getElementById("qrCodeContainer");
    qrCodeContainer.innerHTML = ""; // Eski QR kodunu temizliyoruz
    
    QRCode.toCanvas(
        qrCodeContainer,
        JSON.stringify(data),
        { width: 250 },
        (err) => {
            if (err) {
                console.error("QR kod oluşturulurken bir hata oluştu:", err);
                alert("QR kod oluşturulamadı!");
            } else {
                console.log("QR kod başarıyla oluşturuldu!");
            }
        }
    );
}
