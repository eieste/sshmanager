import "../../../js/index";
import PartitialAjax from "django-partitialajax";
import {createPartitialFromElement} from "django-partitialajax/js/bindings";
import $ from "jquery";
import {getCookie} from "../../../../../partitialajax/src/js/contrib";

$(function () {

    PartitialAjax.initialize();

    let form_device_field = PartitialAjax.getPartitialFromElement(document.getElementById("publickey-create-device-field"));
    registerLazyPartitialButton(form_device_field, ".userarea-device-create-button");

    form_device_field.register("onHandeldRemoteData", function(info){
        registerLazyPartitialButton(info.partitial_ajax, ".userarea-device-create-button");
    });



    let form_key_group_field = PartitialAjax.getPartitialFromElement(document.getElementById("publickey-create-key-group-field"));
    registerLazyPartitialButton(form_key_group_field, ".userarea-key-group-create-button");

    form_key_group_field.register("onHandeldRemoteData", function(info){
        registerLazyPartitialButton(info.partitial_ajax, ".userarea-key-group-create-button");
    });

    /**
     * Method that handles Delete
     * @param partitial
     */
    function registerLazyPartitialButton(partitial, classname){

        // Find delete Button
        let device_field_inner_create_button = $(partitial.options.element).find(classname).get( 0 );
        // Reregister Create Button Partitial
        createPartitialFromElement(device_field_inner_create_button);

        // find previous created partitial
        let device_field_inner_create_partitial = PartitialAjax.getPartitialFromElement(device_field_inner_create_button);
        // Register Events to create button partitial

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
