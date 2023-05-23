<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'HomeView' }">Home</router-link> | 
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
      <router-link :to="{ name: 'LogInView' }">LogIn</router-link> |
      <router-link :to="{ name: 'SignUpView' }">SignUp</router-link> |
    <button @click="logOut">LogOut</button>
    </nav>
    <router-view/>
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
// import axios from 'axios';
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  methods:{
    logOut(){
      if(this.$store.getters.isLogin){
      this.$store.dispatch('deleteToken')
      alert('로그아웃')
      this.$router.push({name: 'LogInView'})
      }else{
        alert('이미 로그아웃 돼있습니다.')
      }
    }
  }
}
</script>
