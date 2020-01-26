import "../../../js/index";
import PartitialAjax from "django-partitialajax";
import {createPartitialFromElement} from "django-partitialajax/js/bindings";
import $ from "jquery";
import {getCookie} from "../../../../../partitialajax/src/js/contrib";

$(function () {
    PartitialAjax.initialize();
    let form_device_field = PartitialAjax.getPartitialFromElement(document.getElementById("publickey-create-device-field"));

    registerCreateDeviceButton(form_device_field);

    form_device_field.register("onHandeldRemoteData", function(info){
        registerCreateDeviceButton(form_device_field);
    });

    function registerCreateDeviceButton(partitial){

        let device_field_inner_create_button = $(partitial.options.element).find(".device-create-button").get( 0 );

        createPartitialFromElement(device_field_inner_create_button);

        let device_field_inner_create_partitial = PartitialAjax.getPartitialFromElement(device_field_inner_create_button);

        device_field_inner_create_partitial.register("onHandeldRemoteData", function(info){

            $(info.partitial_ajax.options.element).find("button").on("click", function(evt){
                evt.preventDefault();

                $.ajax({
                    type: 'POST',
                    url: $(info.partitial_ajax.options.element).find("form").attr("action"),
                    data: $(info.partitial_ajax.options.element).find("form").serialize(),
                    header: {
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                    success: function(response) {
                        //device_field_inner_create_partitial.delete();
                        partitial.getFromRemote();
                        $(info.partitial_ajax.options.element).modal('hide').find(".modal-content").html("");
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
            });

        });
    }



});
