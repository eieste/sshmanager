import "../../../js/index";
import "../../../scss/components/table.scss";
import PartitialAjax from "django-partitialajax";
import setupCrud from "../../../js/crud";

$(function(){

  PartitialAjax.initialize();

  setupCrud(
      PartitialAjax.getPartitialFromElement(document.getElementById("keygroup-list-partitial")),
      PartitialAjax.getPartitialFromElement(document.getElementById("keygroup-create-button")),
      ".keygroup-delete-button"
  );

});