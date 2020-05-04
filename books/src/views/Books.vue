<template>
  <div class="books">
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="6" md="3" align-content-center>
          <v-text-field dark v-model="search" centered label="Search" @keydown.enter="doSearch"></v-text-field>
        </v-col>
      </v-row>
    </v-container>

    <div v-if="dataReady">
      <v-container class="my-8">
        <v-layout justify-center row fill-height="auto" >
          <v-flex xs12 sm4 md2 lg3 v-for="book in visiblePages[0]" :key="book.index">
            <v-hover v-slot:default="{ hover }" open-delay="100">
              <v-card
                :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                :elevation="hover ? 24 : 6"
                class="ma-8"
                
                style="display: 'block'"
              >
                <!-- <v-card  class="ma-3" style="display: 'block'" hover > -->
                <!-- <div :to="{ name: 'bookdetails', params: { id: book.book_id }}"> -->
                <v-card-title class="card-title-style">{{book["title"]}}</v-card-title>
                <v-card-text class="card-title-style mt-n5">{{book["authors"]}}</v-card-text>

                <v-img
                  class="img-style mt-n3 "
                  aspect-ratio="0.668"
                  object-fit:
                  cover
            
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
                    <div>
                   <v-card-actions>
                   </v-card-actions>
                    </div>
                </v-img>
              
            
      
         
            

                
         
              </v-card>
            </v-hover>
          </v-flex>
        </v-layout>
      </v-container>

      <v-pagination v-if="paginate" v-model="page" :length="Math.ceil(10000/this.perPage)" total-visible="6"></v-pagination>

      <!-- <v-container class="my-5">
    <v-flex xs12 sm4 md2 lg3 v-for="item in all_books" :key="book.title">
        <v-card class="ma-3">
          <v-card-title>{{book.title}}</v-card-title>
          <v-img :src="book.image_url"></v-img>
         
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
      paginate: true,
      visiblePages: null,
      URL: "http://127.0.0.1:5000/books"
    };
  },
  methods: {
    doSearch() {
      axios.get(this.URL, { params: { search: this.search } }).then(res => {
        this.search = null;
        this.visiblePages = res.data[0];
        this.paginate=false;
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
  margin-left: 5%;
  margin-right: 5%;
}
.authors-style {
  font-size: small;
}
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
  width: 100%;
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



