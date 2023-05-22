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
          <img v-if="actor.profile_path" class="actor-profile" :src="`https://image.tmdb.org/t/p/w500/${actor.profile_path}`" alt="actor profile" />
          <p>{{ actor.name }}</p>
          </div>
        </div>
        <!-- 감독 이름과 사진 -->
        <div>
          <h2>감독</h2>
          <div v-for="director in movieDetail.director_profiles" :key=director.name>
          <img v-if="director.profile_path" class="director-profile" :src="`https://image.tmdb.org/t/p/w500/${director.profile_path}`" alt="director profile" />
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
      </template>
      <template v-else>
        로딩 중...
      </template>
    </div>
  </template>
  

<script>
export default {
    name: 'DetailView', // 영화 상세 정보
    computed: {
        // movieDetail를 통해 vuex의 state에 getters로 접근
        movieDetail() {
            return this.$store.getters.movieDetail
        },
    },
}
</script>

<style>

</style>