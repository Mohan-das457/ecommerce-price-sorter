// Array of product objects
const products = [
    { name: "Eco-Friendly Bottle", price: 25 },
    { name: "Bamboo Toothbrush", price: 10 },
    { name: "Solar Charger", price: 50 },
    { name: "Organic Tote Bag", price: 15 },
    { name: "Recycled Notebook", price: 30 }
];

// Sort products by price in ascending order
products.sort((a, b) => a.price - b.price);

console.log("Products sorted by price (Low to High):");
console.log(products);
