(function($) {
    "use strict";
    $(document).ready(function() {
        $(".iconwrap .close-cion").on("click", function () {
            $(this).closest('.icon-submenu').hide();
        });

        $(".sidebar .sidebarClose").on("click", function () {
            $(this).closest(".sidebarwrapper").addClass("collapse-leftSidebar");
            $(this).closest(".sidebar").find('.expand-icon').fadeIn(300);
        });
        

        $(".sidebar .expand-icon").on("click", function () {
            $(this).closest(".sidebar").find('.sidebarwrapper').removeClass("collapse-leftSidebar");
            $(this).closest(".sidebar").find('.expand-icon').fadeOut(300);
        });
        $(".sidebar .dataShow").on("click", function () {
            $(this).closest(".sidebar").hide();
            $('.data-sidebar').addClass('open-dataSidebar');
        });
        $(".data-sidebar .dataShow, .data-sidebar .sidebarClose").on("click", function () {
            $(".leftSidebar").show();
            $('.data-sidebar').removeClass('open-dataSidebar');
        });

        $(".buffer-icon").on("click", function () {
            $(".buffer-list").toggle(500);
        });
        $(".buffer-list .buffer-header span").on("click", function () {
            $(this).closest(".buffer-list").hide(500);
        });

        $('.iconwrap a').on('click', function(e) {
            e.preventDefault();
            var targetId = $(this).attr('data-tab');
            $('#' + targetId).show(500);

        });
        
        $('.submenu-list li.drop-list').prepend('<i class="ion ion ion-ios-add"></i>');
        $('.submenu-list li.drop-list ul').hide();
        $('.submenu-list li.drop-list i.ion-ios-add').on('click', function(){
            $(this).siblings('.submenu-list li.drop-list ul').slideToggle(500);
            $(this).toggleClass('list-open');
        });

        

        $('[data-toggle="tooltip"]').tooltip()


        $(".leftSidebar .sidebarwrapper").slimScroll({
            height: "calc(100vh - 68px)",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: !1,
            borderRadius: "3px",
            railBorderRadius: "0"
        });
        $(".data-sidebar .sidebarwrapper .card").slimScroll({
            height: "calc(100vh - 68px)",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: !1,
            borderRadius: "3px",
            railBorderRadius: "0"
        });

        $(".rightSidebar .sidebarwrapper").slimScroll({
            height: "100vh",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: !1,
            borderRadius: "3px",
            railBorderRadius: "0"
        });
        
        
    });
})(jQuery);


            