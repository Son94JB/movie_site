import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import SearchView from '@/views/SearchView.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import DetailView from '@/views/DetailView.vue'

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
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
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
