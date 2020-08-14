import Vue from 'vue';
import VueRouter from 'vue-router';
import Cars from '../views/cars.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/cars',
    name: 'Cars',
    component: Cars,
  }
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
