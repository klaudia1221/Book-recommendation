<template>
  <div>
    <h1>Book details</h1>
    <!-- <p>{{this.id}}</p> -->
    <!-- <p>Current route name: {{ $route.params.id }}</p> -->

    <v-flex>
      <v-card xs12 sm4 md2 lg3 class="ma-3">
        <v-card-title>{{book_details.authors}}</v-card-title>
        <v-img :src="book_details.image_url" contain height="15%" width="15%"></v-img>
        <div class="text-center">
          <v-rating v-model="rating"></v-rating>
        </div>
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
    rating: 0
  }),
  mounted() {
    const URL = "http://127.0.0.1:5000/bookdetails";
    axios.get(URL, { params: { book_id: this.id } }).then(res => {
      this.book_details = res.data[0][0][0];

      this.dataReady = true;
      // this.visiblePages=this.all_books[0].slice((this.page - 1)*this.perPage, this.page*this.perPage)
    });
  }
};
</script>
<style>
.card {
  height: 100px;
  width: 50px;
}
.img {
  height: 10%;
  width: 10%;
  /* overflow: hidden;  */
  /* text-overflow: ellipsis; */
  /* white-space: nowrap; */
}
</style>