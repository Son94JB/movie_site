import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import SearchView from '@/views/SearchView.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import DetailView from '@/views/DetailView.vue'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },

  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView,
  },
  
  {
    path: '/movies/:id',
    name: 'SearchView',
    component: SearchView
  },

  {
    path: '/create',
    name: 'ArticleCreate',
    component: ArticleCreate
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,
    beforeEnter(to, from, next){
      if (store.getters.isLogin === true) {
        alert('이미 로그인 되어있습니다. \n먼저 로그아웃을 해주세요.')
        next(from)
      }else{
        next()
      }
    }
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    beforeEnter(to, from, next){
      if (store.getters.isLogin === true) {
        alert('이미 로그인 되어있습니다. \n먼저 로그아웃을 해주세요.')
        next(from)
      }else{
        next()
      }
    }
  },

  {
    path: '/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
    beforeEnter(to, from, next){
      if (store.getters.isLogin != true) {
        alert('게시글을 보려면 로그인을 해주세요')
        next(false)
      }else{
        next()
      }
    },
  },

  {
    path: '/detail/:id',
    name: 'DetailView',
    component: DetailView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
