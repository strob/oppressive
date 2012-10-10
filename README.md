# oppressive.js
---
totalizing objectification/subjectification

## About

Oppressive.js is a flexible base-class and manager
for (idiosyncratic) javascript pseudo-object patterns.

It is designed to run:

(a) without a webserver at all, by transforming data into code;

(b) in a fileserver environment, where XMLHttpRequests are permitted;

(c) and all the way up to a real-time node/socket server.

Oppressive is intended for ``medium-size'' data,
ie. data that packs down to a reasonable size for network transmission,
data that can be O(N) processed without a second thought.

## Build

Download the Google Closure compiler to the root directory, `compiler.jar.'

```sh
% make
```
## Usage

Oppressive is a hybrid fusion combining (some of) the
associativity of a relational database with (some of) the
looseness of document-based storage.

You can subclass ``OP.Objection'' to make your own objects.
For example:

```js
var ConsumerProduct = function(id, spec) {
  OP.Objection.call(this, id, spec);
};
ConsumerProduct.prototype = new OP.Objection;
ConsumerProduct.prototype.sale = function() {
  this.price *= 0.75;
};
```

When a program is initialized, data must be loaded.
Let's say we have our ConsumerProducts stored in a JSON file,
ConsumerProducts.json:

```js
{
  "nutella": {"price": 2.0, "qty": 10, "name": "Nutella"},
  "mate": {"price": 1.3, "qty": 40, "name": "Club Mate"}
}
```

Then, on page load, we might call something like:

```js
OP.Subjectification.load(
  {"ConsumerProducts": ConsumerProduct},
  function() {
    var products = OP.Subjectification.all(ConsumerProduct);
    products.forEach(function(product) {
        alert(product.name + ", $" + product.price);
        product.sale();
        alert("SALE! " + product.name + ", now only $" + product.price);
    });
  });
```

