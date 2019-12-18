<template>
  <div class="books">
    <h1>This is books page</h1>
    <button @click="getMessage">Get books</button>
    <p>{{all_books}}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Books",
  data() {
    return {
      all_books: null
    };
  },
  methods: {
    getMessage() {
      const URL = "http://127.0.0.1:5000/books";
      axios.get(URL).then(res => {
        this.all_books = res.data;
      });
    }
  }
};

//     async get_all_books(){
//         let v=this;
//         v.all_books= [];

//         var request= new XMLHttpRequest();
//         request.open("POST",URL,true)
//         request.onload=function(){
//         var data=JSON.parse(this.response);

//         for (var m of data){
//             v.all_books.push(m)
//         }};

//     request.send();
//     }}

// }
</script>
