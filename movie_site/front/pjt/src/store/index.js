import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    articles:[],
    token: null,
    movies: [],
    // comments: []
    movieDetail: null,
    searchTerm: '',  // 검색어
    actorDetail: null,
    directorDetail: null,
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
    },
    actorDetail(state) {
      return state.actorDetail
    },
    directorDetail(state) {
      return state.directorDetail
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
    // GET_COMMENTS(state, comments){
    //   state.comments = comments
    // },
    SIGN_UP(state, token){
      state.token = token
    },
    SET_MOVIES(state, movies) {
      state.movies = movies
      console.log(state.movies)
    },
    // detail은 fetchMovieDetail에서 받아온 response.data
    setMoviedetails(state, detail) {
      state.movieDetail = detail
    },
    RESET_SEARCH_DATA(state) {
      state.searchTerm = ''
      state.movies = []
      state.movieDetail = null
      console.log(state.searchTerm)
    },
    setActorDetails(state, detail) {
      state.actorDetail = detail
    },
    setDirectorDetails(state, detail) {
      state.directorDetail = detail
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
    // getComments(context){
    //   axios({
    //     method:'get',
    //     url: `${API_URL}/api/v1/comments/`
    //   }).then(res => {
    //     context.commit('GET_ARTICLES', res.data)
    //   }).catch(err => {
    //   console.log(err)
    //   })
    // },
    searchMovies(context, searchTerm){
      console.log(searchTerm)
      // context.commit('SET_SEARCH_TERM', searchTerm)
      axios.get(`http://127.0.0.1:8000/movies/${searchTerm}/`)
      .then(response => {
        context.commit('SET_MOVIES', response.data)
      })
      .catch(error => {
          console.log(error)
      })
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username : username, 
          password1 : password1, 
          password2 : password2,
        }
      })
        .then((res) => {
          // console.log(res)
          context.commit('SIGN_UP', res.data.key)
          // context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    logIn(context, payload) {
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
    fetchMovieDetail(context, movieId) {
      axios.get(`http://127.0.0.1:8000/movies/detail/${movieId}/`)
      .then(response => {
        context.commit('setMoviedetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    resetSearchTerm(context) {
      context.commit('RESET_SEARCH_DATA', '');
    },
    fetchActorDetail(context, actorId) {
      axios.get(`http://127.0.0.1:8000/movies/actor/${actorId}/`)
      .then(response => {
        context.commit('setActorDetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    },
    fetchDirectorDetail(context, directorId) {
      axios.get(`http://127.0.0.1:8000/movies/director/${directorId}/`)
      .then(response => {
        context.commit('setDirectorDetails', response.data)
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  modules: {
  },
})
