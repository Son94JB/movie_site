<template>
  <div>
    <h2>{{ movieReview.user }}</h2>
    <form @submit.prevent="updatePost">
      <label for="content">내용</label>
      <input type="text" id="content" v-model.trim="content" />
      <label for="score">평점</label>
      <input type="number" id="score" v-model="score" />
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MovieReviewDetailView',
  data() {
    return {
      content: '',
      score: 0,
      selectedPost: null
    };
  },
  mounted() {
    this.fetchPost();
  },
  computed: {
    reviewId() {
      return this.$route.params.id; // Vue Router를 통해 reviewId를 받아옴
    },
    movieReview() {
      return this.$store.getters.movieDetail.reviews.find(review => review.id === parseInt(this.reviewId))
    },
  },
  methods: {
    fetchPost(){
      this.selectedPost = this.movieReviewDetail
      console.log(this.selectedPost)
    },

    updatePost() {
      const content = this.content;
      const score = parseInt(this.score);
      const movie = parseInt(this.movieReviewDetail.movie);
      axios.put(`http://127.0.0.1:8000/movies/review/${this.reviewId}/update/`, {
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
          // response.data는 수정된 리뷰 데이터
          // 이걸 vuex의 스통에 있는 movieReviewDetail을 수정
          const updateReview = response.data  // 새로운 리뷰 데이터
          const movieDetail = this.$store.getters.movieDetail // 옛날꺼
          // movieDeatil순회하며 개별 데이터 조회하고, 그 중 response와 id같은 리뷰 찾아서 업데이트
          movieDetail.reviews.forEach((review, index) => {
            if (review.id === updateReview.id) { //만약 이전 리뷰의 id와 수정된 리뷰의 id가 같다면
              movieDetail.reviews[index] = updateReview
              this.$store.commit('setMovieReviewDetails', movieDetail.reviews[index])
            }
          })
        })
        .catch(error => {
          console.error(error);
        });
        const movieId = this.movieReviewDetail.movie
        this.$router.replace({name: 'DetailView', params: {id: movieId}})
    },
  }
};
</script>

<style>
/* 필요한 스타일링을 추가 */
</style>
