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
    movieDetail: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    Movies(state) {
      return state.movies
    },
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
    },
    movieDetail(state) {
      return state.movieDetail
    }
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
    },
    // detail은 fetchMovieDetail에서 받아온 response.data
    setMoviedetails(state, detail) {
      state.movieDetail = detail
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
    fetchMovieDetail(context, movieId) {
      axios.get(`http://127.0.0.1:8000/movies/detail/${movieId}/`)
      .then(response => {
        context.commit('setMoviedetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
  },
  modules: {
  },
})
