<template>
  <div>
    <h2>Comments</h2>
      <ul v-if="comments.length > 0">
        <li v-for="comment in comments" :key="comment.id">
          {{ comment.content }}
        </li>
      </ul>
      <p v-else>댓글이 없습니다.</p>
    <form @submit.prevent="createComment">
      <label for="content">content : </label>
      <textarea id="content" cols="100" rows="10" v-model="content"></textarea><br>
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
// import { mapState } from 'vuex';

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  props: {
    article: {
      type: Object,
      required: true
    },
  },
  data() {
    return {
      content: '',
      comments: [],
    };
  },
  created() {
    const articleId = this.article.id
    this.fetchComments(articleId);
  },
  computed: {
    // ...mapState(['token']),
  },
  watch: {
    article: {
      immediate: true,
      handler(article){
        if(article){
          const articleId = article.id
          this.fetchComments(articleId)
        }
    }
  },
  },
  methods: {
    fetchComments() {
      // 해당 게시글의 댓글을 가져오는 API 호출
      axios.get(`${API_URL}/api/v1/comments/${this.$route.params.id}/`)
      .then(response => {
        this.comments = response.data;
      })
      .catch(error => {
        if(error.response && error.response.status === 404){
        this.comments = []
        }
        else{
          console.error(error)
        }
      })
    },

    // createComment() {
    //   const commentData = {
    //   content: this.content,
    //   user: this.getUserInfo(),
    // };

  //   const headers = {
  //     Authorization: `Token ${this.token}`
  //   };

  //   axios.post(`${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
  //   commentData, { headers }).then(response => {
  //       // 성공적으로 댓글을 생성한 경우의 처리
  //       alert(this.content)
  //       console.log(response.data);
  //       // 새로운 댓글을 목록에 추가하거나, 목록을 갱신하는 등의 작업 수행
  //       this.fetchComments();
  //       this.content = ''; // 입력 필드 초기화
  //     })
  //     .catch(error => {
  //       // 댓글 생성 중에 오류가 발생한 경우의 처리
  //       console.error(error);
  //     });
  //   },
  //   getUserInfo() {
  //     async function fetchUserProfile(token){
  //       try {
  //         const response = await axios.get(`${API_URL}/accounts/user/`)
  //       }
  //     }
  //   }
  },
}
</script>
  