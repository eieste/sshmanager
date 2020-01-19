import $ from "jquery";
import {getCookie} from "../../../partitialajax/src/js/contrib";

export default function(option, callback){

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

            callback();
          },
        });

        e.preventDefault();
    });

}