const App = {
    data() {
      return {
        category: "Sandman",
        playlist: null,
      }
    },
    mounted () {
        axios
          .get('http://127.0.0.1:5000//track/search/' + this.category)
          .then(response => (this.playlist = response.data.musics))
      },
    methods: {
        generatePlaylist() {
            axios
            .get('http://127.0.0.1:5000//track/search/' + this.category)
            .then(response => (this.playlist = response.data.musics))
            /*.then(function(response) {
                this.playlist = response.data.track
                this.artist = response.data.track.artist_name
                this.song = response.data.track.track_name
                this.lyrics = response.data.track.lyrics

                console.log(this.playlist)
            })*/
        }
    }
  }
  
Vue.createApp(App).mount('#app')
  