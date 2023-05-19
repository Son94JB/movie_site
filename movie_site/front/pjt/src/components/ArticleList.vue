<template>
  <p>여기는 ArticleList입니다.</p>
</template>

<script>
export default {
  name: 'ArticleList',  // 게시글 목록
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
        this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>