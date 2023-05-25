<template>
  <div>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성자 : {{ article?.username }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="onClickDelete">DELETE</button>
    <router-link class="temp" :to="{name:'ArticleUpdate', params:{id:this.article.id} }">수정하기</router-link>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleContent',  // 게시글 내용
  props:{
    article: Object,
  },
  created(){
    this.getArticles()
  },

<<<<<<< HEAD
    onClick(){
        axios.delete(`${API_URL}/api/v1/articles/${this.article.id}/`, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        }).catch(err => {
        console.log(err)
=======
  methods:{

    getArticles() {
        this.$store.dispatch('getArticles')
    },
    onClickDelete(){
      // console.log(this.$store.state.articles)
      axios.delete(`${API_URL}/api/v1/articles/${this.article.id}/`, {
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
>>>>>>> a3dda479796e2014e0d679d0c9d6ab3c98995126
      })
      .then((res) => {
        this.$emit('delete-success'),
        alert('삭제 완료되었습니다!!', res)
      })
      .catch((err) => {
        alert('자신의 게시물만 삭제 가능합니다!');
        console.log(err);
      })
    },
    onClickUpdate(){
      console.log(11111)
    //   axios.put(`${API_URL}/api/v1/articles/${this.article.id}/`, {
    //     headers: {
    //       Authorization: `Token ${this.$store.state.token}`,
    //     },
    //   })
    //   .then((res) => {
    //     this.$emit('delete-success'),
    //     alert('삭제 완료되었습니다!!', res)
    //   })
    //   .catch((err) => {
    //     alert('자신의 게시물만 삭제 가능합니다!');
    //     console.log(err);
    //   })
    }
  },
}

</script>

<style scoped>
.temp{
  text-decoration-line:none;
}
.temp:hover{
  color: aqua;
}
.temp:visited{
  color:red;
}
</style>