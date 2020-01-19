import "../../../js/index";
import PartitialAjax from "django-partitialajax";

$(function () {
    PartitialAjax.initialize();
    $(".modal").modal("show");
});
