var vm = new Vue({
  el: '#starting',
  delimiters: ['${', '}'],
  data: {
    text: '',
  },
  mounted: function () {
    
  },
  methods: {
    getText: function (resultid) {
      this.loading = true;
      this.$http.get('/api/get_text/' + resultid)
        .then((response) => {
          this.text = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
  },
});