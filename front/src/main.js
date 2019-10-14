import Vue from 'vue'
import App from './App.vue'
import App_new from './App_new.vue'
import Router from './router';
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false

new Vue({
  vuetify,
  router:Router,
  render: h => h(App_new)
}).$mount('#app')