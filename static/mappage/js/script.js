(function($) {
    "use strict";
    $(document).ready(function() {
        // $(".iconwrap .close-cion").on("click", function () {
        //     $(this).closest('.icon-submenu').hide();
        // });

        // $(".sidebar .sidebarClose").on("click", function () {
        //     $(this).closest(".sidebarwrapper").addClass("collapse-leftSidebar", 250);
        //     $(this).closest(".sidebar").find('.expand-icon').fadeIn(300);
        // });

        $(".hazard-details .hazardDetails-close").on("click", function () {
            $(this).closest(".hazard-wrapper").addClass("collapse-leftSidebar");
        });
        

        // $(".sidebar .expand-icon").on("click", function () {
        //     $(this).closest(".sidebar").find('.sidebarwrapper').removeClass("collapse-leftSidebar",300);
        //     $(this).closest(".sidebar").find('.expand-icon').fadeOut(300);
        // });
        // $(".sidebar .dataShow").on("click", function () {
        //     $(this).closest(".sidebar").hide();
        //     $('.data-sidebar').addClass('open-dataSidebar');
        // });
        // $(".data-sidebar .dataShow, .data-sidebar .sidebarClose").on("click", function () {
        //     $(".leftSidebar").show();
        //     $('.data-sidebar').removeClass('open-dataSidebar');
        // });

        $(".buffer-icon").on("click", function () {
            $(".buffer-list").toggle(500);
        });
        $(".buffer-list .buffer-header span").on("click", function () {
            $(this).closest(".buffer-list").hide(500);
        });

        
        $(".capacity-list .capacity-header i").on("click", function () {
            $(this).closest("li").find('ul').slideToggle(500);
            $(this).toggleClass('ion-ios-arrow-up');
        
        });
        $(".progress-title i").on("click", function () {
            $(this).closest(".progress-title").find('.info').slideToggle(500);
        
        });
        $(".updown i").on("click", function () {
            $(this).closest(".updown").find('.info').slideToggle(500);
        
        });

        var count= 0;
        $('.hazard-list label, .capacity-list label').on('click', function() {
            var targetId = $(this).attr('data-tab');
            $('#' + targetId).show(500);
            if (targetId == 'flood-1' ) {
                $('#flood-expand').fadeIn(300);
                count ++;
            } else if (targetId == 'capacity-popup' ) {
                    $('#capacity-expand').fadeIn(300);
                    count++;
                
            }
            else if (targetId == 'vulnery-1' ) {
                $('#vulnery-expand').fadeIn(300);
                count++;
            
        }
            // $('#flood-expand').fadeIn(300);
            // $('#capacity-expand').fadeIn(300);
            // $('#vulnery-expand').fadeIn(300);
        });
        $('.hazardDetails-close').on('click', function() {
            
            setTimeout(function(){
                var width = $('.hazardDetails-close').closest('.hazard-details').find(".hazard-wrapper").css('width');
                console.log($(".hazard-details"));
                
                for(var i=0;i<$(".hazard-wrapper").length;i++){
                    for(var j=0; j<$(".hazard-wrapper")[i].classList.length;j++){
                        console.log($(".hazard-wrapper")[i].classList[j]);
                        if ($(".hazard-wrapper")[i].classList[j] == "collapse-leftSidebar") {
                            console.log("ebdsfasdfas");
                            $('.expand-layer').css('right','325px');
                        } 
                    }
                }
                    
                 }, 100);
            
           
            
            // $('#flood-expand').fadeIn(300);
            // $('#capacity-expand').fadeIn(300);
            // $('#vulnery-expand').fadeIn(300);
        });
        
        // $('.submenu-list li.drop-list').prepend('<i class="ion ion ion-ios-add"></i>');
        // $('.submenu-list li.drop-list ul').hide();
        // $('.submenu-list li.drop-list i.ion-ios-add').on('click', function(){
        //     $(this).siblings('.submenu-list li.drop-list ul').slideToggle(500);
        //     $(this).toggleClass('list-open');
        // });

        $('.progress .progress-bar').css("width",
            function() {
                return $(this).attr("aria-valuenow") + "%";
            }
        )

        // function checkbox(){
        //     $(".custom-main-input").change(function () {
        //       $(this).closest('.check-list').find('.custom-checkbox input').prop('checked', $(this).prop("checked"));
        //     });
          
        //     $(".custom-checkbox input").change(function() {
        //         var checkboxes = $(this).closest('.custom-checkbox').find('input');
        //         var checkedboxes = checkboxes.filter(':checked');
            
        //         if(checkboxes.length === checkedboxes.length) {
        //         $(this).closest('.capacity-header').find('.custom-main-input').prop('checked', true);
        //         } else {
        //           $(this).closest('.capacity-header').find('.custom-main-input').prop('checked', false);
        //         }
        //     });
        //   };
        //   checkbox();

        //   $(".capacity-dropdown input").change(function () {
        //     $(this).closest('.check-list').find('.capacity-header .custom-main-input').prop('checked', true);
        //    });


        $(".leftSidebar .sidebarwrapper").slimScroll({
            height: "calc(100vh - 400px)",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: !1,
            borderRadius: "3px",
            railBorderRadius: "0"
        });
        $(".hazard-list").slimScroll({
            height: "132px",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: 1,
            borderRadius: "4px",
            railBorderRadius: "0"
        });

        $(".info-content").slimScroll({
            height: "150px",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: !1,
            borderRadius: "3px",
            railBorderRadius: "0"
        });

        // $(".rightSidebar .sidebarwrapper").slimScroll({
        //     height: "100vh",
        //     color: "#8c909a",
        //     position: "right",
        //     size: "4px",
        //     alwaysVisible: 1,
        //     borderRadius: "3px",
        //     railBorderRadius: "0"
        // });
        
        $('.select2').select2();

        $('.icon-list .ion-md-more').on('click', function(e) {
            e.preventDefault();
            $(this).closest('.upicon').attr('data-toggle','');
            var extraArea =$(this).closest('.icon-list');
			var outSideArea = $(this).closest('.icon-list').find('.more-list').toggle(300);
			$("body").mouseup(function(e) {
                if (!outSideArea.is(e.target) && extraArea.has(e.target).length === 0) {
                    outSideArea.fadeOut(300);
                }
            });

        });
        
    });
})(jQuery);


            