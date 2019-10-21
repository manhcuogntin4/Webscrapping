import Vue from 'vue'
import App_new from './App_new.vue'
import Router from './router';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false
Vue.prototype.$eventBus = new Vue()
export const Authentique = new Vue({
  data: {
    is_authentique: false,
    search:"",
  }
})

new Vue({
  vuetify,
  router:Router,
  render: h => h(App_new)
}).$mount('#app')