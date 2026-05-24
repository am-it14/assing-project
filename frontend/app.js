require('dotenv').config();
const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:8000/api';


app.use(express.urlencoded({ extended: true }));
app.use(express.json());


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});


app.post('/submit', async (req, res) => {
    try {
        const response = await fetch(`${BACKEND_URL}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: req.body.name,
                age: req.body.age,
                mobile: req.body.mobile,
                email: req.body.email
            }) 
        });

        const flaskData = await response.json();

        res.send(`
            <div>
                <h2>Success!</h2>
                <p style="color: green;">${flaskData.message}</p>
                <br>
                <a href="/">Go Back</a>
            </div>
        `);

    } catch (error) {
    console.error(error);

    res.status(500).send(error.message);
}
});

// Start the Express server
app.listen(PORT, () => {
    console.log(`Frontend server running on http://localhost:${PORT}`);
});