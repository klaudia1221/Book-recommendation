<template>
<div class="signup">

  <v-container>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card class="card-theme" centered align-center>
          <v-card-text>
            <v-container>
              <form>
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field class="input-user"
                      name="email"
                      label="Mail"
                      id="email"
                      v-model="email"
                      type="email"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
                <v-layout row>
                  <v-flex xs12>
                    <v-text-field class="input-user"
                      name="password"
                      label="Password"
                      id="password"
                      v-model="password"
                      type="password"
                      required></v-text-field>
                  </v-flex>
                </v-layout>
           
                
                    <v-btn class="brown--text text--lighten-1" @click="signUp">SignUp</v-btn>
               
              </form>
            </v-container>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</div>
</template>



   







<script>
import firebase from "firebase";
import {  mutations} from "../store.js";

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
            mutations.setUser(firebase.auth().currentUser);
          

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
.card-theme{
    background-color: whitesmoke;
    /* border: 2px solid #000; */
  box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.9);

}

</style>
	