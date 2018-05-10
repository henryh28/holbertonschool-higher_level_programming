// Ref: https://stackoverflow.com/questions/16011312/execute-function-on-enter-key
// Ref: http://keycode.info

$(function () {
  function getWind () {
    let city = $('#city_search').val();

    $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json', function (data) {
      $('#wind_speed').text(data.query.results.channel.wind.speed);
    });
  }

  $('#btn_search').click(getWind);

  $('#city_search').on('keydown', function (event) {
    if (event.keyCode === 13) getWind();
  });
});
