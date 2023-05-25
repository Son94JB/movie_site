<template>
  <div>
    <h1>영화 추천</h1>
    <MovieRecommend/>
  </div>
</template>

<script>
import MovieRecommend from '@/components/MovieRecommend.vue'

export default {
  name: 'RecommendView',
  components: {
    MovieRecommend,
  },
}
</script>

<style>

</style>