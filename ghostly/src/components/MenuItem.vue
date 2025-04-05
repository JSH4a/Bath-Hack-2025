<template>
    <div class="menu-item">
      <img :src="item.image" alt="item.name" />
      <h3>{{ item.name }}</h3>
      <p>{{ item.price }}</p>
      <button @click="addToCart(item)">Add to Cart</button>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      item: Object,
    },
    methods: {
      addToCart(item) {
        this.$emit('add-to-cart', item); // Notify parent to add to cart
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your styles here */
  </style>
  