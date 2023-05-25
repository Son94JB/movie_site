<template>
  <div>
    <h2>Comments</h2>
      <ul v-if="comments.length > 0">
        <li v-for="comment in comments" :key="comment.id">
          {{ comment.content }} | <button @click="deleteComment(comment.id)">삭제하기</button>
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
import { mapActions, mapState } from 'vuex';

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
      initLen: null,
    }
  },
  computed:{
    ...mapState(['userDetail']),
  },
  created() {
    const articleId = this.article.id
    this.fetchComments(articleId);
    this.getUserName()
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
    ...mapActions(['getUserName']),
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
    createComment(){
      this.getUserName()
      const content = this.content
      const userId = parseInt(this.userDetail.pk)

      axios.post(`${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`, {
        user: userId,
        content: content,
      }, {
      headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(res => {
        const newComment = res.data
        this.comments.push(newComment)
        this.content = ''
      })
      .catch(err => {
        console.log(err)
      })
    },
    deleteComment(commentId){
      console.log(commentId)
      axios
      .delete(`${API_URL}/comments/${commentId}/`,{
      headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
      .then(() => {
        this.comments = this.comments.filter(comment => comment.id !== commentId)
        alert('댓글이 삭제되었습니다')
      })
      .catch(err => {
        alert('자신의 댓글만 삭제 가능합니다!')
        console.log(err)
      })
    }
  },
}
</script>
  