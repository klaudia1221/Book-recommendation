<template>
<div>
<h1>Book details i co stma</h1>
 <p>{{id}}</p>
       <p>Current route name: {{ $route.params.id }}</p>

</div>
</template>

<script>


export default {
  
name: 'bookdetails',
props: ["id"],

data: () => ({
})}
</script>