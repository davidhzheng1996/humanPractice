var vm = new Vue({
  el: '#starting',
  delimiters: ['${', '}'],
  data: {
    words: [],
  },
  mounted: function () {
    
  },
  methods: {
    getWords: function (resultid) {
      this.loading = true;
      this.$http.get('/api/get_words/' + resultid)
        .then((response) => {
          this.words = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
  },
});