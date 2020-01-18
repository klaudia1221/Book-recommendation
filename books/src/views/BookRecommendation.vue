<template>
 <div class="bookrecommendation">
  <div v-if="dataReady">
    <!-- {{current_book_id}} -->
     <!-- {{current_book_id.rating}} -->

      <v-container class="my-5"> <v-layout justify-center row fill-height="auto" >
        <v-flex xs12 sm4 md2 lg3 v-for="book in visiblePages[0]" :key="book.index">
                    <v-card :to="{ name: 'bookdetails', params: { id: book.book_id }}" class="ma-3" style="display: 'block'" hover >

          <!-- <v-card  class="ma-3" style="display: 'block'" hover > -->
            <!-- <div :to="{ name: 'bookdetails', params: { id: book.book_id }}"> -->
            <v-card-title class="card-title-style">{{book["authors"]}}</v-card-title>
            <v-card-text class="card-title-style">{{book["title"]}}</v-card-text>
            <v-img class="img-style" aspect-ratio="0.66" :src="book.image_url"></v-img>
           
            <v-card-actions>
              <v-chip>
                <v-icon left color="yellow">mdi-star</v-icon>
                {{book.average_rating}}
              </v-chip>

             
            
              <v-rating @input="addRating($event,rating.id,book.book_id)"  @click.native.stop.prevent></v-rating>
               <!-- <v-btn
                :to="{ name: 'bookdetails', params: { id: book.book_id }}"
                right
                color="orange"
                text
              >Explore</v-btn>  -->
  
              <!-- <router-link :to="{ name: 'bookdetails', params: { id: book.book_id }}">Details</router-link> -->
            </v-card-actions>
          </v-card>
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
     <v-container class="my-5"> <v-layout justify-center row fill-height="auto" >
            
                      <v-btn color="red" large @click="getRecommendations" style="min-width: 100px, min-height:200px">Get recommendations</v-btn>

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
      current_book_id:[],
      dataReady: false,
      page: 1,
      perPage: 3,
      search: "",
    
      // URL: "http://127.0.0.1:5000/coldbooks"

    };
  },
  methods:{ 

   addRating(value,id,bk)  {
     var BooksArray=new Array()
     BooksArray.push(value,id,bk)
      this.current_book_id.push(BooksArray.slice())
     
    },
    getRecommendations(){
      if(this.current_book_id.length){
      const URL = "http://127.0.0.1:5000/getrecommendations";
    axios.get(URL).then(res => {
      this.visiblePages = res.data[0];
        this.dataReady = true;
      
    });
  
      }
      else{
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
.authors-style{
  font-size:small;

}
.list-item{
  padding:0;
  margin:0
}
.card-title-style{
  display:inline-block;
 width: 100%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.img-style {
  height:10%;
  width:100%;
  
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

