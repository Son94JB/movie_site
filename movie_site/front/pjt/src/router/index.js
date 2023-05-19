import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleCreate from '@/views/ArticleCreate.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
