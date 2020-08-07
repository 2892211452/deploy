import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

//全局访问的对象
const state={
  msg:'global message',
  
  nowDm:"",
  list:"",
  imgUrl:""
}

const store = new Vuex.Store({
  state
});

export default store;


// export default new Vuex.Store({
//   state: {
//   },
//   mutations: {
//   },
//   actions: {
//   },
//   modules: {
//   }
// })
