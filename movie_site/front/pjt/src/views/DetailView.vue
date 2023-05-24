<template>
    <div>
      <template v-if="movieDetail">
        <h1>{{ movieDetail.title }}</h1>
        <p>{{ movieDetail.overview }}</p>
        <img v-if="movieDetail.poster" class="movie-poster" :src="`https://image.tmdb.org/t/p/w500/${movieDetail.poster}`" alt="movie poster" />
        <!-- 배우 이름과 사진 -->
        <div>
          <h2>출연진</h2>
          <div v-for="actor in movieDetail.actor_profiles" :key=actor.name>
          <img @click="getActorDetail(actor)" v-if="actor.profile_path" class="actor-profile" :src="`https://image.tmdb.org/t/p/w500/${actor.profile_path}`" alt="actor profile" />
          <p>{{ actor.name }}</p>
          </div>
        </div>
        <!-- 감독 이름과 사진 -->
        <div>
          <h2>감독</h2>
          <div v-for="director in movieDetail.director_profiles" :key=director.name>
          <img @click="getDirectorDetail(director)" v-if="director.profile_path" class="director-profile" :src="`https://image.tmdb.org/t/p/w500/${director.profile_path}`" alt="director profile" />
          <p>{{ director.name }}</p>
          </div>
        </div>
        
        <!-- 장르 -->
        <div>
          <h2>장르</h2>
          <div>
          <p>{{ movieDetail.genre }}</p>
          </div>
        </div>
        
        <!-- 트레일러 -->
        <div>
          {{ movieDetail.trailer }}
        </div>

        <!-- 영화 리뷰 -->
        <hr>
        <div>
          <h2>리뷰</h2>
          <div v-for="review in movieDetail.reviews" :key="review.id" @click="getMovieReviewDetail(review)">
          <p>작성자: {{ review.user }}</p>
          <p>내용: {{ review.content }}</p>
          <p>평점: {{ review.score }}</p>
          <hr>
          </div>
        </div>
      </template>
      <template v-else>
        로딩 중...
      </template>
      <YoutubeTrailerVue/>
    </div>
  </template>
  

<script>
import YoutubeTrailerVue from '@/components/YoutubeTrailer.vue'


export default {
    name: 'DetailView', // 영화 상세 정보
    computed: {
        // movieDetail를 통해 vuex의 state에 getters로 접근
        movieDetail() {
            return this.$store.getters.movieDetail
        },
    },
    components: {
      YoutubeTrailerVue
    },
    methods: {
      // 클릭하면 해당 배우의 상세 정보로 이동, 해당 배우 디테일 정보 서버로부터 가져와서 업데이트
      getActorDetail(actor) {
        this.$router.push({name: 'ActorDetailView', params: {id: actor.id}});
        this.$store.dispatch('fetchActorDetail', actor.id)
      },
      getDirectorDetail(director) {
        this.$router.push({name: 'DirectorDetailView', params: {id: director.id}});
        this.$store.dispatch('fetchDirectorDetail', director.id)
      },
      getMovieReviewDetail(review) {
        this.$router.push({name: 'MovieReviewDetailView', params: {id: review.id}});
        this.$store.dispatch('fetchMovieReviewDetail', review.id)
      }

    }
}

</script>

<style>

</style>