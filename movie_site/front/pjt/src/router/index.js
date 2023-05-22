import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import SearchView from '@/views/SearchView.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'

Vue.use(VueRouter)

const isLoggedIn = true

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },

  {
    path: '/article',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/movies/',
    name: 'SearchView',
    component: SearchView
  },

  {
    path: '/create',
    name: 'ArticleCreate',
    component: ArticleCreate
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        alert('이미 로그인 되어 있습니다')
        next(from)
      } else {
        next()  // 로그인이 안 되어 있다면, 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        alert('이미 로그인 되어 있습니다')
        next(from)
      } else {
        next()  // 로그인이 안 되어 있다면, 로그인 페이지로 이동
      }
    }
  },
  {
    path: '/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  // {
  //   path: '/logout',
  //   name: '',
  //   component: 
  // },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
