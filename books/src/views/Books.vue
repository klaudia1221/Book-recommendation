<template>
  <div class="books">
    <v-container fill-height fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="6" md="3" align-content-center>
          <v-text-field v-model="search" centered label="Search" @keydown.enter="doSearch"></v-text-field>
        </v-col>
      </v-row>
    </v-container>

    <div v-if="dataReady">
      <v-container class="my-5">
        <v-flex xs12 sm4 md2 lg3 v-for="book in visiblePages[0]" :key="book.index">
          <v-card :to="{ name: 'bookdetails', params: { id: book.book_id }}" class="ma-3" hover>
            <v-card-title class="one-line">
              <span style="height:10px, width:150px">{{book["authors"]}} {{book.title}}</span>
            </v-card-title>

            <v-img :src="book.image_url" style="height:100px, width:150px"></v-img>
            <v-card-actions>
              <v-chip>
                <v-icon left color="yellow">mdi-star</v-icon>
                {{book.average_rating}}
              </v-chip>
              <v-btn
                :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                right
                color="orange"
                text
              >Explore</v-btn>
              <!-- <router-link :to="{ name: 'bookdetails', params: { id: book.book_id }}">Details</router-link> -->
            </v-card-actions>
          </v-card>
        </v-flex>
        <v-layout wrap></v-layout>
      </v-container>

      <v-pagination v-model="page" :length="Math.ceil(10000/this.perPage)"></v-pagination>

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
      <!-- <p>{{visiblePages[0][3].authors}}</p> -->
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
      perPage: 32,
      search: "",
      limit: 32,
      visiblePages: null,
      URL: "http://127.0.0.1:5000/books"
    };
  },
  methods: {
    doSearch() {
      axios.get(this.URL, { params: { search: this.search } }).then(res => {
        this.search = null;
        this.visiblePages = res.data[0];
      });
    }
  },
  watch: {
    page() {
      axios
        .get(this.URL, { params: { page: this.page, limit: this.limit } })
        .then(res => {
          this.visiblePages = res.data[0];
        });
    }
  },

  mounted() {
    axios
      .get(this.URL, { params: { page: 1, limit: this.limit } })
      .then(res => {
        this.visiblePages = res.data[0];
        this.dataReady = true;
      });
  }
};
</script>
<style scoped>
.container {
  display: inline-flex; /* or inline-flex */
  flex-wrap: wrap;
}
</style>

