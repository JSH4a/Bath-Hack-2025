<template>
    <div class="container">
      <img class="small-logo" src="../assets/mcdonalds-5.svg">
  
      <h1>Where will you be eating today?</h1>
      
      <!-- Add @click event to each card to redirect -->
      <div class="cards-container">
        <CardComponent 
          title="Eat In" 
          imageSrc="/src/assets/eating-in.jpg" 
          @click="redirectToMenuPage"
        />
  
        <CardComponent 
          title="Take-away" 
          imageSrc="/src/assets/take-away.jpg"
          @click="redirectToMenuPage"
        />
      </div>
    </div>
  </template>
  
  <script>
  import CardComponent from '../components/CardComponent.vue';

  export default {
    components: {
      CardComponent
    },
    methods: {
      redirectToMenuPage() {
        this.$router.push('/menu'); // Using this.$router
      }
    }
  }
  </script>
  
  <style scoped>
  /* Container for all content */
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding-top: 50px; /* Adjust the space from the top */
  }
  
  /* Style for the logo */
  .small-logo {
    width: 100px;
    margin-bottom: 20px;
  }
  
  /* Heading style */
  h1 {
    font-size: 2rem;
    margin-bottom: 30px;
  }
  
  /* Cards container with flex to align the cards next to each other */
  .cards-container {
    display: flex;
    gap: 50px; /* Add space between the cards */
    justify-content: center; /* Center the cards horizontally */
    }
  </style>
  