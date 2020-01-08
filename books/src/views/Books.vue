<template>
  <div class="books">
    <v-container fill-height fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="6" md="3" align-content-center>
          <v-text-field v-model="search" centered label="Search"></v-text-field>
        </v-col>
      </v-row>
    </v-container>

    <div v-if="dataReady">
      <v-container class="my-5">
        <v-flex xs12 sm4 md2 lg3 v-for="book in visiblePages" :key="book.index">
          <v-card class="ma-3" hover >
            <v-card-title class="one-line">{{book["authors"]}} <p>{{book.title}}</p></v-card-title>
           
            <v-img :src="book.image_url"></v-img>
            <v-card-actions>
              <v-chip>
                <v-icon left color="yellow">mdi-star</v-icon>
                {{book.average_rating}}
              </v-chip>
              <v-btn to="/about" right color="orange" text>Explore</v-btn>
              <router-link :to="{ name: 'bookdetails', params: { id: book.title }}">Details</router-link>

            </v-card-actions>
          </v-card>
        </v-flex>
        <v-layout wrap></v-layout>
      </v-container>
      <v-pagination v-model="page" :length="Math.ceil(all_books[0].length/perPage)"></v-pagination>
      <!-- <v-container class="my-5">
    <v-flex xs12 sm4 md2 lg3 v-for="item in all_books" :key="book.title">
        <v-card class="ma-3">
          <v-card-title>{{book.title}}</v-card-title>
          <v-img :src="book.image_url"></v-img>
          <v-card-actions>
            <v-btn color="orange" text>Share</v-btn>

            <v-btn color="orange" text>Explore</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
      <v-layout row wrap></v-layout>
      </v-container>-->
      <!-- <v-btn @click="getMessage">Get books</v-btn> -->
      <p>{{all_books[0][3].authors}}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Books",
  data() {
    return {
      all_books: [],

      dataReady: false,
      page: 1,
      perPage: 3,
      search: ""
    };
  },
  computed: {
    filteredList() {
      return this.all_books[0].filter(post => {
        return post.title.toLowerCase().includes(this.search.toLowerCase());
      });
    },
    visiblePages() {
      return this.filteredList.slice(
        (this.page - 1) * this.perPage,
        this.page * this.perPage
      );
    }
  },

  mounted() {
    const URL = "http://127.0.0.1:5000/books";
    axios.get(URL, {params:{offset:15}}).then(res => {
      this.all_books = res.data[0];

      this.dataReady = true;
      // this.visiblePages=this.all_books[0].slice((this.page - 1)*this.perPage, this.page*this.perPage)
    });
  }
};
// methods: {
// getMessage() {
//   const URL = "http://127.0.0.1:5000/books";
//   axios.get(URL).then(res => {
//     this.all_books = res.data;
//   });
// }

// computed: {
//   filteredList() {
//     return this.sample_books.filter(title => {
//       return sample_books.title.toLowerCase().includes(this.search.toLowerCase())
//     });
//   }
// }
</script>
<style scoped>
.container {
  display: flex; /* or inline-flex */
}
.one-line{
  font-size-adjust: inherit;
 /* overflow: hidden;  */
  /* text-overflow: ellipsis; */
  /* white-space: nowrap; */

}
</style>

