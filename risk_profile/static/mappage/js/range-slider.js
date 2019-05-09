
setTimeout(function(){
  console.log('function');
  console.log($(".slider"));
$(".slider").each(function () {
  console.log('each');
    //$this is a reference to .slider in current iteration of each
    var $this = $(this);
    //find any .slider-range element WITHIN scope of $this
          $(".slider-range", $this).slider({
              range: true,
              min: 0,
              max: 1000,
              values: [300, 600],
              slide: function (event, ui) {
                  // find any element with class .amount WITHIN scope of $this
                  $(".amount", $this).val( ui.values[0] + " - " + ui.values[1]);
              }
          });
          $(".amount").val($(".slider-range").slider("values", 0) + " - " + $(".slider-range").slider("values", 1));
});
}, 10000);
