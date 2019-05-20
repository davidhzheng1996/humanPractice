// https://codesandbox.io/s/o29j95wx9
new Vue({
  el: '#starting',
  delimiters: ['${', '}'],
  data: {
    results: []
  },
  mounted: function () {
    this.getResults();
  },
  methods: {
      getResults: function(){
      let api_url = '/api/get_results/';
      this.loading = true;
      this.$http.get(api_url)
        .then((response) => {
          this.results = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
      },
      viewText: function(resultid){
        window.location.href = '/results/'+resultid
      },
      viewWords: function(resultid){
        window.location.href = '/show_results/'+resultid
      },
  },
});