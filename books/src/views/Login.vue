<template>
	<div class="login">
		<h3>Sign In</h3>
		<input type="text" v-model="email" placeholder="Email"><br>
		<input type="password" v-model="password" placeholder="Password"><br>
		<v-btn @click="login">Sign In</v-btn>
		<p>You don't have an account? <router-link to="/signup">Sign Up </router-link>
</p>
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
	