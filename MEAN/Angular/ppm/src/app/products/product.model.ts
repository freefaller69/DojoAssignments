export class Product {

  public name: string;
  public price: number;
  public imagePath: string;

  constructor(name: string, price: number, imagePath: string){
    this.name = name;
    this.price = price;
    this.imagePath = imagePath;
  }

}
