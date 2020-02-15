import "admin-lte";
import "admin-lte/build/js/AdminLTE";
import "popper.js";
import "bootstrap";
import "../scss/index.scss"
import "bs4-toast";
import "bs4-toast/dist/toast.min.css";
import _ from "lodash";

fetch(global_config.message_url)
    .then((response) => response.json())
    .then((jsondata) => {
    _.each(jsondata.text, (item)=> {
        $.toast({
            ...item,
            delay: 3000
        });
    })
});