import express from 'express'; 
import dotenv from 'dotenv';
import { connectDB } from './config/db.js';

dotenv.config(); // Load environment variables from .env file
console.log("Loaded MONGO_URI:", process.env.MONGO_URI); // Debugging
console.log("Loaded SECRET_TOKEN:", process.env.SECRET_TOKEN);

const app = express();

app.use(express.json()); // Middleware to parse JSON request bodies, allows us to accept JSON data in body

const authorize = (req, res, next) => {
    console.log("Authorize middleware triggered"); // Debugging
    const authHeader = req.headers.authorization;
    console.log("Authorization Header:", authHeader); // Debugging

    if (!authHeader || !authHeader.startsWith("Bearer ")) {
        console.log("Missing or invalid Authorization header");
        return res.status(403).json({ success: false, message: "Access forbidden: Missing or invalid authorization header" });
    }

    const token = authHeader.split(" ")[1];
    console.log("Token Received:", token); // Debugging
    console.log("Expected Token:", process.env.SECRET_TOKEN); // Debugging

    if (token !== process.env.SECRET_TOKEN) {
        console.log("Invalid token");
        return res.status(403).json({ success: false, message: "Access forbidden: Invalid token" });
    }

    next(); // Proceed to the next middleware or route handler
};

// Comment out the middleware for now
// app.use(authorize);

app.post("/api/products", async (req, res) => {
    console.log("POST /api/products triggered"); // Debugging
    const product = req.body;
    console.log("Request Body:", product); // Debugging

    if (!product.name || !product.price || !product.image) {
        console.log("Validation failed: Missing fields");
        return res.status(400).json({ success: false, message: "All fields are required" });
    }

    const newProduct = new Product(product);

    try {
        await newProduct.save();
        console.log("Product saved successfully:", newProduct); // Debugging
        res.status(201).json({ success: true, data: newProduct });
    } catch (error) {
        console.error("Error in created product:", error.message);
        res.status(500).json({ success: false, message: "Server Error" });
    }
});

app.listen(5000, () => {
    connectDB(); // Connect to the mongodb database
    console.log("Server started at http://localhost:5000");
});

