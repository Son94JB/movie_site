<template>
    <div>
      <template v-if="movieDetail">
        <p>{{ movieDetail.id }}</p>
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

        <!-- 영화 리뷰 조회 -->
        <hr>
        <div>
          <h2>리뷰</h2>
          <div v-for="review in movieReviews" :key="review.id" @click="getMovieReviewDetail(review)">
          <p>작성자: {{ review.user }}</p>
          <p>내용: {{ review.content }}</p>
          <p>평점: {{ review.score }}</p>
          <button @click="deleteReview(review.id)">삭제</button>
          <hr>
          </div>
        </div>

        <!-- 영화 리뷰 작성 -->
        <div>
          <h2>리뷰 작성</h2>
          <form @submit.prevent="createReview">
            <label for="content">내용</label>
            <input type="text" id="content" v-model.trim="content" />
            <label for="score">평점</label>
            <input type="number" id="score" v-model="score" />
            <input type="submit" id="submit">
          </form>
        </div>
      </template>
      <template v-else>
        로딩 중...
      </template>
      <YoutubeTrailerVue/>
    </div>
  </template>
  

<script>
import axios from 'axios'
import YoutubeTrailerVue from '@/components/YoutubeTrailer.vue'


export default {
    name: 'DetailView', // 영화 상세 정보
    data() {
      return {
        content: '',
        score: 0,
      }
    },
    watch: {
      'movieReviews': {
        deep: true,
        handler(newMovieDetail) {
          console.log('reviews 변경됨')
          this.updateMovieReviews(newMovieDetail.reviews)        
        },
      }
    },
    computed: {
        // movieDetail를 통해 vuex의 state에 getters로 접근
        movieDetail() {
            return this.$store.getters.movieDetail
        },
        movieReviews() {
            return this.$store.state.movieDetail.reviews
        },
        movieID() {
          return this.$route.params.id
        }
    },
    components: {
      YoutubeTrailerVue
    },
    methods: {
      updateMovieReviews(reviews) {
        this.movieDetail.reviews = reviews
      },
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
        // movieid를 정수로 변환
        const movieid = parseInt(this.movieID);
        const reviewid = parseInt(review.id);
        this.$router.push({name: 'MovieReviewDetailView', params: {id: reviewid}});
        this.$store.dispatch('fetchMovieDetail', movieid)
      },
      //path('review/create/', views.MovieReviewCreateView.as_view(), name='movie-review-create'),

      createReview(){
        console.log(this.movieDetail.id)
        const content = this.content
        const score = parseInt(this.score); // score를 정수로 변환
        const movie = parseInt(this.movieDetail.id); // movie를 정수로 변환
        console.log(this.$store.state.token)
        axios.post('http://127.0.0.1:8000/movies/review/create/', {
          content: content,
          score: score,
          movie: movie
        }, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
        .then(response => {
          console.log(response)
          const createdReview = response.data
          this.movieDetail.reviews.push(createdReview)
        })
        .catch(error => {
          console.log(error)
        })
      },
      
    //   deleteReview(reviewId) {
    //     axios.delete(`http://127.0.0.1:8000/movies/review/${reviewId}/delete/`, {
    //       headers: {
    //         Authorization: `Token ${this.$store.state.token}`,
    //       },
    //     })
    //     .then(response => {
    //       console.log(response);
    //       // 삭제된 리뷰를 화면에서 제거
    //       this.movieDetail.reviews = this.movieDetail.reviews.filter(review => review.id !== reviewId);
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },

    }
}

</script>

<style>

</style>