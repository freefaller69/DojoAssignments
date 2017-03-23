var students = [
     {first_name : 'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];

function studentList(obj) {
  for (var i = 0; i < obj.length; i++) {
    console.log(obj[i].first_name + ' ' + obj[i].last_name);
  }
}

studentList(students);
