new Vue({
  el: "#content",
  delimiters: ["[[", "]]"],
  data: {
    country: "",
    city: "",
    result: "",
  },
  mounted() {
    this.resetForm();
    document.getElementById("refresh_btn").style.display = "none";
  },
  methods: {
    refresh: function () {
      location.reload();
    },
    submit: function (event) {
      let url = document.getElementById("form").getAttribute("data-url");
      let hostname = location.toString() + url;

      let vm = this;
      event.preventDefault();

      let config = {
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
      };

      let data = {
        data: {
          country: document.getElementById("form").getAttribute("data-country"),
          city: document.getElementById("city").value,
        },
      };

      axios
        .post(hostname, data, config)
        .then(function (response) {
          vm.result = response.data.result;

          // Post submit UI change
          document.getElementById("city").setAttribute("disabled", "");
          document.getElementById("refresh_btn").style.display = "inherit";
        })
        .catch(function (error) {});
    },

    resetForm: function () {
      this.result = "";
    },
  },
});

// Function snippet from Django, to bypass CSRF error
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
