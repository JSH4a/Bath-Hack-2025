<template>
    <div class="order-container">
      <h1 class="heading">Please take your number and collect your order at the counter.</h1>
      <h1 class="thanks">Thanks</h1>
  
      <div class="order-box">
        <div class="order-number">
          <span class="order-label">No.</span>
          <h1 class="order-id">{{ formattedOrderNum }}</h1> <!-- Display the formatted order number -->
        </div>
      </div>
  
      <img class="small-logo" src="../assets/mcdonalds-5.svg" alt="Logo" @click="redirectToHome">

      <h2 class="thank-you">Thank you for your order.</h2>

      <BackToStart class="next-order" text="Next order" @click="redirectToHome"/>
    </div>
  </template>
  
  <script>
  import BackToStart from '../components/BackToStart.vue';
  export default {
    components: {BackToStart},
    data() {
      return {
        // Random integer between 0 and 99
        orderNum: Math.floor(Math.random() * 100)
      };
    },
    computed: {
      formattedOrderNum() {
        // Zero-pad the order number to 2 digits (e.g., 01, 06, etc.)
        return String(this.orderNum).padStart(2, '0');
      }
    },
    methods: {
    // Method to redirect to the homepage
    redirectToHome() {
      this.$router.push('/'); // Redirects to the root (home) page
    }
  }
  };
  </script>
  
  <style scoped>
  .order-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    height: 100vh; /* Full viewport height */
    margin: 0; /* Remove any default margin */
    transform: translateY(-250px);
  }
  
  .heading, .thanks, .thank-you, .order-box {
    margin-bottom: 30px; /* Adds spacing below each header */
  }
  
  .order-box {
    display: inline-block;
    padding: 20px 30px;
    border: 2px solid #333;
    margin-top: 20px;
    background-color: #f9f9f9;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 15px; /* Rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow effect */
    width: 200px; /* Make the box width fit the content */
    height: 100px; /* Increase the height to make the box taller */
    margin-bottom: 30px; /* Adds spacing below the order box */
  }
  
  .order-number {
    display: flex;
    align-items: flex-start; /* Align "No." at the top */
  }
  
  .order-label {
    font-size: 0.8rem; /* Small font for "No." */
    margin-top: 3px; /* Small gap to create the superscript effect */
    margin-right: 5px; /* Space between "No." and order number */
  }
  
  .order-id {
    font-size: 2rem; /* Larger font size for order number */
    margin: 0; /* Remove any default margin */
  }
  
  .small-logo {
    margin-top: 150px;
    width: 100px;
    margin-bottom: 30px; /* Adds spacing below the logo */
  }
  
  h1, h2 {
    font-size: 1.5rem;
  }

  .next-order {
    width: 300px;
    height: 100px;
  }
  </style>
  