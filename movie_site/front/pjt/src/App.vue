<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'HomeView' }">Home</router-link> | 
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
      <router-link :to="{ name: 'SearchView' }">Search</router-link> |
      <p>여기는 App입니다.</p>
    </nav>
    <router-view/>
    <SearchBar/> <!--MovieSearch 컴포넌트 추가-->
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<script>
import SearchBar from './components/SearchBar.vue'; // SearchBar 컴포넌트를 불러옴

export default {
  name: 'App',
  components: {
    SearchBar, // SearchBar 컴포넌트를 등록
  },
}
</script>
