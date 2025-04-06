const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const ghostImage = document.getElementById('ghostImage');
const enemyImage = document.getElementById('enemyImage');

let ghost = {
  x: 0,
  y: 0,
  speed: 4,
  width: 50, // size of the ghost
  height: 50
};

let enemies = [];
let score = 0;
let gameOver = false;

// Update canvas size based on the window size
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Mouse move listener to follow the cursor
document.addEventListener('mousemove', (e) => {
  ghost.x = e.clientX - ghost.width / 2;
  ghost.y = e.clientY - ghost.height / 2;
});

// Function to spawn enemies randomly
function spawnEnemy() {
  const enemy = {
    x: -50, // start outside the screen
    y: Math.random() * canvas.height,
    speed: Math.random() * 2 + 2, // random speed between 2 and 4
    width: 50, // size of the enemy
    height: 50,
    direction: 1 // move right
  };
  enemies.push(enemy);
}

// Function to update game state
function update() {
  if (gameOver) {
    ctx.fillStyle = 'white';
    ctx.font = '48px Arial';
    ctx.fillText('You Win!', canvas.width / 2 - 100, canvas.height / 2);
    return;
  }

  // Clear canvas and draw the background
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Add the glowing effect to the ghost by setting shadow properties
  ctx.shadowColor = 'white'; // Set the shadow color to white
  ctx.shadowBlur = 15; // Set how much the shadow should blur
  ctx.shadowOffsetX = 0; // No offset in the X direction
  ctx.shadowOffsetY = 0; // No offset in the Y direction

  // Draw the ghost following the mouse with the glow effect
  ctx.drawImage(ghostImage, ghost.x, ghost.y, ghost.width, ghost.height);

  // Reset shadow settings for other drawing operations
  ctx.shadowColor = 'transparent'; // Reset the shadow to transparent (no shadow)
  
  // Update and draw enemies
  enemies.forEach((enemy, index) => {
    enemy.x += enemy.speed;

    // If enemy goes out of the screen, remove it
    if (enemy.x > canvas.width) {
      enemies.splice(index, 1);
    }

    ctx.drawImage(enemyImage, enemy.x, enemy.y, enemy.width, enemy.height);

    // Check if the ghost collides with the enemy (simple bounding box check)
    if (
      ghost.x < enemy.x + enemy.width &&
      ghost.x + ghost.width > enemy.x &&
      ghost.y < enemy.y + enemy.height &&
      ghost.y + ghost.height > enemy.y
    ) {
      // Increase the score when ghost catches the enemy
      score++;

      // Remove enemy and check win condition
      enemies.splice(index, 1);
      if (score >= 5) {
        gameOver = true;
      }
    }
  });

  // Spawn enemies randomly at intervals
  if (Math.random() < 0.01) {
    spawnEnemy();
  }

  // Display score
  ctx.fillStyle = 'white';
  ctx.font = '24px Arial';
  ctx.fillText('Score: ' + score, 20, 30);

  // Request the next frame
  requestAnimationFrame(update);
}

// Start the game
update();
