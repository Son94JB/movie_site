<template>
  <div>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성자 : {{ article?.username }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="onClick">DELETE</button>
  </div>
</template>

<script>
// import { mapActions, mapGetters } from 'vuex'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'ArticleContent',  // 게시글 내용
  props:{
    article: Object,
  },
  computed: {
    // ...mapGetters(['userDetail']),
  },
  created(){
    // this.setUserDetail()
  },
  methods:{
    // ...mapActions(['setUserDetail']),

    onClick(){
        axios.delete(`${API_URL}/api/v1/articles/${this.article.id}/`, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        }).catch(err => {
        console.log(err)
      })
    }
  }
}

</script>

<style>

</style>