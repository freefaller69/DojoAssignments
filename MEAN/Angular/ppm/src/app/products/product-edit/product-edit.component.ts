import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { FormGroup, FormControl, FormArray, Validators } from '@angular/forms';

import { Product } from '../product.model';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-product-edit',
  templateUrl: './product-edit.component.html',
  styleUrls: ['./product-edit.component.css']
})
export class ProductEditComponent implements OnInit {
  id: number;
  editMode = false;
  productForm: FormGroup;

  constructor(private route: ActivatedRoute,
              private productService: ProductService,
              private router: Router) { }

  ngOnInit() {
    this.route.params
      .subscribe(
        (params: Params) => {
          this.id =+params['id'];
          this.editMode = params['id'] != null;
          this.initForm();
        }
      );
  }

  onSubmit() {
    if(this.editMode){
      this.productService.updateProduct(this.id, this.productForm.value);
    } else {
      this.productService.addProduct(this.productForm.value);
    }
    this.onCancel();
  }

  onAddProduct(){
    (<FormArray>this.productForm.get('products')).push(
      new FormGroup({
        'name': new FormControl(null, Validators.required),
        'imagePath': new FormControl(null, Validators.required),
        'price': new FormControl(null, [
          Validators.required,
          Validators.pattern(/^[1-9]+[0-9]*$/)
        ])
      })
    );
  }

  onClear(){
    this.productForm.reset();
    this.editMode = false;
  }

  onDelete(index: number){
    (<FormArray>this.productForm.get('products')).removeAt(index);
    // this.productService.deleteProduct(this.editedItemIndex);
    // this.onClear();
  }

  private initForm() {
    let productName = '';
    let productImagePath = '';
    let productPrice;
    let productItems = new FormArray([]);

    if (this.editMode) {
      const product = this.productService.getProduct(this.id);
      productName = product.name;
      productImagePath = product.imagePath;
      productPrice = product.price;
    }
    this.productForm = new FormGroup({
      'name': new FormControl(productName, [Validators.required, Validators.minLength(4)]),
      'imagePath': new FormControl(productImagePath, Validators.required),
      'price': new FormControl(productPrice, [Validators.required, Validators.pattern(/^\d[\d\,\.]*$/)]),
    });
  }

  onCancel() {
    this.router.navigate(['../'], {relativeTo: this.route});
  }

}
