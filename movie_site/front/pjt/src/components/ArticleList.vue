<template>
<<<<<<< HEAD
  <p>여기는 ArticleList입니다.
  </p>
  
    
=======
  <div class="article-list">
    <p>여기는 ArticleList입니다.</p>
    <ArticleListItem v-for="article in articles"
    :key="article.id"
    :article="article"
    />
  </div>
>>>>>>> 7ea5cc40e83b751d987bb0a51fdf27b2019ac356
</template>

<script>
import ArticleListItem from '@/components/ArticleListItem.vue'

export default {
  name: 'ArticleList',  // 게시글 목록
<<<<<<< HEAD
  created() {
    // this.getArticles()
  },

  methods: {
    getArticles() {
        this.$store.dispatch('getArticles')
=======
  components: {
    ArticleListItem,
  },
  computed: {
    articles(){
      return this.$store.state.articles
>>>>>>> 7ea5cc40e83b751d987bb0a51fdf27b2019ac356
    }
  }
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>

