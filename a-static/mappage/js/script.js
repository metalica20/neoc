(function(jQuery) {
    "use strict";
    $(window).on('load', function() {
        $('.load-popup').fadeIn(5000);
    });
    
    $(document).ready(function() {

        $(".iconwrap a.more-option").on("click", function (e) {
            e.preventDefault();
            $(this).parent().find("ul.dropicons-list").addClass("open", 1000);
        });

        $(".dropicons-list .close-cion").on("click", function () {
            $(this).parent("ul.dropicons-list").removeClass("open", 1000);
        });

        $(".arrow-left").on("click", function () {
            $(this).css({"transform":"rotate(180deg)"});
            $(this).parent(".sidebar.leftSidebar").toggleClass('resize-sidebar');
            $(this).parent(".sidebar.leftSidebar").find('.sidebarwrapper').toggle(300);
        });

        $(".arrow-right").on("click", function () {
            $(this).css({"transform":"rotate(180deg)"});
            $(this).parent(".rightSidebar").toggleClass('resize-sidebar');
            $(this).parent(".rightSidebar").find('.sidebarwrapper').toggle(300);
        });

        /*====================================
        // menu-fix
        ======================================*/

        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 50) {
                $('.site-header').addClass("affix", 500);
            } else {
                $('.site-header').removeClass("affix", 500);
            }
        });

        
        
    });
})(jQuery);

