django.jQuery(document).on('formset:added', function(event, $row, formsetName) {
    $row.find('.select2-container').remove();
    //FIXME: temp dirty fix
    setTimeout(
        () => jQuery('.django-select2').djangoSelect2(),
        200
    );
});

django.jQuery(document).on('formset:removed', function(event, $row, formsetName) {
    // Row removed
});
