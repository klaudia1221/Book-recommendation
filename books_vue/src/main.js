import Vue from 'vue'
import App from './App.vue'
import router from './router'
import firebase from 'firebase'

Vue.config.productionTip = false;

  var firebaseConfig = {
    apiKey: "AIzaSyBmXTY_faw-T_99M_BYqgXhX4FkDSz4NwA",
    authDomain: "test-project-bcf36.firebaseapp.com",
    databaseURL: "https://test-project-bcf36.firebaseio.com",
    projectId: "test-project-bcf36",
    storageBucket: "test-project-bcf36.appspot.com",
    messagingSenderId: "75727552520",
    appId: "1:75727552520:web:7989278b2e10db498ed1bd"
  };

  firebase.initializeApp(firebaseConfig);

  firebase.auth().onAuthStateChanged(()=>{
    new Vue({
      router,
      render: h => h(App)
    }).$mount('#app')
    
  });
