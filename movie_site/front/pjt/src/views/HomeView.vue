<template>
  <div>
    <h1>MOVIE.gg</h1>
    <SearchView/>
  </div>
  
</template>

<script>

import SearchView from '@/views/SearchView.vue';

export default {
  name: 'HomeView',
  components: {
    SearchView,
  },
  computed: {
    // movieList를 통해 vuex의 state에 getters로 접근
    movieList() {
      return this.$store.getters.Movies;
    }
  },
  
}
</script>

<style>

</style>