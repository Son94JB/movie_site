<template>
  <div>
    <h1>SearchView</h1>
    <SearchList :movie-list="movieList"/>
  </div>
</template>

<script>
import SearchList from '@/components/SearchList.vue'

export default {
    name: 'SearchView',
    components: {
        SearchList,
    },
    computed: {
        movieList() {
            return this.$store.getters.getMovies
        },
    },
}
</script>

<style>

</style>