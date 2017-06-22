function VehicleConstructor(name,numWheels,numPass){
  var vehicle = {};
  vehicle.name = name;
  vehicle.numWheels = numWheels;
  vehicle.numPass = numPass;
  vehicle.makeNoise = function(){
    console.log("Vroom");
  };
  return vehicle;
}

var bike = VehicleConstructor("bike",2,1);
bike.makeNoise = function(){
  console.log("ring ring");
};
bike.makeNoise();

var sedan = VehicleConstructor("sedan",4,5);
sedan.makeNoise = function(){
  console.log("honk honk");
};
sedan.makeNoise();

var bus = VehicleConstructor("bus",10,50);
bus.passCount = function(numPass){
  bus.numPass += numPass;
};
bus.passCount(7);
console.log(bus.numPass)
