new Vue({
  el: '#starting',
  delimiters: ['${', '}'],
  data: {
    File: null,
    results: [],
    words: [],
    stop_words: true,
    save_results: {},
    text : '',
    // File Upload Errors
    upload_errors: '',
  },
  mounted: function () {

  },
  methods: {
    
    selectFile: function (event) {
      this.File = event.target.files[0]
    },

    uploadFile: function () {
      this.loading = true;
      // upload this.ingredientCSV to REST api in FormData
        var reader = new FileReader();
        reader.readAsText(this.File)
        reader.onload = (event)=> {
                var textData = event.target.result;
                console.log(textData)
                this.text = textData;
                $.post('/api/file_import/', {'data':textData}).done((response)=>{
                     this.loading = false;
                     // this.upload_errors = response['errors'].join('\n') + response['warnings'].join('\n')
                     this.results = response['result'];
                     this.words = response['all'];
                 }).fail((err)=>{
                  this.upload_errors = err.responseText
                  this.loading = false;
                  console.log(err)
                })
        };
        reader.onerror = function() {
            alert('Unable to read ' + file.fileName);
        }; 
        },

      disableStop: function() {
        this.$http.post('/api/disable_stop/',this.words)
        .then((response) => {
          this.results = response.data;
          this.stop_words = false;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
      },
      saveResult: function() {
        this.save_results['words'] = this.results;
        this.save_results['stop'] = this.stop_words;
        this.save_results['text'] = this.text;
        this.$http.post('/api/save_result/',this.save_results)
        .then((response) => {
          alert('Success')
        })
        .catch((err) => {
          alert('Failure')
        })
      },
    

  },
});