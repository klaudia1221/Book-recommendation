<template>
  <div>
    <!-- <h1>Book details</h1> -->
   <p> </p>
    <!-- <p>{{this.id}}</p> -->
    <!-- <p>Current route name: {{ $route.params.id }}</p> -->

    <v-flex>
      <v-card class="ma-3">
        <v-card-title>{{book_details.authors}} {{book_details.title}}</v-card-title>
        <v-img class="cover-style" :src="book_details.image_url" >  </v-img> <v-rating v-model="rating"></v-rating>

               <v-card-text>       <span v-html="book_details.description"></span></v-card-text>

          <!-- {{description}} -->

            <!-- {{book_details}} -->
         <v-card-text> book rating: {{book_details.average_rating}} </v-card-text>
            
         <v-card-text>Book ratings count:{{book_details.ratings_count}}</v-card-text>
                 <v-card-text>Original year publication:{{book_details.original_publication_year}}</v-card-text>

        
        <!-- <v-card-title{{book["authors"]}} <p>{{book.title}}</p></v-card-title>
           
            <v-img :src="book.image_url"></v-img>
            <v-card-actions>
              <v-chip>
                <v-icon left color="yellow">mdi-star</v-icon>
                {{book.average_rating}}
        </v-chip>-->
      </v-card>
    </v-flex>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "bookdetails",
  props: ["id"],

  data: () => ({
    book_details: null,
    rating: null,
    // book_id:this.id,
    user_id: 1,
    book_details_URL: "http://127.0.0.1:5000/bookdetails",
    user_ratings_URL: "http://127.0.0.1:5000/userbookrating"
  }),
  mounted() {
    axios.get(this.book_details_URL, { params: { book_id: this.id } }).then(res => {
      this.book_details = res.data[0][0][0];
      this.user_id=1;
      this.dataReady = true;
      // this.visiblePages=this.all_books[0].slice((this.page - 1)*this.perPage, this.page*this.perPage)
    });
    axios.get(this.user_ratings_URL,{params:{user_id:this.user_id,book_id:this.id}}).then(res=>{
      this.rating=res.data[0][0];
    });
  } ,
  watch: {
    rating() {
      axios.get("http://127.0.0.1:5000/newbookrating",{params:{user_id:this.user_id,book_id:this.book_id,rating:this.rating}})
      
      // axios
      //   .get(this.URL, { params: { page: this.page, limit: this.limit } })
      //   .then(res => {
      //     this.visiblePages = res.data[0];
      //   });
  }}
};
</script>
<style>

.cover-style {
max-height: 600px;
max-width: 300px; 
margin-left: 1%
}
</style>