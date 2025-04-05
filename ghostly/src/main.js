import { createApp } from 'vue';  // Import Vue's createApp method
import App from './App.vue';      // Import the root App component
import router from './router';    // Import the Vue Router

// Create the Vue app and use the router
createApp(App)
  .use(router)                  // Tell Vue to use the router
  .mount('#app');               // Mount the app to the DOM element with id="app"
