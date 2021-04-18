const App = {
    el: '#app',
    data() {
      return {
        category: "Sandman",
        playlist: [],
      }
    },
    mounted () {
        axios
        .get('http://127.0.0.1:5000//track/search/' + this.category)
        .then(response => (this.playlist = response.data.musics))
    },
    methods: {
        generatePlaylist() {
            new_first_song = this.playlist[1]
            lyrics = new_first_song.lyrics
            this.category = this.selectRandomWord(lyrics)
            console.log(this.category)
            this.playlist = [new_first_song]
            
            axios
            .get('http://127.0.0.1:5000//track/search/' + this.category)
            .then(response => (this.playlist[1] = response.data.musics[1]))
        },
        selectRandomWord(lyrics) {
            // Remove punctuation from string
            lyrics = lyrics.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"")
            
            // Break string by new lines
            words_from_song = lyrics.split("\n", 20)
            
            // Remove empty spaces
            var words_from_song = words_from_song.filter(function (el) {
                return el != "";
            });

            // remove copyright and number at the end of lyrics
            words_from_song.splice(-2) 

            console.log(words_from_song)
            return words_from_song[Math.floor(Math.random() * words_from_song.length)]
        },
    }
  }
  
Vue.createApp(App).mount('#app')
  