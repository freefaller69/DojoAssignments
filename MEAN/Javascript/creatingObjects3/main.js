function VehicleConstructor(name,numWheels,numPass,speed){
  if (!(this instanceof VehicleConstructor)) {
     return new VehicleConstructor(name,numWheels,numPass,speed);
   }
   var chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  this.distance_travelled = 0;
  this.name = name;
  this.numWheels = numWheels || 4;
  this.numPass = numPass || 1;
  this.speed = speed;
  this.vin = generateVIN();

  function generateVIN(){
    var vin = '';
    for(var i = 0; i < 17; i++){
      vin += chars[Math.floor(Math.random()*chars.length)];
    }
    return vin;
  }
}

VehicleConstructor.prototype.makeNoise = function(noise) {
    noise = noise || "vroom";
    console.log(noise);
    return this;
};

VehicleConstructor.prototype.move = function() {
  this.makeNoise();
  this.update_distance_travelled();
  return this;
};

VehicleConstructor.prototype.checkMiles = function() {
    console.log(this.distance_travelled);
    return this;
};

VehicleConstructor.prototype.update_distance_travelled = function(){
    this.distance_travelled += this.speed;
    console.log(this.distance_travelled);
};


var sedan = new VehicleConstructor("sedan",4,5,75);
sedan.makeNoise().move().checkMiles().update_distance_travelled();
