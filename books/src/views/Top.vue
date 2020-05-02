<template>
  <div class="top">
    <v-tabs dark background-color="transparent"  color="orange" v-model="model" centered slider-color="orange" background: transparent>
    <v-tab @click="getTopPopular()">Most popular</v-tab>
    <v-tab @click="getTopRated()">Best rated</v-tab>
    </v-tabs>

    <div v-if="dataReady">
      <v-container class="my-5">
        <v-layout justify-center row fill-height="auto">
          <v-flex xs12 sm4 md2 lg3 v-for="book in visiblePages[0]" :key="book.index">
            <v-card
              :to="{ name: 'bookdetails', params: { id: book.book_id }}"
              class="ma-3"
              style="display: 'block'"
              hover
            >
              <!-- <v-card  class="ma-3" style="display: 'block'" hover > -->
              <!-- <div :to="{ name: 'bookdetails', params: { id: book.book_id }}"> -->
              <v-card-title class="card-title-style">{{book["title"]}}</v-card-title>
              <v-card-text class="card-title-style mt-n5">{{book["authors"]}}</v-card-text>
              <v-img class="img-style mt-n3" aspect-ratio="0.66"  :src="book.book_cover_url"></v-img>

              <v-card-actions>
               <v-chip class='ml-3'>
                  <v-icon left color="yellow">mdi-star</v-icon>
                  {{book.average_rating}}
                </v-chip>
<v-spacer></v-spacer>
                <v-btn
                  :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                  right
                  color="orange"
                  text
                  class=" mr-3"

                >Explore</v-btn>

                <!-- <v-rating v-model="rating"></v-rating> -->

                <!-- <router-link :to="{ name: 'bookdetails', params: { id: book.book_id }}">Details</router-link> -->
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>

      <!-- <v-pagination v-model="page" :length="Math.ceil(100/this.perPage)" total-visible=6 ></v-pagination> -->

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
      top_popular_URL: "http://127.0.0.1:5000/toppopular",
      top_rated_URL: "http://127.0.0.1:5000/toprated"
    };
  },
  model: "tab-2",
  methods: {
    getTopPopular() {
      axios.get(this.top_popular_URL).then(res => {
        this.visiblePages = res.data[0];
        this.dataReady = true;
      });
    },
    getTopRated() {
      axios.get(this.top_rated_URL).then(res => {
        this.visiblePages = res.data[0];
        this.dataReady = true;
      });
    }
  },
  watch: {
    // page() {
    //   axios
    //     .get(this.top_popular_URL)
    //     .then(res => {
    //       this.visiblePages = res.data[0];
    //     });
    // }
  },

  mounted() {
    axios.get(this.top_popular_URL).then(res => {
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
  margin-left: 5%;
  margin-right: 5%;
}
.authors-style {
  font-size: small;
}
.list-item {
  padding: 0;
  margin: 0;
}
.card-title-style {
  display: inline-block;
  width: 100%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.img-style {
  height: 10%;
  width: 100%;

  /* height: 20rem; 
  width: 20rem;
  min-width: 15rem;
  /* max-width: 40rem; */
  /* width: 100px; */
  /* max-height: 42rem; */
  /* max-width: 100px;  */

  /* overflow: hidden;  */
  /* text-overflow: ellipsis; */
  /* white-space: nowrap; */
}
</style>



