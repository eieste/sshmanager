import "../../../js/index";
import $ from "jquery";
import PartitialAjax from "django-partitialajax"
import setupCrud from "../../../js/crud";


$(function () {
  PartitialAjax.initialize();


  setupCrud(
      PartitialAjax.getPartitialFromElement(document.getElementById("hostgroup-list-partitial")),
      PartitialAjax.getPartitialFromElement(document.getElementById("hostgroup-create-button")),
      ".hostgroup-delete-button"
  );


});
