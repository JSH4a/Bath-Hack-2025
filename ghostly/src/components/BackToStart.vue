<template>
    <div class="menu-category" @mouseover="startLoading" @mouseleave="resetLoading">
      <span class="category-name">{{ text }}</span>
  
      <!-- Loading Bar -->
      <div class="loading-bar">
        <div class="loading-progress" :style="{ width: progress + '%' }"></div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      text: String,
    },
    data() {
      return {
        progress: 0,
        loadingInterval: null,
        isHovering: false
      };
    },
    methods: {
      // Start the loading process on hover
      startLoading() {
        if (this.isHovering) return; // Prevent multiple intervals running simultaneously
        this.isHovering = true;
        this.progress = 0;
        this.loadingInterval = setInterval(() => {
          if (this.progress < 100) {
            this.progress += 15;
          } else {
            clearInterval(this.loadingInterval); // Stop once progress reaches 100
            this.$emit("click"); // Emit click event after loading
          }
        }, 100); // Increase progress every 100ms
      },
  
      // Reset loading progress if mouse leaves the category
      resetLoading() {
        clearInterval(this.loadingInterval);
        this.progress = 0;
        this.isHovering = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .menu-category {
    display: flex;
    align-items: center;
    padding: 20px;
    background-color: #f5f5f5; /* Light grey background */
    border-radius: 8px;
    margin-bottom: 15px;
    cursor: pointer;
    position: relative;
  }
  
  .category-image {
    width: 50px;
    height: 50px;
    object-fit: cover;
    border-radius: 50%;
    margin-right: 20px;
  }
  
  .category-name {
    font-size: 1.2rem;
    font-weight: bold;
    flex-grow: 1;
  }
  
  .loading-bar {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 5px;
    background-color: #e0e0e0;
    border-radius: 5px;
    overflow: hidden;
  }
  
  .loading-progress {
    height: 100%;
    background-color: #DA291C; /* Green loading bar */
    transition: width 0.1s linear;
  }
  </style>
  