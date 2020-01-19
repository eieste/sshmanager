import "../../../js/index";
import "../../../scss/components/table.scss";
import PartitialAjax from "django-partitialajax";
import setupCrud from "../../../js/crud";


$(function(){

  PartitialAjax.initialize();

  setupCrud(
      PartitialAjax.getPartitialFromElement(document.getElementById("publickey-list-partitial")),
      PartitialAjax.getPartitialFromElement(document.getElementById("publickey-create-button")),
      ".publickey-delete-button"
  );

});