<template>
  <div>
    <h2>Comments</h2>
    <ul>
      <li v-for="comment in comments" :key="comment.id">
        {{ comment.content }}
      </li>
    </ul>
    <form @submit.prevent="createComment">
      <label for="content">content : </label>
      <textarea id="content" cols="100" rows="10"></textarea><br>
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
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
    console.log(this.article)
    this.fetchComments();
  },
  methods: {
    fetchComments() {
      // 해당 게시글의 댓글을 가져오는 API 호출
      axios.get(`${API_URL}/api/v1/comments/${this.$route.params.id}/`)
        .then(response => {
          this.comments = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    createComment(){
      const content = this.content
      const articleId = this.$route.params.id
      
      axios({
        method: "post",
        url: `${API_URL}/api/v1/articles/${articleId}/comments/`,
        data: {
          content,
        },
      }).then((res) => {
        const newComment = res.data
        this.comment.push(newComment)
        this.content = ''
      }).catch((err) => {
        console.log('시이이이이이이이이이발!!!!! 오류발생!!!!')
        console.log(err)
      })
    },
  }
};
</script>
