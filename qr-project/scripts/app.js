// scripts/app.js

// Firebase configuration
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Reference to the database
const db = firebase.database();

// Function to create a note
function createNote() {
    const noteText = document.getElementById('noteText').value;
    const imageFile = document.getElementById('imageFile').files[0];

    if (noteText && imageFile) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const imageData = event.target.result;

            // Save note and image to Firebase
            const noteId = db.ref('notes').push().key;
            db.ref('notes/' + noteId).set({
                text: noteText,
                image: imageData
            }).then(() => {
                generateQRCode(noteId);
            });
        };
        reader.readAsDataURL(imageFile);
    } else {
        alert("Please enter a note and select an image.");
    }
}

// Function to generate QR code
function generateQRCode(noteId) {
    const qrCodeUrl = `https://yourwebsite.com/note/${noteId}`;
    const qrCodeElement = document.getElementById('qrCode');

    // Use a QR code library to generate the QR code
    const qrCode = new QRCode(qrCodeElement, {
        text: qrCodeUrl,
        width: 128,
        height: 128,
    });

    alert("QR Code generated! Share it with others.");
}

// Event listener for form submission
document.getElementById('noteForm').addEventListener('submit', function(event) {
    event.preventDefault();
    createNote();
});