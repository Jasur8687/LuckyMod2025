const grid = document.getElementById('grid');

function createGrid() {
  for (let i = 0; i < 15; i++) {
    const cell = document.createElement('div');
    cell.className = 'cell';
    grid.appendChild(cell);
  }
}

function generateSignal() {
  const cells = document.querySelectorAll('.cell');
  cells.forEach(cell => cell.classList.remove('highlight'));

  const index = Math.floor(Math.random() * cells.length);
  cells[index].classList.add('highlight');
}

createGrid();
generateSignal();
