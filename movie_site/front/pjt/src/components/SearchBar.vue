<template>
  <div>
    <input v-model="searchTerm" type="text" placeholder="검색어를 입력하세요" />
    <button @click="searchMovies">검색</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchTerm: '', // 검색어를 저장할 데이터
    };
  },
  methods: {
    searchMovies() {
      // Vuex 액션 호출하여 검색 요청 보내기
      this.$store.dispatch('searchMovies', this.searchTerm);
    },
  },
};
</script>
