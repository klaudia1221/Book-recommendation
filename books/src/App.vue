<template>
  <v-app  
  style="
    background: rgba(0,0,0,0);" 
    >

    <v-app-bar app>
      <v-tabs dark fixed-tabs color="white" background-color="orange">
        <v-tab  to="/bookrecommendation">Get book recommendation</v-tab>
        <v-tab to="/books">Browse books</v-tab>
        <!-- <v-tab to="/signup">SignUp</v-tab> -->
        <!-- <v-tab to="/login">Login</v-tab> -->
        <v-tab to="/top">Top 100</v-tab>
      </v-tabs>
    </v-app-bar>
      <span class="bg"></span>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: "App",
  data() {
    
  }
};
</script>
<style >
.bg {
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    
    background: url('~@/assets/bg.jpg') no-repeat center center fixed;
    background-size: cover;
    /* -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover; */
  min-height: 100%;
  min-width: 1024px;
    /* filter: blur(2px); */
  /* -webkit-filter: blur(2px); */
    /* background-color: red; */
    opacity: 0.7;
    /* transform: scale(1.1); */
  }
</style>