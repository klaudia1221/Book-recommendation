import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import firebase from 'firebase'

Vue.config.productionTip = false




  var firebaseConfig = {
    apiKey: "AIzaSyCSBgWAFAU-Tu3K-z76Xu_3XmukKUalHGc",
    authDomain: "books-11298.firebaseapp.com",
    databaseURL: "https://books-11298.firebaseio.com",
    projectId: "books-11298",
    storageBucket: "books-11298.appspot.com",
    messagingSenderId: "682453387980",
    appId: "1:682453387980:web:a9636e777b4f9a4a525069"
  };
  firebase.initializeApp(firebaseConfig);


new Vue({
  router,
  vuetify,
  iconfont: 'mdi' ,
  render: h => h(App)
}).$mount('#app')


