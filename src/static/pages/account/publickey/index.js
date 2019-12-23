import "select2";
import "select2/src/scss/core.scss";

$("select[name=device]").select2({
  theme: "classic",
  ajax: {
    url: '/account/autocomplete/devices',
    data: function (params) {
      var query = {
        term: params.term,
      };
      // Query parameters will be ?search=[term]&type=public
      return query;
    }
  }
});



$("select[name=key_groups]").select2({
  theme: "classic",
  ajax: {
    url: '/account/autocomplete/keygroups',
    data: function (params) {
      var query = {
        term: params.term,
      };
      // Query parameters will be ?search=[term]&type=public
      return query;
    }
  }
});