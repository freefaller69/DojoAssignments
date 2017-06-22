function VehicleConstructor(name,numWheels,numPass,speed){
  if (!(this instanceof VehicleConstructor)) {
     // the constructor was called without "new".
     return new VehicleConstructor(name,numWheels,numPass,speed);
   }
  var distance_travelled = 0;
  var self = this;
  function update_distance_travelled(){
    distance_travelled += self.speed;
    console.log(distance_travelled);
  }

  this.name = name;
  this.numWheels = numWheels || 4;
  this.numPass = numPass || 1;
  this.speed = speed;
  this.makeNoise = function(noise){
    noise = noise || "vroom";
    console.log(noise);
  };
  this.move = function(){
    this.makeNoise();
    update_distance_travelled();
  };
  this.checkMiles = function(){
    console.log(distance_travelled);
  };
}

var bike = new VehicleConstructor("bike",2,1,15);
bike.move();
bike.checkMiles();
console.log(bike.speed);

var sedan = new VehicleConstructor("sedan",4,5,75);
sedan.move();
sedan.checkMiles();
console.log(sedan.speed);


var bus = new VehicleConstructor("bus",10,1,50);
bus.move();
bus.checkMiles();
console.log(bus.speed);
