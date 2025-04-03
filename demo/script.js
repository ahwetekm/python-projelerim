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
        reader.onload = () => {
            data.image = reader.result;

            generateQRCode(data);
        };
        reader.readAsDataURL(imageFile);
    } else {
        generateQRCode(data);
    }
});

function generateQRCode(data) {
    const qrCodeContainer = document.getElementById("qrCodeContainer");
    qrCodeContainer.innerHTML = ""; // Eski QR kodunu temizler
    QRCode.toCanvas(
        JSON.stringify(data), 
        { width: 250 }, 
        (err, canvas) => {
            if (err) console.error(err);
            qrCodeContainer.appendChild(canvas);
        }
    );
}

const data = { text: noteText };

if (imageFile) {
    const reader = new FileReader();
    reader.onload = () => {
        data.image = reader.result; // Dosya içeriğini ekliyoruz
        generateQRCode(data); // QR kod oluşturuyoruz
    };
    reader.readAsDataURL(imageFile);
} else {
    generateQRCode(data); // Resim yoksa yalnızca metni gönderiyoruz
}

QRCode.toCanvas(
    JSON.stringify(data), 
    { width: 250 }, 
    (err, canvas) => {
        if (err) {
            console.error("QR kod oluşturulurken hata:", err);
            return;
        }
        qrCodeContainer.appendChild(canvas);
    }
);
