import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import hello from '../views/hello/hello.vue'
import main from '../views/main/main.vue'
import video from '../views/main/video.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path:'/hello',
    name:'hello',
    component:hello
  },
  {
    path: '/',
    name: 'main',
    component: main
  },
  {
    path:'/video',
    name:'video',
    component:video
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
