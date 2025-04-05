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
      <!-- Displaying the items selected in the order -->
      <ul>
        <li v-for="item in orderList" :key="item.id">
          {{ item.name }} - £{{ item.price.toFixed(2) }} per item
        </li>
      </ul>
      <!-- Checkout button displaying total price -->
      
      <CheckoutItem 
        :price="totalPrice" 
        @click="redirectToConfirmationPage" 
        class="checkout"
      />
    </div>

    <div class="main-content">
      <h1>{{ selectedCategory ? selectedCategory.name : 'Select a Category' }}</h1>
      
      <!-- Card Grid -->
      <div class="cards-container">
        <MenuItem 
          v-for="item in filteredItems" 
          :key="item.id"
          :title="item.name"
          :imageSrc="item.image"
          :price="item.price"
          @click="onCardClick(item)"
        />
      </div>
    </div>
  </div>
</template>

<script>
  import MenuCategory from '../components/MenuCategory.vue';
  import CardComponent from '../components/CardComponent.vue';
  import MenuItem from '../components/MenuItem.vue';
  import CheckoutItem from '../components/CheckoutItem.vue';

  export default {
    components: {
      MenuCategory,
      CardComponent,
      CheckoutItem,
      MenuItem,
    },
    data() {
      return {
        categories: [
          { id: 1, name: 'Burgers', image: '/src/assets/food/cheeseburger.png' },
          { id: 2, name: 'Drinks', image: '/src/assets/food/coke.webp' },
          { id: 3, name: 'Sides', image: '/src/assets/food/fries.png' },
          { id: 4, name: 'Desserts', image: '/src/assets/food/apple-pie.png' }
        ],
        items: [
          { id: 1, name: 'Cheeseburger', categoryId: 1, image: '/src/assets/food/cheeseburger.png', price: 1.99 },
          { id: 2, name: 'Big Mac', categoryId: 1, image: '/src/assets/food/big-mac.png', price: 1.99 },
          { id: 3, name: 'Fries', categoryId: 3, image: '/src/assets/food/fries.png', price: 1.99 },
          { id: 4, name: 'Coke', categoryId: 2, image: '/src/assets/food/coke.webp', price: 1.99 },
          { id: 5, name: 'Apple Pie', categoryId: 4, image: '/src/assets/food/apple-pie.png', price: 1.99 },
        ],
        selectedCategory: null,
        orderList: [], // Array to store selected items for the order
      };
    },
    computed: {
      filteredItems() {
        if (!this.selectedCategory) {
          return [];
        }
        return this.items.filter(item => item.categoryId === this.selectedCategory.id);
      },
      // Calculate the total price for the items in the order list
      totalPrice() {
        return this.orderList.reduce((total, item) => total + item.price, 0);
      }
    },
    methods: {
      selectCategory(category) {
        this.selectedCategory = category;
      },
      onCardClick(item) {
        // Add the item to the order list
        this.orderList.push(item);
      },
      redirectToConfirmationPage() {
        // Redirect to confirmation page
        this.$router.push('/confirmation');
      }
    }
  };
</script>

<style scoped>
.menu-page {
  display: flex;
  height: 100vh;
  margin: 0;
}

.sidebar {
  width: 30%;
  background-color: #f0f0f0;
  padding: 20px;
  box-sizing: border-box;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  box-shadow: 4px 0 12px rgba(0, 0, 0, 0.1);
  border-right: 1px solid #ddd;
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
  margin-left: 30%;
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
