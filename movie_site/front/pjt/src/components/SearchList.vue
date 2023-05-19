<template>
  <div>
    <p>여기는 SearchList입니다.</p>
    <SearchListItem v-for="movie in movieList" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import SearchListItem from '@/components/SearchListItem.vue'
export default {
    name: 'SearchList', // 검색 결과 목록
    components: {
        SearchListItem,
    },
    props: {
        movieList: {
            type: Array,
            default: () => [],
        },
    },
}
</script>

<style>

</style>