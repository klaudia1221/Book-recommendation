<template>
  <div class="bookrecommendation">
    <div v-if="dataReady">
      <!-- <h1>{{this.not_read}}</h1>
      <h1>{{this.not_interested}}</h1>
      <h1>{{this.user_book_ratings_list}}</h1> -->

      <v-container class="my-8">
        <v-layout justify-center row fill-height="auto">
          <v-flex xs12 sm4 md2 lg3 v-for="book in visiblePages[0]" :key="book.index">
            <v-hover v-slot:default="{ hover }" open-delay="100">
              <v-card
                :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                :elevation="hover ? 24 : 6"
                class="ma-8"
                style="display: 'block'"
              >
                <v-card-title class="card-title-style">{{book["title"]}}</v-card-title>
                <v-card-text class="card-title-style mt-n5">{{book["authors"]}}</v-card-text>
                <v-hover v-slot:default="{ hover }">
                  <v-img
                    class="img-style mt-n3"
                    aspect-ratio="0.85"
                    object-fit:
                    contain
                    :src="book.book_cover_url"
                  >
                    <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out white darken-2 v-card--reveal display-1 grey--text"
                        style="height: 20%;"
                      >
                        <v-icon class="mx-3" color="orange">mdi-star</v-icon>
                        {{book.average_rating}}
                      </div>
                    </v-expand-transition>
                  </v-img>
                </v-hover>

                <!-- <v-chip>
                    <v-icon color="yellow">mdi-star</v-icon>
                    {{book.average_rating}}
                </v-chip>-->
                <v-rating
                  class="text-center"
                  background-color="grey lighten-1"
                  color="red"
                  @input="addRating(book.book_id,$event,)"
                  @click.native.stop.prevent
                ></v-rating>

                <!-- <v-btn
                    :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                    color="orange" dark
                    text
                     
                    class="mr-3"
                >Explore</v-btn>-->
                <div class="text-center">
                  <v-btn
                    class="ma-3 mb-4"
                    color="red"
                    @click="addToNotInterested(book.book_id)"
                    @click.native.stop.prevent
                    dark
                  >
                    NOT INTERESTED
                    <v-icon dark right>mdi-cancel</v-icon>
                  </v-btn>
                  <v-btn
                    class="ma-2"
                    color="orange"
                    @click="addToNotRead(book.book_id)"
                    @click.native.stop.prevent
                    dark
                  >
                    NOT READ
                    <v-icon dark right>mdi-eye-off</v-icon>
                  </v-btn>
                </div>

                <!-- <v-btn
                :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                right
                color="orange"
                text
                >Explore</v-btn>-->

                <!-- <router-link :to="{ name: 'bookdetails', params: { id: book.book_id }}">Details</router-link> -->
              </v-card>
            </v-hover>
          </v-flex>
        </v-layout>
      </v-container>
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
      <!-- <v-btn @click="getRecommendations">Get recommendations</v-btn> -->
    </div>
    <v-container class="my-5">
      <v-layout justify-center row fill-height="auto">
        <v-btn
          color="red"
          large
          @click="getRecommendations"
          style="min-width: 100px, min-height:200px"
        >Get recommendations</v-btn>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
// import BookDetails from "@components/BookDetails.vue"
export default {
  name: "BookRecommendations",
  data() {
    return {
      // all_books: [],
      visiblePages: null,
      rating: 0,
      ratings: null,
      user_book_ratings_list: [],
      dataReady: false,
      page: 1,
      perPage: 3,
      search: "",
      not_interested: [],
      not_read: []

      // URL: "http://127.0.0.1:5000/coldbooks"
    };
  },
  methods: {
    addRating(book_id, value) {
      var is_in_list = false;
      for (var i = 0; i < this.user_book_ratings_list.length; i++) {
        if (this.user_book_ratings_list[i][0] === book_id) {
          this.user_book_ratings_list[i][1] = value;
          is_in_list = true;
        }
      }
      if (!is_in_list) {
        var BooksArray = new Array();
        BooksArray.push(book_id, value);
        this.user_book_ratings_list.push(BooksArray);
      }
    },
    updateRatings() {},
    addToNotRead(id) {
      if (this.not_read.indexOf(id) === -1) {
        this.not_read.push(id);
      }
    },
    addToNotInterested(id) {
      if (this.not_interested.indexOf(id) === -1) {
        this.not_interested.push(id);
      }
    },
    getRecommendations() {
      if (this.user_book_ratings_list.length) {
        const URL = "http://127.0.0.1:5000/getrecommendations";
        axios.get(URL).then(res => {
          this.visiblePages = res.data[0];
          this.dataReady = true;
        });
      } else {
        alert("Please provide 20 ratings to get recommendations.");
      }
    }
  },

  mounted() {
    const URL = "http://127.0.0.1:5000/coldbooks";
    axios.get(URL).then(res => {
      this.visiblePages = res.data[0];
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
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
  width: 100%;
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

