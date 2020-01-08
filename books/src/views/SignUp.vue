<template>
  <div class="signup">
    <h3>Sign Up</h3>
    <p>Let's create a new account!</p>
    <v-text-field type="text" v-model="email" placeholder="Email"></v-text-field>
    <br />
    <v-text-field type="password" v-model="password" placeholder="Password"></v-text-field>
    <br />
    <v-btn class="pink" @click="signUp">SignUp</v-btn>
  </div>
</template>

<script>
import firebase from "firebase";

export default {
  name: "SignUp",
  data() {
    return {
      email: "",
      password: ""
    };
  },
  methods: {
    signUp: function() {
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.email, this.password)
        .then(
          function() {
            alert("Your account has been created !");
          },
          function(err) {
            alert("Oops." + err.message);
          }
        );
    }
  }
};
</script>

<style scoped>
.signup {
  margin-top: 40px;
}
input {
  margin: 10px 0;
  width: 20%;
  padding: 15px;
}
button {
  margin-top: 20px;
  width: 10%;
  cursor: pointer;
}
p {
  margin-top: 40px;
  font-size: 13px;
}
p a {
  text-decoration: underline;
  cursor: pointer;
}
</style>
	