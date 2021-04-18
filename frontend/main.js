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
            console.log(this.playlist);
            axios
            .get('http://127.0.0.1:5000//track/search/' + this.category)
            .then(response => (this.playlist = response.data.musics))
        }
    }
  }
  
Vue.createApp(App).mount('#app')
  