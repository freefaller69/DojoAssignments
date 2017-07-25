import { Injectable } from '@angular/core';
import { Subject } from 'rxjs/Subject';

import { Product } from './product.model';

@Injectable()
export class ProductService {
  productsChanged = new Subject<Product[]>();
  startedEditing = new Subject<number>();

  private products: Product[] = [
    new Product(
      'DSLR Camera',
      1499.99,
      'https://static.pexels.com/photos/249597/pexels-photo-249597.jpeg'),
    new Product(
      'Laptop',
      1299.99,
      'https://static.pexels.com/photos/257949/pexels-photo-257949.jpeg'),
  ];

  constructor() {}

  getProducts() {
    return this.products.slice();
  }

  getProduct(index: number) {
    return this.products[index];
  }

  addProduct(product: Product) {
    this.products.push(product);
    this.productsChanged.next(this.products.slice());
  }

  updateProduct(index: number, newProduct: Product) {
    this.products[index] = newProduct;
    this.productsChanged.next(this.products.slice());
  }

  deleteProduct(index: number) {
    this.products.splice(index, 1);
    this.productsChanged.next(this.products.slice());
  }

}
