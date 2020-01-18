import Vue from "vue";

export const store = Vue.observable({
  user: null
});

export const mutations= {
    setUser(user){
        store.user=user;
    }

}