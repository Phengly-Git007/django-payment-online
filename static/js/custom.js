$(document).ready(function () {
  // decrement quantity
  $('.decrement-quantity').click(function (e) {
    e.preventDefault();
    var decrement = $(this)
      .closest('.product-data')
      .find('.quantity-input')
      .val();
    var value = parseInt(decrement, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value = value - 1;
      $(this).closest('.product-data').find('.quantity-input').val(value);
    }
  });

  // increment quantity
  $('.increment-quantity').click(function (e) {
    e.preventDefault();
    var increment = $(this)
      .closest('.product-data')
      .find('.quantity-input')
      .val();
    var value = parseInt(increment, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value = value + 1;
      $(this).closest('.product-data').find('.quantity-input').val(value);
    }
  });
});
