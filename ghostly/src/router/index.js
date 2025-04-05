import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue';
import MenuPage from '../views/MenuPage.vue';
import CartPage from '../views/CartPage.vue';
import ConfirmationPage from '../views/ConfirmationPage.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/menu', component: MenuPage },
  { path: '/cart', component: CartPage },
  { path: '/confirmation', component: ConfirmationPage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
