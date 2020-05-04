<template>
  <div class="bookrecommendation">
    <div v-if="dataReady">
      <!-- <h1>{{this.to_read}}</h1> 
      <h1>{{this.not_interested}}</h1>
            <h1>{{this.temp_not_interested}}</h1> -->

      <!-- <h1>{{this.user_book_ratings_list}}</h1>
      <h2>{{this.temp_book_ratings}}</h2>--> -->

      <v-container class="my-8">
        <v-layout justify-end mr-5>
          <v-btn color="orange" @click="clearRatingsAndReload()" dark>Clear book ratings</v-btn>
        </v-layout>
        <v-layout justify-center row>
          <v-flex class="items" xs12 sm4 md2 lg3  v-for="(book, index) in visiblePages[0]" :key="book.index">
            <div v-if="IsIn(book.book_id, index)">
            <v-hover v-slot:default="{ hover }" open-delay="100">
              <v-card
                :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                :elevation="hover ? 24 : 6"
                class="card ma-8"
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
                <v-rating
                  class="text-center"
                  background-color="grey lighten-1"
                  color="red"
                  v-model="temp_book_ratings[book.book_id]"
                  @input="addRating(book.book_id,$event,)"
                  @click.native.stop.prevent
                ></v-rating>
                <div class="text-center">
                  <v-btn
                    class="ma-3 mb-4"
                    color="red"
                    @click="addToNotInterested(book.book_id, index)"
                    delete
                    @click.native.stop.prevent
                    dark
                  >
                    NOT INTERESTED
                    <v-icon dark right>mdi-cancel</v-icon>
                  </v-btn>
                  <v-btn
                    class="ma-2"
                    color="orange"
                    @click="addToToRead(book.book_id,index)"
                    delete
                    @click.native.stop.prevent
                    dark
                  >
                    TO READ
                    <v-icon dark right>mdi-eye-off</v-icon>
                  </v-btn>
                </div>
              </v-card>
            </v-hover>
            </div>
          </v-flex>
        </v-layout>
      </v-container>
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
import firebase from "firebase";
// import BookDetails from "@components/BookDetails.vue"
const database = firebase.database();
const RatingsRef = database.ref("books/TempRatings");
const ToReadRef= database.ref("books/TempToRead");
const NotInterestedRef=database.ref("books/TempNotInterested");

export default {
  name: "BookRecommendations",
  data() {
    return {
      // all_books: [],
      visiblePages: null,
      temp_book_ratings: null,
      temp_to_read:null,
      temp_not_interested: null,
      // rating: {'3':1},
      ratings: null,
      user_book_ratings_list: [],
      dataReady: false,
      page: 1,
      perPage: 3,
      search: "",
      not_interested: [],
      to_read: []

      // URL: "http://127.0.0.1:5000/coldbooks"
    };
  },
  methods: {
    //   updateRatings() {

    // })
    IsIn(id, index){
      if ((this.to_read.indexOf(id.toString()) === -1)&&(this.not_interested.indexOf(id.toString()) === -1)){
        return true;
      }
      else {
      this.$delete(this.visiblePages[0],index);

        return false;}
    },
     clearRatings() {
      this.user_book_ratings_list = [];
      RatingsRef.remove();
      ToReadRef.remove();
      NotInterestedRef.remove();
      
    },
    clearRatingsAndReload() {
      this.user_book_ratings_list = [];
      RatingsRef.remove();
      ToReadRef.remove();
      NotInterestedRef.remove()
      window.location.reload();
    },
    // storeBookRating(book_id, rating) {
    //   // RatingsRef.push({ book_id: book_id, rating: rating });
    //   RatingsRef.push({ book_id: rating });
    // },
    // deleteBookRating(book_id) {
    //   RatingsRef.child(book_id.id).remove();
    // },
    
    addRating(book_id, value) {
      RatingsRef.child(book_id).set(value);
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
        // this.storeBookRating(book_id,value);
      }
    },

    addToToRead(id, index) {
      if (this.to_read.indexOf(id) === -1) {
        this.to_read.push(id);
      }
      ToReadRef.child(id).set("false");
      this.$delete(this.visiblePages[0],index);

    },
    addToNotInterested(id, index) {
      if (this.not_interested.indexOf(id) === -1) {
        this.not_interested.push(id);
      }
      NotInterestedRef.child(id).set("false");

      this.$delete(this.visiblePages[0],index);

    },
    readfromFirebase() {
      RatingsRef.once("value", snapshot => {
        this.temp_book_ratings = { ...snapshot.val(), id: snapshot.key };
        for (var key in this.temp_book_ratings) {
          //  console.log(key);
          var RatingsArray = new Array();
          RatingsArray.push(key);
          RatingsArray.push(this.temp_book_ratings[key]);
          this.user_book_ratings_list.push(RatingsArray);
        }
      });
      ToReadRef.once("value", snapshot => {
        this.temp_to_read = { ...snapshot.val(), id: snapshot.key };
        for (var key in this.temp_to_read) {
          // var TempArray = new Array();
          // TempArray.push(key);
          // TempArray.push(this.temp_to_read[key]);
          // this.to_read.push(TempArray);
          this.to_read.push(key);
        }
      });
      NotInterestedRef.once("value", snapshot => {
        this.temp_not_interested = { ...snapshot.val(), id: snapshot.key };
        for (var key in this.temp_not_interested) {
          // var TempArray = new Array();
          // TempArray.push(key);
          // TempArray.push(this.temp_not_interested[key]);
          // this.not_interested.push(TempArray);
          // this.to_read.push(key);
          this.not_interested.push(key);
        }
      });
     
    },
    
    getRecommendations() {
      if (this.user_book_ratings_list.length) {
        window.scrollTo(0, 0);
        this.readfromFirebase();
        const URL = "http://127.0.0.1:5000/getrecommendations";
        axios.get(URL,{params:{ratings:JSON.stringify(this.user_book_ratings_list), not_interested: JSON.stringify(this.not_interested), to_read: JSON.stringify(this.to_read) }}).then(res => {
          this.visiblePages = res.data[0];
          this.dataReady = true;
        });
      } else {
        alert("Please provide 20 ratings to get recommendations.");
      }
      this.clearRatings();
    }
  },

  mounted() {
    // RatingsRef.once("value", snapshot => {
    //     this.temp_book_ratings={ ...snapshot.val(), id: snapshot.key };
    //   });
    this.readfromFirebase();
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
.items{
  flex-wrap: nowrap;
  
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

