<template>
  <div class="container">
    <ul class="list-group">
    <li class="list-group-item" v-for="car in cars" :key="cars.id">
      <p>{{ car.model }}</p>
    </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  el: '#app',
  data(){
    return {
      cars: {}
    }
  },

  created() {
    axios.get('http://127.0.0.1:5000/api/cars')
    .then( response => this.cars = response.data)
    .catch(error => console.log(error))
  }

}
</script>
