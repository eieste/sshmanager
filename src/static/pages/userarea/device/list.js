import "../../../js/index";
import "../../../scss/components/table.scss";
import PartitialAjax from "django-partitialajax";
import setupCrud from "../../../js/crud";

$(function(){

  PartitialAjax.initialize();

  setupCrud(
      PartitialAjax.getPartitialFromElement(document.getElementById("device-list-partitial")),
      PartitialAjax.getPartitialFromElement(document.getElementById("device-create-button")),
      ".device-delete-button"
  );

});