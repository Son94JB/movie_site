<template>
  <div>
    <BestArticleList/>
    <ArticleList/>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'
import BestArticleList from '@/components/BestArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    BestArticleList,
    ArticleList,
  }
}
</script>

<style>

</style>