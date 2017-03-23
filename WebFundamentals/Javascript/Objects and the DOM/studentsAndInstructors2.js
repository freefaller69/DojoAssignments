var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
};

 function usersList(obj) {
  var keys = Object.keys(obj);
  for (var i = 0; i < keys.length; i++){
    var curKey = keys[i];
    console.log(curKey);
    var userList = obj[curKey];
    for (var j = 0; j < userList.length; j++) {
      var user = userList[j];
      var name = (user.first_name + ' ' + user.last_name);
      console.log((j + 1) + " - " + name + " - " + (name.length - 1));
    }
  }
 }

 usersList(users);
