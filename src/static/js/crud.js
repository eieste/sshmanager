import PartitialAjax from "django-partitialajax";
import $ from "jquery";
import sendForm from "./formModal";
import {getCookie} from "../../../partitialajax/src/js/contrib";

/**
 * Setup Crud Interface (Create Update Delete)
 * @param list_partitial Partitial Object of list
 * @param create_partitial Partitial Object of Create (Button)
 * @param delete_button_selector selector for all delete buttons inside of list
 */
function setupCrud(list_partitial, create_partitial, delete_button_selector, detail_button_selector=null){

    function subModal(url) {
        let delete_partitial = new PartitialAjax({
            "url": url,
            "element": document.getElementById("baseModal"),
            "textEventCallback": alert,
        }, {
            "onHandeldRemoteData": function (option) {
                $("#baseModal").modal();

                $(option.partitial_ajax.options.element).find("[type=submit]").on("click", function(e){
                    $.ajax({
                        type: 'POST',
                        url: $(option.partitial_ajax.options.element).find("form").attr("action"),
                        data: $(option.partitial_ajax.options.element).find("form").serialize(),
                        header: {
                            "X-CSRFToken": getCookie("csrftoken")
                        },
                        success: function(response) {
                            $(option.partitial_ajax.options.element).modal('hide');
                            list_partitial.getFromRemote();
                        },
                        error: function(){
                            $.toast({
                              title: gettext("Internal Server Error"),
                              content: gettext("This request could be satisfied"),
                              type: 'danger',
                              delay: 3000,
                            });
                        }
                    });
                    e.preventDefault();
                });
            },
            "onRemoteError": function(info){
                $.toast({
                  title: gettext("Internal Server Error"),
                  content: gettext("This request could be satisfied"),
                  type: 'danger',
                  delay: 3000,
                });
            },
            "onResponseError": function(info){
                $.toast({
                  title: gettext("Internal Server Error"),
                  content: gettext("This request could be satisfied"),
                  type: 'danger',
                  delay: 3000,
                });
            },
        });
    }

    function registerDeleteButton(list_element){
       $(list_element).find(delete_button_selector).on("click", function(event){
            let url = $(this).attr("href");
            subModal(url);
            event.preventDefault();
       });
    }

    function registerDetailButton(list_element){
        $(list_element).find(detail_button_selector).on("click", function(event){
            let url = $(this).attr("href");
            subModal(url);
            event.preventDefault();
        });
    }

    if(detail_button_selector != null){
        try{
            registerDetailButton(list_partitial.options.element);
        }catch (e) {
            console.info("CRUD: Cant find detail Buttons", e)
        }
    }

    try{
        registerDeleteButton(list_partitial.options.element);
    }catch (e) {
        console.info("CRUD: Cant find delete Buttons", e)
    }

    create_partitial.register("onHandeldRemoteData", function(option){
        $(option.partitial_ajax.options.element).find("[type=submit]").on("click", function(e){
            $.ajax({
                type: 'POST',
                url: $(option.partitial_ajax.options.element).find("form").attr("action"),
                data: $(option.partitial_ajax.options.element).find("form").serialize(),
                header: {
                    "X-CSRFToken": getCookie("csrftoken")
                },
                success: function(response) {
                    $(option.partitial_ajax.options.element).modal('hide');
                    list_partitial.getFromRemote();
                },
                error: function(){
                    $.toast({
                      title: gettext("Internal Server Error"),
                      content: gettext("This request could be satisfied"),
                      type: 'danger',
                      delay: 3000,
                    });
                }
            });
            e.preventDefault();
        });
    });

    create_partitial.register("onRemoteError", function(option){
        console.log(option);
    });

    create_partitial.register("onResponseError", function(option){
        console.log(option);
    });

    // Register Load Buttons
    list_partitial.register("onHandeldRemoteData", function(info){
        registerDeleteButton(info.partitial_ajax.options.element);
    });

    list_partitial.register("onRemoteError", function(info){
        $.toast({
          title: gettext("Internal Server Error"),
          content: gettext("This request could be satisfied"),
          type: 'danger',
          delay: 3000,
        });
    });

}

export default setupCrud;