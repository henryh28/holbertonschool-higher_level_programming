// Ref: https://www.codecademy.com/courses/web-beginner-en-uCajg/0/1
$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
