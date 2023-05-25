<template>
    <div>
      <button @click="getRecommend">추천영화 받기</button>
      <p v-for="movie in movies"
      :key="movie.id"
      >
      추천작 : {{ movie }} </p>
    </div>
</template>

<script>
    import axios from 'axios';
    const API_URL = 'http://127.0.0.1:8000'

    export default {
      nema: "showRecommend",
      data() {
        return {
          movies: [],
        };
      },
      mounted() {

      },
      computed: {
        token(){
          return this.$store.getters.token
        }
      },
      methods: {
        getRecommend(){
          this.$emit('childEvent')
          axios
          .get(`${API_URL}/polls/recommend/`, {
            headers: {
              Authorization: `Token ${this.token}`
            },
          }).then(res => {
            // 받은 res값, 즉 영화 id 리스트를 통해서 다시 axios요청을 보낸다.
            this.movies = res.data
          }).catch(err => [
            console.log(err)
          ])
        },
      }
    };
</script>
  