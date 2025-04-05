<template>
    <div class="card" @mouseover="startLoading" @mouseleave="resetLoading">
      <h2>{{ title }}</h2>
      <img :src="imageSrc" alt="Card Image" />
      
      <!-- Loading Bar -->
      <div class="loading-bar">
        <div class="loading-progress" :style="{ width: progress + '%' }"></div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      imageSrc: String
    },
    data() {
      return {
        progress: 0,
        loadingInterval: null,
        isHovering: false // To track if the user is hovering
      };
    },
    methods: {
      // Start the loading process on hover
      startLoading() {
        if (this.isHovering) return; // Prevent multiple intervals running simultaneously
        this.isHovering = true; // Set hover state to true
        this.progress = 0; // Reset progress
        this.loadingInterval = setInterval(() => {
          if (this.progress < 100) {
            this.progress += 10; // Increase progress
          } else {
            clearInterval(this.loadingInterval); // Stop the interval once progress is 100
            this.$emit("click"); // Emit click event after 5 seconds
          }
        }, 100); // Increase progress every 100ms
      },
      
      // Reset the progress if the mouse leaves the card
      resetLoading() {
        clearInterval(this.loadingInterval); // Clear interval when hover ends
        this.progress = 0; // Reset progress
        this.isHovering = false; // Reset hover state
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    position: relative;
    background-color: white;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    width: 300px;
    height: 400px;
    border-radius: 8px;
    cursor: pointer;
    overflow: hidden;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 10px;
  }
  
  img {
    width: 80%;
    height: auto;
    object-fit: fill;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  
  /* Style for the loading bar */
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
    background-color: #DA291C; /* Green color for the loading bar */
    transition: width 0.1s linear;
  }
  </style>
  