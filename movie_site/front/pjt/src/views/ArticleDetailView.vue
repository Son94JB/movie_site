<template>
  
</template>

<script>
import ArticleContent from '@/components/ArticleContent.vue'
import Comment from '@/components/Comment.vue'
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleDetailView',
  components:{
    // 3개 필요. 게시글 내용이랑 댓글이랑 다른 게시글 목록
    ArticleContent,
    Comment,
    ArticleList,
  }
}
</script>

<style>

</style>