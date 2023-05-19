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
    movies: [],
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
        .then((res) => {
        // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
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
    }
  },
  modules: {
  }
})
