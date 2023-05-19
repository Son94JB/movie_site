<template>
    <div class="search-list-item">
      <img class="movie-poster" :src="`https://image.tmdb.org/t/p/w500/${movie.poster}`" alt="movie poster" />
      <div class="movie-details">
        <h1 class="movie-title">{{ movie.title }}</h1>
        <p class="movie-overview">{{ movie.overview }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'SearchListItem',
    props: {
      movie: {
        type: Array,
        default: () => [],
      },
    },
  }
  </script>
  
  <style scoped>
  .search-list-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .movie-poster {
    width: 150px;
    height: auto;
    margin-right: 20px;
  }
  
  .movie-details {
    flex: 1;
  }
  
  .movie-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .movie-overview {
    font-size: 16px;
  }
  </style>
  