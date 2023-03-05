use products;

db.products.insertMany([
  {name: 'Hamburger', category: 'food', price: 1.9, amount: 45},
  {name: 'Coca-Cola', category: 'drink', price: 0.6, amount: 55},
  {name: 'Hot-dog', category: 'food', price: 1.3, amount: 34},
  {name: 'Milkshake', category: 'drink', price: 1.1, amount: 27}
]);

db.products.aggregate({$group: {'_id': '$category', total: {$sum: {$multiply: ['$price', '$amount']}}}});

db.products.updateMany({category: ['food', 'drink']}, {$inc: {amount: -1}});

db.products.find().sort({price: -1}).limit(2)

