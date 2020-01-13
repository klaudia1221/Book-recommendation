<template>
<div class="login">

  <v-container>
    <v-layout row>
      <v-flex xs12 sm6 offset-sm3>
        <v-card centered align-center>
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
           
                
                    <v-btn class="pink" @click="login">Login</v-btn>
               <p>You don't have an account? <router-link to="/signup">Sign Up </router-link></p>
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
import firebase from 'firebase'
	export default{
		name: 'Login',
		data() {
			return {
                email: '',
                password: ''
            };
		},
        methods: 
        {
            login: function(){
                firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
                    function(){
                        alert('Now you are logged in!')
                    },
                    function(err){
                        alert('Oops.'+ err.message)
                    }
                )


            this.$router.replace('home');
        }

        }
	}
</script>

<style scoped>
.login{
    margin-top: 40px;
}
input {
    margin: 10px 0;
    width: 20%;
    padding: 15px;
}
button{
    margin-top: 20px;
    width: 10%;
    cursor: pointer;
}
p{
    margin-top: 40px;
    font-size: 13px;
}
p a {
    text-decoration: underline;
    cursor: pointer;

}
	</style>
	