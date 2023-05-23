<template>
  <div>
    <ArticleContent/><hr>
    <CommentList :article="article"/><hr>
    <router-link :to="{ name: 'ArticleView' }">목록으로</router-link>
    <ArticleList/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import ArticleContent from '@/components/ArticleContent.vue'
import ArticleList from '@/components/ArticleList.vue'
import CommentList from '@/components/CommentList.vue'

export default {
  name: 'ArticleDetailView',
  components:{
    // 3개 필요. 게시글 내용이랑 댓글이랑 다른 게시글 목록
    ArticleContent,
    ArticleList,
    CommentList,
  },
  created() {
    // const articleId = this.$route.params.id
    this.fetchArticle()
  },
  data() {
    return {
      article: {
        id: null,
        title: '',
        content: '',
      }
    }
  },
  methods: {
    fetchArticle(){
      axios.get(`${API_URL}/api/v1/articles/${this.$route.params.id}`)
      .then(res => {
        this.article = res.data
      }).catch(err => {
        console.log(err)
      })
    }
  },
  beforeRouterUpdate(to, from, next){
    if (this.$route.params.article.id != to.$route.params.article.id) {
      next()
    }else{
      next(false)
    }
  },
}
</script>

<style>

</style>