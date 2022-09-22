$('INPUT#btn_translate').click(function () {
  const value = $('INPUT#language_code').val();
  const url = 'https://stefanbohacek.com/hellosalut/?lang=' + value;
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
