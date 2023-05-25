<template>
  <div>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'MovieReviewDetailView',
  data() {
    return {
      editedContent: '',
      editedScore: 0
    };
  },
  computed: {
    movieReview() {
      return this.$store.getters.movieReviewDetail;
    },
    reviewId() {
      return this.$route.params.id; // Vue Router를 통해 reviewId를 받아옴
    }
  },
  methods: {
    updateReview() {
      const payload = {
        content: this.editedContent,
        score: this.editedScore
      };

      // API로 리뷰 수정 요청을 보냄
      axios.put(`http://127.0.0.1:8000/movies/review/${this.reviewId}/`, payload)
        .then(response => {
          console.log(response)
          // 수정 성공 시 처리
          // 필요한 로직 구현
          // 수정된 리뷰를 가져와서 Vue의 데이터에 할당
          const updatedReview = response.data;
          this.movieReview.content = updatedReview.content;
          this.movieReview.score = updatedReview.score;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style>
/* 필요한 스타일링을 추가 */
</style>
