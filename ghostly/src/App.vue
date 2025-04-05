<template>
  <div id="app">
        <!-- <router-link to="/">Home</router-link> |  -->
    <!-- The <router-view> is where the matched component will be displayed -->
    <router-view></router-view>
  </div>
</template>

<script>
import { reactive } from 'vue';

export default {
  data() {
    return {
      cart: reactive([]), // Cart state
    };
  },
  methods: {
    addToCart(item) {
      this.cart.push(item);
    },
  },
};
</script>

<style scoped>
#app {
  font-family: 'Arial', sans-serif;
  padding: 20px;
}

.header {
  background-color: #f4f4f4;
  padding: 10px;
  text-align: center;
}

nav {
  margin-top: 20px;
}

nav a {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
}

nav a:hover {
  color: #007bff;
}
</style>
