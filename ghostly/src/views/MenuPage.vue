<template>
  <div class="menu-page">
    <div class="sidebar">
      <img class="small-logo" src="../assets/mcdonalds-5.svg">
      <ul>
        <li 
          v-for="category in categories" 
          :key="category.id"
        >
          <MenuCategory 
            :category="category" 
            :imageSrc="category.image" 
            @click="selectCategory(category)"
          />
        </li>
      </ul>

      <p>Your order:</p>
      <CheckoutItem category="Checkout" class="checkout"/>
    </div>

    <div class="main-content">
      <h1>{{ selectedCategory ? selectedCategory.name : 'Select a Category' }}</h1>
      
      <!-- Card Grid -->
      <div class="cards-container">
        <CardComponent 
          v-for="item in filteredItems" 
          :key="item.id"
          :title="item.name"
          :imageSrc="item.image"
          @click="onCardClick(item)"
        />
      </div>
    </div>
  </div>
</template>

<script>
  import MenuCategory from '../components/MenuCategory.vue';
  import CardComponent from '../components/CardComponent.vue';
  import CheckoutItem from '../components/CheckoutItem.vue';

  export default {

  components: {
    MenuCategory,
    CardComponent,
    CheckoutItem,
  },
  data() {
    return {
      categories: [
        { id: 1, name: 'Burgers', image: '/src/assets/burger-icon.png' },
        { id: 2, name: 'Drinks', image: '/src/assets/drink-icon.png' },
        { id: 3, name: 'Sides', image: '/src/assets/sides-icon.png' },
        { id: 4, name: 'Desserts', image: '/src/assets/dessert-icon.png' }
      ],
      items: [
        { id: 1, name: 'Cheeseburger', categoryId: 1, image: '/src/assets/food/cheeseburger.png' },
        { id: 2, name: 'Big Mac', categoryId: 1, image: '/src/assets/food/big-mac.png' },
        { id: 3, name: 'Fries', categoryId: 3, image: '/src/assets/food/fries.png' },
        { id: 4, name: 'Coke', categoryId: 2, image: '/src/assets/food/coke.png' },
        { id: 5, name: 'Apple Pie', categoryId: 4, image: '/src/assets/food/applepie.png' },
        // Add more items here...
      ],
      selectedCategory: null
    };
  },
  computed: {
    filteredItems() {
      if (!this.selectedCategory) {
        return [];
      }
      return this.items.filter(item => item.categoryId === this.selectedCategory.id);
    }
  },
  methods: {
    selectCategory(category) {
      this.selectedCategory = category;
    },
    onCardClick(item) {
      // Handle card click, e.g., navigate to item details page
      console.log('Card clicked:', item);
    }
  }
};
</script>

<style scoped>
.menu-page {
  display: flex;
  height: 100vh; /* Ensure the page takes the full height of the viewport */
  margin: 0; /* Remove any margin around the entire menu page */
}

.sidebar {
  width: 30%;
  background-color: #f0f0f0; /* Light greyish off-white */
  padding: 20px;
  box-sizing: border-box;
  height: 100vh; /* Ensure the sidebar takes the full height of the viewport */
  position: fixed; /* Make sure the sidebar is fixed to the left */
  top: 0;
  left: 0;
  
  /* Flexbox styles to center logo */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center; /* This will center the logo horizontally */
  
  /* Add a box-shadow and a gentle black border for a more defined look */
  box-shadow: 4px 0 12px rgba(0, 0, 0, 0.1); /* A gentle shadow on the right side */
  border-right: 1px solid #ddd; /* Light border on the right edge */
}

.small-logo {
  width: 100px;
  margin-bottom: 20px;
}

.sidebar h3 {
  text-align: center;
}

.sidebar ul {
  list-style: none;
  padding: 0;
  width: 100%;
}

.main-content {
  flex-grow: 1;
  padding: 20px;
  margin-left: 30%; /* Adjust the main content to start after the sidebar */
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.main-content {
  flex-grow: 1;
  padding: 20px;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.checkout {
  width: 80%;
}
</style>