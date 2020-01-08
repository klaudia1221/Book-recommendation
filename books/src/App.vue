<template>
  <v-app>
    <v-app-bar app color="primary">
      <v-tabs fixed-tabs>
        <v-tab to="/about">Get book recommendations</v-tab>
        <v-tab to="/books">Browse books</v-tab>
        <v-tab to="/signup">SignUp</v-tab>
        <v-tab to="/login">Login</v-tab>
        <v-tab to="/bar">Bar</v-tab>
      </v-tabs>
    </v-app-bar>
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
