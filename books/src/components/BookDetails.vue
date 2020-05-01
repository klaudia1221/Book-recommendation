<template>
  <div>
    <!-- <h1>Book details</h1> -->
    <p></p>
    <!-- <p>{{this.id}}</p> -->
    <!-- <p>Current route name: {{ $route.params.id }}</p> -->
    <v-container fluid>
      <!-- <v-layout row justify-space-between> -->
      <!-- <v-flex> -->

      <v-card class="mx-5">
        <div class="d-flex flex-no-wrap">
          <v-avatar class="ma-5" height="700px" min-width="450px" tile>
            <v-img :src="book_details.image_url" object-fit: fill-height></v-img>
          </v-avatar>
          <div>
            <v-card-title  >{{book_details.title}}</v-card-title>

            <v-card-subtitle v-text="book_details.authors"  >  </v-card-subtitle>
            <v-card-subtitle class="mt-n7" v-text="book_details.original_publication_year"  >

               
            
            </v-card-subtitle>

             
           

            <v-card-text>
              <span v-html="book_details.description"></span>
            </v-card-text>
          </div>
          <div>
            <v-card class="ma-5" style="height:700px; width:450px">
              <v-card-title class="orange lighten-5 justify-center" style="font-size:1.4em">Averege book rating</v-card-title>

              <v-card-text class="text-md-center mt-8" style="font-size:3em; color:orange">
                <v-icon color="orange">mdi-star</v-icon>
                {{book_details.average_rating}}
              </v-card-text>
              <v-card-text
                class="text-md-center"
                style="font-size:1.3em"
              >{{formatNumber(book_details.ratings_count) }} ratings</v-card-text>
              <v-card-text
                class="text-md-center mt-n3"
                style="font-size:1.3em"
              >{{formatNumber(book_details.work_text_reviews_count)}} text reviews</v-card-text>

              <v-divider class='white'></v-divider>
              <v-card-title class=" orange lighten-5 justify-center" style="font-size:1.4em">
                Genres</v-card-title>
                 <v-list disabled>
                    <v-list-item-group v-model="item" color="primary">
                   <v-list-item
             v-for="b in book_genres" :key="b"
           
          >  <v-list-item-content><v-card-text
                class="text-md-center"
                style="font-size:1.2em"  v-text="formatGenre(b[0])"></v-card-text><v-divider class='dark'></v-divider></v-list-item-content></v-list-item></v-list-item-group>
                             </v-list>

            </v-card>
          </div>
        </div>
      </v-card>

      <!-- </v-flex> -->
      <!-- </v-layout> -->
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "bookdetails",
  props: ["id"],

  data: () => ({
    book_details: null,
    book_genres: null,
    rating: null,
    // book_id:this.id,
    user_id: 1,
    book_details_URL: "http://127.0.0.1:5000/bookdetails",
    user_ratings_URL: "http://127.0.0.1:5000/userbookrating",
    book_genres_URL: "http://127.0.0.1:5000/bookgenres"
  }),
  mounted() {
    axios
      .get(this.book_details_URL, { params: { book_id: this.id } })
      .then(res => {
        this.book_details = res.data[0][0][0];
        this.user_id = 1;
        this.dataReady = true;
        // this.visiblePages=this.all_books[0].slice((this.page - 1)*this.perPage, this.page*this.perPage)
      });
    axios
      .get(this.user_ratings_URL, {
        params: { user_id: this.user_id, book_id: this.id }
      })
      .then(res => {
        this.rating = res.data[0][0];
      });
    axios
      .get(this.book_genres_URL, {
        params: { book_id: this.id }
      })
      .then(res => {
        this.book_genres = res.data;
      });
  },
  methods: {
    formatNumber(x) {
      return parseInt(x).toLocaleString();
    },
    formatGenre(x){
      return x.replace(/_/g, " ")
    }
  },

  watch: {
    rating() {
      axios.get("http://127.0.0.1:5000/newbookrating", {
        params: {
          user_id: this.user_id,
          book_id: this.book_id,
          rating: this.rating
        }
      });

      // axios
      //   .get(this.URL, { params: { page: this.page, limit: this.limit } })
      //   .then(res => {
      //     this.visiblePages = res.data[0];
      //   });
    }
  }
};
</script>
<style>
.cover-style {
  max-height: 600px;
  max-width: 300px;
  margin-left: 1%;
}
</style>