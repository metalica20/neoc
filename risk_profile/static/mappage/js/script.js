(function($) {
    "use strict";
    $(document).ready(function() {


        // $(".iconwrap .close-cion").on("click", function () {
        //     $(this).closest('.icon-submenu').hide();
        // });
        $('.compare-button').on('click', function(){
            $('.compare-wrapper').slideToggle(300);
            $("#chart").html('<span>Click on the map to compare</span>');
        });
        $('.compare-header ').on('click','span', function(){
            $('.compare-wrapper').hide(300);
        });



        $(".hazard-details").on("click",".hazardDetails-close", function () {


          // id=$('.hazard-details').attr('id');
          //
            // console.log(id);
          var  id=$(this).closest(".hazard-details").attr('id');
            //$('#'+id).css('display','none');
            $('#'+id).hide(300);



            //$(this).closest(".hazard-wrapper").addClass("collapse-leftSidebar");
        });
        $(".hazard-title ").on("click",'.average-open', function () {
            $(".average-section").show(300);
        });
        $(".average-section").on("click",'.averageClose', function () {
            $(this).closest(".average-section").hide(300);
        });
        $(".metaData-header").on("click",'.metaClose', function () {
            $(this).closest(".metaData").hide(300);
        });
        $(".icon-list").on("click",'.ion-md-albums', function () {
            $(this).closest('.card').find('.collapse ').removeClass('show');
			   $(".metaData").show(500);

        });

        $(".trans_constrast").on("click",'.ion', function () {
          $(this).toggleClass('active');

        });

        $(".trans_constrast").on("click",'.ion-md-contrast', function () {
          console.log("enteddddd");

         //console.log($(this).closest('.card').find('.range-box'));
         //$(this).closest('.card').find('.collapse ').addClass('show');
			  $(this).closest('.opacityParent').find('.range-box').toggle(300);
			 //console.log($(this).closest('.card').find('.range-box').css('display'));


       // setTimeout
     //     setTimeout(function(){
     //   $(this).closest('.card').find('.collapse ').addClass('show');
     // }, 4000);

        });



        // $(".trans_constrast_expo").on("click",'.ion-md-contrast', function () {
        //   console.log($(this).siblings('.opacityParent'));
        //   $(this).siblings('.opacityParent').find('range-box');
        //
        // })




        $(".buffer-list .buffer-header span").on("click", function () {
            $(this).closest(".buffer-list").hide(500);
        });
        $(".legend-list").on("click",".ion-md-close", function () {

            $(this).closest(".legend-wrapper").hide(500);
        });
        $(".updown").on("click",'i', function () {
            $(this).closest('.card').find('.collapse ').removeClass('show');
            var info =$(this).closest('.info');
			var infoOut = $(this).closest(".updown").find('.info').slideToggle(500);
			$("body").mouseup(function(e) {
                if (!infoOut.is(e.target) && info.has(e.target).length === 0) {
                    infoOut.fadeOut(300);
                }
            });

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


        $('.hazard-list label, .capacity-list label').on('click', function() {
            var targetId = $(this).attr('data-tab');
            // ('#hazard_popup_html').removeClass('collapse-leftSidebar');
            //console.log(targetId);
            if (targetId == 'flood-1' ) {

                $('#' + targetId).show(500);
                $('#exposure_popup').hide(300);
                $('#infa_exposure_popup').hide(300);
                $('#capacity-popup').hide(300);
                $('#vulnery-1').hide(300);
                $('#hdi_vul').hide(300);
                $('#remote_vul').hide(300);
                $('#earthquake_risk').hide(300);
                $('#osmLayer_popup').hide(300);
                $('#pci_vul').hide(300);
                $('#le_vul').hide(300);
                $('#hpi_vul').hide(300);
                $('#awt_vul').hide(300);
                $('#toil_vul').hide(300);

              } else if (targetId == 'exposure_popup' ) {
                $('#infa_exposure_popup').hide(300);
                $('#' + targetId).show(500);
                $('#flood-1').hide(300);
                $('#capacity-popup').hide(300);
                $('#vulnery-1').hide(300);
                $('#hdi_vul').hide(300);
                $('#remote_vul').hide(300);
                $('#earthquake_risk').hide(300);
                $('#osmLayer_popup').hide(300);
                $('#pci_vul').hide(300);
                $('#le_vul').hide(300);
                $('#hpi_vul').hide(300);
                $('#awt_vul').hide(300);
                $('#toil_vul').hide(300);

            } else if (targetId == 'infa_exposure_popup' ) {
              $('#exposure_popup').hide(300);
              $('#' + targetId).show(500);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);


            } else if (targetId == 'capacity-popup' ) {

                    $('#' + targetId).show(500);
                    $('#exposure_popup').hide(300);
                    $('#infa_exposure_popup').hide(300);
                    $('#flood-1').hide(300);
                    $('#vulnery-1').hide(300);
                    $('#hdi_vul').hide(300);
                    $('#remote_vul').hide(300);
                    $('#earthquake_risk').hide(300);
                    $('#osmLayer_popup').hide(300);
                    $('#pci_vul').hide(300);
                    $('#le_vul').hide(300);
                    $('#hpi_vul').hide(300);
                    $('#awt_vul').hide(300);
                    $('#toil_vul').hide(300);
            }
            else if (targetId == 'vulnery-1' ) {

                $('#' + targetId).show(500);
                $('#exposure_popup').hide(300);
                $('#infa_exposure_popup').hide(300);
                $('#flood-1').hide(300);
                $('#capacity-popup').hide(300);
                $('#hdi_vul').hide(300);
                $('#remote_vul').hide(300);
                $('#earthquake_risk').hide(300);
                $('#osmLayer_popup').hide(300);
                $('#pci_vul').hide(300);
                $('#le_vul').hide(300);
                $('#hpi_vul').hide(300);
                $('#awt_vul').hide(300);
                $('#toil_vul').hide(300);


        }else if (targetId == 'hdi_vul' ) {

            $('#' + targetId).show(500);
            $('#exposure_popup').hide(300);
            $('#infa_exposure_popup').hide(300);
            $('#flood-1').hide(300);
            $('#capacity-popup').hide(300);
            $('#vulnery-1').hide(300);
            $('#remote_vul').hide(300);
            $('#earthquake_risk').hide(300);
            $('#osmLayer_popup').hide(300);
            $('#pci_vul').hide(300);
            $('#le_vul').hide(300);
            $('#hpi_vul').hide(300);
            $('#awt_vul').hide(300);
            $('#toil_vul').hide(300);


          }else if (targetId == 'remote_vul' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);


          }else if (targetId == 'earthquake_risk' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);


          }else if (targetId == 'osmLayer_popup' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);



          }else if (targetId == 'pci_vul' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);




          }else if (targetId == 'le_vul' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);



          }else if (targetId == 'hpi_vul' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#awt_vul').hide(300);
              $('#toil_vul').hide(300);



          }else if (targetId == 'awt_vul' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#toil_vul').hide(300);



          }else if (targetId == 'toil_vul' ) {

              $('#' + targetId).show(500);
              $('#exposure_popup').hide(300);
              $('#infa_exposure_popup').hide(300);
              $('#flood-1').hide(300);
              $('#capacity-popup').hide(300);
              $('#vulnery-1').hide(300);
              $('#hdi_vul').hide(300);
              $('#remote_vul').hide(300);
              $('#earthquake_risk').hide(300);
              $('#osmLayer_popup').hide(300);
              $('#pci_vul').hide(300);
              $('#le_vul').hide(300);
              $('#hpi_vul').hide(300);
              $('#awt_vul').hide(300);



          }
            // $('#flood-expand').fadeIn(300);
            // $('#capacity-expand').fadeIn(300);
            // $('#vulnery-expand').fadeIn(300);earthquake_risk
        });
        //
        // $('.exoposure_data_pop').on('click',function(){
        //   var targetId = $(this).attr('data-tab');
        //   console.log(targetId);
        //     $('#exposure_popup').show(500);
        //
        // });

        // $('.hazardDetails-close_ex').on('click', function() {
        //   console.log($(this).closest('.hazard-details').attr('id'));
        //  id=$(this).attr('id');
          //$('#'+id).css('display','none');


            // setTimeout(function(){
            //     var width = $('.hazardDetails-close').closest('.hazard-details').find(".hazard-wrapper").css('width');
            //     console.log($(".hazard-details"));
            //
            //     for(var i=0;i<$(".hazard-wrapper").length;i++){
            //         for(var j=0; j<$(".hazard-wrapper")[i].classList.length;j++){
            //             console.log($(".hazard-wrapper")[i].classList[j]);
            //             if ($(".hazard-wrapper")[i].classList[j] == "collapse-leftSidebar") {
            //                 console.log("ebdsfasdfas");
            //                 $('.expand-layer').css('right','325px');
            //             }
            //         }
            //     }
            //
            //      }, 100);



            // $('#flood-expand').fadeIn(300);
            // $('#capacity-expand').fadeIn(300);
            // $('#vulnery-expand').fadeIn(300);
       // });

      // $('#Flood').on('click',function(){
      //   console.log('aaaa');
      //   ('#hazard_popup_html').removeClass('collapse-leftSidebar');
      //
      // });

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
        $("#federal_boundary").slimScroll({
            height: "200px",
            color: "#8c909a",
            position: "right",
            size: "2px",
            alwaysVisible: !1,
            borderRadius: "3px",
            railBorderRadius: "0"
        });
        $(".compare-body").slimScroll({
            height: "250px",
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

        $(".average-content").slimScroll({
            height: "500px",
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

        $("[type=range]").on("change ", function() {
            $(".range-index").html($(this).val());
         });

        $('.select2').select2();

        $('.trans_constrast ').on('click', '.ion-md-more', function(e) {
            e.preventDefault();
            $(this).closest('.icon-list').find('.more-list').toggle(300);
      //       var extraArea =$(this).closest('.icon-list');
			// var outSideArea = $(this).closest('.icon-list').find('.more-list').toggle(300);


        });
        setTimeout(function(){
        $('[data-toggle="popover"]').popover();
       },3000);

       $(".bipadContent").on("click ",".custom-control-input", function() {
         console.log('open');
           $(this).closest('.custom-radio').toggleClass('custom-check');
        });

        $(".filterSelect").on("click","input", function() {
            $(this).closest('.filterSelect').find('.filter-listing').show();
         });

         $(".filter_close").on("click", function() {
             $(this).closest('.filterSelect').find('.filter-listing').hide();
               $('.federal').css('display','');
             $('#fed_filterInput').val("");
             if(map.hasLayer(federal_boundary)){
               map.removeLayer(federal_boundary);
               map.removeLayer(label);
             }
             map.addLayer(province);
             map.addLayer(vt_label_province);
             map.setView([28.410728397237914,84.4024658203125], 7);
          });


          $(".filter_dropdown").on("click", function() {
              $(this).closest('.filterSelect').find('.filter-listing').show();
           });



         $(".filterSelect").on("hover",".type-wrap", function() {
             $('.filterSelect').find('.ion-md-close').hide();
          });
    });
})(jQuery);
