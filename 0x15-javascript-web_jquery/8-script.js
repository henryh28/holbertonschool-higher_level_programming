$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (let film of data.results) {
    $('#list_movies').append('<li>' + film.title + '</li>');
  }
});
