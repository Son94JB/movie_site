<template>
  <div>
    <h4>{{ article.id }}</h4>
    <p>{{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem', // 각 게시물을 나타낼 vue파일
  props: {
    article: Object
  }
}
</script>

<style>

</style>