import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
// import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles:[],
    token: null,
<<<<<<< HEAD
    movies: [],
=======
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
>>>>>>> 7ea5cc40e83b751d987bb0a51fdf27b2019ac356
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'ArticleView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
    SET_MOVIES(state, movies) {
      state.movies = movies
      console.log(state.movies)
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
      })
        .then(res => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch(err => {
        console.log(err)
      })
    },
<<<<<<< HEAD
    searchMovies(context, searchTerm){
      console.log(searchTerm)
      axios.get(`http://127.0.0.1:8000/movies/${searchTerm}/`)
      .then(response => {
         context.commit('SET_MOVIES', response.data)
       })
       .catch(error => {
          console.log(error)
       })
    },
  },
  getters: {
    getMovies(state) {
      return state.movies
=======
    logIn(context, payload){
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        })
      .catch((err) => console.log(err))
>>>>>>> 7ea5cc40e83b751d987bb0a51fdf27b2019ac356
    }
  },
  modules: {
  }
})
