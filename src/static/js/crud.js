import PartitialAjax from "django-partitialajax";
import $ from "jquery";
import sendForm from "./formModal";

/**
 * Setup Crud Interface (Create Update Delete)
 * @param list_partitial Partitial Object of list
 * @param create_partitial Partitial Object of Create (Button)
 * @param delete_button_selector selector for all delete buttons inside of list
 */
function setupCrud(list_partitial, create_partitial, delete_button_selector){

    function errorHandler(info){
        $.toast({
          title: gettext("Internal Server Error"),
          content: gettext("This request could be satisfied"),
          type: 'danger',
          delay: 3000,
        });
    }

    function deleteModal(url) {
        let delete_partitial = new PartitialAjax({
            "url": url,
            "element": document.getElementById("baseModal"),
            "textEventCallback": alert,
        }, {
            "onHandeldRemoteData": function (option) {
                $("#baseModal").modal();
                sendForm(option, deviceListPartitial)
            },
            "onRemoteError": errorHandler
        });
    }

    function registerDeleteButton(list_element){
       $(list_element).find(delete_button_selector).on("click", function(event){
            let url = $(this).attr("href");
            deleteModal(url);
            event.preventDefault();
       });
    }

    try{
        registerDeleteButton(list_partitial.options.element);
    }catch (e) {
        console.info("CRUD: Cant find delete Buttons", e)
    }
    create_partitial.register("onHandeldRemoteData", function(option){
        sendForm(option, deviceListPartitial);
        list_partitial.getFromRemote();
    });

    // Register Load Buttons
    list_partitial.register("onHandeldRemoteData", function(info){
        registerDeleteButton(info.partitial_ajax.options.element);
    });

    list_partitial.register("onRemoteError", errorHandler);

}

export default setupCrud;