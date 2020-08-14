<template>
  <div class="container">
    <ul class="list-group">
    <li class="list-group-item">
      <p>{{ data }}</p>
      <p>test</p>
    </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Cars',
  data() {
    return {
      data: '',
    };
  },
  methods: {
    getCars() {
      const path = 'http://localhost:5000/api/cars';
      axios.get(path)
        .then((res) => {
          this.data = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getCars();
  },
};
</script>
